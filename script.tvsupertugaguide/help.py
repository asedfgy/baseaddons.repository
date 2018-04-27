import xbmc,xbmcaddon,xbmcvfs,xbmcgui
import sys
which = sys.argv[1]

ADDON = xbmcaddon.Addon(id='script.tvsupertugaguide')

if which == "commands":
    path = xbmc.translatePath('special://home/addons/script.tvsupertugaguide/commands.txt')
elif which == "autoplaywith":
    path = xbmc.translatePath('special://home/addons/script.tvsupertugaguide/resources/playwith/readme.txt')
elif which == "Features":
    path = xbmc.translatePath('special://home/addons/script.tvsupertugaguide/Features.txt')
elif which == "Customini":
    path = xbmc.translatePath('special://home/addons/script.tvsupertugaguide/Customini.txt')
elif which == "Facebook":
    path = xbmc.translatePath('special://home/addons/script.tvsupertugaguide/Facebook.txt')
f = xbmcvfs.File(path,"rb")
data = f.read()
dialog = xbmcgui.Dialog()
dialog.textviewer('Help', data)
