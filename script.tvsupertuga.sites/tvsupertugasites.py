import time
import xbmc
import os
import xbmcgui
import urllib2
import webbrowser


def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
		function4,
        function5
        )
        
    call = dialog.select('[B][COLOR cyan]TV[/COLOR]-[COLOR red]supertuga[/COLOR][/B]', [
    '[B][COLOR=deepskyblue]     FORUM [/COLOR][/B]', 
    '[B][COLOR=deepskyblue]     FACEBOOK [/COLOR][/B]',
    '[B][COLOR=deepskyblue]     CANAL YOUTUBE[/COLOR][/B]',
    '[B][COLOR=deepskyblue]     REPOSITORIO[/COLOR][/B]',
    '[B][COLOR=deepskyblue]     DOACOES PAYPAL [/COLOR][/B]'])	
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()
    
def function1():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://forumtvsupertuga.pe.hu/' ) )
    else:
        opensite = webbrowser . open('http://forumtvsupertuga.pe.hu/')

def function2():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.facebook.com/TVsupertuga.PT' ) )
    else:
        opensite = webbrowser . open('https://www.facebook.com/TVsupertuga.PT')
        
def function3():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.youtube.com/channel/UCp1sYUFzRQIMNZqvVeQOF0A?view_as=subscriber' ) )
    else:
        opensite = webbrowser . open('https://www.youtube.com/channel/UCp1sYUFzRQIMNZqvVeQOF0A?view_as=subscriber')
        
def function4():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://repo.tvsupertuga.xyz/' ) )
    else:
        opensite = webbrowser . open('http://repo.tvsupertuga.xyz/')
		
def function5():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.paypal.me/teamtvsupertuga' ) )
    else:
        opensite = webbrowser . open('https://www.paypal.me/teamtvsupertuga')		
		
     
menuoptions()
