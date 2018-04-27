import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,os,xbmcaddon
from resources.modules import main

addon_id = 'plugin.program.romgrabber'
addon = main.addon

mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
ext = addon.queries.get('ext', '')
console = addon.queries.get('console', '')

settings = main.settings
artwork = main.artwork
net = main.net

base_url = 'http://www.freeroms.com'
download_path = settings.getSetting('dl_path')
downloader = main.downloader

def lettersIndex(url):
     link = net.http_GET(url).content
     match=re.compile('\| <a href="(.+?)">(.+?)</a>').findall(link)

     main.addDir('[COLOR blue]Manage Downloads[/COLOR]','none','viewQueue',artwork + '/other/downloads_manage.gif','none')

     for url,name in match:
          if name =='#':
               main.addDir(name,url,'freeromsIndex',artwork + 'letters/hash.gif',console)
          else:
               art = artwork + 'letters/' + name + '.gif'
               art = art.replace(' ','-')
               main.addDir(name,url,'freeromsIndex',art,console)

     main.autoView('default')

def index(url):
     link = net.http_GET(url).content
     match=re.compile('<td align=left nowrap><a href="(.+?)">(.+?)</a>').findall(link)
     pages=re.compile('<a href="(.+?)"><font size=3><B><I>(.+?)</I>').findall(link)
     skipPages = len(pages) / 2
     inc = 1

     main.addDir('[COLOR blue]Manage Downloads[/COLOR]','none','viewQueue',artwork + '/other/downloads_manage.gif','none')

     for url, name in pages:
          if not inc > skipPages:
               name = '[COLOR blue]%s [/COLOR]' % console + '[COLOR blue]Roms Letters [/COLOR]' + '[COLOR blue]%s [/COLOR]' % name
               art = xbmc.translatePath('special://home/addons/plugin.program.romgrabber/icon.png')
               main.addDir(name,url,'freeromsIndex',art,console)
          inc += 1

     for url,name in match:
          if '<' in name:
               head,sep,tail = name.partition('<')
               name = head
          try:
               main.addGDir(name,url,'freeromsRomLinks',artwork + 'none',console) 
          except:
               pass
     main.autoView('addons')
          
def romLinks(name,url):
     xbmc.executebuiltin("XBMC.Action(PreviousMenu)")
     link = net.http_GET(url).content
     match=re.compile('server(.+?)="(.+?)"').findall(link)

     serverA=re.compile("' \+ server(.+?) \+ server.+? \+ '").findall(link)
     serverB=re.compile("' \+ server.+? \+ server(.+?) \+ '").findall(link)

     serverNumOneMatch = int(serverA[0])
     serverNumTwoMatch = int(serverB[0])

     head = ''
     tail = ''

     for number,content in match:
          if int(number) == serverNumOneMatch:
               head = str(content)

          if int(number) == serverNumTwoMatch:
               tail = str(content)

     url = head + tail
       
     downloader.addToQueue(name,url,thumb,'',console)

     


     
     
     

     
     
          


     

 

