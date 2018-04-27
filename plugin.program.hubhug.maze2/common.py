## ################################################## ##
## ################################################## ##
## Common functions for use by TheHighway.            ##
## ################################################## ##
## ################################################## ##
## import common as Common
## from common import *
## import common
## ################################################## ##
## ################################################## ##

import xbmc,xbmcgui,urllib,urllib2,os,sys,logging,array,re,time,datetime,random,string,StringIO,xbmcplugin,xbmcaddon
#import shutil
from config import Config as Config
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']; 

def cFL( t,c='tan'): return '[COLOR '+c+']'+t+'[/COLOR]' ### For Coloring Text ###
def cFL_(t,c='tan'): return '[COLOR '+c+']'+t[0:1]+'[/COLOR]'+t[1:] ### For Coloring Text (First Letter-Only) ###
def deb(s,t): ### for Writing Debug Data to log file ###
	#if (_debugging==True): 
	print s+':  '+t
def debob(t): ### for Writing Debug Object to log file ###
	#if (_debugging==True): 
	print t
def nolines(t):
	it=t.splitlines(); t=''
	for L in it: t=t+L
	t=((t.replace("\r","")).replace("\n",""))
	return t
def art(f,fe=''): return xbmc.translatePath(os.path.join(Config.artPath,f+fe))
def artp(f,fe='.png'): return art(f,fe)
def artj(f,fe='.jpg'): return art(f,fe)
def BusyAnimationShow(): 				xbmc.executebuiltin('ActivateWindow(busydialog)')
def BusyAnimationHide(): 				xbmc.executebuiltin('Dialog.Close(busydialog,true)')
def closeAllDialogs():   				xbmc.executebuiltin('Dialog.Close(all, true)') 
def popYN(title='',line1='',line2='',line3='',n='',y=''):
	diag=xbmcgui.Dialog()
	r=diag.yesno(title,line1,line2,line3,n,y)
	if r: return r
	else: return False
	#del diag
def popOK(msg="",title="",line2="",line3=""):
	dialog=xbmcgui.Dialog()
	#ok=dialog.ok(title, msg, line2, line3)
	dialog.ok(title, msg, line2, line3)
def note(title='',msg='',delay=5000,image='http://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/US_99_%281961%29.svg/40px-US_99_%281961%29.svg.png'): xbmc.executebuiltin('XBMC.Notification("%s","%s",%d,"%s")' % (title,msg,delay,image))
def repo(repository,filename='',h="special://home",a="addons"): 
	if len(filename)==0: return xbmc.validatePath(xbmc.translatePath(os.path.join(h,a,repository)))
	else: return xbmc.validatePath(xbmc.translatePath(os.path.join(h,a,repository,filename)))
def repox(repository,filename='',h="special://xbmc",a="addons"): 
	if len(filename)==0: return xbmc.validatePath(xbmc.translatePath(os.path.join(h,a,repository)))
	else: return xbmc.validatePath(xbmc.translatePath(os.path.join(h,a,repository,filename)))
def _SaveFile(path,data):
	file=open(path,'w')
	file.write(data)
	file.close()
def _OpenFile(path):
	#deb('File',path)
	if os.path.isfile(path): ## File found.
		#deb('Found',path)
		file = open(path, 'r')
		contents=file.read()
		file.close()
		return contents
	else: return '' ## File not found.
def _CreateDirectory(dir_path):
	dir_path = dir_path.strip()
	if not os.path.exists(dir_path): os.makedirs(dir_path)
def _get_dir(mypath, dirname): #...creates sub-directories if they are not found.
	subpath = os.path.join(mypath, dirname)
	if not os.path.exists(subpath): os.makedirs(subpath)
	return subpath
def getURL(url):
	try:
		req=urllib2.Request(url)
		req.add_header(MyBrowser[0],MyBrowser[1]) 
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()
		return(link)
	except: deb('Failed to fetch url',url); return ''
def postURL(url,form_data={},headers={},compression=True):
	try:
		req=urllib2.Request(url)
		if form_data: form_data=urllib.urlencode(form_data); req=urllib2.Request(url,form_data)
		req.add_header(MyBrowser[0],MyBrowser[1])
		for k, v in headers.items(): req.add_header(k, v)
		if compression: req.add_header('Accept-Encoding', 'gzip')
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link
	except: deb('Failed to fetch url',url); return ''
def postURL2(url,form_data={}):
	try:
		postData=urllib.urlencode(form_data)
		req=urllib2.Request(url,postData)
		req.add_header(MyBrowser[0], MyBrowser[1]) 
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()
		return(link)
	except: deb('Failed to fetch url',url); return ''
def setContent(content,h=0):
	h=Config.handle
	try: 		xbmcplugin.setContent(h,content)
	except: pass
def SettingG(setting):
	try: return Config.addon.getSetting(setting)
	except: return ""
def SettingS(setting,value): Config.addon.setSetting(id=setting,value=value)
def tfalse(r,d=False): ## Get True / False
	if   (r.lower()=='true' ) or (r.lower()=='t') or (r.lower()=='y') or (r.lower()=='1') or (r.lower()=='yes'): return True
	elif (r.lower()=='false') or (r.lower()=='f') or (r.lower()=='n') or (r.lower()=='0') or (r.lower()=='no'): return False
	else: return d
def showkeyboard(txtMessage="",txtHeader="",passwordField=False):
	try:
		if txtMessage=='None': txtMessage=''
		keyboard = xbmc.Keyboard(txtMessage, txtHeader, passwordField)#("text to show","header text", True="password field"/False="show text")
		keyboard.doModal()
		if keyboard.isConfirmed(): return keyboard.getText()
		else: return '' #return False
	except: return ''



## ################################################## ##
## ################################################## ##
