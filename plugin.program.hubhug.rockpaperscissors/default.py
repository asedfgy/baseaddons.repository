# ###  - By TheHighway ### #
# ########################################################## #

import xbmc,xbmcgui,urllib,urllib2,os,sys,logging,array,re,time,datetime,random,string,StringIO,xbmcplugin,xbmcaddon
from config import Config as Config
import common as Common
from common import *
import common

def DoA(a): xbmc.executebuiltin("Action(%s)" % a)

class MyWindowCountDown(xbmcgui.WindowDialog):
	button={}; HandAngle=0; cTime=0; 
	def __init__(self,owner,bgArt,TotalTime=50,TotalAngel=90):
		self.background=bgArt; self.ow=owner; self.scr={}; self.scr['L']=0; self.scr['T']=0; self.scr['W']=1280; self.scr['H']=720; 
		focus=artp("button-focus_lightblue"); nofocus=artp("button-focus_seagreen"); 
		self.BG=xbmcgui.ControlImage(self.scr['L'],self.scr['T'],self.scr['W'],self.scr['H'],self.background,aspectRatio=0); self.addControl(self.BG)
		t='3000'; t='0'; 
		self.BG.setAnimations([('WindowOpen','effect=fade time='+t+' start=0 end=100'),('WindowClose','effect=fade time='+t+' end=0')])
		w=135; h=32; l=20; t=70; t=170; self.button[0]=xbmcgui.ControlButton(l,t,w,h,"Back",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=focus,noFocusTexture=nofocus); self.addControl(self.button[0]); 
		zz=[self.button[0]]; #,self.button[1],self.button[2]]
		for z in zz: z.setAnimations([('WindowOpen','effect=rotate delay=0 time=0 center='+str(l)+','+str(t)+' end=90')]); 
		self.button[0].setVisible(False); 
		## ### ## Hands
		w=260; h=373; MyHand=self.ow.Hands[0]; TheirHand=self.ow.Hands[0]; 
		t=(self.scr['H']/2)-(w/1); l=(0)-((w*1)+0);
		self.iMyHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iHands[MyHand],aspectRatio=0); 
		self.addControl(self.iMyHand); aR=90; 
		#aR=((self.HandAngle/TotalTime)*TotalAngel)
		#aR=round(((self.cTime/TotalTime)*TotalAngel),0)
		#aR=((self.cTime/TotalTime)*TotalAngel)
		deb("hand angle",str(aR)); 
		self.cTime=self.cTime+1
		self.iMyHand.setAnimations([('WindowOpen'   ,'effect=rotate delay=0 time=1 start=0 end='+str(0-aR)+' center='+str(l+w)+','+str(t+h))]); 
		t=(self.scr['H']/2)-(w/1); l=(self.scr['W']); #-((w*1)+100); #l=(self.scr['W']/2)+((w*0)+100);
		self.iTheirHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iLHands[TheirHand],aspectRatio=0); self.addControl(self.iTheirHand)
		self.iTheirHand.setAnimations([('WindowOpen','effect=rotate delay=0 time=1 start=0 end='+str(aR)+' center='+str(l)+','+str(t+h))]); 
		
		## ### ## 
		##time.sleep(4); 
		##xbmc.executebuiltin("XBMC.SendClick()"); 
		##DoA("Back"); 
		##self.onInit()
		#self.setFocus(self.button[0])
		##time.sleep(4); 
		self.DoClose()
	def updateHandAngle(self,i): self.HandAngle=i
	def onInit(self): self.DoClose()
	def onFocus(self,control): self.DoClose()
	def onAction(self,action): self.DoClose()
	#	if   action == Config.ACTION_PREVIOUS_MENU: self.CloseWindow1st()
	#	elif action == Config.ACTION_NAV_BACK: self.CloseWindow1st()
	def DoClose(self):
		self.close()

