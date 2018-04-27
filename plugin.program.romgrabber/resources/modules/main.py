import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,os,xbmcaddon,time

try:
     from addon.common.addon import Addon
     print 'Using addon.common.addon'
except:
     from tommo.common.addon import Addon
     print 'Using tommo.common.addon'

try:     
     from addon.common.net import Net
     print 'Using addon.common.net'
except:
     from tommo.common.net import Net
     print 'Using tommo.common.net'

try:
     import threading
except:
     print 'Failed To Import threading'
     xbmcplugin.endOfDirectory(int(sys.argv[1]))
         
try:
     import StorageServer
     print 'Using StorageServer'
except:
     import storageserverdummy as StorageServer
     print 'Using storageserverdummy'

try:
     from sqlite3 import dbapi2 as lite
     print 'Using Sqlite3'
except:
     from pysqlite2 import dbapi2 as lite
     print 'Using Sqlite2'

try:
     from resources.modules import extract
except:
     print 'Failed to import extract'
     pass

try:
     from resources.modules import py7zlib 
except:
     print 'Failed to import py7zlib'
     pass

cache = StorageServer.StorageServer("RomGrabber", 0)
 
addon_id = 'plugin.program.romgrabber'
addon = Addon(addon_id, sys.argv)

mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
ext = addon.queries.get('ext', '')
console = addon.queries.get('console', '')

settings = xbmcaddon.Addon(id=addon_id)
artwork = xbmc.translatePath(os.path.join('http://addonrepo.com/xbmchub/o9r1sh1/romgrabber/artwork', ''))
net = Net()

download_path = settings.getSetting('dl_path')

