# ###  - By TheHighway ### #
# ########################################################## #

import xbmc,xbmcgui,urllib,urllib2,os,sys,logging,array,re,time,datetime,random,string,StringIO,xbmcplugin,xbmcaddon
from config import Config as Config
import common as Common
from common import *
import common
import splash_highway as splash

def SFX(n,e='.wav'):
	if len(n)==0: return
	snd=art(n,e)
	try: xbmc.playSFX(snd,False)
	except: 
		try: xbmc.playSFX(snd)
		except: pass

class MyWindow(xbmcgui.Window):
	countA=0; countB=0; button={}; Ducks={}; NonDucks={}; iDuckShot=''; iDuckShot2=''; isMoving=False; 
	Txt1="               [COLOR mediumpurple][I]Shoot only the[/I]  [B]DUCKS![/B][/COLOR][CR]"; 
	Txt2='               '+cFL('Ducks: %s','red')+cFL('        Non-Ducks: %s','yellow')+'     '
	duckPosY =190; NonDuckPosY =100; wDuck =80; hDuck =80; wNonDuck =250; hNonDuck =250; 
	duckPosY2=460; NonDuckPosY2=410; wDuck2=80; hDuck2=80; wNonDuck2=155; hNonDuck2=155; 
	duckPosY3=620; NonDuckPosY3=590; wDuck3=70; hDuck3=70; wNonDuck3=120; hNonDuck3=120; 
	SleepSpeed=30; 
	DucksSpeed =4; NonDucksSpeed =0-6; 
	DucksSpeed2=2; NonDucksSpeed2=0-4; 
	DucksSpeed3=0-4; NonDucksSpeed3=3; 
	def __init__(self):
		self.current=0; self.content=[]; self.scr={}; self.scr['L']=0; self.scr['T']=0; self.scr['W']=1280; self.scr['H']=720; 
		self.AniTime=' time=2000 '; self.AniEnd=' end=80 '; 
		self.GameArt=[]
		self.GameArt.append([artp('004_duck2'),artp('Planet_Venus'),artp('demon_duck'),'gun-gunshot-01',artp('Alien-Space-Ship_'),'gun-gunshot-02']); 
		self.GameArt.append([artp('001_duck2'),artp('turtle_'),artp('007_ducky'),'gun-gunshot-01',artp('Sea_Turtle_2'),'gun-gunshot-02']); 
		self.GameArt.append([artp('005_duckb2'),artp('fish2'),artp('007_duckb'),'gun-gunshot-01',artp('FishingFunny'),'gun-gunshot-02']); 
		self.GameArt.append(['gun-gunshot-02','','']); 
		self.iSceneBG=artp('scene_water'); 
		self.iDuckShot =self.GameArt[0][2] #artp('007_duck'); 
		self.iDuckShot2=self.GameArt[1][2] #artp('006_duck'); 
		self.iDuckShot3=self.GameArt[2][2] #artp('dead-duck'); 
		self.Dificulty=Config().gSetting('dificulty'); deb('Dificulty',self.Dificulty); 
		if self.Dificulty=='Hard': self.SleepSpeed=15; 
		elif self.Dificulty=='Medium': self.SleepSpeed=23; 
		elif self.Dificulty=='Easy': self.SleepSpeed=30; 
		else: self.SleepSpeed=100; 
		self.makePageItems(); 
	def makePageItems(self):
		self.b1=artp("black1"); self.background=(xbmc.translatePath(Config.fanart)); #self.background=artj("backdrop"); 
		focus=artp("button-focus_lightblue"); nofocus=artp("button-focus_seagreen"); 
		## ### ## Background
		self.BG=xbmcgui.ControlImage(self.scr['L'],self.scr['T'],self.scr['W'],self.scr['H'],self.background,aspectRatio=0); self.addControl(self.BG)
		self.BG.setAnimations([('WindowOpen','effect=fade '+self.AniTime+' start=0')])
		## ### ##
		l=95; t=20; #l=195; t=20; 
		l=t; 
		#w=self.scr['W']-l-30; h=self.scr['H']-(t*2)-100-36; 
		w=self.scr['W']-(l*2); h=self.scr['H']-(t*2); 
		self.HoroTxtBG=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.b1,noFocusTexture=self.b1); 
		self.HoroTxt=xbmcgui.ControlTextBox(l+10,t+2,w-20,h-4,font='font30',textColor="0xFFFFFFFF"); 
		zz=[self.HoroTxtBG,self.HoroTxt]
		for z in zz: self.addControl(z); #z.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0 end=80')]); 
		self.HoroTxtBG.setAnimations([('WindowOpen','effect=fade delay=4000 time=2000 start=0 end=10')]); 
		self.HoroTxt.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0')]); 
		#self.HoroTxt.setText("blah..........."); 
		## ### ## 
		l=0; h=300; 
		w=self.scr['W']-l; t=self.scr['H']-h; 
		self.SceneBG=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iSceneBG,noFocusTexture=self.iSceneBG); self.addControl(self.SceneBG); 
		self.SceneBG.setAnimations([('WindowOpen','effect=fade delay=4000 time=2000 start=0 end=50')]); 
		## ### ## 
		self.AddGameObjects(); 
		## ### ## 
		w=135; h=32; l=20; t=170; 
		self.button[0]=xbmcgui.ControlButton(l,t,w,h,"Exit",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=focus,noFocusTexture=nofocus); self.addControl(self.button[0])
		zz=[self.button[0]] #,self.button[1],self.button[2]]
		##for z in zz: z.setAnimations([('WindowOpen','effect=slide delay=1000 time=1000 start='+str(0-l)+','+str(0-h-10))])
		for z in zz: z.setAnimations([('WindowOpen','effect=rotate delay=0 time=10 center='+str(l)+','+str(t)+' end=90')])
		## ### ## Addon Title
		#zz=["XBMCHUB","Your","HUB-HUG"]; w=1000; h=50; l=15; t=700; t=560; self.LabTitleText=Config.name; self.LabTitle=xbmcgui.ControlLabel(l,t,w,h,'','font30','0xFFFF0000',angle=90); self.addControl(self.LabTitle)
		zz=["XBMCHUB","Your","HUB-HUG"]; w=350; h=50; l=self.scr['W']-370; t=18; self.LabTitleText=Config.name; self.LabTitle=xbmcgui.ControlLabel(l,t,w,h,'','font30','0xFFFF0000'); self.addControl(self.LabTitle)
		#for z in zz:
		#	if z+" " in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace(z+" ","[COLOR deepskyblue][B][I]"+z+"[/I][/B][/COLOR]  ")
		#if "Highway" in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace("Highway","[COLOR tan]Highway[/COLOR]")
		for z in zz:
			if z+" " in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace(z+" ","[COLOR deepskyblue][B][I]"+z+"[/I][/B][/COLOR]  [CR]")
		if "Highway" in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace("Highway","[COLOR tan]Highway[/COLOR]")
		self.LabTitle.setAnimations([('WindowOpen','effect=slide delay=1000 time=1000 start=50,-100')]); self.LabTitle.setLabel(self.LabTitleText); 
		## ### ## 
		#self.AddGameObjects(); 
		
		## ### ## Movements
		i=0; 
		#z=self.button[0]; z.controlUp(self.button[0]); z.controlDown(self.button[0]); z.controlLeft(self.button[0]); z.controlRight(self.button[0]); 
		#for z in self.Horo:
		#	self.eHoro[i]=True; 
		## ### ## Focus
		self.HoroTxt.setText(self.Txt1)
		#self.setFocus(self.button[0])
		self.setFocus(self.HoroTxtBG)
		## ### ## 
		#self.isMoving=True; 
		#self.StartMovement(); 
		## ### ## 
	def AddGameObjects(self):
		f='f2_'; n='nf2_'; self.DateClr='white'; self.Horo=[]; self.Horo2=[]; self.Horo2bg=[]; self.Horo3=[]; self.Horo3bg=[]; #self.horoList.reset(); 
		self.Ducks={}; self.NonDucks={}; wDuck=self.wDuck; hDuck=self.hDuck; wNonDuck=self.wNonDuck; hNonDuck=self.hNonDuck; wDuck2=self.wDuck2; hDuck2=self.hDuck2; wNonDuck2=self.wNonDuck2; hNonDuck2=self.hNonDuck2; wDuck3=self.wDuck3; hDuck3=self.hDuck3; wNonDuck3=self.wNonDuck3; hNonDuck3=self.hNonDuck3; 
		## ############################################### ## >>
		#self.GameArt=[[artp('001_duck'),artp('turtle_'),],[artp('005_duckb'),artp('61dA0iGRdCL'),],[artp('004_duck'),artp('Virtual+Planets+Venus+Planet+01'),]]
		self.iDucks=self.GameArt[0][0] #artp('001_duck'); 
		#self.iDucks=artp('003_duck'); 
		w=wDuck; h=hDuck; t=self.duckPosY; zz=[[0,150],[1,400],[2,650],[3,900],[4,1250]]
		for (z1,z2) in zz: 
			l=z2; 
			self.Ducks[z1]=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iDucks,noFocusTexture=self.iDucks); 
			self.addControl(self.Ducks[z1])
		w=wNonDuck; h=hNonDuck; t=self.NonDuckPosY; zz=[[0,50],[1,350],[2,650],[3,950],[4,1250]]
		self.iNonDucks=self.GameArt[0][1] #artp('turtle_'); 
		for (z1,z2) in zz: l=z2; self.NonDucks[z1]=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iNonDucks,noFocusTexture=self.iNonDucks); self.addControl(self.NonDucks[z1])
		## ############################################### ## <<
		self.iDucks=self.GameArt[1][0] #artp('005_duckb'); 
		w=wDuck2; h=hDuck2; t=self.duckPosY2; zz=[[5,150],[6,400],[7,650],[8,900],[9,1250]]
		for (z1,z2) in zz: 
			l=z2; 
			self.Ducks[z1]=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iDucks,noFocusTexture=self.iDucks); 
			self.addControl(self.Ducks[z1])
		w=wNonDuck2; h=hNonDuck2; t=self.NonDuckPosY2; zz=[[5,150],[6,400],[7,650],[8,900],[9,1250]]
		self.iNonDucks=self.GameArt[1][1] #artp('61dA0iGRdCL'); 
		for (z1,z2) in zz: l=z2; self.NonDucks[z1]=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iNonDucks,noFocusTexture=self.iNonDucks); self.addControl(self.NonDucks[z1])
		## ############################################### ## >>
		artNonDucks=[]
		self.iDucks=self.GameArt[2][0] #artp('004_duck'); 
		w=wDuck3; h=hDuck3; t=self.duckPosY3; zz=[[10,50],[11,300],[12,550],[13,800],[14,1150]]
		for (z1,z2) in zz: 
			l=z2; 
			self.Ducks[z1]=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iDucks,noFocusTexture=self.iDucks); 
			self.addControl(self.Ducks[z1])
		w=wNonDuck3; h=hNonDuck3; t=self.NonDuckPosY3; zz=[[10,50],[11,300],[12,550],[13,800],[14,1150]]
		self.iNonDucks=self.GameArt[2][1] #artp('Virtual+Planets+Venus+Planet+01'); 
		for (z1,z2) in zz: l=z2; self.NonDucks[z1]=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iNonDucks,noFocusTexture=self.iNonDucks); self.addControl(self.NonDucks[z1])
		## ############################################### ##
	def gnY(self,itemHeight=95): return random.randint(self.scr['T']+20,self.scr['H']-itemHeight-100) #Vertical
	def gnX(self, itemWidth=95): return random.randint(self.scr['L']+100,self.scr['W']- itemWidth-30) #Horizontal
	def doRandomMovements(self):
		try:
			try: F=self.getFocus()
			except: F=False
			i=0
			for z in range(0,len(self.Ducks)):
				#try:
				if not F==False:
					x,y=self.Ducks[z].getPosition()
					if z in [10,11,12,13,14]: x=x+self.DucksSpeed3
					elif z in [5,6,7,8,9]: x=x+(self.DucksSpeed2*2) #x=x-self.DucksSpeed
					else: x=x+self.DucksSpeed
					if x > self.scr['W']: x=self.scr['L']-self.wDuck
					if x < (self.scr['L']-self.wDuck): x=self.scr['W']
					self.Ducks[z].setPosition(x,y) #self.duckPosY)
				#except: pass
				i=i+1
			i=0
			for z in range(0,len(self.NonDucks)):
				#try:
				if not F==False:
					x,y=self.NonDucks[z].getPosition()
					if z in [10,11,12,13,14]: x=x+self.NonDucksSpeed3
					elif z in [5,6,7,8,9]: x=x+self.NonDucksSpeed2
					else: x=x+self.NonDucksSpeed
					if x < (self.scr['L']-self.wNonDuck): x=self.scr['W']
					if x > self.scr['W']: x=self.scr['L']-self.wNonDuck
					self.NonDucks[z].setPosition(x,y) #self.NonDuckPosY)
				#except: pass
				i=i+1
		except: pass
	def StartMovement(self):
		#try:
			if self.isMoving==False: 
				self.isMoving=True; 
				while self.isMoving==True:
					curTime=time.time()
					try: self.doRandomMovements()
					except: self.isMoving=False
					#while time.time()-curTime < 0.2: pass #t=''
					xbmc.sleep(self.SleepSpeed)
		#except: pass
	def onAction(self,action):
		try:
			try: F=self.getFocus()
			except: F=False
			if   action==Config.ACTION_PREVIOUS_MENU: self.CloseWindow1st()
			elif action==Config.ACTION_NAV_BACK: self.CloseWindow1st()
			#
			elif (F==self.button[0]): return
			#elif (F==self.HoroTxtBG) or (F==self.HoroTxtBG):
			else: 
				#try:
					self.StartMovement(); 
				#	self.doRandomMovements(); 
				#except: pass
		except: pass
	def shotHitDuck(self,z):
		try:
						self.countA=self.countA+1; self.HoroTxt.setText(self.Txt1+self.Txt2 % (str(self.countA),str(self.countB))); 
						if z in [10,11,12,13,14]: ## Bottom
							SFX(self.GameArt[2][3]); #'gun-gunshot-01'); 
							splash.do_My_Splash(self.GameArt[2][2],1); #splash.do_My_Splash(self.iDuckShot3,1); 
						elif z in [5,6,7,8,9]:    ## Middle
							SFX(self.GameArt[1][3]); #'gun-gunshot-01'); 
							splash.do_My_Splash(self.GameArt[1][2],1); #,True,10,150,self.scr['W']-200,self.scr['H']-150); #splash.do_My_Splash(self.iDuckShot2,2,True,10,150,self.scr['W']-200,self.scr['H']-150); 
						else:                     ## Top
							SFX(self.GameArt[0][3]); #'gun-gunshot-01'); 
							splash.do_My_Splash(self.GameArt[0][2],1); #splash.do_My_Splash(self.iDuckShot,1); 
		except: pass
	def shotHitOther(self,z):
		try: 
			self.countB=self.countB+1; self.HoroTxt.setText(self.Txt1+self.Txt2 % (str(self.countA),str(self.countB))); 
			if z in [10,11,12,13,14]: ## Bottom
				SFX(self.GameArt[2][5]); #'gun-gunshot-02'); 
				splash.do_My_Splash(self.GameArt[2][4],1,True,(self.scr['W']-(400))/2,(self.scr['H']-(384))/2,(400),(384)); #splash.do_My_Splash(artp('Alien-Space-Ship_'),1,True,(self.scr['W']-(400))/2,(self.scr['H']-(384))/2,(400),(384)); 
			elif z in [5,6,7,8,9]:    ## Middle
				SFX(self.GameArt[1][5]); #'gun-gunshot-02'); 
				splash.do_My_Splash(self.GameArt[1][4],1,True,(self.scr['W']-(285*2))/2,(self.scr['H']-(241*2))/2,(285*2),(241*2)); #splash.do_My_Splash(artp('Funny_Fishing_for_Dinner-1trans2'),1,True,(self.scr['W']-(285*2))/2,(self.scr['H']-(241*2))/2,(285*2),(241*2)); 
			elif z in [0,1,2,3,4]:    ## Top
				SFX(self.GameArt[0][5]); #'gun-gunshot-02'); 
				splash.do_My_Splash(self.GameArt[0][4],1,True,(self.scr['W']-400)/2,(self.scr['H']-400)/2,400,400); #splash.do_My_Splash(artp('Sea_Turtle_2'),1,True,(self.scr['W']-400)/2,(self.scr['H']-400)/2,400,400); 
			#
		except: pass
	def shotMiss(self):
		try: 
			SFX(self.GameArt[3][0]); #'gun-gunshot-02'); 
			self.countB=self.countB+1; self.HoroTxt.setText(self.Txt1+self.Txt2 % (str(self.countA),str(self.countB))); 
		except: pass
	def onControl(self,control):
		if   control==self.button[0]: self.CloseWindow1st()
		elif control==self.HoroTxtBG: self.shotMiss()
		elif control==self.HoroTxt:   self.shotMiss()
		elif control==self.SceneBG:   self.shotMiss()
		else:
			for z in range(0,len(self.Ducks)):
				try:
					self.isMoving=False; 
					if (control==self.Ducks[z]): self.shotHitDuck(z)
				except: pass
			for z in range(0,len(self.NonDucks)):
				try:
					if (control==self.NonDucks[z]): self.shotHitOther(z)
				except: pass
	def DoImageChange(self,offset):
		i=(int(self.current)+int(offset))
		if i < 0: i=len(self.content)-1
		if i > (len(self.content)-1): i=0
		self.current=i; self.imgHeart.setImage(self.content[i])
	def CloseWindow1st(self):
		#try: zz=[self.CtrlList,self.RepoThumbnail,self.RepoFanart2,self.RepoFanart,self.LabCurrentRepo,self.LabTitle,self.button[0],self.TVS,self.TVSBGB,self.BGB]
		#except: zz=[]
		#for z in zz:
		#	try: self.removeControl(z); del z
		#	except: pass
		self.close()
## ################################################## ##
## ################################################## ##
## Start of program
TempWindow=MyWindow(); TempWindow.doModal(); del TempWindow
## ################################################## ##
## ################################################## ##