class MyWindowFight(xbmcgui.WindowDialog):
	button={}
	def __init__(self,owner,bgArt,MyHand,TheirHand):
		self.background=bgArt; self.ow=owner; self.scr={}; self.scr['L']=0; self.scr['T']=0; self.scr['W']=1280; self.scr['H']=720; 
		self.BG=xbmcgui.ControlImage(self.scr['L'],self.scr['T'],self.scr['W'],self.scr['H'],self.background,aspectRatio=0); self.addControl(self.BG)
		#t='3000'; self.BG.setAnimations([('WindowOpen','effect=fade time='+t+' start=0 end=100'),('WindowClose','effect=fade time='+t+' end=0')])
		focus=artp("button-focus_lightblue"); nofocus=artp("button-focus_seagreen"); 
		## ### ## Results
		w=400; h=60; l=(self.scr['W']/2)-(w/2); t=(self.scr['H']/2)-(h+50); t=80; l=l-50; 
		self.txtResultBGL=xbmcgui.ControlImage(l,t,w,h,nofocus,aspectRatio=0); 
		self.txtResultL=xbmcgui.ControlLabel(l,t,w,h,"",'font14','0xFF000000',alignment=2); 
		for z in [self.txtResultBGL,self.txtResultL]: self.addControl(z); z.setAnimations([('WindowOpen','effect=fade delay=1500 time=1000 start=0')]); 
		## ### ## Hands
		w=260; h=373; 
		t=(self.scr['H']/2)-(w/1); l=(0)-((w*1)+0);
		self.iMyHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iHands[MyHand],aspectRatio=0); self.addControl(self.iMyHand)
		self.iMyHand.setAnimations([('WindowOpen'   ,'effect=rotate delay=500 time=1000 start=0 end=-90 center='+str(l+w)+','+str(t+h))]); 
		t=(self.scr['H']/2)-(w/1); l=(self.scr['W']); #-((w*1)+100); #l=(self.scr['W']/2)+((w*0)+100);
		self.iTheirHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iLHands[TheirHand],aspectRatio=0); self.addControl(self.iTheirHand)
		self.iTheirHand.setAnimations([('WindowOpen','effect=rotate delay=500 time=1000 start=0 end=90 center='+str(l)+','+str(t+h))]); 
		
		#t=self.scr['H']-h; l=(self.scr['W']/2)-((w*1)+100);
		#self.iMyHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iHands[MyHand],aspectRatio=0); self.addControl(self.iMyHand)
		#self.iMyHand.setAnimations([('WindowOpen','effect=rotate delay=500 time=1000 start=180 center='+str(l+w)+','+str(t+h))]); 
		##self.iMyHand.setAnimations([('WindowOpen','effect=slide delay=500 time=1000 start='+str(0-self.scr['W'])+','+str(0))]); 
		#t=self.scr['H']-h; l=(self.scr['W']/2)+((w*0)+100);
		#self.iTheirHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iLHands[TheirHand],aspectRatio=0); self.addControl(self.iTheirHand)
		#self.iTheirHand.setAnimations([('WindowOpen','effect=rotate delay=500 time=1000 start=180 center='+str(l+w)+','+str(t+h))]); 
		##self.iTheirHand.setAnimations([('WindowOpen','effect=slide delay=500 time=1000 start='+str(0+self.scr['W'])+','+str(0))]); 
		## ### ## 
		Hands=self.ow.Hands; self.beats=" "+"beats"+" "; self.loser="LOSER"; self.winner="WINNER"; self.draw="DRAW"; self.noonewins="NO ONE WINS"; 
		self.beats=" "+SettingG("txt-beats")+" "; self.loser=SettingG("txt-loser"); self.winner=SettingG("txt-winner"); self.draw=SettingG("txt-draw"); self.noonewins=SettingG("txt-noonewins"); 
		if MyHand==TheirHand: tResult1=self.draw; tResult2=self.noonewins; 
		elif (MyHand,TheirHand)==(Hands[0],Hands[1]): tResult1= self.loser; tResult2=TheirHand+self.beats+MyHand; 
		elif (MyHand,TheirHand)==(Hands[0],Hands[2]): tResult1=self.winner; tResult2=MyHand+self.beats+TheirHand; 
		elif (MyHand,TheirHand)==(Hands[1],Hands[0]): tResult1=self.winner; tResult2=MyHand+self.beats+TheirHand; 
		elif (MyHand,TheirHand)==(Hands[1],Hands[2]): tResult1= self.loser; tResult2=TheirHand+self.beats+MyHand; 
		elif (MyHand,TheirHand)==(Hands[2],Hands[0]): tResult1= self.loser; tResult2=TheirHand+self.beats+MyHand; 
		elif (MyHand,TheirHand)==(Hands[2],Hands[1]): tResult1=self.winner; tResult2=MyHand+self.beats+TheirHand; 
		self.tResult1=tResult1; self.tResult2=tResult2; 
		
		#"WINNER[CR]Rock beats Scissors"
		self.txtResultL.setLabel(""+tResult1+"[CR]"+tResult2+"")
		#if self.tResult1 == self.winner: xbmc.playSFX(art('snd_winner','.mp3'))
		## ### ## Exit
		w=135; h=32; l=20; t=70; t=170; self.button[0]=xbmcgui.ControlButton(l,t,w,h,"Back",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=focus,noFocusTexture=nofocus); self.addControl(self.button[0]); 
		zz=[self.button[0]]; #,self.button[1],self.button[2]]
		for z in zz: z.setAnimations([('WindowOpen','effect=rotate delay=0 time=1 center='+str(l)+','+str(t)+' end=90')]); 
		## ### ## Focus
		self.setFocus(self.button[0])
		## ### ## 
		self.DoClose()
	def onInit(self): self.DoClose()
	def onClick(self,control): self.DoClose()
	def onControl(self,control): 
		if   control==self.button[0]: self.DoClose()
		else: self.DoClose()
	def onAction(self,action):
		if   action == Config.ACTION_PREVIOUS_MENU: self.DoClose()
		elif action == Config.ACTION_NAV_BACK: self.DoClose()
		else: self.DoClose()
	def DoClose(self):
		#if self.tResult1 == self.winner: xbmc.playSFX(art('snd_winner','.mp3'))
		self.close()