class downloadThread (threading.Thread):
     def __init__(self):
          threading.Thread.__init__(self)
          
     def addQDir(self,name,url,mode,thumb,console):
          contextMenuItems = []

          fanart = artwork + '/fanarts/' + console + '.gif'
          fanart = fanart.replace(' ','-')
          
          params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb,'console':console, 'ext':ext}

          contextMenuItems.append(('Remove From Queue', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 'removeFromQueue', 'name': name,'url': url,'thumb': thumb,'ext': ext,'console': console})))

          if os.path.exists(xbmc.translatePath("special://home/addons/plugin.program.advanced.launcher")):
               contextMenuItems.append(('Open Advanced Launcher','XBMC.RunAddon(plugin.program.advanced.launcher)'))
          if os.path.exists(xbmc.translatePath("special://home/addons/script.games.rom.collection.browser")):
               contextMenuItems.append(('Open Rom Collection Browser','XBMC.RunAddon(script.games.rom.collection.browser)'))

          contextMenuItems.append(('Addon Settings', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 'addonSettings', 'name': name,'url': url,'thumb': thumb,'ext': ext,'console': console})))

          addon.add_directory(params, {'title':name}, contextmenu_items=contextMenuItems, context_replace=True, img=thumb, fanart=fanart)

     def addDir(self,name,url,mode,thumb,console):
          contextMenuItems = []

          if os.path.exists(xbmc.translatePath("special://home/addons/plugin.program.advanced.launcher")):
               contextMenuItems.append(('Open Advanced Launcher','XBMC.RunAddon(plugin.program.advanced.launcher)'))
          if os.path.exists(xbmc.translatePath("special://home/addons/script.games.rom.collection.browser")):
               contextMenuItems.append(('Open Rom Collection Browser','XBMC.RunAddon(script.games.rom.collection.browser)'))

          contextMenuItems.append(('Addon Settings', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 'addonSettings', 'name': name,'url': url,'thumb': thumb,'ext': ext,'console': console})))

          fanart = artwork + '/fanarts/' + console + '.gif'
          fanart = fanart.replace(' ','-')
          
          params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'ext':ext, 'console':console}
          addon.add_directory(params, {'title':name}, contextmenu_items=contextMenuItems, context_replace=True, img= thumb, fanart=fanart)

     def viewQueue(self):
          self.addDir('[COLOR blue]Start Downloads[/COLOR]','none','download',artwork + '\other\downloads_start.gif','none')

          queue = cache.get('queue')
          if queue:
               queue_items = sorted(eval(queue), key=lambda item: item[1])
               
               for item in queue_items:
                    self.addQDir(item[0],item[1],'viewQueue',item[2],item[4])

     def addToQueue(self,name,url,thumb,ext,console):
          if '.zip' in url:
               ext = '.zip'
          if '.7z' in url:
               ext = '.7z'

          name = name.replace(':','')

          queue = cache.get('queue')
          queue_items = []
          if queue:
               queue_items = eval(queue)
               if queue_items:
                    if (name,url,thumb,ext,console) in queue_items:
                         addon.show_small_popup(title='Item Already In Your Queue', msg=name + ' Is Already In Your Download Queue', delay=int(5000), image=thumb)
                         return
          queue_items.append((name,url,thumb,ext,console))
          cache.set('queue', str(queue_items))
          if not ' - Download Failed' in name:
               addon.show_small_popup(title='Item Added To Your Queue', msg=name + ' Was Added To Your Download Queue', delay=int(5000), image=thumb)
          
     def removeFromQueue(self,name,url,thumb,ext,console):
          queue = cache.get('queue')
          if queue:
               queue_items = sorted(eval(queue), key=lambda item: item[1])
               try:
                    queue_items.remove((name,url,thumb,'.zip',console))
               except:
                    queue_items.remove((name,url,thumb,'.7z',console))
               cache.set('queue', str(queue_items))
               xbmc.executebuiltin("XBMC.Container.Refresh")

     def download(self):
          if download_path == '':
               addon.show_small_popup(title='File Not Downloadable', msg='You need to set your download folder in addon settings first', delay=int(5000), image='')
          else:
               self.start()
                         
     def run(self):
          queue = cache.get('queue')

          if queue:
               queue_items = sorted(eval(queue), key=lambda item: item[1])
               for item in queue_items:
                    time.sleep(2.5)

                    self.name = item[0]
                    self.url = item[1]
                    self.thumb = item[2]
                    self.ext = item[3]
                    self.console = item[4]
                              
                    self.path = os.path.join(download_path, self.console)
                    if not os.path.exists(self.path):
                         os.makedirs(self.path)

                    self.file_name = self.name + self.ext
                    filePath = os.path.join(self.path,self.file_name)

                    if not ' - Download Failed' in self.name:

                         try:
                              u = urllib.urlopen(self.url)
                              addon.show_small_popup(title='Downloads Started', msg=self.name + ' Is Downloading', delay=int(5000), image=self.thumb)

                              f = open(filePath, 'wb')
                              meta = u.info()
                              file_size = int(meta.getheaders("Content-Length")[0])

                              file_size_dl = 0
                              block_sz = 8192
                              while True:
                                   buffer = u.read(block_sz)
                                   if not buffer:
                                        break

                                   file_size_dl += len(buffer)
                                   f.write(buffer)
                                   status = int( file_size_dl * 1000. / file_size)

                                   if status > 99 and status < 101:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='10% Complete',delay=int(1000), image=self.thumb)

                                   elif status > 199 and status < 201:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='20% Complete',delay=int(1000), image=self.thumb)

                                   elif status > 299 and status < 301:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='30% Complete',delay=int(1000), image=self.thumb)

                                   elif status > 399 and status < 401:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='40% Complete',delay=int(1000), image=self.thumb)

                                   elif status > 499 and status < 501:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='50% Complete',delay=int(1000), image=self.thumb)

                                   elif status > 599 and status < 601:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='60% Complete',delay=int(1000), image=self.thumb)

                                   elif status > 699 and status < 701:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='70% Complete',delay=int(1000), image=self.thumb)

                                   elif status > 799 and status < 801:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='80% Complete',delay=int(1000), image=self.thumb)

                                   elif status > 899 and status < 901:
                                        print self.thumb
                                        addon.show_small_popup(title=self.name, msg='90% Complete',delay=int(1000), image=self.thumb)
                                  
                              f.close()
                              time.sleep(2.5)
                              addon.show_small_popup(title='Download Complete', msg=self.name + ' Finished Downloading', delay=int(5000), image=self.thumb)

                              
                              extractArchive(os.path.join(self.path, self.file_name), os.path.join(self.path, self.name), self.console)
                              self.removeFromQueue(self.name,self.url,self.thumb,self.ext,self.console)

                         except:
                              self.removeFromQueue(self.name,self.url,self.thumb,self.ext,self.console)
                              self.name = '[COLOR red]%s[/COLOR]' % self.name + '[COLOR red] - Download Failed[/COLOR]'
                              addon.show_small_popup(title='Error', msg=self.name + ' There Was A Issue With This File', delay=int(5000), image=self.thumb)
                              self.addToQueue(self.name,self.url,self.thumb,self.ext,self.console)
                              print 'Failed To Fetch File'
                              pass
                    else:
                         pass
                                     
