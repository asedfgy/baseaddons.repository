# -*- coding: UTF-8 -*-


import base64,json,re,traceback,urllib,urlparse

from resources.lib.modules import client
from resources.lib.modules import cleantitle
from resources.lib.modules import directstream
from resources.lib.modules import dom_parser2
from resources.lib.modules import log_utils

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['123hulu.com','123hulu.unblockall.org']
        self.base_link = 'http://123hulu.unblockall.org'
        self.search_link = '%s/search?q=123hulu.unblockall.org+%s+%s'
        self.goog = 'https://www.google.co.uk'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            scrape = cleantitle.geturl(title)
            start_url = self.search_link %(self.goog,scrape,year)
            html = client.request(start_url, timeout='10')
            results = client.parseDOM(html, 'a', ret='href')
            for url in results:
                if self.base_link in url:
                    if 'webcache' in url:
                        continue
                    if cleantitle.get(title) in cleantitle.get(url):
                        if year in cleantitle.get(url):
                            return url
            return
        except:
            failure = traceback.format_exc()
            log_utils.log('123Hulu - Exception: \n' + str(failure))
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year, 'aliases': aliases}
            url = urllib.urlencode(url)
            return url
        except:
            failure = traceback.format_exc()
            log_utils.log('123Hulu - Exception: \n' + str(failure))
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return

            urldata = urlparse.parse_qs(url)
            urldata = dict((i, urldata[i][0]) for i in urldata)
            tvshowtitle = cleantitle.geturl(urldata['tvshowtitle'])

            season_str = 'season %01d' % (int(season))
            episode_str = 'episode %01d' % (int(episode))
            start_url = self.search_link %(self.goog,tvshowtitle,season_str.replace(' ', '+'))
            html = client.request(start_url, timeout='10')
            results = client.parseDOM(html, 'a', ret='href')
            for url in results:
                if self.base_link in url:
                    if 'webcache' in url:
                        continue
                    if cleantitle.get(urldata['tvshowtitle']) in cleantitle.get(url):
                        if cleantitle.get(season_str) in cleantitle.get(url):
                            chkhtml = client.request(url)
                            chktitle = re.compile('<title>(.+?)</title>',re.DOTALL).findall(chkhtml)[0]
                            if cleantitle.get(urldata['tvshowtitle']) in cleantitle.get(chktitle):
                                if cleantitle.get(season_str) in cleantitle.get(chktitle):
                                    episode_list = client.parseDOM(chkhtml, 'div', attrs={'class':'section-box'})[0]
                                    episode_link = client.parseDOM(episode_list, 'a', ret='href')[int(episode)-1]
                                    return episode_link
            return
        except:
            failure = traceback.format_exc()
            log_utils.log('123Hulu - Exception: \n' + str(failure))
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            if url == None or not 'http' in url: return
            sources = []

            log_utils.log('url: ' + str(url))
            html = client.request(url)
            servers = client.parseDOM(html, 'div', attrs={'class':'server_line'})
            if len(servers) == 0:
                servers = client.parseDOM(html, 'div', attrs={'class':'server_line.+?'})
            log_utils.log('servers: ' + str(servers))
            for line in servers:
                try:
                    vid_page = client.parseDOM(line, 'a', ret='href')[0]
                    log_utils.log('vid_page: ' + str(vid_page))
                    host_html = client.request(vid_page)
                    vid_url = re.findall('document.write.+?"([^"]*)', host_html)[0]
                    vid_url = base64.b64decode(vid_url)
                    vid_url = re.findall('src="([^"]*)', vid_url)[0]
                    log_utils.log('vid_url: ' + str(vid_url))
                    host = vid_url.split('//')[1].replace('www.','')
                    host = host.split('/')[0].split('.')[0].title()
                    if str(host).lower() in str(hostDict):
                        log_utils.log('host: ' + str(host))
                        sources.append({ 'source': host, 'quality': 'SD', 'language': 'en', 'url': vid_url, 'direct': False, 'debridonly': False })
                except:
                    failure = traceback.format_exc()
                    log_utils.log('123Hulu - Exception: \n' + str(failure))
                    return sources
            return sources
        except:
            failure = traceback.format_exc()
            log_utils.log('123Hulu - Exception: \n' + str(failure))
            return sources

    def resolve(self, url):
        return url