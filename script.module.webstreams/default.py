import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,base64

addon_id            = 'script.module.webstreams'
AddonTitle          = '[COLOR mediumpurple]Web Streams[/COLOR]'
fanarts             = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon                = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
dialog              = xbmcgui.Dialog()
dp                  = xbmcgui.DialogProgress()
baseurl             = base64.b64decode(b'aHR0cDovL2dvb2dsZS5jb20=')

def GetMenu():

	addLink("                          [COLOR cyan]TV[/COLOR]-[COLOR red]supertuga[/COLOR]",baseurl,999,icon,fanarts,'')

	addLink("[COLOR yellow]Aqui poderao encontrar listas diarias de iptv.[/COLOR]",baseurl,999,icon,fanarts,'')
	addLink("[COLOR yellow]Listas atualizadas automaticamente pelo server.[/COLOR]",baseurl,999,icon,fanarts,'')
	
	
	addLink("[COLOR cyan]####################################################[/COLOR]",baseurl,999,icon,fanarts,'')



	addDir('                         [COLOR white]WEB SERVER 1[/COLOR]',base64.b64decode(b'aHR0cDovL3NvdXJjZXR2LmluZm8='),203,icon,fanarts)

	
	
	
	#addDir('[COLOR mediumpurple]Source 3[/COLOR]',base64.b64decode(b'aHR0cDovL3d3dy5pcHR2ZW1iZWQubmV0L2lwdHYv'),202,icon,fanarts)

	
	xbmc.executebuiltin('Container.SetViewMode(50)')

def SCRAPE_DVBSAT():

	i = 0
	result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MA=='))
	match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
	for item in match:
		i = i + 1
		item = item.replace('<br />','\n')
		url = item
		addDir('[COLOR white]LIST ' + str(i) + '[/COLOR]',url,3,icon,fanarts)

	result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MTA='))
	match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
	for item in match:
		i = i + 1
		item = item.replace('<br />','\n')
		url = item
		addDir('[COLOR white]LIST ' + str(i) + '[/COLOR]',url,3,icon,fanarts)
		
	result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MjA='))
	match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
	for item in match:
		i = i + 1
		item = item.replace('<br />','\n')
		url = item
		addDir('[COLOR white]LIST ' + str(i) + '[/COLOR]',url,3,icon,fanarts)

	xbmc.executebuiltin('Container.SetViewMode(50)')

def SCRAPE_IPTVEMBED(url):

	result = open_url(url)
	match = re.compile('<div class="entry-content"(.+?)</div>',re.DOTALL).findall(result)

	for item in match:
		name=re.compile('title="(.+?)"').findall(item)[0]         				
		url=re.compile('<a href="(.+?)"').findall(item)[0]     
		iconimage=re.compile('<img.+?src="(.+?)"').findall(item)[0]         						
		addDir('[COLOR white]'+ name +'[/COLOR]',url,2,iconimage,fanarts)

	try:
		nexturl=re.compile("<link rel='next' href='(.+?)'",re.DOTALL).findall(result)[0]         				
		addDir('[COLOR yellow]Next Page -->[/COLOR]',nexturl,202,icon,fanarts)
	except: pass

	xbmc.executebuiltin('Container.SetViewMode(500)')

def SCRAPE_SOURCETV_CATS(url):

	result = open_url(url)
	match = re.compile('<li class="cat-item cat-item(.+?)</li>',re.DOTALL).findall(result)
	for item in match:
		try:
			name=re.compile('title=".+?">(.+?)</a>').findall(item)[0]         				
		except:
			name=re.compile('<a href=".+?" >(.+?)</a>').findall(item)[0]         				
		url=re.compile('<a href="(.+?)"').findall(item)[0]     
		addDir('[COLOR white]'+ name +'[/COLOR]',url,204,icon,fanarts)

def SCRAPE_SOURCETV(url):

	result = open_url(url)
	match = re.compile('<div class="panel-wrapper">(.+?)<div class="article-excerpt-wrapper">',re.DOTALL).findall(result)
	fail = 0
	for item in match:
		try:
			name=re.compile('title="(.+?)"').findall(item)[0]        				         				
			url=re.compile('<a href="(.+?)"').findall(item)[0] 
			iconimage=re.compile('<img.+?src="(.+?)"').findall(item)[0]  
		except: fail = 1
		
		if fail == 0:
			addDir('[COLOR white]'+ name +'[/COLOR]',url,2,iconimage,fanarts)
		fail = 0

	try:
		nexturl=re.compile('<link rel="next" href="(.+?)" />',re.DOTALL).findall(result)[0]         				
		addDir('[COLOR yellow]Next Page -->[/COLOR]',nexturl,204,icon,fanarts)
	except: pass

	xbmc.executebuiltin('Container.SetViewMode(500)')


