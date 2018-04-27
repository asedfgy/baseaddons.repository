import os, xbmc, xbmcaddon
import base64

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = base64.b64decode('UHJvamVjdCBYIFdpemFyZA==')
EXCLUDES       = [ADDON_ID, 'tvsupertuga.repository', 'projectx.wizard']
# Text File with build info in it.
BUILDFILE      = base64.b64decode('aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9wcm9qZWN0eHdpemFyZC50eHQ=')
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = base64.b64decode('aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9wcm9qZWN0eHdpemFyZGFway50eHQ=')
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = base64.b64decode('UHJvamVjdCBYIFlvdXR1YmU=')
YOUTUBEFILE    = base64.b64decode('aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkL3N1Yi95b3V0dWJlLnR4dA==')
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = base64.b64decode('aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9hZGRvbnMudHh0')
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = base64.b64decode('aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9hZHZhbmNlZHNldHRpbmdzLnR4dA==')

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
ICONBUILDS     = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONMAINT      = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONAPK        = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONADDONS     = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONYOUTUBE    = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONSAVE       = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONTRAKT      = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONREAL       = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONLOGIN      = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONCONTACT    = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONSETTINGS   = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONSPINZ      = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONKODI       = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONSPMC       = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONGAMES      = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONMOVIES     = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONANDROID    = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONSPEED      = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONPRO        = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONADDONS     = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONYOUTUBE    = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
ICONLOGIN      = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'cyan'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
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
CONTACT        = 'Thank you for choosing Project X Wizard                    tvsupertuga@gmail.com'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
CONTACTFANART  = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
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
AUTOINSTALL    = 'yes'
# Addon ID for the repository
REPOID         = base64.b64decode('dHZzdXBlcnR1Z2EucmVwb3NpdG9yeQ==')
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = base64.b64decode('aHR0cDovL3R2c3VwZXJ0dWdhLnh5ei90dnN1cGVydHVnYS5yZXBvc2l0b3J5L3R2c3VwZXJ0dWdhLnJlcG9zaXRvcnkvYWRkb24ueG1s')
# Url to folder zip is located in
REPOZIPURL     = base64.b64decode('aHR0cDovL3R2c3VwZXJ0dWdhLnh5ei90dnN1cGVydHVnYS5yZXBvc2l0b3J5L2luc3RhbC90dnN1cGVydHVnYS5yZXBvc2l0b3J5Lw==')
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = base64.b64decode('aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9wcm9qZWN0eHdpemFyZG5vdGlmaWNhdGlvbi54bWw=')
# Use either 'Text' or 'Image'
HEADERTYPE     = base64.b64decode('VGV4dA==')
HEADERMESSAGE  = base64.b64decode('UHJvamVjdCBYIFdpemFyZA==')
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = base64.b64decode('aHR0cHM6Ly9pNTguc2VydmltZy5jb20vdS9mNTgvMTkvNDQvOTEvNDMvcHJvamVjMTAucG5n')
#########################################################
