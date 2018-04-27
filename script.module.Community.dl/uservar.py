import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Project X Wizard'
EXCLUDES       = [ADDON_ID, '']
# Text File with build info in it.
BUILDFILE      = ''
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = ''
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Project X Youtube'
YOUTUBEFILE    = ''
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://tvsupertuga.website/wizard/projectxwizard4/submenus/Community.dl/themes.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = ''
# Text file for roms and emus
ROMPACK        = 'http://tvsupertuga.website/wizard/projectxwizard4/submenus/power%20installer/programas%20windows/rom-packs.txt.txt'
EMUAPKS        = 'http://tvsupertuga.website/wizard/projectxwizard4/submenus/power%20installer/programas%20windows/programas%20windows.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://'
ICONMAINT      = 'https://'
ICONSPEED      = 'https://'
ICONAPK        = 'https://'
ICONRETRO      = 'https://'
ICONADDONS     = 'https://'
ICONYOUTUBE    = 'https://'
ICONSAVE       = 'https://'
ICONTRAKT      = 'https://'
ICONREAL       = 'https://'
ICONLOGIN      = 'https://'
ICONCONTACT    = 'https://'
ICONSETTINGS   = 'https://'
ICONWIZARD1URL   = 'https://'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
#COLOR1         = 'dodgerblue'
#COLOR2         = 'yellow'
COLOR1         = 'snow'
COLOR2         = 'floralwhite'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+''+COLOR2+''+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = ''
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://'
CONTACTFANART  = 'https://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'Project X Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################