downloader = downloadThread()

def addDir(name,url,mode,thumb,console):
     
     contextMenuItems = []
     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.program.advanced.launcher")):
          contextMenuItems.append(('Open Advanced Launcher','XBMC.RunAddon(plugin.program.advanced.launcher)'))
     if os.path.exists(xbmc.translatePath("special://home/addons/script.games.rom.collection.browser")):
          contextMenuItems.append(('Open Rom Collection Browser','XBMC.RunAddon(script.games.rom.collection.browser)'))

     contextMenuItems.append(('Addon Settings', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 'addonSettings', 'name': name,'url': url,'thumb': thumb,'ext': ext,'console': console})))

     fanart = artwork + '/fanarts/' + console + '.gif'
     fanart = fanart.replace(' ','-')
     
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'ext':ext, 'console':console}
     addon.add_directory(params, {'title':name}, contextmenu_items=contextMenuItems, context_replace=True, img= thumb, fanart=fanart)

def addGDir(name,url,mode,thumb,console):

     meta = []

     if settings.getSetting('meta') == 'true':
          meta = scrapeTitle(name,console)

     contextMenuItems = []
     
     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.program.advanced.launcher")):
          contextMenuItems.append(('Open Advanced Launcher','XBMC.RunAddon(plugin.program.advanced.launcher)'))
     if os.path.exists(xbmc.translatePath("special://home/addons/script.games.rom.collection.browser")):
          contextMenuItems.append(('Open Rom Collection Browser','XBMC.RunAddon(script.games.rom.collection.browser)'))

     contextMenuItems.append(('Addon Settings', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 'addonSettings', 'name': name,'url': url,'thumb': thumb,'ext': ext,'console': console})))

     fanart = artwork + '/fanarts/' + console + '.gif'
     fanart = fanart.replace(' ','-')

     if meta:
          thumb = meta['thumb']
          properties = {'Addon.Description':meta['plot'], 'Addon.Creator':meta['author'], 'Addon.Version':console}
          
          params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'ext':ext, 'console':console}
          addon.add_directory(params, meta, properties=properties, contextmenu_items=contextMenuItems, context_replace=True, img=thumb, fanart=fanart)

     else:
          params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'ext':ext, 'console':console}
          addon.add_directory(params, {'title':name}, contextmenu_items=contextMenuItems, context_replace=True, img=thumb, fanart=fanart)
     
def extractArchive(archive_file, archive_path, console):
     if '.zip' in archive_file:
          if settings.getSetting('extractZip') == 'true':
               if settings.getSetting(console + ' Zip') == 'true':
                    if not os.path.exists(archive_path):
                         os.makedirs(archive_path)
                    extract.allNoProgress(archive_file, archive_path)
                    os.remove(archive_file)

     if '.7z' in archive_file:
          if settings.getSetting('extract7Zip') == 'true':
               if settings.getSetting(console + ' 7Zip') == 'true':
                    if not os.path.exists(archive_path):
                         os.makedirs(archive_path)
                    extract7z(archive_file,archive_path)
                    os.remove(archive_file)

