# ###  - By TheHighway ### #
# ########################################################## #

import xbmc,xbmcgui,urllib,urllib2,os,sys,logging,array,re,time,datetime,random,string,StringIO,xbmcplugin,xbmcaddon
from config import Config as Config
import common as Common
from common import *
import common

def DoA(a): xbmc.executebuiltin("Action(%s)" % a)

class MyWindow(xbmcgui.Window):
	button={}; tWinner='winner'; GridButton={}; GridButtonUD={}; GridButtonUDC={}; GridButtonUDN={}; Mistakes=0; NoOfMoves=0; 
	Hands=[1,2,3];
	PuzzleGridA=''; PuzzleGridB=''; PuzzleWordList=''; PuzzleFileHolder=''; 
	#Hands=['Rock','Paper','Scissors']
	def __init__(self):
		self.Fanart=(xbmc.translatePath(Config.fanart)); self.b1=artp("black1"); self.current=0; self.content=[]; self.scr={}; self.scr['L']=0; self.scr['T']=0; self.scr['W']=1280; self.scr['H']=720; 
		self.AniTime=' time=2000 '; self.AniEnd=' end=80 '; 
		note("HUB-HUG Movement Series","Please wait.  Preparing screen.  Load Time may vary from device to device.",delay=10000); 
		##self.iHands={'Rock':artp('PRS2_rock'),'Paper':artp('PRS2_paper'),'Scissors':artp('PRS2_scissors')}
		#self.iHands={self.Hands[0]:artp('PRS2_'+self.Hands[0].lower()),self.Hands[1]:artp('PRS2_'+self.Hands[1].lower()),self.Hands[2]:artp('PRS2_'+self.Hands[2].lower())}
		#self.iHandsF={self.Hands[0]:artp('PRS2F_'+self.Hands[0].lower()),self.Hands[1]:artp('PRS2F_'+self.Hands[1].lower()),self.Hands[2]:artp('PRS2F_'+self.Hands[2].lower())}
		#p='watch__'; self.iHands={}; 
		#for z in self.Hands:self.iHands[z]=artp(p+z.lower()); 
		#self.iHands={self.Hands[0]:artp(p+self.Hands[0].lower()),self.Hands[1]:artp(p+self.Hands[1].lower()),self.Hands[2]:artp(p+self.Hands[2].lower())}
		self.LoadGridFile(); 
		self.makePageItems(); 
	def LoadGridFile(self):
		self.PuzzlePath=xbmc.translatePath(os.path.join(Config.path,'puzzles')); 
		self.PuzzleFiles=os.listdir(self.PuzzlePath); debob(self.PuzzleFiles); 
		zz=self.PuzzleFiles; 
		for z in zz:
			if '.bak' in z: self.PuzzleFiles.remove(z)
		PuF=self.PuzzleFiles[random.randint(0,len(self.PuzzleFiles)-1)]; 
		self.PuzzleFile=xbmc.translatePath(os.path.join(self.PuzzlePath,PuF)); 
		if tfalse(SettingG("select-puzzle"))==True:
			dialog=xbmcgui.Dialog()
			fn=str(dialog.browse(1,'Select Puzzle','files','.txt|.puzzle|.puz',False,False,self.PuzzleFile,False))
			try:
				if (fn==False) or (len(fn)==0): self.close; return
				if len(fn) > 1: deb('fn',fn); self.PuzzleFile=fn; 
			except: pass
		#self.PuzzleFile=xbmc.translatePath(os.path.join(self.PuzzlePath,PuF)); 
		deb('Random File Chosen',self.PuzzleFile); self.PuzzleFileHolder=Common._OpenFile(self.PuzzleFile); deb('Length of Grid File',str(len(self.PuzzleFileHolder))); 
		self.lineBreaker='||'; #'\n\n'; 
		self.PuzzleGridA=self.PuzzleFileHolder.split(self.lineBreaker)[0].replace('\n','').replace('\a','').replace('\r',''); deb('Length of GridA',str(len(self.PuzzleFileHolder))); 
		self.PuzzleGridA=self.PuzzleGridA.replace(' ','+').replace('=','+').replace('?','')
		self.PuzzleGridB=self.PuzzleFileHolder.split(self.lineBreaker)[1].replace('\n','').replace('\a','').replace('\r',''); deb('Length of GridB',str(len(self.PuzzleFileHolder))); 
		self.PuzzleWordList=self.PuzzleFileHolder.split(self.lineBreaker)[2].replace('\n','').replace('\a','').replace('\r','').replace(', ','\n').replace(' ','\n').replace(',','\n'); deb('Length of Word List',str(len(self.PuzzleFileHolder))); 
		self.PuzzleGridAList=list(self.PuzzleGridA); 
		self.PuzzleFileHolder=self.PuzzleFileHolder.replace('\a','\n').replace('\r','\n')
		for i in range(0,len(self.PuzzleGridAList)):
			#if self.PuzzleGridAList[i] in [' ','+','=','?']:
			if self.PuzzleGridAList[i]=='+':
				z=str(chr(random.randint(65,90)))
				self.PuzzleGridAList[i]=z
				#self.PuzzleGridA[i]=chr(random.randint(65,90))
		#self.PuzzleGridA=''.join(str(e) for e in self.PuzzleGridAList); 
		#self.PuzzleGridA=str(self.PuzzleGridAList) #.join(); 
		self.PuzzleGridA=''
		for e in self.PuzzleGridAList: self.PuzzleGridA+=e
		#self.Puzzle
		##
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
		## ### ## Game Board
		## ### ## Game Peices
		self.gridBGnormal=artp('button-focus_fire2'); self.gridBGcircled=artp('button-focus_darkblue2'); 
		gridNoW=30; gridNoH=20; curI=0; curH=0; 
		gridNoW=len(self.PuzzleFileHolder.split(self.lineBreaker)[0].split('\n')[0])
		if gridNoW==0: gridNoW=30; 
		overALLl=100; overALLt=30; overALLw=1200; overALLh=650; 
		Pw=28; Ph=28; SpacingW=5; SpacingH=5; 
		cPuzzleGridA=len(self.PuzzleGridA)
		for i in range(0,(1+cPuzzleGridA)):
			if (curI==gridNoW): curI=0; curH=curH+1; 
			elif (curI==(gridNoW*curH)) and (not curI==0): curI=0; curH=curH+1; 
			l=overALLl+(curI*(Pw+SpacingW)); t=overALLt+(curH*(Ph+SpacingH)); w=0+Pw; h=0+Ph; 
			try:
				#self.GridButton[i]=xbmcgui.ControlButton(l,t,w,h,self.PuzzleGridA[i],textColor="0xFF000000",focusedColor="0xFF000000",alignment=0,font='font16',textOffsetX=3,textOffsetY=-6); 
				self.GridButton[i]=xbmcgui.ControlButton(l,t,w,h,self.PuzzleGridA[i],textColor="0xFF000000",focusedColor="0xFF000000",alignment=0,font='font16',focusTexture=self.gridBGcircled,noFocusTexture=self.gridBGnormal,textOffsetX=3,textOffsetY=-6); 
				self.addControl(self.GridButton[i]); 
				self.GridButtonUD[i]=0; 
				self.GridButtonUDN[i]=i; 
				try:
					#if self.PuzzleGridB[i] in [' ','+','=','?']: self.GridButtonUDC[i]=0; 
					if self.PuzzleGridB[i]=='+': self.GridButtonUDC[i]=0; 
					#if (self.PuzzleGridB[i]==' ') or (self.PuzzleGridB[i]=='?') or (self.PuzzleGridB[i]=='+') or (self.PuzzleGridB[i]=='='): self.GridButtonUDC[i]=0; 
					else: self.GridButtonUDC[i]=1; 
				except: self.GridButtonUDC[i]=0; 
				if i==0: self.GridButton[i].controlLeft(self.button[0]); 
				else: self.GridButton[i].controlLeft(self.GridButton[i-1]); 
				if not i==(cPuzzleGridA): self.GridButton[i-1].controlRight(self.GridButton[i]); 
				if curH > 0:
					try: self.GridButton[i].controlUp(self.GridButton[(i-gridNoW)]); 
					except: pass
				if curH > 0:
					try: self.GridButton[(i-gridNoW)].controlDown(self.GridButton[i]); 
					except: pass
				#self.button[0].controlUp(self.button[3]); self.button[0].controlDown(self.button[1]); 
				#self.button[0].controlLeft(self.button[3]); self.button[0].controlRight(self.button[1]); 
				#self.GridButtonUDN[i]
			except: pass
			curI=curI+1; 
			#
		curI=0; 
		for i in range(((cPuzzleGridA)-gridNoW),(1+cPuzzleGridA)):
			try: 
				self.GridButton[curI].controlUp(self.GridButton[i]); 
				self.GridButton[i].controlDown(self.GridButton[curI]); 
				curI=curI+1; 
			except: pass
		#self.addControls(list(self.GridButton)); 
		#
		
		
		## ### ## Game Message
		#l=95; t=20; w=self.scr['W']-l-30; h=self.scr['H']-(t*2)-100-36; w=1030-l; h=130; 
		l=1100-10; t=30; w=180; h=self.scr['H']-t-35; 
		self.HoroTxtBG=xbmcgui.ControlImage(l,t,w,h,self.b1,aspectRatio=0); 
		self.HoroTxtBG2=xbmcgui.ControlImage(l,t,w,h,nofocus,aspectRatio=0); 
		#self.HoroTxt=xbmcgui.ControlTextBox(l+10,t+2,w-20,h-4,font='font12',textColor="0xFF000000"); 
		self.HoroTxt=xbmcgui.ControlList(l+5,t+20,w-10,h-40,font='font12',textColor="0xFF000000",selectedColor="0xFF000000",buttonFocusTexture=focus,buttonTexture=nofocus); 
		self.HoroTxt.setSpace(2); 
		self.HoroTxt.setImageDimensions(0,0); 
		#,itemTextXOffset=-30,itemTextYOffset=-5
		self.HoroTxt.setItemHeight(14); 
		zz=[self.HoroTxtBG,self.HoroTxtBG2,self.HoroTxt]
		for z in zz: self.addControl(z); #z.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0 end=80')]); 
		self.HoroTxtBG.setWidth(w); self.HoroTxtBG.setHeight(h); self.HoroTxtBG2.setWidth(w); self.HoroTxtBG2.setHeight(h); 
		self.HoroTxtBG.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0 end=70')]); 
		self.HoroTxtBG2.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0 end=98')]); 
		self.HoroTxt.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0')]); 
		#self.HoroTxt.setText(self.PuzzleWordList); 
		
		#self.HoroTxt.reset(); 
		self.HoroTxt.addItems(self.PuzzleWordList.split('\n')); 
		## ### ## Hands
		#f_hand=artp('nutshell_down_f'); nf_hand=artp('nutshell_down_nf'); 
		#w=87; h=86; w=w*3; h=h*3; t=self.scr['H']-h; msg=""; 
		#l=(self.scr['W']/3)-((w*1)+50); #msg=""+self.Hands[0]; 
		#aniHands='effect=rotate time=2000 start=180 '
		#self.button[1]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=f_hand,noFocusTexture=nf_hand); self.addControl(self.button[1])
		#self.button[1].setAnimations([('WindowOpen',aniHands+' delay=4000 center='+str(l+w)+','+str(t+h))]); 
		#l=(self.scr['W']/2)-((int(w*0.5))+40); #msg=""+self.Hands[1]; 
		#self.button[2]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=f_hand,noFocusTexture=nf_hand); self.addControl(self.button[2])
		#self.button[2].setAnimations([('WindowOpen',aniHands+' delay=2000 center='+str(l+w)+','+str(t+h))]); 
		#l=(self.scr['W']/2)+((int(w*0.5))+100); #msg=""+self.Hands[2]; 
		#self.button[3]=xbmcgui.ControlButton(l,t,w,h,""+msg,textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=f_hand,noFocusTexture=nf_hand); self.addControl(self.button[3])
		#self.button[3].setAnimations([('WindowOpen',aniHands+' delay=1 center='+str(l+w)+','+str(t+h))]); 
		
		
		## ### ## Addon Title
		zz=["XBMCHUB","Your","HUB-HUG"]; w=1000; h=50; l=15; t=700; 
		t=560; 
		self.LabTitleText=Config.name; self.LabTitle=xbmcgui.ControlLabel(l,t,w,h,'','font30','0xFFFF0000',angle=90); self.addControl(self.LabTitle)
		for z in zz:
			if z+" " in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace(z+" ","[COLOR deepskyblue][B][I]"+z+"[/I][/B][/COLOR]  [CR]")
		if "Highway" in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace("Highway","[COLOR tan]Highway[/COLOR]")
		self.LabTitle.setAnimations([('WindowOpen','effect=slide delay=1000 time=1000 start=-100')]); self.LabTitle.setLabel(self.LabTitleText); 
		## ### ## Movements
		#self.button[0].controlUp(self.button[3]); self.button[0].controlDown(self.button[1]); self.button[1].controlUp(self.button[0]); self.button[1].controlDown(self.button[2]); self.button[2].controlUp(self.button[1]); self.button[2].controlDown(self.button[3]); self.button[3].controlUp(self.button[2]); self.button[3].controlDown(self.button[0]); 
		#self.button[0].controlLeft(self.button[3]); self.button[0].controlRight(self.button[1]); self.button[1].controlLeft(self.button[0]); self.button[1].controlRight(self.button[2]); self.button[2].controlLeft(self.button[1]); self.button[2].controlRight(self.button[3]); self.button[3].controlLeft(self.button[2]); self.button[3].controlRight(self.button[0]); 
		self.button[0].controlRight(self.GridButton[0]); self.button[0].controlDown(self.GridButton[0]); 
		#self.button[0].controlLeft(self.GridButton[len(self.GridButton)-1]); 
		#self.button[0].controlUp(self.GridButton[len(self.GridButton)-1]); 
		#self.GridButton[len(self.GridButton)-1].controlRight(self.button[0]); 
		self.button[0].controlLeft(self.HoroTxt); self.button[0].controlUp(self.HoroTxt); 
		self.GridButton[len(self.GridButton)-1].controlRight(self.HoroTxt); 
		self.HoroTxt.controlRight(self.button[0]); self.HoroTxt.controlDown(self.button[0]); 
		self.HoroTxt.controlLeft(self.GridButton[len(self.GridButton)-1]); self.HoroTxt.controlUp(self.GridButton[len(self.GridButton)-1]); 
		
		## ### ## Focus
		self.setFocus(self.button[0])
		## ### ##
	def onAction(self,action):
		if   action == Config.ACTION_PREVIOUS_MENU: self.CloseWindow1st()
		elif action == Config.ACTION_NAV_BACK: self.CloseWindow1st()
	def onControl(self,control):
		if   control==self.button[0]: self.CloseWindow1st()
		#elif control==self.button[1]: self.DoFight(self.Hands[0])
		#elif control==self.button[2]: self.DoFight(self.Hands[1])
		#elif control==self.button[3]: self.DoFight(self.Hands[2])
		elif control==self.HoroTxt: return
		else:
			self.DoFight(control)
		##
	def DoFight(self,control):
			for i in range(0,(1+len(self.PuzzleGridA))):
				try:
					if control==self.GridButton[i]:
						t=self.GridButton[i].getLabel(); 
						if self.GridButtonUD[i]==0: 
							if self.GridButtonUDC[i]==1:
								self.GridButtonUD[i]=1; c="0xFFFFFFFF"; t=self.PuzzleGridA[i]; self.NoOfMoves=self.NoOfMoves+1; 
							else:
								self.GridButtonUD[i]=2; c="0xFF808080"; t='?'; self.Mistakes=self.Mistakes+1; self.NoOfMoves=self.NoOfMoves+1; 
						elif self.GridButtonUD[i]==2: 
								#self.GridButtonUD[i]=2; c="0xFF808080"; t='?'; 
								self.GridButtonUD[i]=0; c="0xFF000000"; t=self.PuzzleGridA[i]; 
						else: 
								self.GridButtonUD[i]=0; c="0xFF000000"; t=self.PuzzleGridA[i]; 
						self.GridButton[i].setLabel(t,textColor=c,focusedColor=c); 
						if self.GridButtonUDC==self.GridButtonUD:
							popOK(msg="All Words Found!",title="HUB-HUG Movement Series",line2="Moves:  "+str(self.NoOfMoves),line3="Mistakes:  "+str(self.Mistakes)); 
						return
				except: pass
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