class MyWindow(xbmcgui.Window):
	button={}
	Hands=['Rock','Paper','Scissors']
	def __init__(self):
		self.Fanart=(xbmc.translatePath(Config.fanart)); self.b1=artp("black1"); self.current=0; self.content=[]; self.scr={}; self.scr['L']=0; self.scr['T']=0; self.scr['W']=1280; self.scr['H']=720; 
		self.AniTime=' time=2000 '; self.AniEnd=' end=80 '; 
		#self.iHands={'Rock':artp('PRS2_rock'),'Paper':artp('PRS2_paper'),'Scissors':artp('PRS2_scissors')}
		self.iHands={self.Hands[0]:artp('PRS2_'+self.Hands[0].lower()),self.Hands[1]:artp('PRS2_'+self.Hands[1].lower()),self.Hands[2]:artp('PRS2_'+self.Hands[2].lower())}
		self.iHandsF={self.Hands[0]:artp('PRS2F_'+self.Hands[0].lower()),self.Hands[1]:artp('PRS2F_'+self.Hands[1].lower()),self.Hands[2]:artp('PRS2F_'+self.Hands[2].lower())}
		self.iLHands={self.Hands[0]:artp('LPRS2_'+self.Hands[0].lower()),self.Hands[1]:artp('LPRS2_'+self.Hands[1].lower()),self.Hands[2]:artp('LPRS2_'+self.Hands[2].lower())}
		self.iLHandsF={self.Hands[0]:artp('LPRS2F_'+self.Hands[0].lower()),self.Hands[1]:artp('LPRS2F_'+self.Hands[1].lower()),self.Hands[2]:artp('LPRS2F_'+self.Hands[2].lower())}
		self.makePageItems(); 
	def makePageItems(self):
		self.background=self.Fanart; #self.background=artj("backdrop_temp"); 
		focus=artp("button-focus_lightblue"); nofocus=artp("button-focus_seagreen"); 
		## ### ## Background
		self.BG=xbmcgui.ControlImage(self.scr['L'],self.scr['T'],self.scr['W'],self.scr['H'],self.background,aspectRatio=0); self.addControl(self.BG)
		self.BG.setAnimations([('WindowOpen','effect=fade '+self.AniTime+' start=0')])
		## ### ## Exit
		w=135; h=32; l=20; t=70; t=170; 
		self.button[0]=xbmcgui.ControlButton(l,t,w,h,"Exit",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=focus,noFocusTexture=nofocus); self.addControl(self.button[0])
		zz=[self.button[0]] #,self.button[1],self.button[2]]
		for z in zz: z.setAnimations([('WindowOpen','effect=rotate delay=0 time=1 center='+str(l)+','+str(t)+' end=90')])
		## ### ## Hands
		
		w=260; h=373; t=self.scr['H']-h; msg=""; 
		l=(self.scr['W']/3)-((w*1)+50); #msg=""+self.Hands[0]; 
		aniHands='effect=rotate delay=500 time=2000 start=180 '
		self.button[1]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iHandsF[self.Hands[0]],noFocusTexture=self.iHands[self.Hands[0]]); self.addControl(self.button[1])
		self.button[1].setAnimations([('WindowOpen',aniHands+' center='+str(l+w)+','+str(t+h))]); 
		l=(self.scr['W']/2)-((int(w*0.5))+40); #msg=""+self.Hands[1]; 
		self.button[2]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iHandsF[self.Hands[1]],noFocusTexture=self.iHands[self.Hands[1]]); self.addControl(self.button[2])
		self.button[2].setAnimations([('WindowOpen',aniHands+' center='+str(l+w)+','+str(t+h))]); 
		l=(self.scr['W']/2)+((int(w*0.5))+100); #msg=""+self.Hands[2]; 
		self.button[3]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.iHandsF[self.Hands[2]],noFocusTexture=self.iHands[self.Hands[2]]); self.addControl(self.button[3])
		self.button[3].setAnimations([('WindowOpen',aniHands+' center='+str(l+w)+','+str(t+h))]); 
		
		
		## ### ## Addon Title
		zz=["XBMCHUB","Your","HUB-HUG"]; w=1000; h=50; l=15; t=700; self.LabTitleText=Config.name; self.LabTitle=xbmcgui.ControlLabel(l,t,w,h,'','font30','0xFFFF0000',angle=90); self.addControl(self.LabTitle)
		for z in zz:
			if z+" " in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace(z+" ","[COLOR deepskyblue][B][I]"+z+"[/I][/B][/COLOR]  ")
		if "Highway" in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace("Highway","[COLOR tan]Highway[/COLOR]")
		self.LabTitle.setAnimations([('WindowOpen','effect=slide delay=1000 time=1000 start=-100')]); self.LabTitle.setLabel(self.LabTitleText); 
		## ### ## Movements
		self.button[0].controlUp(self.button[3]); self.button[0].controlDown(self.button[1]); self.button[1].controlUp(self.button[0]); self.button[1].controlDown(self.button[2]); self.button[2].controlUp(self.button[1]); self.button[2].controlDown(self.button[3]); self.button[3].controlUp(self.button[2]); self.button[3].controlDown(self.button[0]); 
		self.button[0].controlLeft(self.button[3]); self.button[0].controlRight(self.button[1]); self.button[1].controlLeft(self.button[0]); self.button[1].controlRight(self.button[2]); self.button[2].controlLeft(self.button[1]); self.button[2].controlRight(self.button[3]); self.button[3].controlLeft(self.button[2]); self.button[3].controlRight(self.button[0]); 
		## ### ## Focus
		self.setFocus(self.button[0])
		## ### ##
	def onAction(self,action):
		if   action == Config.ACTION_PREVIOUS_MENU: self.CloseWindow1st()
		elif action == Config.ACTION_NAV_BACK: self.CloseWindow1st()
	def onControl(self,control):
		if   control==self.button[0]: self.CloseWindow1st()
		elif control==self.button[1]: self.DoFight(self.Hands[0])
		elif control==self.button[2]: self.DoFight(self.Hands[1])
		elif control==self.button[3]: self.DoFight(self.Hands[2])
	def DoFight(self,MyHand):
		TheirHand=self.Hands[random.randint(0,len(self.Hands)-1)]; deb('MyHand',MyHand); deb('TheirHand',TheirHand); 
		#for z in ['3','2','1']: self.TempWindow2=MyWindowCountDown(owner=self,bgArt=artp('hubhug_321_'+z)); self.TempWindow2.doModal(); del self.TempWindow2; 
		if tfalse(SettingG("show-countdowns"))==True:
			TimeOnCountDowns=60; w=260; h=373; t=(self.scr['H']/2)-(w/1); l=(0)-((w*1)+0); t2=(self.scr['H']/2)-(w/1); l2=(self.scr['W']); 
			for z in ['3','2','1']: 
				self.TempWindow2=MyWindowCountDown(owner=self,bgArt=artp('hubhug_321_a'+z),TotalTime=TimeOnCountDowns,TotalAngel=90); 
				#self.TempWindow2.doModal(); 
				self.cTime=0; 
				for i in range(0,TimeOnCountDowns): 
					#self.TempWindow2=MyWindowCountDown(owner=self,bgArt=artp('hubhug_321_a'+z),TotalTime=TimeOnCountDowns,TotalAngel=90); 
					self.TempWindow2.updateHandAngle(i); 
					#self.TempWindow2.show(); 
					
					## ### ## Hands
					if tfalse(SettingG("ani-hands"))==True:
						self.cTime=self.cTime+1; aR=int((90.00 / TimeOnCountDowns) * i); #debob(str(aR)); 
						try:
							self.TempWindow2.iMyHand.setAnimations([('WindowOpen'   ,'effect=rotate delay=0 time=0 end='+str(0-aR)+' center='+str(l+w)+','+str(t+h))]); 
							self.TempWindow2.iTheirHand.setAnimations([('WindowOpen','effect=rotate delay=0 time=0 end='+str(aR)+' center='+str(l2)+','+str(t2+h))]); 
						except: pass
					self.TempWindow2.show(); 
				try: del self.TempWindow2; 
				except: pass
		self.TempWindow2=MyWindowFight(owner=self,bgArt=self.Fanart,MyHand=MyHand,TheirHand=TheirHand); self.TempWindow2.doModal(); del self.TempWindow2; 
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
