# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
#
#      Modified for FTV Guide (09/2014 onwards)
#      by Thomas Geppert [bluezed] - bluezed.apps@gmail.com
#
#      Modified for Echo TV Guide (2016)
#      by primaeval - primaeval.dev@gmail.com
#
# This Program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with XBMC; see the file COPYING. If not, write to
# the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# http://www.gnu.org/copyleft/gpl.html
#

import os
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs

def deleteDB():
    try:
        xbmc.log("[script.tvsupertugaguide] Deleting database...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvsupertugaguide').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'source.db')

        delete_file(dbPath)

        passed = not os.path.exists(dbPath)

        if passed:
            xbmc.log("[script.tvsupertugaguide] Deleting database...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.tvsupertugaguide] Deleting database...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.tvsupertugaguide] Deleting database...EXCEPTION', xbmc.LOGDEBUG)
        return False

def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = int(sys.argv[1])

        if mode in [1,2]:
            if deleteDB():
                d = xbmcgui.Dialog()
                d.ok('Echo TV Guide', 'The database has been successfully deleted.', 'It will be re-created next time you start the guide')
            else:
                d = xbmcgui.Dialog()
                d.ok('Echo TV Guide', 'Failed to delete database.', 'Database may be locked,', 'Restart Kodi and Try Again')
        if mode == 2:
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/addons.ini')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/addons.ini.local')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/category_count.ini')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/categories.ini')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/custom_stream_urls.ini')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/channel_id_title.ini')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/mapping.ini')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/custom_stream_urls_autosave.ini')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/icons.ini')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/folders.list')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/tvdb.pickle')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/tvdb_banners.pickle')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/settings.xml')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/guide.xml')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/guide.xml.md5')
        if mode == 3:
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/tvdb.pickle')
            xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/tvdb_banners.pickle')
        if mode in [2,4]:
            dirs, files = xbmcvfs.listdir('special://profile/addon_data/script.tvsupertugaguide/logos')
            for f in files:
                xbmcvfs.delete('special://profile/addon_data/script.tvsupertugaguide/logos/%s' % f)