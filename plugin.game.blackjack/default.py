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
		closing=False; firsttime=False; c={}; strXMLname=''; strFallbackPath=''; List01D=[]; List01DB=[]
		maxW=1280; maxH=720; 
		##
		def __init__(self,strXMLname,strFallbackPath):
			self.strXMLname=strXMLname
			self.strFallbackPath=strFallbackPath
		def onInit(self):
			try:
				try: self.wID=xbmcgui.getCurrentWindowId()
				except: self.wID=0
				deb('CurrentWindowId()',str(self.wID)); 
				deb('getResolution()',str(self.getResolution())); 
				self.firsttime=True
				debob(['screen size',self.getWidth(),self.getHeight()])
				debob(['skin size',self.maxW,self.maxH])
				self.LoadSkinItems()
				try: self.setFocus(self.bExit)
				except: pass
				self.setupScreen()
				#try: self.setFocus(self.List01)
				#except: pass
			except: pass
		def ResetTheList(self):
			try: 
				PlaySndWav('cards_shuffling')
				self.ScrTp('0','erCount'); 
				self.List01.reset(); 
				self.List02.reset(); 
				self.List03.reset(); 
				self.List01DB=[]; #self.ErrLabel01.setLabel(' '); 
				self.List01D=[]; 
				self.DeckImage=iDeck()
				self.ImgCard01.setImage(self.DeckImage)
				self.ImgCard02.setImage(self.DeckImage)
				self.CardNo1=''
				self.CardNo2=''
			except: pass
		def loadCardList(self):
			try:
				self.ResetTheList()
				
				self.List01D=[]; #debob(self.List01D)
				#for sSuit in ["R","B"]:
				#	self.List01D.append([0,"Joker",sSuit])
				for sSuit in ["D","H","S","C"]:
					self.List01D.append([1,"A",sSuit])
					self.List01D.append([2,"2",sSuit])
					self.List01D.append([3,"3",sSuit])
					self.List01D.append([4,"4",sSuit])
					self.List01D.append([5,"5",sSuit])
					self.List01D.append([6,"6",sSuit])
					self.List01D.append([7,"7",sSuit])
					self.List01D.append([8,"8",sSuit])
					self.List01D.append([9,"9",sSuit])
					self.List01D.append([10,"10",sSuit])
					self.List01D.append([10,"J",sSuit])
					self.List01D.append([10,"Q",sSuit])
					self.List01D.append([10,"K",sSuit])
				
				self.List01.reset(); self.List01DB=[]; iCount=0; 
				d=self.DeckImage
				#if isFile(d): print "Found:  "+d
				##print "---"
				##print self.List01D
				##print "+++"
				
				self.List01D=random.sample(self.List01D,len(self.List01D))
				
				##print self.List01D
				##print "==="
				k1=True; k2=True; k3=True; 
				for iValue,iLabel,iSuit in self.List01D:
					try:
						i=iCard(iSuit,iLabel)
						t='[B]'+iLabel+'[/B]'
						#d=i
						item=xbmcgui.ListItem(t); 
						#item.setArt({'thumb':i,'poster':i,'banner':i,'fanart':i,'clearart':i,'clearlogo':i,'landscape':i}); 
						#item.setIconImage(d); 
						item.setThumbnailImage(d); 
						item.setThumbnailImage(i); 
						#debob(['img',i]); 
						item.setLabel(t); 
						item.setProperty('iCount',str(iCount)); 
						item.setProperty('iThumb',str(i)); 
						item.setProperty('iCard',str(i)); 
						item.setProperty('iDeck',str(d)); 
						item.setProperty('isdeckup',str(k3).lower()); 
						item.setProperty('isdeckup','true'); 
						item.setProperty('iValue',str(iValue)); 
						item.setProperty('iSuit',str(iSuit)); 
						item.setProperty('iLabel',str(iLabel)); 
						item.setProperty('iVisible',str(k2).lower()); 
						#item.setProperty('iVisible','true'); 
						#item.setProperty('iEnabled','true'); 
						item.setProperty('iEnabled',str(k1).lower()); 
						self.List01DB.append((iCount,k1,k2,k3,iValue,iLabel,iSuit,t,i,d))
						self.List01.addItem(item); iCount=iCount+1; 
					except: pass
				#note("Cards in the deck",str(self.List01.size()))
				self.CardCountTotal=int(self.List01.size())
				self.CardCountCurrent=int(self.List01.size())
				#self.ScrTp(str(self.CardCountCurrent),'erCount'); 
				#if int(self.List01.size()) > 0:
				#	try: self.setFocus(self.List01)
				#	except: pass