#Thanks to malte for the 7z handling code.                   
def extract7z(archive_file,archive_path):
     names = getNames7z(archive_file)
     archives = getArchives7z(archive_file, names)

     for archive in archives:
          newPath = os.path.join(archive_path, archive[0])
          fp = open(newPath, 'wb')
          fp.write(archive[1])
          fp.close()

def getNames7z(filepath):
	fp = open(str(filepath), 'rb')
	archive = py7zlib.Archive7z(fp)
	names = archive.getnames()
	fp.close()
	return names
     
def getArchives7z(filepath, archiveList):
	fp = open(str(filepath), 'rb')
	archive = py7zlib.Archive7z(fp)
	archivesDecompressed =  [(name, archive.getmember(name).read())for name in archiveList]
	fp.close()
	return archivesDecompressed     

def scrapeTitle(name,console):
     baseScraperUrl = 'http://www.gamefaqs.com'
     scraperUrl = ''
     consoleID = ''

     cover_url = ''
     description = ''
     company = ''
     
     dbPath = xbmc.translatePath(os.path.join('special://userdata/Database/', ''))
     dbPath = dbPath + 'romgrabber.db'
     
     con = lite.connect(dbPath)
     cur = con.cursor()
     cur.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, console TEXT, cover_url TEXT, description TEXT, author TEXT)')

     cur.execute('SELECT * FROM data WHERE name = "%s"' % name)
     cached = cur.fetchone()

     meta = []

     if cached:
          meta = {'title':name, 'thumb':cached[2], 'plot':cached[3], 'author':cached[4]}
          return meta

     else:
          if console == 'Atari Jaguar':
               consoleID = '72'

          elif console == 'Atari Lynx':
               consoleID = '58'

          elif console == 'CPS2':
               consoleID = '2'

          elif console == 'MAME':
               consoleID = '2'

          elif console == 'Neo Geo':
               consoleID = '64'

          elif console == 'Neo Geo Pocket':
               consoleID = '89'

          elif console == 'Nintendo':
               consoleID = '41'

          elif console == 'Nintendo 64':
               consoleID = '84'

          elif console == 'Nintendo GameBoy Advance':
               consoleID = '91'

          elif console == 'Nintendo GameBoy Color':
               consoleID = '57'

          elif console == 'Super Nintendo':
               consoleID = '63'

          elif console == 'Sega CD':
               consoleID = '65'

          elif console == 'Sega Dreamcast':
               consoleID = '67'

          elif console == 'Sega Game Gear':
               consoleID = '62'

          elif console == 'Sega Genesis':
               consoleID = '54'

          elif console == 'Sega Master System':
               consoleID = '49'

          elif console == 'Sony Playstation':
               consoleID = '78'

          scraperUrl = baseScraperUrl + '/search/index.html?platform=' + consoleID + '&game=' + name

          scraperUrl = scraperUrl.replace(' ','%20')
          
          link = net.http_GET(scraperUrl).content
          match=re.compile('<td class="rtitle">\r\n                                <a href="(.+?)"\r\n                                class=".+?">.+?</a>').findall(link)
          

          if len(match) > 0:
               gameUrl = baseScraperUrl + str(match[0])

               imageUrl = gameUrl + '/images'
               
               link = net.http_GET(gameUrl).content
               imageLink = net.http_GET(imageUrl).content

               match=re.compile('<div class="head"><h2 class="title">Description</h2></div><div class="body game_desc"><div class="desc">(.+?)</div>').findall(link)
               imageMatch=re.compile('<a href=".+?"><img class=".+?" src="(.+?)" alt="(.+?)" />').findall(imageLink)
               companyMatch=re.compile('href="/features/company/.+?">(.+?)</a></li>').findall(link)

               if len(companyMatch) > 0:
                    temp = str(companyMatch[0])
                    company,b,c = temp.partition('<')
               if len(match) > 0:
                    description = str(match[0])
               if len(imageMatch) > 0:
                    for thumbnail, title in imageMatch:
                         cover_url = thumbnail
                    
          statement = 'INSERT INTO data (name, console, cover_url, description, author) VALUES (?,?,?,?,?)'
          cur.execute(statement, (name, console, cover_url, description, company))
          con.commit()

          cur.execute('SELECT * FROM data WHERE name = "%s"' % name)

          cached = cur.fetchone()
          if cached:
               meta = {'title':name, 'thumb':cached[2], 'plot':cached[3], 'author':cached[4]}
               return meta
                  
          else:
               return False

