
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import shutil
import urllib2,urllib
import re
import extract
import downloader
import time
import plugintools
from addon.common.addon import Addon

addon_id = 'script.module.skinwizard'
AddonID = 'script.module.skinwizard'
AddonTitle = "Project X Wizard"
dialog = xbmcgui.Dialog()

ADDON = xbmcaddon.Addon(id=addon_id)
ADDONTITLE = 'Project X Wizard'
ART = xbmc.translatePath(os.path.join('special://home/addons/script.module.skinwizard' + '/resources/art/'))
BASEURL = "http://fanriffic.com"
DBPATH = xbmc.translatePath('special://database')
EXCLUDES = ['script.module.skinwizard','script.module.addon.common']
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
H = 'http://'
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
INTRO = xbmc.translatePath(os.path.join('special://home/addons/script.module.skinwizard/resources/intro.mp4'))  
PATH = "Project X Wizard"
THDATA = xbmc.translatePath('special://userdata/Thumbnails/')
TNPATH = xbmc.translatePath('special://thumbnails');
U = ADDON.getSetting('User')
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
VERSION = "1.0"
YTDATA = xbmc.translatePath('special://userdata/addon_data/plugin.video.youtube/')

def INTROS():            
    if ADDON.getSetting('intro') == "true":
        xbmcPlayer=xbmc.Player()
        xbmcPlayer.play(INTRO)
        xbmc.sleep(250)
        ADDON.setSetting('intro','false')
    else:
        pass
        if ADDON.getSetting('message') == "true":
            intro=xbmcgui.Dialog()
            msg = intro.ok("script.module.skinwizard",
                            "Force Close",
                            "Project X Wizard"
                            )
            if msg == True:
                ADDON.setSetting('message','false')
            else:
                pass
        else:
            pass      

INTROS()    

# MAIN MENU LAYOUT #

def INDEX():

    addDir('[COLOR cyan]NEW JARVIS SKINS [/COLOR] ',BASEURL,13,ART+'new.png',FANART,'newfan.jpg')
    addDir('[COLOR cyan]JARVIS SKINS [/COLOR]  ',BASEURL,41,ART+'jthemesarc.png',FANART,'newfan.jpg')  
    addDir('[COLOR cyan]JARVIS SKINS [/COLOR]  ',BASEURL,23,ART+'new.png',FANART,'newfan.jpg')	


    addDir('[COLOR cyan]NEW KRYPTON SKINS[/COLOR] ',BASEURL,40,ART+'kthemesarc.png',FANART,'buildfan.jpg')	
    addDir('[COLOR cyan]KRYPTON SKINS[/COLOR] ',BASEURL,37,ART+'krypton1.png',FANART,'splshfan.jpg')
    addDir('[COLOR cyan]KRYPTON SKINS[/COLOR]',BASEURL,38,ART+'krypton1.png',FANART,'splshfan.jpg')	
	
    addDir('[COLOR cyan]COMMUNITY BACKGROUNDS[/COLOR] ',BASEURL,42,ART+'backgrounds.png',FANART,'splshfan.jpg')
	
    addDir('[COLOR cyan]OLD SKINS[/COLOR] ',BASEURL,16,ART+'old.png',FANART,'oldfan.jpg')
	

    addDir('[COLOR cyan]OLD SKINS[/COLOR] ',BASEURL,24,ART+'old.png',FANART,'oldfan.jpg')




	
def THEMEOLDMENU():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/themeoldmenu.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
	
def THEMESNEWMENU():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/themesnewmenu.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
	


	
def KRYPTONMENU2():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/kryptonmenu2.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
    



	
def THEMEOLDMENU1():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/themeoldmenu1.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
	
def THEMESNEWMENU1():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/themesnewmenu1.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
	


	
def KRYPTONMENU3():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/kryptonmenu3.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')	
    
	



def KRYPTONTHEMESARC():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/kryptonthemesarc.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
	
	
def NEWTHEMESARC():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/newthemesarc.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')	

	
	
def BACKGROUNDS():
    link = OPEN_URL('http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/skins/backgrounds.xml').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')	
	

	
	
	
	
	
	
		

# MAINTENANCE MENU LAYOUT #

