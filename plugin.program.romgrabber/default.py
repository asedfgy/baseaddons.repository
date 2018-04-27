import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,os,xbmcaddon

from resources.modules import main
from resources.modules import freeroms

addon_id = 'plugin.program.romgrabber'
addon = main.addon

mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
ext = addon.queries.get('ext', '')
console = addon.queries.get('console', '')

print 'Mode is: ' + mode
print 'Url is: ' + url
print 'Name is: ' + name
print 'Thumb is: ' + thumb
print 'Extension is: ' + ext
print 'Console is: ' + console

settings = xbmcaddon.Addon(id=addon_id)
artwork = main.artwork
net = main.net
downloader = main.downloader

if main.download_path == '':
     dialog = xbmcgui.Dialog()
     ok = dialog.ok('Download Directory Not Set', 'Please Choose A Download Directory')
     if ok:
          addon.show_settings()
          ok = dialog.ok('Please Restart The Addon', 'Please Exit And Re-Enter The Addon')
          xbmcplugin.endOfDirectory(int(sys.argv[1]))
               
def categories():
     main.generateConsoleFolders()
     main.addDir('[COLOR blue]Manage Downloads[/COLOR]','none','viewQueue',artwork + '/other/downloads_manage.gif','none')
     main.addDir('Atari Jaguar','http://www.freeroms.com/atari_jaguar.htm','lettersIndex',artwork + '/consoles/jaguar.gif','Atari Jaguar')
     main.addDir('Atari Lynx','http://www.freeroms.com/atari_lynx.htm','lettersIndex',artwork + '/consoles/lynx.gif','Atari Lynx')
     main.addDir('CPS2','http://www.freeroms.com/cps2.htm','lettersIndex',artwork + '/consoles/cps2.gif','CPS2')
     main.addDir('MAME','http://www.freeroms.com/mame.htm','lettersIndex',artwork + '/consoles/mame.gif','MAME')
     main.addDir('Neo Geo','http://www.freeroms.com/neogeo.htm','lettersIndex',artwork + '/consoles/neogeo.gif','Neo Geo')
     main.addDir('Neo Geo Pocket','http://www.freeroms.com/neogeo_pocket.htm','lettersIndex',artwork + '/consoles/neogeopocket.gif','Neo Geo Pocket')
     main.addDir('Nintendo','http://www.freeroms.com/nes.htm','lettersIndex',artwork + '/consoles/nintendo.gif','Nintendo')
     main.addDir('Nintendo 64','http://www.freeroms.com/n64.htm','lettersIndex',artwork + '/consoles/nintendo64.gif','Nintendo 64')
     main.addDir('Nintendo GameBoy Advance','http://www.freeroms.com/gameboy_advance.htm','lettersIndex',artwork + '/consoles/gameboyadvance.gif','Nintendo GameBoy Advance')
     main.addDir('Nintendo GameBoy Color','http://www.freeroms.com/gameboy_color.htm','lettersIndex',artwork + '/consoles/gameboycolor.gif','Nintendo GameBoy Color')
     main.addDir('Super Nintendo','http://www.freeroms.com/snes.htm','lettersIndex',artwork + '/consoles/supernintendo.gif','Super Nintendo')
     main.addDir('Sega CD','http://www.freeroms.com/sega_cd.htm','lettersIndex',artwork + '/consoles/segacd.gif','Sega CD')
     main.addDir('Sega Dreamcast','http://www.freeroms.com/sega_dreamcast.htm','lettersIndex',artwork + '/consoles/dreamcast.gif','Sega Dreamcast')
     main.addDir('Sega Game Gear','http://www.freeroms.com/game_gear.htm','lettersIndex',artwork + '/consoles/gamegear.gif','Sega Game Gear')
     main.addDir('Sega Genesis','http://www.freeroms.com/genesis.htm','lettersIndex',artwork + '/consoles/segagenesis.gif','Sega Genesis')
     main.addDir('Sega Master System','http://www.freeroms.com/sega_master_system.htm','lettersIndex',artwork + '/consoles/segamastersystem.gif','Sega Master System')
     main.addDir('Sony Playstation','http://www.freeroms.com/psx.htm','lettersIndex',artwork + '/consoles/playstation.gif','Sony Playstation')

     main.autoView('default')
     
if mode==None or url==None or len(url)<1:
        print ""
        categories()

elif mode=='lettersIndex':
        print ""+url
        freeroms.lettersIndex(url)

elif mode=='freeromsIndex':
        print ""+url
        freeroms.index(url)

elif mode=='freeromsRomLinks':
        print ""+url
        freeroms.romLinks(name,url)

elif mode=='viewQueue':
        print ""+url
        downloader.viewQueue()

elif mode=='download':
        xbmc.executebuiltin("XBMC.Action(ParentDir)")
        print ""+url
        downloader.download()

elif mode=='removeFromQueue':
        print ""+url
        downloader.removeFromQueue(name,url,thumb,ext,console)

elif mode=='addonSettings':
        print ""+url
        addon.show_settings()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
