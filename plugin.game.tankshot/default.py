#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)

#############################################################################
#############################################################################
ACTION_PREVIOUS_MENU 		=  10	## ESC action
ACTION_NAV_BACK 				=  92	## Backspace action
ACTION_MOVE_LEFT 				=   1	## Left arrow key
ACTION_MOVE_RIGHT 			=   2	## Right arrow key
ACTION_MOVE_UP 					=   3	## Up arrow key
ACTION_MOVE_DOWN 				=   4	## Down arrow key
ACTION_MOUSE_CLICK_LEFT	= 101	## Mouse click left ??
ACTION_MOUSE_WHEEL_UP 	= 104	## Mouse wheel up
ACTION_MOUSE_WHEEL_DOWN = 105	## Mouse wheel down
ACTION_MOUSE_DRAG 			= 106	## Mouse drag
ACTION_MOUSE_MOVE 			= 107	## Mouse move
#
ACTION_KEY_P						=	 79	## P - Pause
ACTION_KEY_R						=	 78	## R - Rewind
ACTION_KEY_F						=	 77	## F - Fast Forward
ACTION_SELECT_ITEM			=		7	## ?
ACTION_PARENT_DIR				=		9	## ?
ACTION_CONTEXT_MENU			=	117	## ?
ACTION_NEXT_ITEM				=	 14	## ?
ACTION_BACKSPACE				=	110	## ?
#
ACTION_KEY_X						=	 13	## X - Stop
ACTION_aID_0						=	  0	## ???
#
ACTION_REMOTE_MUTE					=	 91	## MUTE
#ACTION_REMOTE_FULLSCREEN		=	 ??	## FullScreen
ACTION_REMOTE_INFO					=	 11	## Info
ACTION_REMOTE_PLAYPAUSE			=	 12	## Play / Pause
ACTION_REMOTE_CONTEXTMENU		=	117	## Context Menu
ACTION_REMOTE_STOP					=	 13	## Stop
#
ACTION_KEY_VOL_MINUS				=	 89	## F - Fast Forward
ACTION_KEY_VOL_PLUS					=	 88	## F - Fast Forward
#
ACTION_SHOW_FULLSCREEN			=  36 ## Show Full Screen
ACTION_TOGGLE_FULLSCREEN		= 199 ## Toggle Full Screen
#############################################################################
#############################################################################

d=xbmcgui.Dialog(); 

