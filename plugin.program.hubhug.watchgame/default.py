# ###  - By TheHighway ### #
# ########################################################## #

import xbmc,xbmcgui,urllib,urllib2,os,sys,logging,array,re,time,datetime,random,string,StringIO,xbmcplugin,xbmcaddon
from config import Config as Config
import common as Common
from common import *
import common

def DoA(a): xbmc.executebuiltin("Action(%s)" % a)

class MyWindowCountDown(xbmcgui.WindowDialog):
	button={}
	def __init__(self,owner,bgArt):
		self.background=bgArt; self.ow=owner; self.scr={}; self.scr['L']=0; self.scr['T']=0; self.scr['W']=1280; self.scr['H']=720; 
		focus=artp("button-focus_lightblue"); nofocus=artp("button-focus_seagreen"); 
		self.BG=xbmcgui.ControlImage(self.scr['L'],self.scr['T'],self.scr['W'],self.scr['H'],self.background,aspectRatio=0); self.addControl(self.BG)
		t='3000'; self.BG.setAnimations([('WindowOpen','effect=fade time='+t+' start=0 end=100'),('WindowClose','effect=fade time='+t+' end=0')])
		w=135; h=32; l=20; t=70; t=170; self.button[0]=xbmcgui.ControlButton(l,t,w,h,"Back",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=focus,noFocusTexture=nofocus); self.addControl(self.button[0]); 
		zz=[self.button[0]]; #,self.button[1],self.button[2]]
		for z in zz: z.setAnimations([('WindowOpen','effect=rotate delay=0 time=1 center='+str(l)+','+str(t)+' end=90')]); 
		#time.sleep(1); 
		#xbmc.executebuiltin("XBMC.SendClick()"); 
		#DoA("Back"); 
		#self.onInit()
		self.setFocus(self.button[0])
		self.DoClose()
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
		w=500; h=360; 
		t=self.scr['H']-h; l=(self.scr['W']/2)-((w*1)+100);
		self.iMyHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iHands[TheirHand],aspectRatio=0); self.addControl(self.iMyHand)
		self.iMyHand.setAnimations([('WindowOpen','effect=rotate delay=500 time=1500 start=-180 center='+str(l)+','+str(t+h))]); 
		#w=260; h=373; 
		#t=self.scr['H']-h; l=(self.scr['W']/2)-((w*1)+100);
		#self.iMyHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iHands[MyHand],aspectRatio=0); self.addControl(self.iMyHand)
		#self.iMyHand.setAnimations([('WindowOpen','effect=rotate delay=500 time=1000 start=180 center='+str(l+w)+','+str(t+h))]); 
		##self.iMyHand.setAnimations([('WindowOpen','effect=slide delay=500 time=1000 start='+str(0-self.scr['W'])+','+str(0))]); 
		#t=self.scr['H']-h; l=(self.scr['W']/2)+((w*0)+100);
		#self.iTheirHand=xbmcgui.ControlImage(l,t,w,h,self.ow.iHands[TheirHand],aspectRatio=0); self.addControl(self.iTheirHand)
		#self.iTheirHand.setAnimations([('WindowOpen','effect=rotate delay=500 time=1000 start=180 center='+str(l+w)+','+str(t+h))]); 
		##self.iTheirHand.setAnimations([('WindowOpen','effect=slide delay=500 time=1000 start='+str(0+self.scr['W'])+','+str(0))]); 
		## ### ## 
		#Hands=self.ow.Hands; self.beats=" "+"beats"+" "; self.loser="LOSER"; self.winner="WINNER"; self.draw="DRAW"; self.noonewins="NO ONE WINS"; 
		#self.beats=" "+SettingG("txt-beats")+" "; self.loser=SettingG("txt-loser"); self.winner=SettingG("txt-winner"); self.draw=SettingG("txt-draw"); self.noonewins=SettingG("txt-noonewins"); 
		#if MyHand==TheirHand: tResult1=self.draw; tResult2=self.noonewins; 
		#elif (MyHand,TheirHand)==(Hands[0],Hands[1]): tResult1= self.loser; tResult2=TheirHand+self.beats+MyHand; 
		#elif (MyHand,TheirHand)==(Hands[0],Hands[2]): tResult1=self.winner; tResult2=MyHand+self.beats+TheirHand; 
		#elif (MyHand,TheirHand)==(Hands[1],Hands[0]): tResult1=self.winner; tResult2=MyHand+self.beats+TheirHand; 
		#elif (MyHand,TheirHand)==(Hands[1],Hands[2]): tResult1= self.loser; tResult2=TheirHand+self.beats+MyHand; 
		#elif (MyHand,TheirHand)==(Hands[2],Hands[0]): tResult1= self.loser; tResult2=TheirHand+self.beats+MyHand; 
		#elif (MyHand,TheirHand)==(Hands[2],Hands[1]): tResult1=self.winner; tResult2=MyHand+self.beats+TheirHand; 
		#self.tResult1=tResult1; self.tResult2=tResult2; 
		if TheirHand.lower()=='winner': tResult1='Congrats'; tResult2="You've found your watch."; 
		else: tResult1='Sorry'; tResult2='Wrong Pocket Watch.'; 
		self.txtResultL.setLabel(""+tResult1+"[CR]"+tResult2+"")
		#"WINNER[CR]Rock beats Scissors"
		#self.txtResultL.setLabel(""+tResult1+"[CR]"+tResult2+"")
		##if self.tResult1 == self.winner: xbmc.playSFX(art('snd_winner','.mp3'))
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
	button={}; tWinner='winner'; 
	Hands=['blaze-2','hw99-3','pumpkin',tWinner,'showgun-1',tWinner,'sorry-1']
	#Hands=['Rock','Paper','Scissors']
	def __init__(self):
		self.Fanart=(xbmc.translatePath(Config.fanart)); self.b1=artp("black1"); self.current=0; self.content=[]; self.scr={}; self.scr['L']=0; self.scr['T']=0; self.scr['W']=1280; self.scr['H']=720; 
		self.AniTime=' time=2000 '; self.AniEnd=' end=80 '; 
		#self.iHands={'Rock':artp('PRS2_rock'),'Paper':artp('PRS2_paper'),'Scissors':artp('PRS2_scissors')}
		#self.iHands={self.Hands[0]:artp('PRS2_'+self.Hands[0].lower()),self.Hands[1]:artp('PRS2_'+self.Hands[1].lower()),self.Hands[2]:artp('PRS2_'+self.Hands[2].lower())}
		self.iHandsF={self.Hands[0]:artp('PRS2F_'+self.Hands[0].lower()),self.Hands[1]:artp('PRS2F_'+self.Hands[1].lower()),self.Hands[2]:artp('PRS2F_'+self.Hands[2].lower())}
		p='watch__'; self.iHands={}; 
		for z in self.Hands:self.iHands[z]=artp(p+z.lower()); 
		#self.iHands={self.Hands[0]:artp(p+self.Hands[0].lower()),self.Hands[1]:artp(p+self.Hands[1].lower()),self.Hands[2]:artp(p+self.Hands[2].lower())}
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
		## ### ## Game Message
		l=95; t=20; w=self.scr['W']-l-30; h=self.scr['H']-(t*2)-100-36; w=1030-l; h=130; 
		self.HoroTxtBG=xbmcgui.ControlImage(l,t,w,h,self.b1,aspectRatio=0); 
		self.HoroTxtBG2=xbmcgui.ControlImage(l,t,w,h,nofocus,aspectRatio=0); 
		self.HoroTxt=xbmcgui.ControlTextBox(l+10,t+2,w-20,h-4,font='font30',textColor="0xFF000000"); 
		zz=[self.HoroTxtBG,self.HoroTxtBG2,self.HoroTxt]
		for z in zz: self.addControl(z); #z.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0 end=80')]); 
		self.HoroTxtBG.setWidth(w); self.HoroTxtBG.setHeight(h); self.HoroTxtBG2.setWidth(w); self.HoroTxtBG2.setHeight(h); 
		self.HoroTxtBG.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0 end=70')]); 
		self.HoroTxtBG2.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0 end=98')]); 
		self.HoroTxt.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0')]); 
		self.HoroTxt.setText("It's party time @ the HUB-HOUSE, and today's contestants have handed over their pocket watches to be randomly hidden inside some pumpkins.  Can you find the right one?  (It says \"WIN\" on it.) "); 
		## ### ## Hands
		f_hand=artp('hub-punkin'); nf_hand=artp('hub-punkin-f'); 
		w=300; h=300; t=self.scr['H']-h; msg=""; 
		l=(self.scr['W']/3)-((w*1)+50); #msg=""+self.Hands[0]; 
		aniHands='effect=rotate delay=500 time=2000 start=180 '
		self.button[1]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=f_hand,noFocusTexture=nf_hand); self.addControl(self.button[1])
		self.button[1].setAnimations([('WindowOpen',aniHands+' center='+str(l+w)+','+str(t+h))]); 
		l=(self.scr['W']/2)-((int(w*0.5))+40); #msg=""+self.Hands[1]; 
		self.button[2]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=f_hand,noFocusTexture=nf_hand); self.addControl(self.button[2])
		self.button[2].setAnimations([('WindowOpen',aniHands+' center='+str(l+w)+','+str(t+h))]); 
		l=(self.scr['W']/2)+((int(w*0.5))+100); #msg=""+self.Hands[2]; 
		self.button[3]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=f_hand,noFocusTexture=nf_hand); self.addControl(self.button[3])
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
		#TheirHand=self.Hands[random.randint(0,len(self.Hands)-1)]; 
		TheirHand=self.Hands[random.randint(0,len(self.Hands)-1)]; 
		deb('MyHand',MyHand); deb('TheirHand',TheirHand); 
		#for z in ['3','2','1']: self.TempWindow2=MyWindowCountDown(owner=self,bgArt=artp('hubhug_321_'+z)); self.TempWindow2.doModal(); del self.TempWindow2; 
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
