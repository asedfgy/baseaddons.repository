# -*- coding: utf-8 -*-
#
# Copyright (C) 2016, 2017, 2018, 2019 RACC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the 1-N General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the 1-N General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
from xbmcgui import ListItem
from routing import Plugin

import sys
import os
import traceback
import time

import requests
from datetime import timedelta
from requests_cache import CachedSession
from Cryptodome.Cipher import AES
from hashlib import md5
from binascii import b2a_hex

try:
    from http.cookiejar import LWPCookieJar
except ImportError:
    from cookielib import LWPCookieJar
try:
    from urllib.parse import quote_from_bytes as orig_quote
except ImportError:
    from urllib import quote as orig_quote
try:
    from urllib.parse import unquote_to_bytes as orig_unquote
except ImportError:
    from urllib import unquote as orig_unquote


addon = xbmcaddon.Addon()
plugin = Plugin()
plugin.name = addon.getAddonInfo("name")
player_user_agent = "Lavf/56.15.102"
user_agent = "okhttp/3.10.0"
USER_DATA_DIR = xbmc.translatePath(addon.getAddonInfo("profile")).decode("utf-8")  # !!
CACHE_TIME = int(addon.getSetting("cache_time"))
CACHE_FILE = os.path.join(USER_DATA_DIR, "cache")
COOKIE_FILE = os.path.join(USER_DATA_DIR, "lwp_cookies.dat")
expire_after = timedelta(hours=CACHE_TIME)

if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

s = CachedSession(
    CACHE_FILE,
    allowable_methods=("GET", "POST"),
    expire_after=expire_after,
    old_data_on_error=True,
    ignored_parameters=["data"],
)
s.hooks = {"response": lambda r, *args, **kwargs: r.raise_for_status()}
s.cookies = LWPCookieJar(filename=COOKIE_FILE)
if os.path.isfile(COOKIE_FILE):
    s.cookies.load(ignore_discard=True, ignore_expires=True)

data_url = "http://swiftstreamz.com/SwiftPanel/apiv1.php"
cat_url = "http://swiftstreamz.com/SwiftPanel/apiv1.php?get_category"
list_url = "http://swiftstreamz.com/SwiftPanel/apiv1.php?get_channels_by_cat_id={0}"


def quote(s, safe=""):
    return orig_quote(s.encode("utf-8"), safe.encode("utf-8"))


def unquote(s):
    return orig_unquote(s).decode("utf-8")


def get_post_data():
    _key = b"cLt3Gp39O3yvW7Gw"
    _iv = b"bRRhl2H2j7yXmuk4"
    cipher = AES.new(_key, AES.MODE_CBC, iv=_iv)
    _time = str(int(time.time()))
    _hash = md5(
        "{0}e31Vga4MXIYss1I0jhtdKlkxxwv5N0CYSnCpQcRijIdSJYg".format(_time).encode("utf-8")
    ).hexdigest()
    _plain = "{0}&{1}".format(_time, _hash).ljust(48).encode("utf-8")
    cry = cipher.encrypt(_plain)
    return b2a_hex(cry).decode("utf-8")


@plugin.route("/refresh")
def refresh():
    s.cache.clear()
    xbmc.executebuiltin("Container.Refresh")


@plugin.route("/")
def root():
    headers = {"Connection": "Keep-Alive", "Accept-Encoding": "gzip"}
    req = requests.Request("GET", cat_url, headers=headers)
    prepped = req.prepare()
    r = s.send(prepped, timeout=10)
    res = r.json(strict=False)

    list_items = []
    for cat in res["LIVETV"]:
        li = ListItem(cat["category_name"])
        li.setArt({"thumb": "{0}|User-Agent={1}".format(cat["category_image"], quote(user_agent))})
        url = plugin.url_for(list_channels, cat_id=cat["cid"])
        list_items.append((url, li, True))

    xbmcplugin.addDirectoryItems(plugin.handle, list_items)
    xbmcplugin.endOfDirectory(plugin.handle)