def autoView(content):
     if content:
          xbmcplugin.setContent(int(sys.argv[1]), 'addons')
          if settings.getSetting('auto-view') == 'true':
               if content == 'addons':
                    xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('addonsView'))
               else:
                    xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('default-view'))
               
def generateConsoleFolders():
     rootFolder = ''
     artworkFolder =''
     if not download_path == '':
          if not os.path.exists(os.path.join(download_path,'Atari Jaguar')):
               rootFolder = os.path.join(download_path,'Atari Jaguar')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))

          if not os.path.exists(os.path.join(download_path,'Atari Lynx')):
               rootFolder = os.path.join(download_path,'Atari Lynx')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)

                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))

          if not os.path.exists(os.path.join(download_path,'CPS2')):
               rootFolder = os.path.join(download_path,'CPS2')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'MAME')):
               rootFolder = os.path.join(download_path,'MAME')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Neo Geo')):
               rootFolder = os.path.join(download_path,'Neo Geo')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Neo Geo Pocket')):
               rootFolder = os.path.join(download_path,'Neo Geo Pocket')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Nintendo')):
               rootFolder = os.path.join(download_path,'Nintendo')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Nintendo 64')):
               rootFolder = os.path.join(download_path,'Nintendo 64')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Nintendo GameBoy Advance')):
               rootFolder = os.path.join(download_path,'Nintendo GameBoy Advance')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Nintendo GameBoy Color')):
               rootFolder = os.path.join(download_path,'Nintendo GameBoy Color')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Super Nintendo')):
               rootFolder = os.path.join(download_path,'Super Nintendo')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Sega CD')):
               rootFolder = os.path.join(download_path,'Sega CD')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Sega Dreamcast')):
               rootFolder = os.path.join(download_path,'Sega Dreamcast')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Sega Game Gear')):
               rootFolder = os.path.join(download_path,'Sega Game Gear')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Sega Genesis')):
               rootFolder = os.path.join(download_path,'Sega Genesis')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Sega Master System')):
               rootFolder = os.path.join(download_path,'Sega Master System')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    
          if not os.path.exists(os.path.join(download_path,'Sony Playstation')):
               rootFolder = os.path.join(download_path,'Sony Playstation')
               artworkFolder = os.path.join(rootFolder,'_Artwork')
               os.makedirs(rootFolder)
               if settings.getSetting('artworkFolders') == 'true':
                    os.makedirs(artworkFolder)
                    
                    os.makedirs(os.path.join(artworkFolder,'boxfront'))
                    os.makedirs(os.path.join(artworkFolder,'boxback'))
                    os.makedirs(os.path.join(artworkFolder,'cartridge'))
                    os.makedirs(os.path.join(artworkFolder,'screenshot'))
                    os.makedirs(os.path.join(artworkFolder,'fanart'))
                    os.makedirs(os.path.join(artworkFolder,'action'))
                    os.makedirs(os.path.join(artworkFolder,'title'))
                    os.makedirs(os.path.join(artworkFolder,'3dbox'))
                    os.makedirs(os.path.join(artworkFolder,'romcollection'))
                    os.makedirs(os.path.join(artworkFolder,'developer'))
                    os.makedirs(os.path.join(artworkFolder,'publisher'))
                    os.makedirs(os.path.join(artworkFolder,'gameplay(video)'))
                    os.makedirs(os.path.join(artworkFolder,'cabinet'))
                    os.makedirs(os.path.join(artworkFolder,'marquee'))
                    

     



     
        