#					self.ScrTp(str(self.List01.size()),'erCount'); 
#					self.List01.selectItem(0)
#					iCount=int(self.List01.getListItem(0).getProperty('iCount')); 
#					name=self.List01.getListItem(0).getLabel(); 
				self.Initialdeal()
				try: self.setFocus(self.BtnTopMenu03)
				except: pass
			except: pass
		def setupScreen(self):
			try:
				#self.iBack.setImage(artp("black1")); 
				#self.iBackground.setImage(MediaFile("black1.png")); 
				self.iBack.setImage(MediaFile("black1.png")); 
				self.iBackground.setImage(addonFanart); 
				
				#wegweg
				#return
				#self.loadLogFile()
				self.loadCardList()
				
				##
			except: pass
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
				
				self.c['List01']=9000; 
				try: self.List01=self.getControl(self.c['List01']); 
				except: pass
				self.c['List02']=9001; 
				try: self.List02=self.getControl(self.c['List02']); 
				except: pass
				self.c['List03']=9002; 
				try: self.List03=self.getControl(self.c['List03']); 
				except: pass
				self.c['ErrLabel02']=101; 
				try: self.ErrLabel02=self.getControl(self.c['ErrLabel02']); 
				except: pass
				self.c['ErrLabel03']=102; 
				try: self.ErrLabel03=self.getControl(self.c['ErrLabel03']); 
				except: pass
				self.c['BtnTopMenu01']=400; 
				try: self.BtnTopMenu01=self.getControl(self.c['BtnTopMenu01']); 
				except: pass
				self.c['BtnTopMenu02']=401; 
				try: self.BtnTopMenu02=self.getControl(self.c['BtnTopMenu02']); 
				except: pass
				self.c['BtnTopMenu03']=402; 
				try: self.BtnTopMenu03=self.getControl(self.c['BtnTopMenu03']); 
				except: pass
				
				self.c['BtnCard01']=501; 
				try: self.BtnCard01=self.getControl(self.c['BtnCard01']); 
				except: pass
				self.c['ImgCard01']=502; 
				try: self.ImgCard01=self.getControl(self.c['ImgCard01']); 
				except: pass
				self.c['BtnCard02']=503; 
				try: self.BtnCard02=self.getControl(self.c['BtnCard02']); 
				except: pass
				self.c['ImgCard02']=504; 
				try: self.ImgCard02=self.getControl(self.c['ImgCard02']); 
				except: pass
				#self.DeckImage=iDeck('Black Skull')
				#self.ImgCard01.setImage(self.DeckImage)
				#self.ImgCard02.setImage(self.DeckImage)
				self.CardNo1=''
				self.CardNo2=''
				
				#self.ScrTp('0','erCount'); 
				
				
				
			except: pass
		def ScrTp(self,s='',v='ScreenType'):
			try:
				if len(v) > 0:
					self.setProperty(v,s); 
			except: pass
		def Initialdeal(self):
			try:
				self.dealCard(1)
				self.dealCard()
				self.dealCard(1)
				self.dealCard()
			except: pass
		def CompareCards(self):
			try:
				PlayerCount=self.CountCards(1)
				DealerCount=self.CountCards(0)
				self.List02.getListItem(0).setThumbnailImage(self.List02.getListItem(0).getProperty('iCard'))
				if (PlayerCount < 22) and ((PlayerCount > DealerCount) or (DealerCount > 21)): ## Win
					a='Player won!'; b='You win'; 
					if PlayerCount==21: b='You win double for winning with "21".'; 
					PlaySndWav('applause')
				elif (PlayerCount < 22) and (PlayerCount==DealerCount): ## Tie
					a='We have a tie.'; b='No one wins in a draw.'; 
					PlaySndWav('guitar')
				elif (PlayerCount > 21) or ((PlayerCount < DealerCount) and (DealerCount < 22)): ## Loose
					a='Dealer won.'; b='"...and remember to pay the lady!"'; 
					PlaySndWav('crowd_boo')
				else: ## Unknown
					a='[ Unknown ]'; b=''; 
					#PlaySndWav('crowd_boo')
				c='[ Dealer ] %s vs %s [Player]'%(str(DealerCount),str(PlayerCount)); 
				popOK(a,"Game Results",b,c)
				
				try: self.setFocus(self.BtnTopMenu01)
				except: pass
				
				if tfalse(getSet("auto-deal"))==True:
					xbmc.sleep(1000); self.loadCardList(); 
				##try: self.setFocus(self.BtnTopMenu03); 
				##except: pass
			except: pass
		def StandCards(self):
			try:
				PlayerCount=self.CountCards(1)
				if PlayerCount < 22:
					for i in range(0,20):
						DealerCount=self.CountCards(0)
						if DealerCount < 11:
							self.dealCard()
					if (DealerCount < 21) and (PlayerCount < 22) and (DealerCount < PlayerCount):
						for i in range(0,10):
							DealerCount=self.CountCards(0)
							if (DealerCount < 21) and (PlayerCount < 22) and (DealerCount < PlayerCount):
								self.dealCard()
				self.CompareCards()
			except: pass
		def dealCard(self,ToPerson=0,CardSlot=0):
			try:
				if ToPerson==1: CurPersonList=self.List03
				else: CurPersonList=self.List02
				debob([ToPerson,'List Size',int(CurPersonList.size())])
				PlaySndWav('game_move')
				if (int(CurPersonList.size())==0) and (ToPerson==0):
					self.List01.getListItem(CardSlot).setThumbnailImage(self.List01.getListItem(CardSlot).getProperty('iDeck'))
				CurPersonList.addItem(self.List01.getListItem(CardSlot))
				self.List01.removeItem(CardSlot)
				
				
				if ToPerson==1: 
					CardCount=self.CountCards(1)
					#debob(['CardCount',CardCount,str(CardCount)])
					self.ScrTp(str(CardCount),'erCount'); 
					PlayerCount=CardCount
					if PlayerCount > 21:
						DealerCount=self.CountCards(0)
						self.List02.getListItem(0).setThumbnailImage(self.List02.getListItem(0).getProperty('iCard'))
						a='Dealer won.'; b='"...and remember to pay the lady!"'; 
						c='[ Dealer ] %s vs %s [Player]'%(str(DealerCount),str(PlayerCount)); 
						PlaySndWav('crowd_boo')
						popOK(a,"Game Results",b,c)
						try: self.setFocus(self.BtnTopMenu01)
						except: pass
						if tfalse(getSet("auto-deal"))==True:
							xbmc.sleep(1000); self.loadCardList(); 
				pass
			except: pass
		def CountCards(self,ToPerson=0):
			try:
				if ToPerson==1: CurPersonList=self.List03
				else: CurPersonList=self.List02
				CardCount=0; AceCount=0
				if CurPersonList.size() > 0:
					for i in range(0,CurPersonList.size()):
						#try:
							CurCardValue=int(CurPersonList.getListItem(i).getProperty('iValue'))
							if CurCardValue==1: CurCardValue=CurCardValue+10; AceCount=AceCount+1
							CardCount=CardCount+CurCardValue
							#debob([ToPerson,i,CurCardValue,CardCount])
						#except: pass
					debob(['no of aces',AceCount,'CardCount',CardCount])
					if (CardCount > 21) and ((AceCount > 0)):
							for i in range(0,AceCount):
									if (CardCount > 21):
											CardCount=CardCount-10
									debob([i,'CardCount *',CardCount])
					debob(['CardCount ==',CardCount])
					return CardCount
				else: return 0
			except: return 0
		def onClick(self,controlId):
			try:
				if   controlId==self.c['bExit']: self.AskToClose()
				#elif   controlId==self.c['SideGroup01ocBtn']: 
				#	gX=self.SideGroup01.getX(); gY=self.SideGroup01.getY(); 
				#	debob(['From',gX,gY])
				#	if gX==self.maxW: self.SideGroup01.setPosition(1030,gY); debob(['To',1030,gY])
				#	else: self.SideGroup01.setPosition(self.maxW,gY); debob(['To',self.maxW,gY])
				#	
				#	pass
				elif   controlId==self.c['BtnTopMenu01']: ## New Game ##
						#print "test0"
						self.loadCardList()
						#print "test1"
						pass
				elif   controlId==self.c['BtnTopMenu02']: ## Stand ##
						self.StandCards()
						pass
				elif   controlId==self.c['BtnTopMenu03']: ## Draw Card ##
						self.dealCard(1)
						pass
				elif   controlId==self.c['BtnCard01']:
						#self.BtnCard01
						#self.ImgCard01
						#note("Card","1")
						self.dealCard(1)
						pass
				elif   controlId==self.c['BtnCard02']: 
						#self.BtnCard02
						#self.ImgCard02
						#note("Card","2")
						self.StandCards()
						pass
				elif   controlId==self.c['List01']: 
						#iCount=int(self.List01.getSelectedItem().getProperty('iCount')); 
						#name=self.List01.getSelectedItem().getLabel(); 
						pass
				else:
					try:
						
						pass
					except: pass
			except Exception,e: debob(["Error",e])
			except: pass
		def onAction(self,action): 
			try:
				actId=int(action.getId()); actIds=str(action.getId()); actBC=str(action.getButtonCode()); xx=0; yy=0; 
				try: actAmnt1=action.getAmount1()
				except: actAmnt1=0-900
				try: actAmnt2=action.getAmount2()
				except: actAmnt2=0-900
				mW=self.maxW; mH=self.maxH; mWa=int(self.getWidth()); mHa=int(self.getHeight()); 
				actAmnt1k=int(actAmnt1*mW/mWa); actAmnt2k=int(actAmnt2*mH/mHa); 
				##
				if   action==ACTION_PREVIOUS_MENU: self.AskToClose()
				elif action==ACTION_NAV_BACK: self.AskToClose()
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