class CustomWindow(xbmcgui.WindowXML):
#class CustomWindow(xbmcgui.WindowXMLDialog):
		closing=False; firsttime=False; c={}; strXMLname=''; strFallbackPath=''; 
		maxW=1280; maxH=720; 
		
		##
		def __init__(self,strXMLname,strFallbackPath):
			self.strXMLname=strXMLname
			self.strFallbackPath=strFallbackPath
			##
		def onInit(self):
			try: self.wID=xbmcgui.getCurrentWindowId()
			except: self.wID=0
			deb('CurrentWindowId()',str(self.wID)); 
			deb('getResolution()',str(self.getResolution())); 
			self.firsttime=True
			
			debob(['screen size',self.getWidth(),self.getHeight()])
			debob(['skin size',self.maxW,self.maxH])
			
			self.LoadSkinItems()
			
			self.setupScreen()
			
			
			
			#try: self.setFocus(self.bExit)
			#except: pass
			pass
			##
		def ScrTp(self,s='',v='ScreenType'):
			try:
				if len(v) > 0:
					self.setProperty(v,s); 
			except: pass
		def setupScreen(self):
			#self.iBack.setImage(artp("black1")); 
			self.iBackground.setImage(MediaFile("back01.jpg")); 
			
			
			##
		def LoadSkinItems(self):
			try:
				self.c['iBack']=1; 
				self.c['iBackground']=2; 
				self.c['bExit']=10; 
				try: self.iBack=self.getControl(self.c['iBack']); 
				except: pass
				try: self.iBackground=self.getControl(self.c['iBackground']); 
				except: pass
				try: self.bExit=self.getControl(self.c['bExit']); 
				except: pass
				
				self.c['TestObj1']=5; 
				self.c['TestObj2']=400; 
				self.c['PlayerObj1']=400; 
				self.c['PlayerObj1Tank']=401; 
				self.c['PlayerObj1Line']=402; 
				self.c['TestObj3']=20; 
				self.c['TestObj4']=21; 
				self.c['TestObj5']=22; 
				try: self.TestObj1=self.getControl(self.c['TestObj1']); 
				except: pass
				try: self.TestObj2=self.getControl(self.c['TestObj2']); 
				except: pass
				try: self.TestObj3=self.getControl(self.c['TestObj3']); 
				except: pass
				try: self.TestObj4=self.getControl(self.c['TestObj4']); 
				except: pass
				try: self.TestObj5=self.getControl(self.c['TestObj5']); 
				except: pass
				try: self.PlayerObj1=self.getControl(self.c['PlayerObj1']); 
				except: pass
				try: self.PlayerObj1Tank=self.getControl(self.c['PlayerObj1Tank']); 
				except: pass
				try: self.PlayerObj1Line=self.getControl(self.c['PlayerObj1Line']); 
				except: pass
				self.EnemyObjs=[]
				self.EnemyObjsVis={}
				self.c['EnemyObj1'] =28; self.c['EnemyObj2'] =27; 
				self.c['EnemyObj3'] =26; self.c['EnemyObj4'] =25; 
				self.c['EnemyObj5'] =24; 
				self.c['EnemyObj6'] =29; self.c['EnemyObj7'] =30; 
				self.c['EnemyObj8'] =31; self.c['EnemyObj9'] =32; 
				self.c['EnemyObj10']=33; self.c['EnemyObj11']=34; 
				self.c['EnemyObj12']=35; self.c['EnemyObj13']=36; 
				self.c['EnemyObj14']=37; self.c['EnemyObj15']=38; 
				self.c['EnemyObj16']=39; self.c['EnemyObj17']=40; 
				self.c['EnemyObj18']=41; self.c['EnemyObj19']=42; 
				#try:
				Enemies=['EnemyObj1','EnemyObj2','EnemyObj3','EnemyObj4','EnemyObj5','EnemyObj6','EnemyObj7','EnemyObj8','EnemyObj9','EnemyObj10','EnemyObj11','EnemyObj12','EnemyObj13','EnemyObj14','EnemyObj15','EnemyObj16','EnemyObj17','EnemyObj18','EnemyObj19']; HowManyEnemies=0; 
				for a in Enemies:
					try:
						self.EnemyObjs.append([self.getControl(self.c[a]),a,self.c[a]]); self.EnemyObjsVis[a]=True; self.ScrTp('true',a+'Animate'); HowManyEnemies=HowManyEnemies+1; #debob(['Adding Tank',a]); 
					except: pass
				self.HowManyEnemies=HowManyEnemies; self.ScrTp(str(self.HowManyEnemies),'EnemiesRemaining'); 
				self.WaveNo=1; self.ScrTp(str(self.WaveNo),'WaveNo'); 
				#	a='EnemyObj1'; self.EnemyObjs.append([self.getControl(self.c[a]),a]); self.EnemyObjsVis[a]=True; self.ScrTp('true',a+'Animate'); 
				#	a='EnemyObj2'; self.EnemyObjs.append([self.getControl(self.c[a]),a]); self.EnemyObjsVis[a]=True; self.ScrTp('true',a+'Animate'); 
				#	a='EnemyObj3'; self.EnemyObjs.append([self.getControl(self.c[a]),a]); self.EnemyObjsVis[a]=True; self.ScrTp('true',a+'Animate'); 
				#	a='EnemyObj4'; self.EnemyObjs.append([self.getControl(self.c[a]),a]); self.EnemyObjsVis[a]=True; self.ScrTp('true',a+'Animate'); 
				#	a='EnemyObj5'; self.EnemyObjs.append([self.getControl(self.c[a]),a]); self.EnemyObjsVis[a]=True; self.ScrTp('true',a+'Animate'); 
				#except: pass
				
				#self.TestObj1.setPosition(self.maxW-int(self.TestObj1.getWidth()),0)
				self.PlayerObj1.setPosition(0,self.maxH-int(self.PlayerObj1.getHeight()))
				self.TestObj5.setVisible(False)
				
				
				
				
			except Exception,e: debob(["Error",e])
			except: pass
			##
		def onClick(self,controlId):
			try:
				if   controlId==self.c['bExit']: self.AskToClose()
				if   controlId==self.c['iBack']:
					PlaySndWav('gun-gunshot-02.wav')
				else:
					AnyBeenShotYet=False
					for Enmys,EnmysNameTag,EnmysAID in self.EnemyObjs:
						if controlId==EnmysAID:
							eX=int(Enmys.getX()); eW=int(Enmys.getWidth()); eX2=eX+eW; 
							##debob(['Enemy',eX,eX2]); 
							self.EnemyObjsVis[EnmysNameTag]=False
							#debob(["Enemy tank shot!",EnmysNameTag])
							##note("Enemy tank shot!  (%s)"%EnmysNameTag)
							AnyBeenShotYet=True
							self.ScrTp('',EnmysNameTag+'Animate')
							PlaySndWav('gun-gunshot-01.wav')
							self.EnemiesCheckFor()
							
			except Exception,e: debob(["Error",e])
			except: pass
		def EnemiesCheckFor(self): 
			try:
				AllEnemiesAreDead=True; HowManyEnemies=0
				for Enmys,EnmysNameTag,EnmysAID in self.EnemyObjs:
					if self.EnemyObjsVis[EnmysNameTag]==True:
						HowManyEnemies=HowManyEnemies+1; AllEnemiesAreDead=False; #debob(["there are still enemies on the board",EnmysNameTag]); 
				self.HowManyEnemies=HowManyEnemies; self.ScrTp(str(self.HowManyEnemies),'EnemiesRemaining'); 
				if AllEnemiesAreDead==True:
					self.EnemiesRepopulateAll()
					PlaySndWav('fanfare2.wav')
			except Exception,e: debob(["Error",e])
			except: pass
		def EnemiesRepopulateAll(self): 
			try:
				#debob("Repopulating Enemy Tanks"); 
				HowManyEnemies=0; self.WaveNo=self.WaveNo+1; self.ScrTp(str(self.WaveNo),'WaveNo'); 
				for Enmys,EnmysNameTag,EnmysAID in self.EnemyObjs:
					self.EnemyObjsVis[EnmysNameTag]=True; HowManyEnemies=HowManyEnemies+1; self.ScrTp('true',EnmysNameTag+'Animate'); #debob(["Repopulating",EnmysNameTag]); #Enmys.setVisible(True); 
				self.HowManyEnemies=HowManyEnemies; self.ScrTp(str(self.HowManyEnemies),'EnemiesRemaining'); 
			except Exception,e: debob(["Error",e])
			except: pass
		def onAction(self,action): 
			try:
				actId=int(action.getId()); actIds=str(action.getId()); actBC=str(action.getButtonCode()); xx=0; yy=0; 
				try: actAmnt1=action.getAmount1()
				except: actAmnt1=0-900
				try: actAmnt2=action.getAmount2()
				except: actAmnt2=0-900
				mW=self.maxW
				mH=self.maxH
				mWa=int(self.getWidth())
				mHa=int(self.getHeight())
				try: cX=int(self.PlayerObj1.getX())
				except: cX=0
				try: cXL=cX+int(self.PlayerObj1Line.getX())
				except: cXL=cX+0
				
				if   action==ACTION_PREVIOUS_MENU: self.AskToClose()
				elif action==ACTION_NAV_BACK: self.AskToClose()
				elif action==ACTION_MOVE_LEFT: #1
					#debob({'getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif action==ACTION_MOVE_RIGHT: #2
					#debob({'getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif action==ACTION_MOVE_UP: #3
					#debob({'getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif action==ACTION_MOVE_DOWN: #4
					#debob({'getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif action==ACTION_MOUSE_WHEEL_UP: #104
					#debob({'getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif action==ACTION_MOUSE_WHEEL_DOWN: #105
					#debob({'getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif action==ACTION_SELECT_ITEM: #7
					#debob({'info':'ACTION_SELECT_ITEM a.k.a. ENTER','getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif action==ACTION_MOUSE_CLICK_LEFT: #101 ??
					#debob({'info':'ACTION_MOUSE_CLICK_LEFT','getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif action==ACTION_MOUSE_MOVE: #107
					#debob({'action type':'MOUSE MOVE','getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					try: cY=int(self.PlayerObj1.getY())
					except: cY=0
					try: cYL=cY+int(self.PlayerObj1Line.getY())
					except: cYL=0
					try: cLH=int(self.PlayerObj1Line.getHeight())
					except: cLH=0
					try: cLY=int(self.PlayerObj1Line.getY())
					except: cLY=0
					try: cLX=int(self.PlayerObj1Line.getX())
					except: cLX=0
					###
					XX=int(actAmnt1); XX=XX*mW/mWa; 
					if   XX <  0: XX=0
					elif XX > mW: XX=mW
					YY=int(actAmnt2); YY=YY*mH/mHa; 
					if   YY <  0: YY=0
					elif YY > mH: YY=mH
					###
					cLH=cY-YY
					self.PlayerObj1Line.setHeight(cLH+5); 
					LineOffsetX=29
					self.PlayerObj1Line.setPosition(LineOffsetX,YY-cY); 
					xx=int(self.PlayerObj1.getX()); 
					yy=int(self.PlayerObj1.getY()); 
					cY=int(self.PlayerObj1.getY())
					#cX=int(self.TestObj1.getX())
					c2Y=int(self.PlayerObj1.getY())
					c2X=int(self.PlayerObj1.getX())
					c2W=int(self.PlayerObj1.getWidth())
					c2H=int(self.PlayerObj1.getHeight())
					self.PlayerObj1.setPosition(XX-LineOffsetX,cY)
					pass
				elif action==ACTION_MOUSE_DRAG: #106
					#debob({'action type':'MOUSE DRAG','getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
					pass
				elif actId == 100: 
					#deb("Remote Button Pressed","100"); deb('action.getId',str(actIds)); 
					pass
				elif actId == ACTION_aID_0: pass
				elif actId == ACTION_KEY_R: return
				elif actId == ACTION_KEY_F: return
				elif actId == ACTION_REMOTE_INFO: return
				elif actId == ACTION_REMOTE_MUTE: return
				elif actId == ACTION_REMOTE_CONTEXTMENU: return
				elif actId == ACTION_REMOTE_PLAYPAUSE: return
				elif actId == ACTION_REMOTE_STOP: return
				elif actId == ACTION_KEY_X: return
				else:
					if not actId==0:
						#debob({'action type':'UNKNOWN','getId':actId,'getButtonCode':actBC,'getAmount1':actAmnt1,'getAmount2':actAmnt2})
						pass
						##
					##
				##
			except Exception,e: debob(["Error",e]); debob([actId,actIds,actBC])
			except: pass
		def CloseWindow(self):
			try:
				self.closing=True; 
				
			except: pass
			self.close()
		def CW(self): self.CloseWindow()
		def AskToClose(self):
			try:
				if self.closing==False:
					if d.yesno(addonName," ","Are you sure that you want to exit?","","No","Yes"): self.closing=True; self.CloseWindow()
				else: self.CloseWindow()
			except: pass
		##
######


#############################################################################
#############################################################################
skinFilename='CustomWindow001.xml'
try:    Emulating=xbmcgui.Emulating
except: Emulating=False
if __name__=='__main__':
	#cWind=CustomWindow(skinFilename,addon_path,'default')
	cWind=CustomWindow(skinFilename,addon_path) #,'default'
	cWind.doModal()
	del cWind
	sys.modules.clear()

#############################################################################
#############################################################################