def MAINT():
    addDir('Delete Cache','url',9007,ART+'cache.png',FANART,'')
    addDir('Delete Packages','url',9008,ART+'packages.png',FANART,'')
    addDir('Delete Thumbnails','url',9013,ART+'thumbs.png',FANART,'')
    addDir('Fresh Start','url',9006,ART+'fresh.png',FANART,'')
    addDir('Reset YouTube','url',9009,ART+'youtube.png',FANART,'')
    addDir('Toggle Debug','url',9014,ART+'debug.png',FANART,'')
   
    addDir('Force Close','url',9010,ART+'killxbmc.png',FANART,'')
    setView('movies', 'MAIN')

#POPUP TEXT BOX #

def TextBoxes(heading,announce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(announce); text=f.read()
      except: text=announce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()

# POPUP MESSAGES #

def facebook():
    TextBoxes('Project X Wizard Support Tinyurl.com/Project X')

# BUILD MENU #

def WIZARD(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Project X Wizard","Downloading ",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"Project X Wizard", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("Project X Wizard", "To save changes you now need to force close Kodi, Press OK to force close Kodi")
    killxbmc()

# DELETE PACKAGES #

def deletepackages(url):
    print '############################################################       DELETING PACKAGES             ###############################################################'
    packages_cache_path = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
    try:    
        for root, dirs, files in os.walk(packages_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Package Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                    dialog = xbmcgui.Dialog()
                    dialog.ok("Fanriffic Wizard", "Packages Successfuly Removed")
    except: 
        dialog = xbmcgui.Dialog()
        dialog.ok("Fanriffic Wizard", "Sorry we were not able to remove Package Files")

# DELETE CACHE FILES #

def deletecachefiles(url):
    print '############################################################       DELETING APP CACHE             ###############################################################'
    xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
    if os.path.exists(xbmc_cache_path)==True:    
        for root, dirs, files in os.walk(xbmc_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        try:
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
            else:
                pass
    wtf_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.whatthefurk/cache'), '')
    if os.path.exists(wtf_cache_path)==True:    
        for root, dirs, files in os.walk(wtf_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete WTF Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
            else:
                pass
    channel4_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.4od/cache'), '')
    if os.path.exists(channel4_cache_path)==True:    
        for root, dirs, files in os.walk(channel4_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete 4oD Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
            else:
                pass
    iplayer_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache'), '')
    if os.path.exists(iplayer_cache_path)==True:    
        for root, dirs, files in os.walk(iplayer_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete BBC iPlayer Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
            else:
                pass
    downloader_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/script.module.simple.downloader'), '')
    if os.path.exists(downloader_cache_path)==True:    
        for root, dirs, files in os.walk(downloader_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Simple Downloader Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
            else:
                pass
    itv_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.itv/Images'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(itv_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ITV Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
            else:
                pass
    temp_cache_path = os.path.join(xbmc.translatePath('special://home/temp'), '')
    if os.path.exists(temp_cache_path)==True:    
        for root, dirs, files in os.walk(temp_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete TEMP dir Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
            else:
                pass
    dialog = xbmcgui.Dialog()
    dialog.ok("Fanriffic Wizard", " All Cache Files Removed")

# RESET YOUTUBE #
def YTFix():
	dialog = xbmcgui.Dialog()
	if os.path.exists(YTDATA):
		try:
			shutil.rmtree(YTDATA)
		except:
			dialog.ok(ADDONTITLE,"[COLOR red]Oops, There Was An Error Removing Data![/COLOR]")
			sys.exit(0)
		dialog.ok(ADDONTITLE,"[COLOR aqua]Fixed!.[/COLOR]")
		xbmc.executebuiltin("Container.Refresh")
		sys.exit(0)
	else:
		dialog.ok(ADDONTITLE,"[COLOR orange]No YouTube Data Present![/COLOR]")
		sys.exit(0)

# FRESH START #

def freshstart(params):
    plugintools.log("freshstart.main_list "+repr(params)); yes_pressed=plugintools.message_yes_no(AddonTitle,"Do You Wish To Wipe Your","Curreny Kodi Configuration?")
    if yes_pressed:
        addonPath=xbmcaddon.Addon(id=AddonID).getAddonInfo('path'); addonPath=xbmc.translatePath(addonPath); 
        xbmcPath=os.path.join(addonPath,"..",".."); xbmcPath=os.path.abspath(xbmcPath); plugintools.log("freshstart.main_list xbmcPath="+xbmcPath); failed=False
        try:
            for root, dirs, files in os.walk(xbmcPath,topdown=True):
                dirs[:] = [d for d in dirs if d not in EXCLUDES]
                for name in files:
                    try: os.remove(os.path.join(root,name))
                    except:
                        if name not in ["Addons15.db","MyVideos75.db","Textures13.db","xbmc.log"]: failed=True
                        plugintools.log("Error Removing "+root+" "+name)
                for name in dirs:
                    try: os.rmdir(os.path.join(root,name))
                    except:
                        if name not in ["Database","userdata"]: failed=True
                        plugintools.log("Error Removing "+root+" "+name)
            if not failed: plugintools.log("freshstart.main_list All User Files Removed, You Now Have A Clean Install"); plugintools.message(AddonTitle,"The Process Is Complete, Kodi is now clean Fanriffic wizard ready to install new goodies","Please Exit And Reboot Your System In Order For The Changes To Be Applied.")
            else: plugintools.log("freshstart.main_list User files partially removed"); plugintools.message(AddonTitle,"The Process Is Complete, Kodi is now clean Fanriffic wizard ready to install new goodies","Please Exit And Reboot Your System In Order For The Changes To Be Applied.")
        except: plugintools.message(AddonTitle,"Problem found","Your settings has not been changed"); import traceback; plugintools.log(traceback.format_exc()); plugintools.log("freshstart.main_list NOT Removed")
        plugintools.add_item(action="",title="Now Exit And Reboot Your System",folder=False)
    else: plugintools.message(AddonTitle,"Your Settings","Have Not Been Changed"); plugintools.add_item(action="",title="Done",folder=False)

# OPEN URL #

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

# FORCE CLOSE KODI #

def killxbmc():
    choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    if choice == 0:
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os._exit(1)
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass        
        dialog.ok("[COLOR=yellow][B]TO COMPLETE Fanriffic UPDATE[/COLOR][/B]", "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI")
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.","iOS detected.  Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo.")    

# DELETE THUMBNAILS #

def clearthumb():
	dialog=xbmcgui.Dialog()
	if dialog.yesno(ADDONTITLE, "Delete The Thumbnails Folder?" , "They Will Re-Populate On startup", nolabel='No, Cancel',yeslabel='Yes, Delete'):
		shutil.rmtree(THDATA)
		killxbmc()

# CHECK PLATFORM #
def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

# GET PARAMS #

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

# ADD DIRECTORY #

def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])

except:
        pass

print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

# SET VIEW TYPE #

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('Auto-View')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )

# VARIABLES #

if mode==None or url==None or len(url)<1:
        INDEX()
elif mode==5:
        WIZARD(name,url,description)

elif mode==2:
        BUILDMENU()	
		
elif mode==12:
        BUILDTHEMESMENU()		
		
elif mode==13:
        THEMESNEWMENU()



elif mode==15:
        UPDATESMENU()	

elif mode==16:
        THEMEOLDMENU()	
		
elif mode==17:
        BUILDUPMENU()	
		
elif mode==18:
        KRYPTONMENU()			
		
elif mode==19:
        SERVER1()

elif mode==20:
        SERVER2()

	
elif mode==21:
       BUILDMENU1()


		
elif mode==23:
        THEMESNEWMENU1()		
		
elif mode==24:
        THEMEOLDMENU1()

elif mode==25:
        BUILDUPMENU1()



elif mode==27:
        KRYPTONMENU1()	
		
elif mode==28:
        SERVER3()	
		
elif mode==29:
        REQUESTEDBUILDS()			
		


elif mode==31:
        REQUESTEDTHEMES()
		
		
elif mode==32:
        OTHER()


elif mode==33:
        UPDATESMENU1()




elif mode==37:
        KRYPTONMENU2()

elif mode==38:
        KRYPTONMENU3()

elif mode==39:
        SERVER4()	
		
elif mode==40:
        KRYPTONTHEMESARC()

elif mode==41:
        NEWTHEMESARC()	
				
elif mode==42:
        BACKGROUNDS()		
		
elif mode==9006:        
	    freshstart(params)
elif mode==9007:
        deletecachefiles(url)
elif mode==9008:
       deletepackages(url)
elif mode==9009:
       YTFix()
elif mode==9010:
       killxbmc()
elif mode==9011:
        MAINT()
elif mode==9012:
        facebook()
elif mode==9013:
        clearthumb()
elif mode==9014:
        xbmc.executebuiltin("ToggleDebug")
		
xbmcplugin.endOfDirectory(int(sys.argv[1]))

