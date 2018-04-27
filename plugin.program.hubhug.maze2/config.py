## from config import Config as Config

import xbmc,xbmcaddon,xbmcplugin,os
_addon_id="plugin.program.hubhug.maze2"; _addon_name="HUB-HUG Exit The Maze 2"; 
_addon=xbmcaddon.Addon(id=_addon_id); 

def gAI(t):
	try: return _addon.getAddonInfo(t)
	except: 
		#if t=="name": return _addon_name
		#else: return ""
		return ""

class Config:
	addon_id=_addon_id
	#name='Repositories Browser'
	addon=_addon
	handle=0
	name=gAI('name'); 
	#name="XBMCHUB Repositories Browser"; 
	path=gAI('path'); 
	#profile=xbmc.translatePath(gAI('profile'))
	disclaimer=gAI('disclaimer'); description=gAI('description'); summary=gAI('summary'); 
	icon=gAI('icon'); fanart=gAI('fanart'); 
	addon_type=gAI('type'); author=gAI('author'); version=gAI('version'); stars=gAI('stars'); changelog=gAI('changelog'); 
	
	artPath=xbmc.translatePath(os.path.join(path,'art'))
	
	
	ACTION_PREVIOUS_MENU 		=  10	## ESC action
	ACTION_NAV_BACK 				=  92	## Backspace action
	ACTION_MOVE_LEFT 				=   1	## Left arrow key
	ACTION_MOVE_RIGHT 			=   2	## Right arrow key
	ACTION_MOVE_UP 					=   3	## Up arrow key
	ACTION_MOVE_DOWN 				=   4	## Down arrow key
	ACTION_MOUSE_WHEEL_UP 	= 104	## Mouse wheel up
	ACTION_MOUSE_WHEEL_DOWN = 105	## Mouse wheel down
	ACTION_MOUSE_DRAG 			= 106	## Mouse drag
	ACTION_MOUSE_MOVE 			= 107	## Mouse move
	def gSetting(self,setting):
		try: return self.addon.getSetting(setting)
		except: return ""
	def set_setting(self,setting,value):
		self.addon.setSetting(id=setting,value=value)
	def get_string(self, string_id):
		try: return self.addon.getLocalizedString(string_id)
		except: return ""
	def get_id(self):
		try: return self.addon.getAddonInfo('id')
		except: return self.addon_id
	def note(self,title='',msg='',delay=5000,image='http://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/US_99_%281961%29.svg/40px-US_99_%281961%29.svg.png'):
		xbmc.executebuiltin('XBMC.Notification("%s","%s",%d,"%s")' % (title,msg,delay,image))
	def show_settings(self): self.addon.openSettings()
	def eod(self):
		xbmcplugin.endOfDirectory(self.handle)
	
	
	
	
	