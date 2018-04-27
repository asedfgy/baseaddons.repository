# ###  - By TheHighway ### #
# ########################################################## #

import xbmc,xbmcgui,urllib,urllib2,os,sys,logging,array,re,time,datetime,random,string,StringIO,xbmcplugin,xbmcaddon
from config import Config as Config
import common as Common
from common import *
import common

class MyWindow(xbmcgui.Window):
	isMoving=False; button={}; eHoro=[False,False,False,False,False,False,False,False,False,False,False,False]
	SleepSpeed=100; 
	def __init__(self):
		self.current=0; self.content=[]; self.scr={}; self.scr['L']=0; self.scr['T']=0; self.scr['W']=1280; self.scr['H']=720; 
		self.AniTime=' time=2000 '; self.AniEnd=' end=80 '; 
		self.Dificulty=Config().gSetting('dificulty'); deb('Dificulty',self.Dificulty); 
		if self.Dificulty=='Hard': self.SleepSpeed=40; 
		elif self.Dificulty=='Medium': self.SleepSpeed=100; 
		elif self.Dificulty=='Easy': self.SleepSpeed=200; 
		else: self.SleepSpeed=100; 
		self.makePageItems(); 
	def makePageItems(self):
		self.b1=artp("black1"); self.background=(xbmc.translatePath(Config.fanart)); self.background=artj("backdrop"); 
		#self.background='http://www.horoscopedates.com/images/scorpio.jpg'; 
		#self.background=artp("q5LCZ"); 
		focus=artp("button-focus_lightblue"); nofocus=artp("button-focus_seagreen"); 
		## ### ## Background
		self.BG=xbmcgui.ControlImage(self.scr['L'],self.scr['T'],self.scr['W'],self.scr['H'],self.background,aspectRatio=0); self.addControl(self.BG)
		self.BG.setAnimations([('WindowOpen','effect=fade '+self.AniTime+' start=0')])
		## ### ##
		l=95; t=20; #l=195; t=20; 
		w=self.scr['W']-l-30; h=self.scr['H']-(t*2)-100-36; 
		#self.imgHeart=xbmcgui.ControlImage(l,t,w,h,self.content[self.current],aspectRatio=0); self.addControl(self.imgHeart); 
		#self.HoroTxtBG=xbmcgui.ControlImage(l,t,w,h,self.b1,aspectRatio=0); 
		self.HoroTxtBG=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=self.b1,noFocusTexture=self.b1); 
		self.HoroTxt=xbmcgui.ControlTextBox(l+10,t+2,w-20,h-4,font='font30',textColor="0xFFFFFFFF"); 
		zz=[self.HoroTxtBG,self.HoroTxt]
		for z in zz: self.addControl(z); #z.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0 end=80')]); 
		self.HoroTxtBG.setAnimations([('WindowOpen','effect=fade delay=4000 time=2000 start=0 end=70')]); 
		self.HoroTxt.setAnimations([('WindowOpen','effect=fade delay=2000 time=2000 start=0')]); 
		
		#self.HoroTxt.setText("blah..........."); 
		## ### ##
		w=135; h=32; l=20; t=70; t=170; 
		self.button[0]=xbmcgui.ControlButton(l,t,w,h,"Exit",textColor="0xFF000000",focusedColor="0xFF00BFFF",alignment=2,focusTexture=focus,noFocusTexture=nofocus); self.addControl(self.button[0])
		#t=t+10+h; self.button[1]=xbmcgui.ControlButton(l,t,w,h,"Next",textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=focus,noFocusTexture=nofocus); self.addControl(self.button[1])
		#t=t+10+h; self.button[2]=xbmcgui.ControlButton(l,t,w,h,"Previous",textColor="0xFFB22222",focusedColor="0xFF00BFFF",alignment=2,focusTexture=focus,noFocusTexture=nofocus); self.addControl(self.button[2])
		zz=[self.button[0]] #,self.button[1],self.button[2]]
		#for z in zz: z.setAnimations([('WindowOpen','effect=slide delay=1000 time=1000 start='+str(0-l)+','+str(0-h-10))])
		for z in zz: z.setAnimations([('WindowOpen','effect=rotate delay=0 time=10 center='+str(l)+','+str(t)+' end=90')])
		#for z in zz: z.setAnimations([('WindowOpen','effect=rotate delay=0 time=10 center='+str(l)+','+str(t)+' end=90'),('Focus','effect=slide delay=1000 time=1000 start='+str(0-l)+','+str(0-h-10))])
		## ### ## Addon Title
		zz=["XBMCHUB","Your","HUB-HUG"]; w=1000; h=50; l=15; t=700; self.LabTitleText=Config.name; self.LabTitle=xbmcgui.ControlLabel(l,t,w,h,'','font30','0xFFFF0000',angle=90); self.addControl(self.LabTitle)
		for z in zz:
			if z+" " in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace(z+" ","[COLOR deepskyblue][B][I]"+z+"[/I][/B][/COLOR]  ")
		if "Highway" in self.LabTitleText: self.LabTitleText=self.LabTitleText.replace("Highway","[COLOR tan]Highway[/COLOR]")
		self.LabTitle.setAnimations([('WindowOpen','effect=slide delay=1000 time=1000 start=-100')]); self.LabTitle.setLabel(self.LabTitleText); 
		## ### ## 
		#w=135; h=300; l=55; t=220; 
		#self.horoListBG=xbmcgui.ControlImage(l,t,w,h,self.b1,aspectRatio=0); self.addControl(self.horoListBG); 
		#self.horoList=xbmcgui.ControlList(l,t,w,h,font='font12',textColor="0xFFFF0000",selectedColor="0xFF00FF00",buttonFocusTexture=focus,buttonTexture=nofocus); self.horoList.setSpace(2); self.addControl(self.horoList); 
		self.AddHoroList(); 
		self.HoroTxt.setText("[COLOR mediumpurple][I]You've gotta gotta smack them[/I]  [B]A L L ![/B][/COLOR][CR][CR]")
		
		## ### ## Movements
		#self.button[0].controlUp(self.button[2]); self.button[0].controlDown(self.button[1]); self.button[1].controlUp(self.button[0]); self.button[1].controlDown(self.button[2]); self.button[2].controlUp(self.button[1]); self.button[2].controlDown(self.button[0]); 
		#self.button[0].controlLeft(self.button[2]); self.button[0].controlRight(self.button[1]); self.button[1].controlLeft(self.button[0]); self.button[1].controlRight(self.button[2]); self.button[2].controlLeft(self.button[1]); self.button[2].controlRight(self.button[0]); 
		i=0; #self.button[0].controlUp(self.Horo[-1]); self.button[0].controlDown(self.Horo[0]); 
		#self.button[0].controlLeft(self.Horo[-1]); self.button[0].controlRight(self.Horo[0]); 
		z=self.button[0]; z.controlUp(self.button[0]); z.controlDown(self.button[0]); z.controlLeft(self.button[0]); z.controlRight(self.button[0]); 
		#self.eHoro=[]; 
		for z in self.Horo:
			self.eHoro[i]=True; 
			#self.eHoro.append(True); 
			z.controlUp(self.button[0]); z.controlDown(self.button[0]); i=i+1; 
			z.controlLeft(self.button[0]); z.controlRight(self.button[0]); 
			#try: z.controlLeft(self.Horo[i-2]); 
			#except: pass
			#try: z.controlRight(self.Horo[i]); 
			#except: z.controlRight(self.Horo[0]); 
		## ### ## Focus
		self.setFocus(self.button[0])
		## ### ##
	def AddHoroList(self):
		f='f2_'; n='nf2_'; self.DateClr='white'; self.Horo=[]; self.Horo2=[]; self.Horo2bg=[]; self.Horo3=[]; self.Horo3bg=[]; #self.horoList.reset(); 
		self.AddToHoroList("Capricorn",		"[COLOR orange]Dec. 22[/COLOR]",				"[COLOR orange]Jan. 19[/COLOR]",				"The Mountain Goat. An Earth sign, ruled by Saturn...",					"http://www.horoscopedates.com/img/icons/capricorn_128.png",		artp(n+"capricorn"),		artp(f+"capricorn")); 
		self.AddToHoroList("Aquarius",		"[COLOR lime]Jan. 20[/COLOR]",					"[COLOR lime]Feb. 18[/COLOR]",					"The Man who Carries Water. An Air sign, ruled by Uranus...",		"http://www.horoscopedates.com/img/icons/aquarius_128.png",			artp(n+"aquarius"),			artp(f+"aquarius")); 
		self.AddToHoroList("Pisces",			"[COLOR lightskyblue]Feb. 19[/COLOR]",	"[COLOR lightskyblue]Mar. 20[/COLOR]",	"The Fish. A Water sign, ruled by Neptune...",									"http://www.horoscopedates.com/img/icons/pisces_128.png",				artp(n+"pisces"),				artp(f+"pisces")); 
		self.AddToHoroList("Aries",				"[COLOR crimson]Mar. 21[/COLOR]",				"[COLOR crimson]Apr. 19[/COLOR]",				"The Ram. A Fire sign, ruled by Mars...",												"http://www.horoscopedates.com/img/icons/aries_128.png",				artp(n+"aries"),				artp(f+"aries")); 
		self.AddToHoroList("Taurus",			"[COLOR orange]Apr. 20[/COLOR]",				"[COLOR orange]May 20[/COLOR]",					"The Bull. An Earth sign, ruled by Venus...",										"http://www.horoscopedates.com/img/icons/taurus_128.png",				artp(n+"taurus"),				artp(f+"taurus")); 
		self.AddToHoroList("Gemini",			"[COLOR lime]May 21[/COLOR]",						"[COLOR lime]Jun. 20[/COLOR]",					"The Twins. An Air sign, ruled by Mercury...",									"http://www.horoscopedates.com/img/icons/gemini_128.png",				artp(n+"gemini"),				artp(f+"gemini")); 
		self.AddToHoroList("Cancer",			"[COLOR lightskyblue]Jun. 21[/COLOR]",	"[COLOR lightskyblue]Jul. 22[/COLOR]",	"The Crab. An Water sign, ruled by the Moon...",								"http://www.horoscopedates.com/img/icons/cancer_128.png",				artp(n+"cancer"),				artp(f+"cancer")); 
		self.AddToHoroList("Leo",					"[COLOR crimson]Jul. 23[/COLOR]",				"[COLOR crimson]Aug. 22[/COLOR]",				"The Lion. A Fire sign, ruled by the Sun...",										"http://www.horoscopedates.com/img/icons/leo_128.png",					artp(n+"leo"),					artp(f+"leo")); 
		self.AddToHoroList("Virgo",				"[COLOR orange]Aug. 23[/COLOR]",				"[COLOR orange]Sept. 22[/COLOR]",				"The Maiden. An Earth sign, ruled by Mercury...",								"http://www.horoscopedates.com/img/icons/virgo_128.png",				artp(n+"virgo"),				artp(f+"virgo")); 
		self.AddToHoroList("Libra",				"[COLOR lime]Sept. 23[/COLOR]",					"[COLOR lime]Oct. 22[/COLOR]",					"The Scales. An Air sign, ruled by Venus...",										"http://www.horoscopedates.com/img/icons/libra_128.png",				artp(n+"libra"),				artp(f+"libra")); 
		self.AddToHoroList("Scorpio",			"[COLOR lightskyblue]Oct. 23[/COLOR]",	"[COLOR lightskyblue]Nov. 21[/COLOR]",	"The Scorpion. A Water sign, ruled by Pluto...",								"http://www.horoscopedates.com/img/icons/scorpio_128.png",			artp(n+"scorpio"),			artp(f+"scorpio")); 
		self.AddToHoroList("Sagittarius",	"[COLOR crimson]Nov. 22[/COLOR]",				"[COLOR crimson]Dec. 21[/COLOR]",				"The Centaur. A Fire sign, ruled by Jupiter...",								"http://www.horoscopedates.com/img/icons/sagittarius_128.png",	artp(n+"sagittarius"),	artp(f+"sagittarius")); 
		#self.horoListBG.setVisible(False); self.horoList.setVisible(False); 
		for z in self.Horo:    ## Buttons
			self.addControl(z); z.setAnimations([('WindowOpen','effect=slide delay=500 time=2000 start=0,200')]); 
			z.setAnimations([('WindowOpen','effect=fade '+self.AniTime+' start=0 '+self.AniEnd)]); 
			#z.setAnimations([('WindowOpen','effect=slide delay=0 time=2000 tween=sine pulse=true loop=true start='+str(0)+','+str(0-z.getY()+30)+' end='+str(0)+','+str(0)+' ')]); # tween=elastic  loop=false
			##z.setAnimations([('WindowOpen','effect=slide delay=0 time=2000 tween=sine pulse=true loop=true start='+str(0-z.getY()+30)+' end='+str(0)+' ')]); # tween=elastic  loop=false
			##z.setAnimations([('WindowOpen','effect=slide delay=0 time=2000 start='+str(z.getX())+','+str(0-z.getY())+' end='+str(z.getX())+','+str(self.scr['H'])+' pulse="true" loop="true" tween="elastic" ')]); 
			##z.setAnimations([('WindowOpen','effect=slide delay=500 time=2000 start='+z.getX()+','+z.getY()+' end='+self.scr['W']+','+self.scr['H']+' pulse="true"')]); 
		for z in self.Horo2bg:   ## Titles
			self.addControl(z); z.setAnimations([('WindowOpen','effect=slide delay=500 time=2000 start=0,200')]); 
			z.setAnimations([('WindowOpen','effect=fade '+self.AniTime+' start=0 '+self.AniEnd)]); 
		for z in self.Horo2:   ## Titles
			self.addControl(z); z.setAnimations([('WindowOpen','effect=slide delay=500 time=2000 start=0,200')]); 
			z.setAnimations([('WindowOpen','effect=fade '+self.AniTime+' start=0')]); 
		for z in self.Horo3bg: ## Label BGs
			self.addControl(z); z.setAnimations([('WindowOpen','effect=slide delay=500 time=2000 start=0,200')]); 
			z.setAnimations([('WindowOpen','effect=fade '+self.AniTime+' start=0 '+self.AniEnd)]); 
		for z in self.Horo3:   ## Labels
			self.addControl(z); z.setAnimations([('WindowOpen','effect=slide delay=500 time=2000 start=0,200')]); 
			z.setAnimations([('WindowOpen','effect=fade '+self.AniTime+' start=0')]); 
	def AddToHoroList(self,signName,dateFrom="",dateTo="",signDesc="",signImg="",signImg2="",signImg3=""):
		## ### ## 
		if len(signImg2)==0: signImg2=signImg
		if len(signImg3)==0: signImg3=signImg
		w=95; h=95; l=65+((len(self.Horo))*(w+5)); t=self.scr['H']-h; 
		#ho=xbmcgui.ControlImage(l,t,w,h,signImg,aspectRatio=0); debob(signImg); 
		#ho=xbmcgui.ControlButton(l,t,w,h,"[CR]"+dateFrom+"[CR]"+dateTo+"",textColor="0xFFFFFFFF",focusedColor="0xFFFFFFFF",alignment=2,noFocusTexture=signImg2,focusTexture=signImg3); ## ,textColor="0xFFFFFFFF",focusedColor="0xffdeb887"
		ho=xbmcgui.ControlButton(l,t,w,h,"",textColor="0xFFFFFFFF",focusedColor="0xFFFFFFFF",alignment=2,noFocusTexture=signImg2,focusTexture=signImg3); ## ,textColor="0xFFFFFFFF",focusedColor="0xffdeb887"
		l=l+5; t=t-21; w=w-10; h=20; 
		ho2bg=xbmcgui.ControlImage(l,t+2,w,h,self.b1,aspectRatio=0); 
		ho2=xbmcgui.ControlLabel(l,t,w,h,signName,'font12','0xFF00ffd8',alignment=2,angle=0); 
		t=t-37; h=35; 
		ho3bg=xbmcgui.ControlImage(l+10,t,w-20,h+3,self.b1,aspectRatio=0); 
		ho3=xbmcgui.ControlLabel(l,t,w,h,""+dateFrom+"[CR]"+dateTo+"",'font10','0xFFFFFFFF',alignment=2,angle=0); 
		self.Horo.append(ho); self.Horo2bg.append(ho2bg); self.Horo2.append(ho2); self.Horo3bg.append(ho3bg); self.Horo3.append(ho3); 
		## ### ## 
		#c1=xbmcgui.ListItem(signName+"[CR]"+dateFrom+" - "+dateTo); #,iconImage=r1,thumbnailImage=r1
		#c1.setProperty("signName",signName); c1.setProperty("dateFrom",dateFrom); c1.setProperty("dateTo",dateTo); c1.setProperty("signImg",signImg); c1.setProperty("signDesc",signDesc); 
		##c1.setProperty("",); #c1.setProperty("",); 
		#self.horoList.addItem(c1)
	def gnY(self,itemHeight=95): return random.randint(self.scr['T']+20,self.scr['H']-itemHeight-100) #Vertical
	def gnX(self, itemWidth=95): return random.randint(self.scr['L']+100,self.scr['W']- itemWidth-30) #Horizontal
	def StartMovement(self):
		#try:
			if self.isMoving==False: 
				self.isMoving=True; 
				while self.isMoving==True:
					curTime=time.time()
					self.doRandomMovements()
					#while time.time()-curTime < 0.2: pass #t=''
					xbmc.sleep(self.SleepSpeed)
		#except: pass
	def doRandomMovements(self):
		i=0
		try: F=self.getFocus()
		except: F=False
		for z in self.Horo:
			try:
				if (not F==z) and (self.eHoro[i]==True): z.setPosition(self.gnX(),self.gnY())
			except: pass
			i=i+1
	def onAction(self,action):
		try: F=self.getFocus()
		except: F=False
		if   action == Config.ACTION_PREVIOUS_MENU: self.CloseWindow1st()
		elif action == Config.ACTION_NAV_BACK: self.CloseWindow1st()
		elif (F==self.button[0]): return
		#elif (F==self.HoroTxtBG) or (F==self.HoroTxtBG):
		else:
			self.StartMovement(); 
		#	self.doRandomMovements()
	def onControl(self,control):
		if   control==self.button[0]: self.CloseWindow1st()
		#elif control==self.button[1]: self.DoImageChange(1)
		#elif control==self.button[2]: self.DoImageChange(-1)
		#elif control==self.Horo[0]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/capricorn/')));  
		#elif control==self.Horo[1]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/aquarius/')));  
		#elif control==self.Horo[2]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/pisces/')));  
		#elif control==self.Horo[3]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/aries/')));  
		#elif control==self.Horo[4]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/taurus/')));  
		#elif control==self.Horo[5]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/gemini/')));  
		#elif control==self.Horo[6]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/cancer/')));  
		#elif control==self.Horo[7]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/leo/')));  
		#elif control==self.Horo[8]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/virgo/')));  
		#elif control==self.Horo[9]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/libra/')));  
		#elif control==self.Horo[10]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/scorpio/')));  
		#elif control==self.Horo[11]: self.DoHoroTxt(nolines(getURL('http://www.horoscopedates.com/daily-horoscope/sagittarius/')));  
		else:
			i=0
			for z in self.Horo:
				try:
					if (control==z) and (self.eHoro[i]==True): self.eHoro[i]=False; w=95; h=95; l=65+((i)*(w+5)); t=self.scr['H']-h; z.setPosition(l,t); 
				except: pass
				i=i+1
			if True not in self.eHoro:
			#if eHoro==[True,True,True,True,True,True,True,True,True,True,True,True]:
				t="[COLOR mediumpurple][I]You've found them all.[/I][/COLOR][CR][CR]"+"[COLOR deepskyblue][B]!!  C O N G R A T S  !![/B][/COLOR][CR][CR]"
				self.HoroTxt.setText(t)
				popOK(msg="!!  C O N G R A T S  !!",title=Config.name,line2="You've found them all.",line3="")
	def DoHoroTxt(self,html):
			s='</div><h1>(\D+\sDaily Horoscope)</h1>\s*<p class="lead">(Your\s\D+\shoroscope for\s.+?)</p>\s*<p>(.+?)</p><div class="row">\s*'
			try:
				t1,t2,t3=re.compile(s).findall(html)[0]
				debob([t1,t2,t3]); 
				t="[COLOR deepskyblue][B]\t\t\t\t\t\t"+t1+"[/B][/COLOR][CR][COLOR mediumpurple][I]"+t2+"[/I][/COLOR][CR][COLORtan]"+t3+"[/COLOR]"; 
				t=t.replace("<p>","[CR]").replace("</p>","[CR]").replace("<br>","[CR]").replace("<BR>","[CR]")
				self.HoroTxt.setText(t); 
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