def FIND_OUT(name,url,iconimage):

	try:
		result = open_url(url)

		if "username" in result:
			i = 1
			match = re.compile('<p>Copy the iptv stream and open in VLC(.+?)<br class="clearer" />',re.DOTALL).findall(result)
			string = str(match)
			match2 = re.compile('http(.+?)br',re.DOTALL).findall(string)
			fail = 0
			for item in match2:
				try:
					url=re.compile('//(.+?)<').findall(item)[0] 
					url = url.replace('&amp;','&')
					if "username" in url:
						a = url.split('username=')[1]
						b = a.split('&')[0]
					else: fail = 1
				except: 
					fail = 1

				if fail == 0:
					addDir("[COLOR yellow][I]" + str(b).upper() + ' [/I][/COLOR]  - [COLOR mediumpurple]Thank you for this list![/COLOR]','http://'+url,3,iconimage,fanarts)
				fail = 0
		else:
			GENERATE_M3U8(name,url,iconimage)
	except: 
		dialog.ok(AddonTitle, "There was an error connecting to the host. Please try again later.")
		quit()

def GENERATE_M3U8(name,url,iconimage):

	try:
		if "iptvembed" in url:
			result = open_url(url)
			match = re.compile('#EXTM3U<br />(.+?)<div></div>',re.DOTALL).findall(result)
			for item in match:
				item = item.replace('<br />','\n')
				item = item.replace('</pre>','')
				url = item
		elif "sourcetv" in url:
			result = open_url(url)
			match = re.compile('<pre class="alt2"(.+?)<br class="clearer" />',re.DOTALL).findall(result)
			for item in match:
				item = item.replace('<br />','\n')
				item = item.replace('</pre>','')
				url = item
		elif not " " in url:
			url = open_url(url)
		else: url = url

		url = url.replace('#AAASTREAM:','#A:')
		url = url.replace('#EXTINF:','#A:')
		matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
		li = []
		for params, display_name, url in matches:
			item_data = {"params": params, "display_name": display_name, "url": url}
			li.append(item_data)
		list = []
		for channel in li:
			item_data = {"display_name": channel["display_name"], "url": channel["url"]}
			matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
			for field, value in matches:
				item_data[field.strip().lower().replace('-', '_')] = value.strip()
			list.append(item_data)
			found = 0
		for channel in list:
			found = 1
			name = GetEncodeString(channel["display_name"])
			url = GetEncodeString(channel["url"])
			url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
			if not ".m3u8" in url:
				addLink('[COLOR mediumpurple]' + name + '[/COLOR]',url,4,iconimage,fanarts,'')
			if found == 0:
				addLink('[COLOR red]Sorry, No links found in this list.[/COLOR]',url,999,icon,fanarts,'')
	except: 
		dialog.ok(AddonTitle, "There was an error gathering the list. Please try another.")
		quit()

def GetEncodeString(str):
	try:
		import chardet
		str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
	except:
		try:
			str = str.encode("utf-8")
		except:
			pass
	return str

def PLAYLINK(name,url,iconimage):

	if not 'f4m'in url:
		if '.m3u8'in url:
			url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url		
		elif '.ts'in url:
			url = url.replace('.ts','.m3u8')
			url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url		

	if "plugin://" in url:
		url = "PlayMedia("+url+")"
		xbmc.executebuiltin(url)
		quit()

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	xbmc.Player().play(url,liz,False)

def open_url(url):

    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

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
	
def addDir(name,url,mode,iconimage,fanart,description=''):

	if "imgur" in iconimage:
		if not ".jpg" in iconimage:
			if not ".png" in iconimage:
				iconimage = iconimage + ".jpg"
	if "imgur" in fanart:
		if not ".jpg" in fanart:
			if not ".png" in fanart:
				fanart = fanart + ".jpg"
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setProperty( "fanart_Image", fanart )
	liz.setProperty( "icon_Image", iconimage )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

def addLink(name, url, mode, iconimage, fanart, description=''):

	if "imgur" in iconimage:
		if not ".jpg" in iconimage:
			if not ".png" in iconimage:
				iconimage = iconimage + ".jpg"
	if "imgur" in fanart:
		if not ".jpg" in fanart:
			if not ".png" in fanart:
				fanart = fanart + ".jpg"
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setProperty( "fanart_Image", fanart )
	liz.setProperty( "icon_Image", iconimage )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None; fanart=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: fanart=urllib.unquote_plus(params["fanart"])
except: pass
 
if mode==None or url==None or len(url)<1: GetMenu()
elif mode==1:SCRAPE(url)
elif mode==2:FIND_OUT(name,url,iconimage)
elif mode==3:GENERATE_M3U8(name,url,iconimage)
elif mode==4:PLAYLINK(name,url,iconimage)
elif mode==201:SCRAPE_DVBSAT()
elif mode==202:SCRAPE_IPTVEMBED(url)
elif mode==203:SCRAPE_SOURCETV_CATS(url)
elif mode==204:SCRAPE_SOURCETV(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))