@plugin.route("/list_channels/<cat_id>")
def list_channels(cat_id=None):
    list_items = []
    headers = {"Connection": "Keep-Alive", "Accept-Encoding": "gzip"}
    req = requests.Request("GET", list_url.format(cat_id), headers=headers)
    prepped = req.prepare()
    r = s.send(prepped, timeout=10)
    res = r.json(strict=False)

    refresh_streams = "RunPlugin({0})".format(plugin.url_for(refresh))
    for ch in res["LIVETV"]:
        image = "{0}|User-Agent={1}".format(ch["channel_thumbnail"], quote(user_agent))
        li = ListItem(ch["channel_title"])
        li.setProperty("IsPlayable", "true")
        li.addContextMenuItems([("Refresh Streams", refresh_streams)])
        li.setArt({"thumb": image, "icon": image})
        li.setInfo(type="Video", infoLabels={"Title": ch["channel_title"], "mediatype": "video"})
        li.setContentLookup(False)
        url = plugin.url_for(play, cat_id=cat_id, channel_id=ch.get("id"))
        list_items.append((url, li, False))

    xbmcplugin.addDirectoryItems(plugin.handle, list_items)
    xbmcplugin.endOfDirectory(plugin.handle)


@plugin.route("/play/<cat_id>/<channel_id>/play.pvr")
def play(cat_id, channel_id):
    headers = {"Connection": "Keep-Alive", "Accept-Encoding": "gzip"}
    req = requests.Request("GET", list_url.format(cat_id), headers=headers)
    prepped = req.prepare()
    r = s.send(prepped, timeout=10)
    res = r.json(strict=False)

    for ch in res["LIVETV"]:
        if ch.get("id") == channel_id:
            title = ch.get("channel_title")
            image = "{0}|User-Agent={1}".format(ch["channel_thumbnail"], quote(user_agent))
            stream_list = ch.get("stream_list")

    post_data = {"data": get_post_data()}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    req = requests.Request("POST", data_url, data=post_data, headers=headers)
    prepped = req.prepare()
    r = s.send(prepped, timeout=10)
    data = r.json(strict=False)
    token_list = data["LIVETV"]["token_list"]

    for _stream in stream_list:
        stream_url = _stream.get("stream_url")
        stream_token = _stream.get("token")
        break

    for _token in token_list:
        if _token["t_id"] == stream_token:
            token_link = _token["token_link"]
            break

    with s.cache_disabled():
        post_data = {"data": get_post_data()}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        }
        req = requests.Request("POST", token_link, data=post_data, headers=headers)
        prepped = req.prepare()
        r = s.send(prepped, timeout=10)
        auth_token = r.text.partition("=")[2]

    auth_token = "".join(
        [
            auth_token[:-59],
            auth_token[-58:-47],
            auth_token[-46:-35],
            auth_token[-34:-23],
            auth_token[-22:-11],
            auth_token[-10:],
        ]
    )
    media_url = "{0}?wmsAuthSign={1}|User-Agent={2}".format(
        stream_url, auth_token, quote(player_user_agent)
    )
    li = ListItem(title, path=media_url)

    if "playlist.m3u8" in media_url:
        if addon.getSetting("inputstream") == "true":
            li.setMimeType("application/vnd.apple.mpegurl")
            li.setProperty("inputstreamaddon", "inputstream.adaptive")
            li.setProperty("inputstream.adaptive.manifest_type", "hls")
            li.setProperty("inputstream.adaptive.stream_headers", media_url.split("|")[-1])
        else:
            li.setMimeType("application/vnd.apple.mpegurl")
    else:
        li.setMimeType("video/x-mpegts")

    li.setArt({"thumb": image, "icon": image})
    li.setContentLookup(False)
    xbmcplugin.setResolvedUrl(plugin.handle, True, li)


if __name__ == "__main__":
    try:
        plugin.run(sys.argv)
        s.cookies.save(ignore_discard=True, ignore_expires=True)
        s.close()
    except requests.exceptions.RequestException as e:
        dialog = xbmcgui.Dialog()
        dialog.notification(plugin.name, str(e), xbmcgui.NOTIFICATION_ERROR)
        traceback.print_exc()
        xbmcplugin.endOfDirectory(plugin.handle, False)
    except (ImportError, UnicodeDecodeError):
        """ Invalidate cache when requests version changes """
        s.cache.clear()
