################################################################################
#      Copyright (C) 2015 Surfacingx                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys , xbmcvfs , glob
import shutil
import urllib2 , urllib
import re
import zipfile
import uservar
import fnmatch
import plugintools
import base64
import time
import platform , subprocess
import zipfile
import yt
import ookla
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
try : from sqlite3 import dbapi2 as database
except : from pysqlite2 import dbapi2 as database
from datetime import date , datetime , timedelta
from urlparse import urljoin
from resources . libs import extract , downloader , notify , debridit , traktit , loginit , skinSwitch , uploadLog , yt , wizard as wiz
if 73 - 73: II111iiii
IiII1IiiIiI1 = uservar . ADDON_ID
iIiiiI1IiI1I1 = uservar . ADDON_ID
o0OoOoOO00 = uservar . ADDON_ID
I11i = xbmcaddon . Addon ( IiII1IiiIiI1 )
O0O = xbmc . translatePath ( 'special://home/addons/' )
Oo = xbmc . translatePath ( 'special://home/addonsbroke/' )
I1ii11iIi11i = wiz . addonId ( IiII1IiiIiI1 )
I1IiI = xbmcgui . DialogProgress ( )
o0OOO = uservar . ADDONTITLE
if 13 - 13: ooOo + Ooo0O
IiiIII111iI = base64 . decodestring
IiII = I1ii11iIi11i . getSetting ( 'User' )
iI1Ii11111iIi = I11i . getAddonInfo ( 'path' ) . decode ( "utf-8" )
i1i1II = xbmc . translatePath ( os . path . join ( iI1Ii11111iIi , "resources" , "iiNT3LiiList.txt" ) )
O0oo0OO0 = wiz . addonInfo ( IiII1IiiIiI1 , 'version' )
I1i1iiI1 = wiz . addonInfo ( IiII1IiiIiI1 , 'path' )
iiIIIII1i1iI = xbmcgui . Dialog ( )
o0oO0 = xbmcgui . Dialog ( )
oo00 = xbmcgui . DialogProgress ( )
o00 = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = ( IiiIII111iI ( 'aHR0cDovL3Byb2plY3R4d2l6YXJkLm9yZy8=' ) )
o0oOoO00o = xbmc . translatePath ( 'special://home/userdata/addon_data/script.module.projectx.wizard' )
i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/script.module.projectx.wizard/imports/tvGuide/ResetDatabase.py' ) )
oOOoo00O0O = xbmc . translatePath ( 'special://thumbnails' ) ;
i1111 = "Xhoans"
i11 = base64 . decodestring ( 'LnBocA==' )
I11 = I1ii11iIi11i . getLocalizedString
if 98 - 98: I1111 * o0o0Oo0oooo0 / I1I1i1 * oO0 / IIIi1i1I
if 72 - 72: iii11iiII % i11IiIiiIIIII / IiiIII111ii / iiIIi1IiIi11 . i1Ii
if 25 - 25: OO00O0O0O00Oo + OOoooooO / i1IIi . i11IiIiiIIIII % I1111 . I1I1i1
i1I111I = int ( sys . argv [ 1 ] )
i11I1IIiiIi = xbmc . translatePath ( I1ii11iIi11i . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
IiIiIi = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
II = o0oOoO00o + '/addons.ini'
iI = xbmc . translatePath ( os . path . join ( '//storage//emulated//0//Download' , '' ) )
iI11iiiI1II = xbmc . translatePath ( 'special://logpath/' )
O0oooo0Oo00 = xbmc . translatePath ( 'special://profile/' )
O0O = os . path . join ( o00 , 'addons' )
zip = plugintools . get_setting ( "zip" )
Ii11iii11I = xbmc . translatePath ( os . path . join ( zip ) )
oOo00Oo00O = os . path . join ( o00 , 'userdata' )
iI11i1I1 = os . path . join ( O0O , IiII1IiiIiI1 )
o0o0OOO0o0 = os . path . join ( O0O , 'packages' )
ooOOOo0oo0O0 = os . path . join ( oOo00Oo00O , 'addon_data' )
o0 = os . path . join ( oOo00Oo00O , 'addon_data' , IiII1IiiIiI1 )
I11II1i = os . path . join ( oOo00Oo00O , 'advancedsettings.xml' )
IIIII = os . path . join ( oOo00Oo00O , 'sources.xml' )
ooooooO0oo = os . path . join ( oOo00Oo00O , 'favourites.xml' )
IIiiiiiiIi1I1 = os . path . join ( oOo00Oo00O , 'profiles.xml' )
I1IIIii = os . path . join ( oOo00Oo00O , 'guisettings.xml' )
oOoOooOo0o0 = os . path . join ( oOo00Oo00O , 'Thumbnails' )
OOOO = os . path . join ( oOo00Oo00O , 'Database' )
OOO00 = os . path . join ( I1i1iiI1 , 'fanart.jpg' )
iiiiiIIii = os . path . join ( I1i1iiI1 , 'icon.png' )
O000OO0 = os . path . join ( I1i1iiI1 , 'resources' , 'art' )
I11iii1Ii = os . path . join ( o0 , 'wizard.log' )
I1IIiiIiii = xbmc . getSkinDir ( )
O000oo0O = wiz . getS ( 'buildname' )
OOOOi11i1 = wiz . getS ( 'defaultskin' )
IIIii1II1II = wiz . getS ( 'defaultskinname' )
i1I1iI = wiz . getS ( 'defaultskinignore' )
oo0OooOOo0 = wiz . getS ( 'buildversion' )
o0O = wiz . getS ( 'buildtheme' )
O00oO = wiz . getS ( 'latestversion' )
I11i1I1I = wiz . getS ( 'installmethod' )
oO0Oo = wiz . getS ( 'show15' )
oOOoo0Oo = wiz . getS ( 'show16' )
o00OO00OoO = wiz . getS ( 'show17' )
OOOO0OOoO0O0 = wiz . getS ( 'show18' )
O0Oo000ooO00 = wiz . getS ( 'adult' )
oO0Ii1iIiII1ii1 = wiz . getS ( 'showmaint' )
ooOooo000oOO = wiz . getS ( 'autoclean' )
Oo0oOOo = wiz . getS ( 'clearcache' )
Oo0OoO00oOO0o = wiz . getS ( 'clearpackages' )
OOO00O = wiz . getS ( 'clearthumbs' )
OOoOO0oo0ooO = wiz . getS ( 'autocleanfeq' )
O0o0O00Oo0o0 = wiz . getS ( 'nextautocleanup' )
O00O0oOO00O00 = wiz . getS ( 'includevideo' )
i1Oo00 = wiz . getS ( 'includeall' )
i1i = wiz . getS ( 'includebob' )
iiI111I1iIiI = wiz . getS ( 'includephoenix' )
IIIi1I1IIii1II = wiz . getS ( 'includespecto' )
O0ii1ii1ii = wiz . getS ( 'includegenesis' )
oooooOoo0ooo = wiz . getS ( 'includeexodus' )
I1I1IiI1 = wiz . getS ( 'includeonechan' )
III1iII1I1ii = wiz . getS ( 'includesalts' )
oOOo0 = wiz . getS ( 'includesaltslite' )
oo00O00oO = wiz . getS ( 'seperate' )
iIiIIIi = wiz . getS ( 'notify' )
ooo00OOOooO = wiz . getS ( 'noteid' )
O00OOOoOoo0O = wiz . getS ( 'notedismiss' )
O000OOo00oo = wiz . getS ( 'traktlastsave' )
oo0OOo = wiz . getS ( 'debridlastsave' )
ooOOO00Ooo = wiz . getS ( 'loginlastsave' )
IiIIIi1iIi = wiz . getS ( 'keepfavourites' )
ooOOoooooo = wiz . getS ( 'keepsources' )
II1I = wiz . getS ( 'keepprofiles' )
O0i1II1Iiii1I11 = wiz . getS ( 'keepadvanced' )
IIII = wiz . getS ( 'keeprepos' )
iiIiI = wiz . getS ( 'keepsuper' )
o00oooO0Oo = wiz . getS ( 'keepwhitelist' )
o0O0OOO0Ooo = wiz . getS ( 'keeptrakt' )
iiIiII1 = wiz . getS ( 'keepdebrid' )
OOO00O0O = wiz . getS ( 'keeplogin' )
ooOOO00Ooo = wiz . getS ( 'loginlastsave' )
iii = wiz . getS ( 'developer' )
oOooOOOoOo = wiz . getS ( 'enable3rd' )
i1Iii1i1I = wiz . getS ( 'wizard1name' )
OOoO00 = wiz . getS ( 'wizard1url' )
IiI111111IIII = wiz . getS ( 'wizard2name' )
i1Iiii111iI1iIi1 = wiz . getS ( 'wizard2url' )
OOO = wiz . getS ( 'wizard3name' )
oo0OOo0 = wiz . getS ( 'wizard3url' )
I11IiI = I1ii11iIi11i . getSetting ( 'path' ) if not I1ii11iIi11i . getSetting ( 'path' ) == '' else 'special://home/'
O0ooO0Oo00o = os . path . join ( I11IiI , 'My_Builds' , '' )
OOoOO0oo0ooO = int ( float ( OOoOO0oo0ooO ) ) if OOoOO0oo0ooO . isdigit ( ) else 0
ooO0oOOooOo0 = date . today ( )
i1I1ii11i1Iii = ooO0oOOooOo0 + timedelta ( days = 1 )
I1IiiiiI = ooO0oOOooOo0 + timedelta ( days = 3 )
o0OIiII = float ( xbmc . getInfoLabel ( "System.BuildVersion" ) [ : 4 ] )
ii1iII1II = wiz . mediaCenter ( )
Iii1I1I11iiI1 = uservar . EXCLUDES
I1I1i1I = uservar . BUILDFILE
ii1I = uservar . APKFILE
O0oO0 = uservar . YOUTUBETITLE
oO0O0OO0O = uservar . YOUTUBEFILE
OO = uservar . ADDONFILE
OoOoO = uservar . ADVANCEDFILE
Ii1I1i = uservar . UPDATECHECK if str ( uservar . UPDATECHECK ) . isdigit ( ) else 1
OOI1iI1ii1II = ooO0oOOooOo0 + timedelta ( days = Ii1I1i )
O0O0OOOOoo = uservar . NOTIFICATION
oOooO0 = uservar . ENABLE
Ii1I1Ii = uservar . HEADERMESSAGE
OOoO0 = uservar . AUTOUPDATE
OO0Oooo0oOO0O = uservar . WIZARDFILE
o00O0 = uservar . HIDECONTACT
oOO0O00Oo0O0o = uservar . CONTACT
ii1 = uservar . CONTACTICON if not uservar . CONTACTICON == 'http://' else iiiiiIIii
I1iIIiiIIi1i = uservar . CONTACTFANART if not uservar . CONTACTFANART == 'http://' else OOO00
O0O0ooOOO = uservar . HIDESPACERS
oOOo0O00o = uservar . COLOR1
iIiIi11 = uservar . COLOR2
OOOiiiiI = uservar . THEME1
oooOo0OOOoo0 = uservar . THEME2
OOoO = uservar . THEME3
OO0O000 = uservar . THEME4
iiIiI1i1 = uservar . THEME5
oO0O00oOOoooO = uservar . ICONBUILDS if not uservar . ICONBUILDS == 'http://' else iiiiiIIii
IiIi11iI = uservar . ICONMAINT if not uservar . ICONMAINT == 'http://' else iiiiiIIii
Oo0O00O000 = uservar . ICONAPK if not uservar . ICONAPK == 'http://' else iiiiiIIii
i11I1IiII1i1i = uservar . ICONADDONS if not uservar . ICONADDONS == 'http://' else iiiiiIIii
oo = uservar . ICONYOUTUBE if not uservar . ICONYOUTUBE == 'http://' else iiiiiIIii
I1111i = uservar . ICONSAVE if not uservar . ICONSAVE == 'http://' else iiiiiIIii
iIIii = uservar . ICONTRAKT if not uservar . ICONTRAKT == 'http://' else iiiiiIIii
o00O0O = uservar . ICONREAL if not uservar . ICONREAL == 'http://' else iiiiiIIii
ii1iii1i = uservar . ICONLOGIN if not uservar . ICONLOGIN == 'http://' else iiiiiIIii
Iii1I1111ii = uservar . ICONCONTACT if not uservar . ICONCONTACT == 'http://' else iiiiiIIii
ooOoO00 = uservar . ICONSETTINGS if not uservar . ICONSETTINGS == 'http://' else iiiiiIIii
Ii1IIiI1i = uservar . ICONSPINZ if not uservar . ICONSPINZ == 'http://' else iiiiiIIii
o0O00Oo0 = uservar . ICONKODI if not uservar . ICONKODI == 'http://' else iiiiiIIii
IiII111i1i11 = uservar . ICONSPMC if not uservar . ICONSPMC == 'http://' else iiiiiIIii
i111iIi1i1II1 = uservar . ICONGAMES if not uservar . ICONGAMES == 'http://' else iiiiiIIii
oooO = uservar . ICONMOVIES if not uservar . ICONMOVIES == 'http://' else iiiiiIIii
i1I1i111Ii = uservar . ICONANDROID if not uservar . ICONANDROID == 'http://' else iiiiiIIii
ooo = uservar . ICONSPEED if not uservar . ICONSPEED == 'http://' else iiiiiIIii
i1i1iI1iiiI = uservar . ICONPRO if not uservar . ICONPRO == 'http://' else iiiiiIIii
i11I1IiII1i1i = os . path . join ( O000OO0 , 'projectxwizardicon.png' )
oo = os . path . join ( O000OO0 , 'projectxwizardicon.png' )
ii1iii1i = os . path . join ( O000OO0 , 'projectxwizardicon.png' )
Ooo0oOooo0 = wiz . LOGFILES
oOOOoo00 = traktit . TRAKTID
iiIiIIIiiI = debridit . DEBRIDID
iiI1IIIi = loginit . LOGINID
II11IiIi11 = 'http://tribeca.tvaddons.ag/tools/maintenance/modules/'
IIOOO0O00O0OOOO = 'http://mirrors.kodi.tv/addons/jarvis/'
I1iiii1I = [ 'Always Ask' , 'Reload Profile' , 'Force Close' ]
OOo0 = [ 'metadata.album.universal' , 'metadata.artists.universal' , 'metadata.common.fanart.tv' , 'metadata.common.imdb.com' , 'metadata.common.musicbrainz.org' , 'metadata.themoviedb.org' , 'metadata.tvdb.com' , 'service.xbmc.versioncheck' ]
if 73 - 73: iiIIi1IiIi11
if 42 - 42: i11iIiiIii * iIii1I11I1II1 / oO0 . i11iIiiIii % i11IiIiiIIIII
if 41 - 41: i1Ii / O0
if 51 - 51: i11IiIiiIIIII % ooOo
OooOo = 'http://projectxwizard.16mb.com/projectxwizard4/submenus/projectxwizardapk.txt'
i11III1111iIi = 'http://projectxwizard.16mb.com/projectxwizard4/submenus/xxxapks.txt'
I1i111I = 'http://projectxwizard.16mb.com/projectxwizard4/submenus/emulator.txt'
Ooo = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNBLUIudHh0" )
Oo0oo0O0o00O = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNDLUUudHh0" )
I1i11 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNGLUgudHh0" )
IiIi1I1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNJLUsudHh0" )
IiIIi1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNMLU0udHh0" )
IIIIiii1IIii = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNOLU8udHh0" )
II1i11I = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNQLVIudHh0" )
ii1I1IIii11 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNTLnR4dA==" )
O0o0oO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNULVYudHh0" )
IIIIiIiIi1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1NORVNXLVoudHh0" )
I11iiiiI1i = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU0EtQi50eHQ=" )
iI1i11 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU0MudHh0" )
OoOOoooOO0O = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU0QtRS50eHQ=" )
ooo00Ooo = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU0YtRy50eHQ=" )
Oo0o0O00 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU0gtSy50eHQ=" )
ii1I1i11 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU0wtTS50eHQ=" )
OOo0O0oo0OO0O = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU04tUS50eHQ=" )
OO0 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU1ItUy50eHQ=" )
o0Oooo = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU1QtVi50eHQ=" )
iiI = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05FU1ctWi50eHQ=" )
oO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0dFTkEtQi50eHQ=" )
IIiIi = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0dFTkMtRC50eHQ=" )
OOoOooOoOOOoo = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0dFTkUtRy50eHQ=" )
Iiii1iI1i = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0dFTkgtTC50eHQ=" )
I1ii1ii11i1I = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0dFTk0tTy50eHQ=" )
o0OoOO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0dFTlAtUi50eHQ=" )
O0O0Oo00 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0dFTlMtVC50eHQ=" )
oOoO00o = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0dFTlUtWi50eHQ=" )
oO00O0 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0FUUkEtQi50eHQ=" )
IIi1IIIi = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0FUUkMtRC50eHQ=" )
O00Ooo = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0FUUkUtRy50eHQ=" )
OOOO0OOO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0FUUkgtTC50eHQ=" )
i1i1ii = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0FUUk0tTy50eHQ=" )
iII1ii1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0FUUlAtUi50eHQ=" )
I1i1iiiI1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0FUUlMtVS50eHQ=" )
iIIi = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL0FUUlYtWi50eHQ=" )
oO0o00oo0 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL042NEEtQi50eHQ=" )
ii1IIII = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL042NEMtRS50eHQ=" )
oO00oOooooo0 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL042NEYtSi50eHQ=" )
oOo = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL042NEstTS50eHQ=" )
O0OOooOoO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL042NE4tUi50eHQ=" )
i1II1I1Iii1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL042NFMtVC50eHQ=" )
iiI11Iii = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL042NFYtWi50eHQ=" )
O0o0O0 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1RHQS1CLnR4dA==" )
Ii1II1I11i1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1RHQy1FLnR4dA==" )
oOoooooOoO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1RHRi1JLnR4dA==" )
Ii111 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1RHSi1NLnR4dA==" )
I111i1i1111 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1RHTi1RLnR4dA==" )
IIII1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1RHUi1VLnR4dA==" )
I1I1i = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1RHVi1aLnR4dA==" )
I1IIIiIiIi = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU0EudHh0" )
IIIII1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU0IudHh0" )
iIi1Ii1i1iI = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU0MudHh0" )
IIiI1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU0QudHh0" )
i1iI1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU0UtRi50eHQ=" )
ii1I1IiiI1ii1i = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU0ctSC50eHQ=" )
O0o = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU0ktSi50eHQ=" )
oO0OoO00o = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU0stTC50eHQ=" )
II1iiiiII = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU00udHh0" )
O0OoOO0oo0 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU04tTy50eHQ=" )
oOO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU1AtUS50eHQ=" )
O0o0OO0000ooo = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU1IudHh0" )
iIIII1iIIii = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU1MudHh0" )
oOOO00o000o = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU1QtVS50eHQ=" )
iIi11i1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL05EU1YtWi50eHQ=" )
oO00oo0o00o0o = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTQS50eHQ=" )
IiIIIIIi = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTQi50eHQ=" )
IiIi1iIIi1 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTQy1ELnR4dA==" )
O0OoO0ooOO0o = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTRS1GLnR4dA==" )
OoOo0oOooOoOO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTRy1KLnR4dA==" )
oo00ooOoO00 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTSy1OLnR4dA==" )
o00oOoOo0 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTTy1SLnR4dA==" )
o0O0O0ooo0oOO = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTUy1ULnR4dA==" )
oo000 = base64 . b64decode ( "aHR0cDovL3Byb2plY3R4d2l6YXJkLjE2bWIuY29tL3Byb2plY3R4d2l6YXJkNC9zdWJtZW51cy9ST01TVFhUL1BTVS1aLnR4dA==" )
if 32 - 32: i1IIi . IiiIII111ii
if 59 - 59: OoooooooOO
if 47 - 47: OOoooooO - ooOo / II111iiii
if 12 - 12: iii11iiII
if 83 - 83: iiIIi1IiIi11 . O0 / Ooo0O / iii11iiII - II111iiii
if 100 - 100: I1111
if 46 - 46: o0o0Oo0oooo0 / iIii1I11I1II1 % iiIIi1IiIi11 . iIii1I11I1II1 * iiIIi1IiIi11
if 38 - 38: oO0 - iiIIi1IiIi11 / O0 . OO00O0O0O00Oo
def i1iiIiI1Ii1i ( ) :
 if OOoO0 == 'Yes' :
  if wiz . workingURL ( OO0Oooo0oOO0O ) == True :
   i1iIi = wiz . checkWizard ( 'version' )
   if i1iIi > O0oo0OO0 : iiiii1II ( '%s [v%s] [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( o0OOO , O0oo0OO0 , i1iIi ) , 'wizardupdate' , themeit = oooOo0OOOoo0 )
   else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
  else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
 else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
 if len ( O000oo0O ) > 0 :
  O0OOO0OOooo00 = wiz . checkBuild ( O000oo0O , 'version' )
  I111iIi1 = '%s (v%s)' % ( O000oo0O , oo0OooOOo0 )
  if O0OOO0OOooo00 > oo0OooOOo0 : I111iIi1 = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( I111iIi1 , O0OOO0OOooo00 )
  oo00O00oO000o ( I111iIi1 , 'viewbuild' , O000oo0O , themeit = OO0O000 )
  OOo00OoO = wiz . themeCount ( O000oo0O )
  if not OOo00OoO == False :
   iiiii1II ( 'None' if o0O == "" else o0O , 'theme' , O000oo0O , themeit = iiIiI1i1 )
 else : oo00O00oO000o ( 'None' , 'builds' , themeit = OO0O000 )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 oo00O00oO000o ( 'Builds' , 'builds' , icon = oO0O00oOOoooO , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Maintenance' , 'maint' , icon = IiIi11iI , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Android Zone' , 'apk1' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 iiiii1II ( 'Speed Test' , 'speed' , icon = ooo , themeit = OOOiiiiI )
 if not OO == 'http://' : oo00O00oO000o ( 'Addon Installer' , 'addons' , icon = i11I1IiII1i1i , themeit = OOOiiiiI )
 if not oO0O0OO0O == 'http://' and not O0oO0 == '' : oo00O00oO000o ( O0oO0 , 'youtube' , icon = oo , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Save Data' , 'savedata' , icon = I1111i , themeit = OOOiiiiI )
 if o00O0 == 'No' : iiiii1II ( 'Contact' , 'contact' , icon = Iii1I1111ii , themeit = OOOiiiiI )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Settings' , 'settings' , icon = ooOoO00 , themeit = OOOiiiiI )
 if iii == 'true' : oo00O00oO000o ( 'Developer Menu' , 'developer' , icon = ooOoO00 , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 21 - 21: i11IiIiiIIIII
def OoO00 ( ) :
 if OOoO0 == 'Yes' :
  if wiz . workingURL ( OO0Oooo0oOO0O ) == True :
   i1iIi = wiz . checkWizard ( 'version' )
   if i1iIi > O0oo0OO0 : iiiii1II ( '%s [v%s] [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( o0OOO , O0oo0OO0 , i1iIi ) , 'wizardupdate' , themeit = oooOo0OOOoo0 )
   else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
  else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
 else : iiiii1II ( '%s [v%s]' % ( o0OOO , O0oo0OO0 ) , '' , themeit = oooOo0OOOoo0 )
 if len ( O000oo0O ) > 0 :
  O0OOO0OOooo00 = wiz . checkBuild ( O000oo0O , 'version' )
  I111iIi1 = '%s (v%s)' % ( O000oo0O , oo0OooOOo0 )
  if O0OOO0OOooo00 > oo0OooOOo0 : I111iIi1 = '%s [COLOR red][B][UPDATE v%s][/B][/COLOR]' % ( I111iIi1 , O0OOO0OOooo00 )
  oo00O00oO000o ( I111iIi1 , 'viewbuild' , O000oo0O , themeit = OO0O000 )
  OOo00OoO = wiz . themeCount ( O000oo0O )
  if not OOo00OoO == False :
   iiiii1II ( 'None' if o0O == "" else o0O , 'theme' , O000oo0O , themeit = iiIiI1i1 )
 else : oo00O00oO000o ( 'None' , 'builds' , themeit = OO0O000 )
 OO0Ooooo000Oo = wiz . workingURL ( I1I1i1I )
 if not OO0Ooooo000Oo == True :
  iiiii1II ( '%s Version: %s' % ( ii1iII1II , o0OIiII ) , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  iiiii1II ( 'Url for txt file not valid' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  iiiii1II ( '%s' % OO0Ooooo000Oo , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 else :
  O0oOoo0o000O0 , o00oO0o0o , oo0O0Ooooooo , I1IIIiI1I1ii1 , iiiI1I1iIIIi1 , Iii , I1iiiiI1iI = wiz . buildCount ( )
  iIiiiii1i = False ; iiIi1IIiI = [ ]
  if oOooOOOoOo == 'true' :
   if not i1Iii1i1I == '' and not OOoO00 == '' : iIiiiii1i = True ; iiIi1IIiI . append ( '1' )
   if not IiI111111IIII == '' and not i1Iiii111iI1iIi1 == '' : iIiiiii1i = True ; iiIi1IIiI . append ( '2' )
   if not OOO == '' and not oo0OOo0 == '' : iIiiiii1i = True ; iiIi1IIiI . append ( '3' )
  i1oO0OO0 = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' ) . replace ( 'adult=""' , 'adult="no"' )
  o0O0Oo00 = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)".+?ounter="(.+?)"' ) . findall ( i1oO0OO0 )
  if O0oOoo0o000O0 == 1 and iIiiiii1i == False :
   for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in o0O0Oo00 :
    if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
    if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
    oOOo000oOoO0 ( o0O0Oo00 [ 0 ] [ 0 ] )
    return
  iiiii1II ( '%s Version: %s' % ( ii1iII1II , o0OIiII ) , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  if iIiiiii1i == True :
   for OoOo00o0OO in iiIi1IIiI :
    O0Oo0o000oO = eval ( 'THIRD%sNAME' % OoOo00o0OO )
    oo00O00oO000o ( "[B]%s[/B]" % O0Oo0o000oO , 'viewthirdparty' , OoOo00o0OO , icon = oO0O00oOOoooO , themeit = OOoO )
  if len ( o0O0Oo00 ) >= 1 :
   if oo00O00oO == 'true' :
    for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in o0O0Oo00 :
     if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
     if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
     ii1IIIIiI11 = iI1IIIii ( 'install' , '' , O0Oo0o000oO )
     I1i11ii11 = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( IiI11i1IIiiI ) ) + "[/COLOR]"
     oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 , I1i11ii11 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = ii1IIIIiI11 , themeit = oooOo0OOOoo0 )
   else :
    if iiiI1I1iIIIi1 > 0 :
     OO00O0oOO = '+' if OOOO0OOoO0O0 == 'false' else '-'
     iiiii1II ( '[B]%s Leia Builds(%s)[/B]' % ( OO00O0oOO , iiiI1I1iIIIi1 ) , 'togglesetting' , 'show17' , themeit = OOoO )
     if OOOO0OOoO0O0 == 'true' :
      for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in o0O0Oo00 :
       if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
       Ii1iI111 = int ( float ( oOOOO ) )
       if Ii1iI111 == 18 :
        ii1IIIIiI11 = iI1IIIii ( 'install' , '' , O0Oo0o000oO )
        I1i11ii11 = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( IiI11i1IIiiI ) ) + "[/COLOR]"
        oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 , I1i11ii11 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = ii1IIIIiI11 , themeit = oooOo0OOOoo0 )
    if I1IIIiI1I1ii1 > 0 :
     OO00O0oOO = '+' if o00OO00OoO == 'false' else '-'
     iiiii1II ( '[B]%s Krypton Builds(%s)[/B]' % ( OO00O0oOO , I1IIIiI1I1ii1 ) , 'togglesetting' , 'show17' , themeit = OOoO )
     if o00OO00OoO == 'true' :
      for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in o0O0Oo00 :
       if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
       Ii1iI111 = int ( float ( oOOOO ) )
       if Ii1iI111 == 17 :
        ii1IIIIiI11 = iI1IIIii ( 'install' , '' , O0Oo0o000oO )
        I1i11ii11 = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( IiI11i1IIiiI ) ) + "[/COLOR]"
        oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 , I1i11ii11 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = ii1IIIIiI11 , themeit = oooOo0OOOoo0 )
    if oo0O0Ooooooo > 0 :
     OO00O0oOO = '+' if oOOoo0Oo == 'false' else '-'
     iiiii1II ( '[B]%s Jarvis Builds(%s)[/B]' % ( OO00O0oOO , oo0O0Ooooooo ) , 'togglesetting' , 'show16' , themeit = OOoO )
     if oOOoo0Oo == 'true' :
      for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in o0O0Oo00 :
       if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
       Ii1iI111 = int ( float ( oOOOO ) )
       if Ii1iI111 == 16 :
        ii1IIIIiI11 = iI1IIIii ( 'install' , '' , O0Oo0o000oO )
        I1i11ii11 = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( IiI11i1IIiiI ) ) + "[/COLOR]"
        oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 , I1i11ii11 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = ii1IIIIiI11 , themeit = oooOo0OOOoo0 )
    if o00oO0o0o > 0 :
     OO00O0oOO = '+' if oO0Oo == 'false' else '-'
     iiiii1II ( '[B]%s Isengard and Below Builds(%s)[/B]' % ( OO00O0oOO , o00oO0o0o ) , 'togglesetting' , 'show15' , themeit = OOoO )
     if oO0Oo == 'true' :
      for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o , IiI11i1IIiiI in o0O0Oo00 :
       if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
       if not iii == 'true' and wiz . strTest ( O0Oo0o000oO ) : continue
       Ii1iI111 = int ( float ( oOOOO ) )
       if Ii1iI111 <= 15 :
        ii1IIIIiI11 = iI1IIIii ( 'install' , '' , O0Oo0o000oO )
        I1i11ii11 = " | [COLOR powderblue] Downloads:[/COLOR][COLOR white] Total:[/COLOR] [COLOR yellow]" + str ( wiz . count_total ( IiI11i1IIiiI ) ) + "[/COLOR]"
        oo00O00oO000o ( '[%s] %s (v%s) %s' % ( float ( oOOOO ) , O0Oo0o000oO , O0OOO0OOooo00 , I1i11ii11 ) , 'viewbuild' , O0Oo0o000oO , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , menu = ii1IIIIiI11 , themeit = oooOo0OOOoo0 )
  elif I1iiiiI1iI > 0 :
   if Iii > 0 :
    iiiii1II ( 'There is currently only Adult builds' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
    iiiii1II ( 'Enable Show Adults in Addon Settings > Misc' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
   else :
    iiiii1II ( 'Currently No Builds Offered from %s' % o0OOO , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  else : iiiii1II ( 'Text file for builds not formated correctly.' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 51 - 51: i1Ii * O0 / II111iiii . IiiIII111ii % iii11iiII / ooOo
def oOOo000oOoO0 ( name , counter ) :
 OO0Ooooo000Oo = wiz . workingURL ( I1I1i1I )
 if not OO0Ooooo000Oo == True :
  iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
  iiiii1II ( '%s' % OO0Ooooo000Oo , '' , themeit = OOoO )
  return
 if wiz . checkBuild ( name , 'version' ) == False :
  iiiii1II ( 'Error reading the txt file.' , '' , themeit = OOoO )
  iiiii1II ( '%s was not found in the builds list.' % name , '' , themeit = OOoO )
  return
 i1oO0OO0 = wiz . openURL ( I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'gui=""' , 'gui="http://"' ) . replace ( 'theme=""' , 'theme="http://"' )
 o0O0Oo00 = re . compile ( 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?review="(.+?)".+?dult="(.+?)".+?escription="(.+?)".+?ounter="(.+?)"' % name ) . findall ( i1oO0OO0 )
 for O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , OOo00OoO , Ii1ii111i1 , i1i1i1I , ii1iii1I1I , oOoo000 , OooOo00o , counter in o0O0Oo00 :
  Ii1ii111i1 = Ii1ii111i1 if wiz . workingURL ( Ii1ii111i1 ) else iiiiiIIii
  i1i1i1I = i1i1i1I if wiz . workingURL ( i1i1i1I ) else OOO00
  I111iIi1 = '%s (v%s)' % ( name , O0OOO0OOooo00 )
  if O000oo0O == name and O0OOO0OOooo00 > oo0OooOOo0 :
   I111iIi1 = '%s [COLOR red][CURRENT v%s][/COLOR]' % ( I111iIi1 , oo0OooOOo0 )
  iiiii1II ( I111iIi1 , '' , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OO0O000 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  oo00O00oO000o ( 'Save Data Menu' , 'savedata' , icon = I1111i , themeit = OOoO )
  iiiii1II ( 'Build Information' , 'buildinfo' , name , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
  if not ii1iii1I1I == "http://" : iiiii1II ( 'View Video Preview' , 'buildpreview' , name , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
  oO0Ooo0ooOO0 = int ( float ( o0OIiII ) ) ; i1IIiIii1i = int ( float ( oOOOO ) )
  if not oO0Ooo0ooOO0 == i1IIiIii1i :
   if oO0Ooo0ooOO0 == 16 and i1IIiIii1i <= 15 : ooOOO0OooOo = False
   else : ooOOO0OooOo = True
  else : ooOOO0OooOo = False
  if ooOOO0OooOo == True :
   iiiii1II ( '[I]Build designed for kodi version %s(installed: %s)[/I]' % ( str ( oOOOO ) , str ( o0OIiII ) ) , '' , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
  iiiii1II ( wiz . sep ( 'INSTALL' ) , '' , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
  iiiii1II ( 'Fresh Install' , 'install' , name , 'fresh' , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOOiiiiI )
  iiiii1II ( 'Standard Install' , 'install' , name , 'normal' , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOOiiiiI )
  if not OOOoO000 == 'http://' : iiiii1II ( 'Apply guiFix' , 'install' , name , 'gui' , description = OooOo00o , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOOiiiiI )
  if not OOo00OoO == 'http://' :
   if wiz . workingURL ( OOo00OoO ) == True :
    iiiii1II ( wiz . sep ( 'THEMES' ) , '' , fanart = i1i1i1I , icon = Ii1ii111i1 , themeit = OOoO )
    i1oO0OO0 = wiz . openURL ( OOo00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
    o0O0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)".+?ounter"(.+?)"' ) . findall ( i1oO0OO0 )
    for I1Ii , oOOIi1II , O0Oo00 , ii1IiIIi1i , oOOo0OOOOo0Oo , OooOo00o , counter in o0O0Oo00 :
     if not O0Oo000ooO00 == 'true' and oOOo0OOOOo0Oo . lower ( ) == 'yes' : continue
     O0Oo00 = O0Oo00 if O0Oo00 == 'http://' else Ii1ii111i1
     ii1IiIIi1i = ii1IiIIi1i if ii1IiIIi1i == 'http://' else i1i1i1I
     iiiii1II ( I1Ii if not I1Ii == o0O else "[B]%s (Installed)[/B]" % I1Ii , 'theme' , name , I1Ii , description = OooOo00o , fanart = ii1IiIIi1i , icon = O0Oo00 , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 67 - 67: IIIi1i1I / iiIIi1IiIi11 . i11IiIiiIIIII . iIii1I11I1II1
def iiiI ( number ) :
 O0Oo0o000oO = eval ( 'THIRD%sNAME' % number )
 oO0o00oOOooO0 = eval ( 'THIRD%sURL' % number )
 IiIi1 = wiz . workingURL ( oO0o00oOOooO0 )
 if not IiIi1 == True :
  iiiii1II ( 'Url for txt file not valid' , '' , icon = oO0O00oOOoooO , themeit = OOoO )
  iiiii1II ( '%s' % WORKINGURL , '' , icon = oO0O00oOOoooO , themeit = OOoO )
 else :
  type , i111iiI1ii = wiz . thirdParty ( oO0o00oOOooO0 )
  iiiii1II ( "[B]%s[/B]" % O0Oo0o000oO , '' , themeit = OOoO )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  if type :
   for O0Oo0o000oO , O0OOO0OOooo00 , oO0o00oOOooO0 , oOOOO , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in i111iiI1ii :
    if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
    iiiii1II ( "[%s] %s v%s" % ( oOOOO , O0Oo0o000oO , O0OOO0OOooo00 ) , 'installthird' , O0Oo0o000oO , oO0o00oOOooO0 , icon = Ii1ii111i1 , fanart = i1i1i1I , description = OooOo00o , themeit = oooOo0OOOoo0 )
  else :
   for O0Oo0o000oO , oO0o00oOOooO0 , Ii1ii111i1 , i1i1i1I , OooOo00o in i111iiI1ii :
    iiiii1II ( O0Oo0o000oO , 'installthird' , O0Oo0o000oO , oO0o00oOOooO0 , icon = Ii1ii111i1 , fanart = i1i1i1I , description = OooOo00o , themeit = oooOo0OOOoo0 )
    if 24 - 24: o0o0Oo0oooo0 / OoooooooOO . II111iiii . ooOo % O0 % IiiIII111ii
def IiIII1i1i ( number ) :
 O0Oo0o000oO = eval ( 'THIRD%sNAME' % number )
 oO0o00oOOooO0 = eval ( 'THIRD%sURL' % number )
 II11I = wiz . getKeyboard ( O0Oo0o000oO , 'Enter the Name of the Wizard' )
 oo0oOO00oO = wiz . getKeyboard ( oO0o00oOOooO0 , 'Enter the URL of the Wizard Text' )
 if 36 - 36: iii11iiII
 wiz . setS ( 'wizard%sname' % number , II11I )
 wiz . setS ( 'wizard%surl' % number , oo0oOO00oO )
 if 84 - 84: OO00O0O0O00Oo . I1111 . II111iiii . i11IiIiiIIIII / IiiIII111ii % oO0
def OOO0oOoO0O ( name = "" ) :
 if name == 'kodi' :
  OoOo000oOo0oo = 'http://mirrors.kodi.tv/releases/android/arm/'
  oO0O = 'http://mirrors.kodi.tv/releases/android/arm/old/'
  oOOiiiIIiIi = wiz . openURL ( OoOo000oOo0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  oo0oOO00oO = wiz . openURL ( oO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OooOOO = 0
  Ii1iI11iI1 = re . compile ( '<tr><td><a href="(.+?)".+?>(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( oOOiiiIIiIi )
  i11I1II = re . compile ( '<tr><td><a href="(.+?)".+?>(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>' ) . findall ( oo0oOO00oO )
  if 79 - 79: I1111 . iiIIi1IiIi11 * IiiIII111ii - iii11iiII + OOoooooO
  iiiii1II ( "Official Kodi Apk\'s" , themeit = OOOiiiiI )
  ii11II1i = False
  for oO0o00oOOooO0 , name , OOOO000o0 , oO0o000OoOoO0 in Ii1iI11iI1 :
   if oO0o00oOOooO0 in [ '../' , 'old/' ] : continue
   if not oO0o00oOOooO0 . endswith ( '.apk' ) : continue
   if not oO0o00oOOooO0 . find ( '_' ) == - 1 and ii11II1i == True : continue
   try :
    OO0ooOOO0O00o = name . split ( '-' )
    if not oO0o00oOOooO0 . find ( '_' ) == - 1 :
     ii11II1i = True
     II11I , Ooo0o0oo = OO0ooOOO0O00o [ 2 ] . split ( '_' )
    else :
     II11I = OO0ooOOO0O00o [ 2 ]
     Ooo0o0oo = ''
    Ii1i1i1111 = "[COLOR %s]%s v%s%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , OO0ooOOO0O00o [ 0 ] . title ( ) , OO0ooOOO0O00o [ 1 ] , Ooo0o0oo . upper ( ) , II11I , iIiIi11 , OOOO000o0 . replace ( ' ' , '' ) , oOOo0O00o , oO0o000OoOoO0 )
    o0oO0O00oOo = urljoin ( OoOo000oOo0oo , oO0o00oOOooO0 )
    iiiii1II ( Ii1i1i1111 , 'apkinstall' , "%s v%s%s %s" % ( OO0ooOOO0O00o [ 0 ] . title ( ) , OO0ooOOO0O00o [ 1 ] , Ooo0o0oo . upper ( ) , II11I ) , o0oO0O00oOo )
    OooOOO += 1
   except :
    wiz . log ( "Error on: %s" % name )
    if 26 - 26: i1Ii % OO00O0O0O00Oo % IIIi1i1I % IiiIII111ii
  for oO0o00oOOooO0 , name , OOOO000o0 , oO0o000OoOoO0 in i11I1II :
   if oO0o00oOOooO0 in [ '../' , 'old/' ] : continue
   if not oO0o00oOOooO0 . endswith ( '.apk' ) : continue
   if not oO0o00oOOooO0 . find ( '_' ) == - 1 : continue
   try :
    OO0ooOOO0O00o = name . split ( '-' )
    Ii1i1i1111 = "[COLOR %s]%s v%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , OO0ooOOO0O00o [ 0 ] . title ( ) , OO0ooOOO0O00o [ 1 ] , OO0ooOOO0O00o [ 2 ] , iIiIi11 , OOOO000o0 . replace ( ' ' , '' ) , oOOo0O00o , oO0o000OoOoO0 )
    o0oO0O00oOo = urljoin ( oO0O , oO0o00oOOooO0 )
    iiiii1II ( Ii1i1i1111 , 'apkinstall' , "%s v%s %s" % ( OO0ooOOO0O00o [ 0 ] . title ( ) , OO0ooOOO0O00o [ 1 ] , OO0ooOOO0O00o [ 2 ] ) , o0oO0O00oOo )
    OooOOO += 1
   except :
    wiz . log ( "Error on: %s" % name )
  if OooOOO == 0 : iiiii1II ( "Error Kodi Scraper Is Currently Down." )
 elif name == 'spmc' :
  O0oo0ooOOOO = 'https://github.com/koying/SPMC/releases'
  oOOiiiIIiIi = wiz . openURL ( O0oo0ooOOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OooOOO = 0
  Ii1iI11iI1 = re . compile ( '<div.+?lass="release-body.+?div class="release-header".+?a href=.+?>(.+?)</a>.+?ul class="release-downloads">(.+?)</ul>.+?/div>' ) . findall ( oOOiiiIIiIi )
  if 14 - 14: ooOo / OoooooooOO % ooOo . O0
  iiiii1II ( "Official SPMC Apk\'s" , themeit = OOOiiiiI )
  if 94 - 94: o0o0Oo0oooo0 - Ooo0O - ooOo % i1IIi
  for name , iIIiiiiI in Ii1iI11iI1 :
   I111i1I1 = ''
   i11I1II = re . compile ( '<li>.+?<a href="(.+?)" rel="nofollow">.+?<small class="text-gray float-right">(.+?)</small>.+?strong>(.+?)</strong>.+?</a>.+?</li>' ) . findall ( iIIiiiiI )
   for O0o00OOo00O0O , II1i , OoOOoO000O00oO in i11I1II :
    if OoOOoO000O00oO . find ( 'armeabi' ) == - 1 : continue
    if OoOOoO000O00oO . find ( 'launcher' ) > - 1 : continue
    I111i1I1 = urljoin ( 'https://github.com' , O0o00OOo00O0O )
    break
   if I111i1I1 == '' : continue
   try :
    name = "SPMC %s" % name
    Ii1i1i1111 = "[COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name , iIiIi11 , II1i . replace ( ' ' , '' ) )
    o0oO0O00oOo = I111i1I1
    iiiii1II ( Ii1i1i1111 , 'apkinstall' , name , o0oO0O00oOo )
    OooOOO += 1
   except Exception , i1OoOO :
    wiz . log ( "Error on: %s / %s" % ( name , str ( i1OoOO ) ) )
  if OooOOO == 0 : iiiii1II ( "Error SPMC Scraper Is Currently Down." )
  if 44 - 44: iii11iiII
def O0O0o0o0o ( ) :
 oo00O00oO000o ( 'EMULATORS AND ROMS' , 'emurom' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PROJECT X WIZARD APKS' , 'apkshow' , url = OooOo , icon = Ii1IIiI1i , themeit = OOOiiiiI )
  #oo00O00oO000o ( '[COLOR cyan]apk drawer[/COLOR]' , 'intellaunch' , )
 oo00O00oO000o ( 'KODI OFFICIAL APK\'s' , 'apkscrape' , 'kodi' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SPMC OFFICIAL APK\'s' , 'apkscrape' , 'spmc' , icon = Oo0O00O000 , themeit = OOOiiiiI )
 IIIIIiI = Oo0000O0OOooO ( base64 . b64decode ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 o0O0Oo00 = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( IIIIIiI )
 i11I1II = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( IIIIIiI )
 for oO0o00oOOooO0 , O00OO in o0O0Oo00 :
  Oo0 ( '[COLOR cyan]ANDROID APPS[/COLOR]' + O00OO , 'https://www.apkfiles.com' + oO0o00oOOooO0 , 'apkgame' , i1I1i111Ii )
 for oO0o00oOOooO0 , O00OO in i11I1II :
  Oo0 ( '[COLOR cyan]ANDROID GAMES[/COLOR]' + O00OO , 'https://www.apkfiles.com' + oO0o00oOOooO0 , 'apkgame' , i111iIi1i1II1 )
 iIi1 ( 'movies' , 'MAIN' )
 #oo00O00oO000o ( 'Apk Picks' , 'apkshow' , url = ii1I , icon = Oo0O00O000 , themeit = OOOiiiiI )
 if O0Oo000ooO00 == 'true' : oo00O00oO000o ( 'XXX Apk' , 'apkshow' , url = i11III1111iIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 20 - 20: i1Ii % i1Ii
def OOooo0O ( url ) :
 i1oO0OO0 = Oo0000O0OOooO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o0O0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"' ) . findall ( i1oO0OO0 )
 if len ( o0O0Oo00 ) > 0 :
  for O0Oo0o000oO , url , Ii1ii111i1 , i1i1i1I in o0O0Oo00 :
   iiiii1II ( O0Oo0o000oO , 'apkinstall' , O0Oo0o000oO , url , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOOiiiiI )
  else : wiz . log ( "[APK Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[APK Menu] ERROR: URL for emu list not working." )
 if 34 - 34: iii11iiII
def IiIIiIIIiIii ( url ) :
 IIIIIiI = Oo0000O0OOooO ( url )
 o0O0Oo00 = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( IIIIIiI )
 for url , O0Oo0o000oO in o0O0Oo00 :
  if '/cat' in url :
   Oo0 ( ( O0Oo0o000oO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 'select' , O000OO0 + 'APK.png' )
   if 23 - 23: iiIIi1IiIi11 + i11IiIiiIIIII . o0o0Oo0oooo0 * ooOo + oO0
def I1iIi1iiiIiI ( url ) :
 IIIIIiI = Oo0000O0OOooO ( url )
 oOOiiiIIiIi = url
 if "page=" in str ( url ) :
  oOOiiiIIiIi = url . split ( '?' ) [ 0 ]
 o0O0Oo00 = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( IIIIIiI )
 i11I1II = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( IIIIIiI )
 for url , III1I1Ii11iI , O0Oo0o000oO in o0O0Oo00 :
  if 'apk' in url :
   Oo0 ( ( O0Oo0o000oO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 'grab' , 'http:' + III1I1Ii11iI )
 if len ( i11I1II ) > 1 :
  i11I1II = str ( i11I1II [ len ( i11I1II ) - 1 ] )
 Oo0 ( 'Next Page' , oOOiiiIIiIi + str ( i11I1II ) , 'select' , O000OO0 + 'Next.png' )
 if 52 - 52: iii11iiII - iiIIi1IiIi11 * IIIi1i1I
def Ii1I11I ( name , url ) :
 IIIIIiI = Oo0000O0OOooO ( url )
 name = name
 o0O0Oo00 = re . compile ( 'href="([^"]*)".+?lass="yellow_button".+?itle=' ) . findall ( IIIIIiI )
 for url in o0O0Oo00 :
  url = 'https://www.apkfiles.com' + url
  iiIii1I ( name , url , 'Brackets' )
  if 47 - 47: OOoooooO . i11IiIiiIIIII / I1I1i1
  if 83 - 83: I1I1i1 / iii11iiII / iii11iiII + I1I1i1 * OO00O0O0O00Oo + I1I1i1
  if 36 - 36: o0o0Oo0oooo0 + I1I1i1 - OoooooooOO . IIIi1i1I . OoooooooOO / Ooo0O
  if 72 - 72: i1IIi
def OOoo0oo ( ) :
 xbmc . executebuiltin ( 'Runscript("special://home/addons/script.module.projectx.wizard/ookla.py")' )
 if 58 - 58: IIIi1i1I
 if 4 - 4: II111iiii . OOoooooO / oO0 - i11iIiiIii
 if 72 - 72: O0 / OOoooooO + OoooooooOO * iiIIi1IiIi11
 if 61 - 61: OoooooooOO % II111iiii - ooOo % oO0 + i1IIi
def i1II ( ) :
 if 15 - 15: o0o0Oo0oooo0
 if os . path . isfile ( i1i1II ) :
  oOoOoO000OO = True
  ii11II11 = open ( i1i1II )
  oOooOo00OooO0oO = ii11II11 . read ( )
  ii11II11 . close ( )
 else :
  xbmcgui . Dialog ( ) . ok ( "[COLOR orange]PROJECT X WIZARD[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "[COLOR ghostwhite]First Time Launching Will Take a Couple Minutes[/COLOR]" , "[COLOR ghostwhite]Please Be Patient![/COLOR]" )
  oOoOoO000OO = False
  if 16 - 16: i1Ii / Ooo0O + iii11iiII / IiiIII111ii
  if 42 - 42: Ooo0O + II111iiii - ooOo / i11IiIiiIIIII % i1Ii
  if 66 - 66: iii11iiII + i1IIi . ooOo + iii11iiII - i11IiIiiIIIII
  if 17 - 17: O0 . OO00O0O0O00Oo . O0 + O0 / Ooo0O . OOoooooO
  if 62 - 62: oO0 % iiIIi1IiIi11 * I1111 - i1IIi
  if 66 - 66: i11iIiiIii / I1I1i1 - OoooooooOO / i1IIi . i11iIiiIii
  if 16 - 16: Ooo0O % oO0 + i11IiIiiIIIII - O0 . iiIIi1IiIi11 / OO00O0O0O00Oo
  if 35 - 35: IIIi1i1I / OO00O0O0O00Oo / II111iiii - iIii1I11I1II1 + II111iiii . OO00O0O0O00Oo
  if 81 - 81: iiIIi1IiIi11 * iii11iiII - oO0 * IiiIII111ii % o0o0Oo0oooo0 * o0o0Oo0oooo0
  if 59 - 59: iIii1I11I1II1
  if 7 - 7: iii11iiII * ooOo / I1I1i1 * i11iIiiIii
 o00II1i111 = ""
 i1iiiIii11 = OOoOOO000O0 ( )
 for oOo0 in i1iiiIii11 :
  if oOoOoO000OO == True :
   if oOo0 not in oOooOo00OooO0oO :
    if 48 - 48: Ooo0O - OoooooooOO % iii11iiII * o0o0Oo0oooo0
    if 69 - 69: i1IIi
    ooOoOOOOo = ooooOooooOOo ( o00II1i111 , oOo0 )
    o00II1i111 = ooOoOOOOo
    if 96 - 96: iiIIi1IiIi11
  else :
   ooOoOOOOo = ooooOooooOOo ( o00II1i111 , oOo0 )
   o00II1i111 = ooOoOOOOo
   if 18 - 18: iiIIi1IiIi11 * i11IiIiiIIIII - IiiIII111ii
 if oOoOoO000OO == True :
  ii11II11 = open ( i1i1II , 'a' )
  if 31 - 31: Ooo0O - O0 % o0o0Oo0oooo0 % IIIi1i1I
  if 45 - 45: oO0 + II111iiii * i11iIiiIii
 else :
  ii11II11 = open ( i1i1II , 'w' )
  if 13 - 13: OoooooooOO * IIIi1i1I - IiiIII111ii / iii11iiII + i11IiIiiIIIII + i1Ii
  if 39 - 39: iIii1I11I1II1 - OoooooooOO
 ii11II11 . write ( o00II1i111 )
 ii11II11 . close ( )
 if 81 - 81: oO0 - O0 * OoooooooOO
 if 23 - 23: II111iiii / IIIi1i1I
 ii11II11 = open ( i1i1II )
 oOooOo00OooO0oO = ii11II11 . read ( )
 ii11II11 . close ( )
 oOooOo00OooO0oO = oOooOo00OooO0oO . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?nstallRating="(.+?)"' ) . findall ( oOooOo00OooO0oO )
 if 28 - 28: Ooo0O * OOoooooO - I1111
 if 19 - 19: i11IiIiiIIIII
 for O0Oo0o000oO , oO0o00oOOooO0 , Ooooo0OoO0 , i1i1i1I , OooOo00o , iI1 in sorted ( o0O0Oo00 , key = lambda o0O0Oo00 : o0O0Oo00 [ 0 ] ) :
  if oO0o00oOOooO0 in i1iiiIii11 :
   iIi1i ( '[COLOR ghostwhite]' + str ( O0Oo0o000oO ) + '[/COLOR]' , oO0o00oOOooO0 , 'intelselect' , Ooooo0OoO0 , i1i1i1I , OooOo00o , iI1 )
   if 67 - 67: o0o0Oo0oooo0 / I1I1i1 * I1111 / iii11iiII * oO0 / IIIi1i1I
def OOoOOO000O0 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  try :
   i1iiiIii11 = subprocess . Popen ( [ 'exec ' '/system/bin/pm list packages -3' '' ] , executable = '/system/bin/sh' , shell = True , stdout = subprocess . PIPE , stderr = subprocess . STDOUT ) . communicate ( ) [ 0 ] . rstrip ( '\n' ) . splitlines ( )
  except :
   i1iiiIii11 = [ ]
   if 64 - 64: IIIi1i1I - ooOo / iiIIi1IiIi11 - I1111
  for oOo0 in range ( len ( i1iiiIii11 ) ) :
   i1iiiIii11 [ oOo0 ] = i1iiiIii11 [ oOo0 ] . partition ( ':' ) [ 2 ]
   if 37 - 37: i11iIiiIii / iiIIi1IiIi11
 return i1iiiIii11
 if 85 - 85: i11iIiiIii + OO00O0O0O00Oo * o0o0Oo0oooo0
def ooooOooooOOo ( theList , i ) :
 global theNotList
 iiiII = "https://play.google.com/store/apps/details?id=" + i
 i1oO0OO0 = o0Oii1111i ( iiiII )
 if 75 - 75: i1Ii + II111iiii / IIIi1i1I - IIIi1i1I / OoooooooOO
 if i1oO0OO0 != False :
  i1oO0OO0 = i1oO0OO0 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 2 - 2: I1I1i1
  i11ii = r'<div class="id-app-title".tabindex=".">(.+?)</div>'
  o0O0Oo00 = re . search ( i11ii , i1oO0OO0 )
  if o0O0Oo00 != None : O0Oo0o000oO = o0O0Oo00 . group ( 1 )
  else : O0Oo0o000oO = i
  if 50 - 50: IiiIII111ii / o0o0Oo0oooo0 * IiiIII111ii
  if 34 - 34: O0 * O0 % OoooooooOO + iiIIi1IiIi11 * iIii1I11I1II1 % IiiIII111ii
  if 25 - 25: i11IiIiiIIIII + o0o0Oo0oooo0 . I1I1i1 % o0o0Oo0oooo0 * iii11iiII
  if 32 - 32: i11iIiiIii - OO00O0O0O00Oo
  if 53 - 53: OoooooooOO - i1Ii
  Ooooo0OoO0 = "androidapp://sources/apps/" + str ( i ) + ".png"
  if 87 - 87: IIIi1i1I . ooOo
  if 17 - 17: IiiIII111ii . i11iIiiIii
  if 5 - 5: oO0 + O0 + O0 . OO00O0O0O00Oo - OOoooooO
  if 63 - 63: IIIi1i1I
  if 71 - 71: i1IIi . IiiIII111ii * iiIIi1IiIi11 % OoooooooOO + iii11iiII
  if 36 - 36: i1Ii
  i1iiI = r'data-expand-to="full-screenshot-[0-9]{1,2}" src="(//\w+?.\w+?.\S+?=h900)"'
  o0O0Oo00 = re . compile ( i1iiI ) . findall ( i1oO0OO0 )
  if len ( o0O0Oo00 ) != 0 : i1i1i1I = "https:" + o0O0Oo00 [ len ( o0O0Oo00 ) - 1 ]
  else : i1i1i1I = "None"
  if 74 - 74: OO00O0O0O00Oo % oO0
  iiIiIi1 = r'data-video-url="https://www.youtube.com/embed/(\S.+?)\?ps=play.+?"'
  o0O0Oo00 = re . search ( iiIiIi1 , i1oO0OO0 )
  if o0O0Oo00 != None : OooOo00o = o0O0Oo00 . group ( 1 )
  else : OooOo00o = "None"
  if 78 - 78: iii11iiII % I1I1i1
  IIIiIiI = r'<div class="content" itemprop="numDownloads">\s+?(\d.+?\s-\s\d.+?)\s+?</div>'
  o0O0Oo00 = re . search ( IIIiIiI , i1oO0OO0 )
  if o0O0Oo00 != None : I1i = 'Installed ' + o0O0Oo00 . group ( 1 )
  else : I1i = "Installs: N/A"
  if 49 - 49: oO0
  O0oOOo0o = r'<div class="score" aria-label=" Rated .+? stars out of five stars ">(.+?)</div>'
  o0O0Oo00 = re . search ( O0oOOo0o , i1oO0OO0 )
  if o0O0Oo00 != None : I1 = o0O0Oo00 . group ( 1 ) + " Stars"
  else : I1 = "Rating: N/A"
  iI1 = I1 + " " + I1i
  if 7 - 7: I1111 * i11IiIiiIIIII + II111iiii % i11iIiiIii
  if 8 - 8: OOoooooO * O0
  if 73 - 73: I1I1i1 / IIIi1i1I / i11IiIiiIIIII / I1111
  oO0o00oOOooO0 = i
  theList += 'name="' + O0Oo0o000oO + '"url="' + oO0o00oOOooO0 + '"img="' + Ooooo0OoO0 + '"fanart="' + i1i1i1I + '"description="' + OooOo00o + '"installRating="' + iI1 + '"'
  return theList
  if 11 - 11: o0o0Oo0oooo0 + i1Ii - OoooooooOO / I1111
  if 34 - 34: OOoooooO
  if 45 - 45: OOoooooO / Ooo0O / IiiIII111ii
  if 44 - 44: oO0 - IiiIII111ii / II111iiii * I1111 * Ooo0O
  if 73 - 73: I1I1i1 - ooOo * i1IIi / i11iIiiIii * iii11iiII % II111iiii
  if 56 - 56: OoooooooOO * Ooo0O . Ooo0O . oO0
  if 24 - 24: Ooo0O . i11IiIiiIIIII * IiiIII111ii % iiIIi1IiIi11 / iii11iiII
  if 58 - 58: ooOo - oO0 % O0 . ooOo % I1111 % i1Ii
  if 87 - 87: IIIi1i1I - i11iIiiIii
 else :
  if 78 - 78: i11iIiiIii / iIii1I11I1II1 - I1I1i1
  return theList
  if 23 - 23: i11IiIiiIIIII
def iIiiIiiIi ( name , url , iconimage , fanart , videolink ) :
 i1iiIIIi = 0
 if 62 - 62: O0 / ooOo % O0 * I1111 % ooOo
 if videolink != "None" :
  i1iiIIIi += 1
  if 33 - 33: ooOo . IIIi1i1I * I1111 * iIii1I11I1II1
 if i1iiIIIi == 1 : II11 = xbmcgui . Dialog ( ) . select ( '[COLOR cyan]' + name + '[/COLOR]' , [ '[COLOR cyan]Launch[/COLOR]' , '[COLOR ghostwhite]Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if i1iiIIIi == 0 : II11 = xbmcgui . Dialog ( ) . select ( '[COLOR cyan]' + name + '[/COLOR]' , [ '[COLOR cyan]Launch[/COLOR]' , '[COLOR ghostwhite]No Preview Video[/COLOR]' , '[COLOR tomato]Uninstall[/COLOR]' ] )
 if 12 - 12: OO00O0O0O00Oo
 if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + I1I1i1 / I1I1i1 / II111iiii
 if 49 - 49: iii11iiII . oO0 . i11iIiiIii - II111iiii / IiiIII111ii
 if II11 == 1 :
  if videolink != 'None' :
   yt . PlayVideo ( videolink )
 if II11 == 0 :
  ooOo0O0o0 = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]PROJECT X WIZARD[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Launch:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if ooOo0O0o0 == 1 :
   xbmc . executebuiltin ( 'StartAndroidActivity(%s)' % url )
 if II11 == 2 :
  o0oo0O = xbmcgui . Dialog ( ) . yesno ( "[COLOR orange]PROJECT X WIZARD[/COLOR]" , "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]" , "" , "[COLOR ghostwhite]Would You Like To Remove:[/COLOR] [COLOR cyan]" + name + "[/COLOR]" , "[COLOR red]No Way[/COLOR]" , "[COLOR cyan]Heck Ya![/COLOR]" )
  if o0oo0O :
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.DELETE","","package:' + url + '")' )
   xbmc . sleep ( 2000 )
   try : shutil . rmtree ( "/sdcard/Android/data/" + url , ignore_errors = True , onerror = None )
   except : pass
   try : shutil . rmtree ( "/sdcard/Android/obb/" + url , ignore_errors = True , onerror = None )
   except : pass
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 19 - 19: OO00O0O0O00Oo + i1IIi . ooOo - Ooo0O
def o0Oii1111i ( url ) :
 try :
  iIi1I1 = urllib2 . Request ( url )
  iIi1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  O0oOoo0OoO0O = urllib2 . urlopen ( iIi1I1 )
  i1oO0OO0 = O0oOoo0OoO0O . read ( )
  O0oOoo0OoO0O . close ( )
  return i1oO0OO0
 except :
  return False
  if 63 - 63: OoooooooOO / OOoooooO
  if 91 - 91: i1IIi - iIii1I11I1II1
  if 55 - 55: ooOo * I1I1i1 % OOoooooO . iIii1I11I1II1 * OO00O0O0O00Oo
def o0oo0000 ( ) :
 oo00O00oO000o ( 'EMULATORS' , 'apkshow' , url = I1i111I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'ROMS' , 'roms' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 42 - 42: OO00O0O0O00Oo + OO00O0O0O00Oo * II111iiii
 if 78 - 78: OoooooooOO
 if 77 - 77: oO0 / i1IIi / Ooo0O % iii11iiII
 if 48 - 48: i11IiIiiIIIII - i1Ii + iIii1I11I1II1 + OoooooooOO
def IiI1i111IiIiIi1 ( ) :
 oo00O00oO000o ( 'NES' , 'nes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES' , 'snes' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo 64' , 'n64' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS' , 'nds' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis' , 'gen' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation' , 'ps' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari' , 'atr' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine & Turbo Grafx' , 'tbg' , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 39 - 39: i11IiIiiIIIII - oO0
def OOO0o0OO0OO ( url ) :
 i1oO0OO0 = Oo0000O0OOooO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o0O0Oo00 = re . compile ( '.+?ame="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)"description="(.+?)"' ) . findall ( i1oO0OO0 )
 if len ( o0O0Oo00 ) > 0 :
  for O0Oo0o000oO , url , Ii1ii111i1 , i1i1i1I , OooOo00o in o0O0Oo00 :
   oOo0O ( O0Oo0o000oO , 'rominstall' , O0Oo0o000oO , url , icon = Ii1ii111i1 , fanart = i1i1i1I , description = OooOo00o , themeit = OOOiiiiI )
  else : wiz . log ( "[ROM Menu] ERROR: Invalid Format." )
 else : wiz . log ( "[ROM Menu] ERROR: URL for apk list not working." )
 if 43 - 43: I1I1i1 . iiIIi1IiIi11 . i11IiIiiIIIII + iIii1I11I1II1
 if 78 - 78: iIii1I11I1II1 % o0o0Oo0oooo0 + oO0 / i1IIi % II111iiii + iii11iiII
 if 91 - 91: iIii1I11I1II1 % I1111 . I1I1i1 + IiiIII111ii + I1I1i1
 if 95 - 95: IiiIII111ii + oO0 * iii11iiII
def I1IiooooOoO0O ( ) :
 oo00O00oO000o ( 'SNES Titles A Thru B' , 'rom' , url = Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles C Thru E' , 'rom' , url = Oo0oo0O0o00O , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles F Thru H' , 'rom' , url = I1i11 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles I Thru K' , 'rom' , url = IiIi1I1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles L Thru M' , 'rom' , url = IiIIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles N Thru O' , 'rom' , url = IIIIiii1IIii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles P Thru R' , 'rom' , url = II1i11I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles S' , 'rom' , url = ii1I1IIii11 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles T Thru V' , 'rom' , url = O0o0oO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'SNES Titles W Thru Z' , 'rom' , url = IIIIiIiIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 1 - 1: oO0 / I1111 + IIIi1i1I . I1I1i1 / oO0 - iiIIi1IiIi11
 if 5 - 5: iii11iiII
 if 4 - 4: iiIIi1IiIi11 % OO00O0O0O00Oo / I1111 . iii11iiII / iii11iiII - oO0
 if 79 - 79: oO0 + OO00O0O0O00Oo
def iIiIIi ( ) :
 oo00O00oO000o ( 'NES Titles A Thru B' , 'rom' , url = I11iiiiI1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles C' , 'rom' , url = iI1i11 , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles D Thru E' , 'rom' , url = OoOOoooOO0O , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles F Thru G' , 'rom' , url = ooo00Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles H Thru K' , 'rom' , url = Oo0o0O00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles L Thru M' , 'rom' , url = ii1I1i11 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles N Thru Q' , 'rom' , url = OOo0O0oo0OO0O , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles R Thru S' , 'rom' , url = OO0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles T Thru V' , 'rom' , url = o0Oooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'NES Titles W Thru Z' , 'rom' , url = iiI , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 14 - 14: I1I1i1 / iii11iiII - iIii1I11I1II1 - IIIi1i1I % OOoooooO
 if 49 - 49: OOoooooO * IIIi1i1I / I1I1i1 / Ooo0O * iIii1I11I1II1
 if 57 - 57: o0o0Oo0oooo0 - IIIi1i1I / OOoooooO % i11iIiiIii
 if 3 - 3: iiIIi1IiIi11 . OOoooooO % ooOo + oO0
 if 64 - 64: i1IIi
def IIii1 ( ) :
 oo00O00oO000o ( 'Genesis Titles A Thru B' , 'rom' , url = oO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles C Thru D' , 'rom' , url = IIiIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles E Thru G' , 'rom' , url = OOoOooOoOOOoo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles H Thru L' , 'rom' , url = Iiii1iI1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles M Thru O' , 'rom' , url = I1ii1ii11i1I , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles P Thru R' , 'rom' , url = o0OoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles S Thru T' , 'rom' , url = O0O0Oo00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Genesis Titles U Thru Z' , 'rom' , url = oOoO00o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 35 - 35: i11iIiiIii - ooOo / iii11iiII + IiiIII111ii * IIIi1i1I
 if 49 - 49: I1I1i1 * IiiIII111ii + i11IiIiiIIIII + iiIIi1IiIi11
 if 30 - 30: I1I1i1 / iii11iiII / i1Ii % OOoooooO + II111iiii
 if 4 - 4: iiIIi1IiIi11 - Ooo0O - i1Ii - i11IiIiiIIIII % i11iIiiIii / I1111
 if 50 - 50: OOoooooO + i1IIi
def i11IiIIi11I ( ) :
 oo00O00oO000o ( 'Atari Titles A Thru B' , 'rom' , url = oO00O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles C Thru D' , 'rom' , url = IIi1IIIi , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles E Thru G' , 'rom' , url = O00Ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles H Thru L' , 'rom' , url = OOOO0OOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles M Thru O' , 'rom' , url = i1i1ii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles P Thru R' , 'rom' , url = iII1ii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles S Thru U' , 'rom' , url = I1i1iiiI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Atari Titles V Thru Z' , 'rom' , url = iIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 78 - 78: i1Ii
 if 83 - 83: iIii1I11I1II1 % o0o0Oo0oooo0 % I1I1i1 % OO00O0O0O00Oo . oO0 % O0
 if 47 - 47: I1I1i1
 if 66 - 66: ooOo - i1Ii
 if 33 - 33: ooOo / I1111
def iiIIi ( ) :
 oo00O00oO000o ( 'N64 Titles A Thru B' , 'rom' , url = oO0o00oo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles C Thru E' , 'rom' , url = ii1IIII , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles F Thru J' , 'rom' , url = oO00oOooooo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles K Thru M' , 'rom' , url = oOo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles N Thru R' , 'rom' , url = O0OOooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles S Thru T' , 'rom' , url = i1II1I1Iii1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'N64 Titles V Thru Z' , 'rom' , url = iiI11Iii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 36 - 36: i11IiIiiIIIII . II111iiii
 if 25 - 25: IIIi1i1I
 if 34 - 34: o0o0Oo0oooo0 . iIii1I11I1II1 % O0
 if 43 - 43: oO0 - iiIIi1IiIi11
 if 70 - 70: iiIIi1IiIi11 / iii11iiII % OOoooooO - IiiIII111ii
def i1II11Iii1I ( ) :
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles A Thru B' , 'rom' , url = O0o0O0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles C Thru E' , 'rom' , url = Ii1II1I11i1 , icon = Oo0O00O000 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles F Thru I' , 'rom' , url = oOoooooOoO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles J Thru M' , 'rom' , url = Ii111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles N Thru Q' , 'rom' , url = I111i1i1111 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles R Thru U' , 'rom' , url = IIII1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'PC Engine And Turbo Grafx Titles V Thru Z' , 'rom' , url = I1I1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 92 - 92: iii11iiII % i1Ii % o0o0Oo0oooo0
 if 4 - 4: o0o0Oo0oooo0 + IiiIII111ii / IIIi1i1I
 if 13 - 13: iiIIi1IiIi11
 if 80 - 80: IiiIII111ii - I1I1i1
 if 41 - 41: I1I1i1 - Ooo0O * ooOo
def OO0OoOo0OOO ( ) :
 oo00O00oO000o ( 'Nintendo DS Titles A' , 'rom' , url = I1IIIiIiIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles B' , 'rom' , url = IIIII1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles C' , 'rom' , url = iIi1Ii1i1iI , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles D' , 'rom' , url = IIiI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles E Thru F' , 'rom' , url = i1iI1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles G Thru H' , 'rom' , url = ii1I1IiiI1ii1i , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles I Thru J' , 'rom' , url = O0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles K Thru L' , 'rom' , url = oO0OoO00o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles M' , 'rom' , url = II1iiiiII , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles N Thru O' , 'rom' , url = O0OoOO0oo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles P Thru Q' , 'rom' , url = oOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles R' , 'rom' , url = O0o0OO0000ooo , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles S' , 'rom' , url = iIIII1iIIii , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles T Thru U' , 'rom' , url = oOOO00o000o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Nintendo DS Titles V Thru Z' , 'rom' , url = iIi11i1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 47 - 47: OoooooooOO % O0 * iiIIi1IiIi11 . IiiIII111ii
 if 38 - 38: O0 - i1Ii % OO00O0O0O00Oo
 if 64 - 64: iIii1I11I1II1
 if 15 - 15: oO0 + iii11iiII / oO0 / OO00O0O0O00Oo
def I1Iii1I ( ) :
 oo00O00oO000o ( 'Playstation Titles A' , 'rom' , url = oO00oo0o00o0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles B' , 'rom' , url = IiIIIIIi , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles C Thru D' , 'rom' , url = IiIi1iIIi1 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles E Thru F' , 'rom' , url = O0OoO0ooOO0o , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles G Thru J' , 'rom' , url = OoOo0oOooOoOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles K Thru N' , 'rom' , url = oo00ooOoO00 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles O Thru R' , 'rom' , url = o00oOoOo0 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles S Thru T' , 'rom' , url = o0O0O0ooo0oOO , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Playstation Titles U Thru Z' , 'rom' , url = oo000 , icon = i111iIi1i1II1 , themeit = OOOiiiiI )
 if 13 - 13: I1I1i1 + O0
def O00o0O ( url = None ) :
 if not OO == 'http://' :
  if url == None :
   iIIIiI = wiz . workingURL ( OO )
   O00 = uservar . ADDONFILE
  else :
   iIIIiI = wiz . workingURL ( url )
   O00 = url
  if iIIIiI == True :
   i1oO0OO0 = wiz . openURL ( O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   o0O0Oo00 = re . compile ( 'name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( i1oO0OO0 )
   if len ( o0O0Oo00 ) > 0 :
    OooOOO = 0
    for O0Oo0o000oO , i1iiIII1IIiIIII , url , I1iIIII1 , OO0I11Ii1iI11iI1 , i1III1 , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
     if i1iiIII1IIiIIII . lower ( ) == 'section' :
      OooOOO += 1
      oo00O00oO000o ( "[B]%s[/B]" % O0Oo0o000oO , 'addons' , url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
     else :
      if not O0Oo000ooO00 == 'true' and oOoo000 . lower ( ) == 'yes' : continue
      try :
       Iii111IiIii = xbmcaddon . Addon ( id = i1iiIII1IIiIIII ) . getAddonInfo ( 'path' )
       if os . path . exists ( Iii111IiIii ) :
        O0Oo0o000oO = "[COLOR white][Installed][/COLOR] %s" % O0Oo0o000oO
      except :
       pass
      OooOOO += 1
      iiiii1II ( O0Oo0o000oO , 'addoninstall' , i1iiIII1IIiIIII , O00 , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = oooOo0OOOoo0 )
     if OooOOO < 1 :
      iiiii1II ( "No addons added to this menu yet!" , '' , themeit = oooOo0OOOoo0 )
   else :
    iiiii1II ( 'Text File not formated correctly!' , '' , themeit = OOoO )
    wiz . log ( "[Addon Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[Addon Menu] ERROR: URL for Addon list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % iIIIiI , '' , themeit = OOoO )
 else : wiz . log ( "[Addon Menu] No Addon list added." )
 iIi1 ( 'files' , 'viewType' )
 if 100 - 100: II111iiii - I1I1i1 . II111iiii * II111iiii . i1Ii
def iIiI ( plugin , url ) :
 if not OO == 'http://' :
  iIIIiI = wiz . workingURL ( url )
  if iIIIiI == True :
   i1oO0OO0 = wiz . openURL ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( 'repository=""' , 'repository="none"' ) . replace ( 'repositoryurl=""' , 'repositoryurl="http://"' ) . replace ( 'repositoryxml=""' , 'repositoryxml="http://"' )
   o0O0Oo00 = re . compile ( 'name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin ) . findall ( i1oO0OO0 )
   if len ( o0O0Oo00 ) > 0 :
    for O0Oo0o000oO , url , I1iIIII1 , OO0I11Ii1iI11iI1 , i1III1 , Ii1ii111i1 , i1i1i1I , oOoo000 , OooOo00o in o0O0Oo00 :
     if os . path . exists ( os . path . join ( O0O , plugin ) ) :
      oO00Ooo0oO = [ 'Launch Addon' , 'Remove Addon' ]
      OOOo = iiIIIII1i1iI . select ( "[COLOR %s]Addon already installed what would you like to do?[/COLOR]" % iIiIi11 , oO00Ooo0oO )
      if OOOo == 0 :
       wiz . ebi ( 'RunAddon(%s)' % plugin )
       xbmc . sleep ( 500 )
       return True
      elif OOOo == 1 :
       wiz . cleanHouse ( os . path . join ( O0O , plugin ) )
       try : wiz . removeFolder ( os . path . join ( O0O , plugin ) )
       except : pass
       if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to remove the addon_data for:" % iIiIi11 , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , plugin ) , yeslabel = "[B][COLOR white]Yes Remove[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
        o0ooOo00O ( plugin )
       wiz . refresh ( )
       return True
      else :
       return False
     Ii1i1I1 = os . path . join ( O0O , I1iIIII1 )
     if not I1iIIII1 . lower ( ) == 'none' and not os . path . exists ( Ii1i1I1 ) :
      wiz . log ( "Repository not installed, installing it" )
      if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % ( iIiIi11 , oOOo0O00o , plugin ) , "[COLOR %s]%s[/COLOR]?[/COLOR]" % ( oOOo0O00o , I1iIIII1 ) , yeslabel = "[B][COLOR white]Yes Install[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) :
       i1iIi = wiz . parseDOM ( wiz . openURL ( OO0I11Ii1iI11iI1 ) , 'addon' , ret = 'version' , attrs = { 'id' : I1iIIII1 } )
       if len ( i1iIi ) > 0 :
        O0O00OooO = '%s%s-%s.zip' % ( i1III1 , I1iIIII1 , i1iIi [ 0 ] )
        wiz . log ( O0O00OooO )
        if o0OIiII >= 17 : wiz . addonDatabase ( I1iIIII1 , 1 )
        I1IiI1iI11 ( I1iIIII1 , O0O00OooO )
        wiz . ebi ( 'UpdateAddonRepos()' )
        if 2 - 2: iIii1I11I1II1
        wiz . log ( "Installing Addon from Kodi" )
        iiii1 = OO0o0oO0O000o ( plugin )
        wiz . log ( "Install from Kodi: %s" % iiii1 )
        if iiii1 :
         wiz . refresh ( )
         return True
       else :
        wiz . log ( "[Addon Installer] Repository not installed: Unable to grab url! (%s)" % I1iIIII1 )
      else : wiz . log ( "[Addon Installer] Repository for %s not installed: %s" % ( plugin , I1iIIII1 ) )
     elif I1iIIII1 . lower ( ) == 'none' :
      wiz . log ( "No repository, installing addon" )
      I1iI11iii = plugin
      oo0oO = url
      I1IiI1iI11 ( plugin , url )
      wiz . refresh ( )
      return True
     else :
      wiz . log ( "Repository installed, installing addon" )
      iiii1 = OO0o0oO0O000o ( plugin , False )
      if iiii1 :
       wiz . refresh ( )
       return True
     if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
     IiIi1iI11 = wiz . parseDOM ( wiz . openURL ( OO0I11Ii1iI11iI1 ) , 'addon' , ret = 'version' , attrs = { 'id' : plugin } )
     if len ( IiIi1iI11 ) > 0 :
      url = "%s%s-%s.zip" % ( url , plugin , IiIi1iI11 [ 0 ] )
      wiz . log ( str ( url ) )
      if o0OIiII >= 17 : wiz . addonDatabase ( plugin , 1 )
      I1IiI1iI11 ( plugin , url )
      wiz . refresh ( )
     else :
      wiz . log ( "no match" ) ; return False
   else : wiz . log ( "[Addon Installer] Invalid Format" )
  else : wiz . log ( "[Addon Installer] Text File: %s" % iIIIiI )
 else : wiz . log ( "[Addon Installer] Not Enabled." )
 if 11 - 11: oO0
def OO0o0oO0O000o ( plugin , over = True ) :
 if over == True :
  xbmc . sleep ( 2000 )
  if 26 - 26: iIii1I11I1II1 * OO00O0O0O00Oo - iii11iiII
 wiz . ebi ( 'RunPlugin(plugin://%s)' % plugin )
 if not wiz . whileWindow ( 'yesnodialog' ) :
  return False
 xbmc . sleep ( 500 )
 if wiz . whileWindow ( 'okdialog' ) :
  return False
 wiz . whileWindow ( 'progressdialog' )
 if os . path . exists ( os . path . join ( O0O , plugin ) ) : return True
 else : return False
 if 27 - 27: oO0 * OO00O0O0O00Oo - I1111 + IiiIII111ii * IiiIII111ii
def I1IiI1iI11 ( name , url ) :
 if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]Addon Installer[/COLOR]" % oOOo0O00o , '[COLOR %s]%s:[/COLOR] [COLOR %s]Invalid Zip Url![/COLOR]' % ( oOOo0O00o , name , iIiIi11 ) ) ; return
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 o0OO0O0OO0oO0 = url . split ( '/' )
 iIiiIi11IIi = os . path . join ( o0o0OOO0o0 , o0OO0O0OO0oO0 [ - 1 ] )
 try : os . remove ( iIiiIi11IIi )
 except : pass
 downloader . download ( url , iIiiIi11IIi , oo00 )
 Ii1i1i1111 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , Ii1i1i1111 , '' , '[COLOR %s]Please Wait[/COLOR]' % iIiIi11 )
 Oo0oO , II1ii1ii11I1 , o0ooOO0o = extract . all ( iIiiIi11IIi , O0O , oo00 , title = Ii1i1i1111 )
 oo00 . update ( 0 , Ii1i1i1111 , '' , '[COLOR %s]Installing Dependencies[/COLOR]' % iIiIi11 )
 ooo0 ( name )
 i1iI1i1I1 ( name , oo00 )
 oo00 . close ( )
 wiz . ebi ( 'UpdateAddonRepos()' )
 wiz . ebi ( 'UpdateLocalAddons()' )
 wiz . refresh ( )
 if 99 - 99: OOoooooO / iIii1I11I1II1 - IiiIII111ii * oO0 % ooOo
def i1iI1i1I1 ( name , DP = None ) :
 i1II1i = os . path . join ( O0O , name , 'addon.xml' )
 if os . path . exists ( i1II1i ) :
  I1iIiiiI1 = open ( i1II1i , mode = 'r' ) ; i1oO0OO0 = I1iIiiiI1 . read ( ) ; I1iIiiiI1 . close ( ) ;
  o0O0Oo00 = wiz . parseDOM ( i1oO0OO0 , 'import' , ret = 'addon' )
  for I1iIII1IiiI in o0O0Oo00 :
   if not 'xbmc.python' in I1iIII1IiiI :
    if not DP == None :
     DP . update ( 0 , '' , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , I1iIII1IiiI ) )
    wiz . createTemp ( I1iIII1IiiI )
    if 96 - 96: ooOo % i1IIi . I1I1i1 . O0
    if 37 - 37: i1IIi - iii11iiII % OoooooooOO / iii11iiII % OOoooooO
    if 48 - 48: i11iIiiIii % IIIi1i1I
    if 29 - 29: iiIIi1IiIi11 + i11iIiiIii % i11IiIiiIIIII
    if 93 - 93: o0o0Oo0oooo0 % iIii1I11I1II1
    if 90 - 90: ooOo - iii11iiII / IiiIII111ii / O0 / i11IiIiiIIIII
    if 87 - 87: o0o0Oo0oooo0 / i1Ii + iIii1I11I1II1
    if 93 - 93: iIii1I11I1II1 + IIIi1i1I % OOoooooO
    if 21 - 21: iii11iiII
    if 6 - 6: i1Ii
    if 46 - 46: i1Ii + IIIi1i1I
    if 79 - 79: OoooooooOO - i1Ii * i1Ii . o0o0Oo0oooo0
    if 100 - 100: II111iiii * i11IiIiiIIIII % ooOo / oO0
    if 90 - 90: oO0 . OOoooooO . o0o0Oo0oooo0 . IiiIII111ii
    if 4 - 4: IiiIII111ii + o0o0Oo0oooo0 % oO0 / i11iIiiIii
    if 74 - 74: II111iiii . O0 - ooOo + i1Ii % i11iIiiIii % o0o0Oo0oooo0
    if 78 - 78: IiiIII111ii + o0o0Oo0oooo0 + i1Ii - i1Ii . i11iIiiIii / I1111
    if 27 - 27: IiiIII111ii - O0 % i11IiIiiIIIII * OO00O0O0O00Oo . i1Ii % iIii1I11I1II1
    if 37 - 37: OoooooooOO + O0 - i1IIi % OOoooooO
    if 24 - 24: o0o0Oo0oooo0
    if 94 - 94: i1IIi * i1IIi % II111iiii + iii11iiII
    if 28 - 28: ooOo
    if 49 - 49: i11IiIiiIIIII . I1I1i1 % IIIi1i1I / IiiIII111ii
    if 95 - 95: O0 * o0o0Oo0oooo0 * i1Ii . OOoooooO / iIii1I11I1II1
    if 28 - 28: i1Ii + IIIi1i1I - OOoooooO / iIii1I11I1II1 - ooOo
    if 45 - 45: O0 / i1IIi * IIIi1i1I * I1111
def ooo0 ( addon ) :
 oO0o00oOOooO0 = os . path . join ( O0O , addon , 'addon.xml' )
 if os . path . exists ( oO0o00oOOooO0 ) :
  try :
   list = open ( oO0o00oOOooO0 , mode = 'r' ) ; II11IiiiI11iIIi1 = list . read ( ) ; list . close ( )
   O0Oo0o000oO = wiz . parseDOM ( II11IiiiI11iIIi1 , 'addon' , ret = 'name' , attrs = { 'id' : addon } )
   Ii1ii111i1 = os . path . join ( O0O , addon , 'icon.png' )
   wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , O0Oo0o000oO [ 0 ] ) , '[COLOR %s]Addon Enabled[/COLOR]' % iIiIi11 , '2000' , Ii1ii111i1 )
  except : pass
  if 72 - 72: iiIIi1IiIi11 * iii11iiII
def oooo ( url = None ) :
 if not oO0O0OO0O == 'http://' :
  if url == None :
   iiiIIIii = wiz . workingURL ( oO0O0OO0O )
   ooOoo00 = uservar . YOUTUBEFILE
  else :
   iiiIIIii = wiz . workingURL ( url )
   ooOoo00 = url
  if iiiIIIii == True :
   i1oO0OO0 = wiz . openURL ( ooOoo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o0O0Oo00 = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1oO0OO0 )
   if len ( o0O0Oo00 ) > 0 :
    for O0Oo0o000oO , Ii11IiI , url , Ii1ii111i1 , i1i1i1I , OooOo00o in o0O0Oo00 :
     if Ii11IiI . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % O0Oo0o000oO , 'youtube' , url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
     else :
      iiiii1II ( O0Oo0o000oO , 'viewVideo' , url = url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[YouTube Menu] ERROR: Invalid Format." )
  else :
   wiz . log ( "[YouTube Menu] ERROR: URL for YouTube list not working." )
   iiiii1II ( 'Url for txt file not valid' , '' , themeit = OOoO )
   iiiii1II ( '%s' % iiiIIIii , '' , themeit = OOoO )
 else : wiz . log ( "[YouTube Menu] No YouTube list added." )
 iIi1 ( 'files' , 'viewType' )
 if 91 - 91: i11IiIiiIIIII % iIii1I11I1II1 * oO0
def iIiiIIi1iiII ( view = None ) :
 oooO00Oo = '[B][COLOR white]ON[/COLOR][/B]' ; ooO00o = '[B][COLOR red]OFF[/COLOR][/B]'
 o0o00O0oOooO0 = 'true' if ooOooo000oOO == 'true' else 'false'
 o0oO0OO00ooOO = 'true' if Oo0oOOo == 'true' else 'false'
 IiIIiii11II1 = 'true' if Oo0OoO00oOO0o == 'true' else 'false'
 iiii1i1II1 = 'true' if OOO00O == 'true' else 'false'
 ooOO0ooo0o = 'true' if oO0Ii1iIiII1ii1 == 'true' else 'false'
 i1IiI1I = 'true' if O00O0oOO00O00 == 'true' else 'false'
 o0OOo00oO0oOO = 'true' if i1Oo00 == 'true' else 'false'
 iiiii1I1III1 = 'true' if oOooOOOoOo == 'true' else 'false'
 if wiz . Grab_Log ( True ) == False : i1oO00O = 0
 else : i1oO00O = oo0o0ooooo ( wiz . Grab_Log ( True ) , True , True )
 if wiz . Grab_Log ( True , True ) == False : O0o0O = 0
 else : O0o0O = oo0o0ooooo ( wiz . Grab_Log ( True , True ) , True , True )
 ii111 = int ( i1oO00O ) + int ( O0o0O )
 ooOo000OoO0o = str ( ii111 ) + ' Error(s) Found' if ii111 > 0 else 'None Found'
 ooooo0O0 = ': [COLOR red]Not Found[/COLOR]' if not os . path . exists ( I11iii1Ii ) else ": [COLOR white]%s[/COLOR]" % wiz . convertSize ( os . path . getsize ( I11iii1Ii ) )
 if o0OOo00oO0oOO == 'true' :
  i1III1iI = 'true'
  ii1i = 'true'
  i1IiiiiIi1I = 'true'
  ooo0O0o0OoOO = 'true'
  iIi11i = 'true'
  o0o00o0Oo = 'true'
  OOOOOo = 'true'
  oOOoo = 'true'
 else :
  i1III1iI = 'true' if i1i == 'true' else 'false'
  ii1i = 'true' if iiI111I1iIiI == 'true' else 'false'
  i1IiiiiIi1I = 'true' if IIIi1I1IIii1II == 'true' else 'false'
  ooo0O0o0OoOO = 'true' if O0ii1ii1ii == 'true' else 'false'
  iIi11i = 'true' if oooooOoo0ooo == 'true' else 'false'
  o0o00o0Oo = 'true' if I1I1IiI1 == 'true' else 'false'
  OOOOOo = 'true' if III1iII1I1ii == 'true' else 'false'
  oOOoo = 'true' if oOOo0 == 'true' else 'false'
 i1I1iIii11 = wiz . getSize ( o0o0OOO0o0 )
 oOoO0O0oO = wiz . getSize ( oOoOooOo0o0 )
 oOOoO = wiz . getCacheSize ( )
 oOo0Oo0O0O = i1I1iIii11 + oOoO0O0oO + oOOoO
 III1II1i = [ 'Always' , 'Daily' , '3 Days' , 'Weekly' ]
 oo00O00oO000o ( '[COLOR lime][B]CLEANING TOOLS[/B][/COLOR]' , 'maint' , 'clean' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "clean" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Total Clean Up: [COLOR white][B]%s[/B][/COLOR]' % wiz . convertSize ( oOo0Oo0O0O ) , 'fullclean' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Cache: [COLOR white][B]%s[/B][/COLOR]' % wiz . convertSize ( oOOoO ) , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Packages: [COLOR white][B]%s[/B][/COLOR]' % wiz . convertSize ( i1I1iIii11 ) , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Thumbnails: [COLOR white][B]%s[/B][/COLOR]' % wiz . convertSize ( oOoO0O0oO ) , 'clearthumb' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Old Thumbnails' , 'oldThumbs' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Crash Logs' , 'clearcrash' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Purge Databases' , 'purgedb' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Fresh Start' , 'freshstart' , icon = IiIi11iI , themeit = OOoO )
 oo00O00oO000o ( '[COLOR lime][B]ADDON TOOLS[/B][/COLOR]' , 'maint' , 'addon' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "addon" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Remove Addons' , 'removeaddons' , icon = IiIi11iI , themeit = OOoO )
  oo00O00oO000o ( 'Remove Addon Data' , 'removeaddondata' , icon = IiIi11iI , themeit = OOoO )
  oo00O00oO000o ( 'Enable/Disable Addons' , 'enableaddons' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Enable/Disable Adult Addons' , 'toggleadult' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Force Update Addons' , 'forceupdate' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Hide Passwords On Keyboard Entry' , 'hidepassword' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Unhide Passwords On Keyboard Entry' , 'unhidepassword' , icon = IiIi11iI , themeit = OOoO )
 oo00O00oO000o ( '[COLOR lime][B]MISC MAINTENANCE[/B][/COLOR]' , 'maint' , 'misc' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "misc" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Kodi 17 Fix' , 'kodi17fix' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Reload Skin' , 'forceskin' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Reload Profile' , 'forceprofile' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Force Close Kodi' , 'forceclose' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Upload Kodi.log' , 'uploadlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Errors in Log: %s' % ( ooOo000OoO0o ) , 'viewerrorlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Log File' , 'viewlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'View Wizard Log File' , 'viewwizlog' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Clear Wizard Log File%s' % ooooo0O0 , 'clearwizlog' , icon = IiIi11iI , themeit = OOoO )
 oo00O00oO000o ( '[COLOR lime][B]BACK UP/RESTORE[/B][/COLOR]' , 'maint' , 'backup' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "backup" or oO0Ii1iIiII1ii1 == 'true' :
  iiiii1II ( 'Clean Up Back Up Folder' , 'clearbackup' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Back Up Location: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , O0ooO0Oo00o ) , 'settings' , 'Maintenance' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Back Up]: Build' , 'backupbuild' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Back Up]: GuiFix' , 'backupgui' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Back Up]: Theme' , 'backuptheme' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Back Up]: Addon_data' , 'backupaddon' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: Local Build' , 'restorezip' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: Local GuiFix' , 'restoregui' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: Local Addon_data' , 'restoreaddon' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: External Build' , 'restoreextzip' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: External GuiFix' , 'restoreextgui' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '[Restore]: External Addon_data' , 'restoreextaddon' , icon = IiIi11iI , themeit = OOoO )
 oo00O00oO000o ( '[COLOR lime][B]SYSTEM TWEAKS/FIXES[/B][/COLOR]' , 'maint' , 'tweaks' , icon = IiIi11iI , themeit = OOOiiiiI )
 if view == "tweaks" or oO0Ii1iIiII1ii1 == 'true' :
  if not OoOoO == 'http://' and not OoOoO == '' :
   oo00O00oO000o ( '[COLOR lime][B]ADVANCED SETTINGS[/B][/COLOR]' , 'advancedsetting' , icon = IiIi11iI , themeit = OOoO )
  else :
   if os . path . exists ( I11II1i ) :
    iiiii1II ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = IiIi11iI , themeit = OOoO )
    iiiii1II ( 'Remove Currect AdvancedSettings.xml' , 'removeadvanced' , icon = IiIi11iI , themeit = OOoO )
   iiiii1II ( 'Quick Configure AdvancedSettings.xml' , 'autoadvanced' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Scan Sources for broken links' , 'checksources' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Scan For Broken Repositories' , 'checkrepos' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Fix Addons Not Updating' , 'fixaddonupdate' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Remove Non-Ascii filenames' , 'asciicheck' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Convert Paths to special' , 'convertpath' , icon = IiIi11iI , themeit = OOoO )
  oo00O00oO000o ( 'System Information' , 'systeminfo' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR lime][B]SHOW ALL MAINTENANCE:[/B][/COLOR] %s' % ooOO0ooo0o . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'showmaint' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 oo00O00oO000o ( '[COLOR white][B]<< RETURN TO MAIN MENU[/B][/COLOR]' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR lime][B]THIRD PARTY WIZARDS:[/B][/COLOR] %s' % iiiii1I1III1 . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'enable3rd' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 if iiiii1I1III1 == 'true' :
  iI1i1IiIIIIi = i1Iii1i1I if not i1Iii1i1I == '' else 'Not Set'
  OooOooO0O0o0 = IiI111111IIII if not IiI111111IIII == '' else 'Not Set'
  iIiiiii1i = OOO if not OOO == '' else 'Not Set'
  iiiii1II ( 'Edit Third Party Wizard 1: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , iI1i1IiIIIIi ) , 'editthird' , '1' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 2: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , OooOooO0O0o0 ) , 'editthird' , '2' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( 'Edit Third Party Wizard 3: [COLOR %s]%s[/COLOR]' % ( iIiIi11 , iIiiiii1i ) , 'editthird' , '3' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Auto Clean' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Auto Clean Up On Startup: %s' % o0o00O0oOooO0 . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'autoclean' , icon = IiIi11iI , themeit = OOoO )
 if o0o00O0oOooO0 == 'true' :
  iiiii1II ( '--- Auto Clean Fequency: [B][COLOR white]%s[/COLOR][/B]' % III1II1i [ OOoOO0oo0ooO ] , 'changefeq' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Cache on Startup: %s' % o0oO0OO00ooOO . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'clearcache' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Packages on Startup: %s' % IiIIiii11II1 . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'clearpackages' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Clear Old Thumbs on Startup: %s' % iiii1i1II1 . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'clearthumbs' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( 'Clear Video Cache' , '' , fanart = OOO00 , icon = IiIi11iI , themeit = OOOiiiiI )
 iiiii1II ( 'Include Video Cache in Clear Cache: %s' % i1IiI1I . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includevideo' , icon = IiIi11iI , themeit = OOoO )
 if i1IiI1I == 'true' :
  iiiii1II ( '--- Include All Video Addons: %s' % o0OOo00oO0oOO . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includeall' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Bob: %s' % i1III1iI . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includebob' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Phoenix: %s' % ii1i . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includephoenix' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Specto: %s' % i1IiiiiIi1I . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includespecto' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Exodus: %s' % iIi11i . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includeexodus' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts: %s' % OOOOOo . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includesalts' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Salts HD Lite: %s' % oOOoo . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includesaltslite' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include One Channel: %s' % o0o00o0Oo . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includeonechan' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Include Genesis: %s' % ooo0O0o0OoOO . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglecache' , 'includegenesis' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Enable All Video Addons' , 'togglecache' , 'true' , icon = IiIi11iI , themeit = OOoO )
  iiiii1II ( '--- Disable All Video Addons' , 'togglecache' , 'false' , icon = IiIi11iI , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 59 - 59: Ooo0O + iiIIi1IiIi11 - iii11iiII . I1I1i1 + ooOo % IIIi1i1I
def i111Iii ( url = None ) :
 if not OoOoO == 'http://' :
  if url == None :
   o0o0 = wiz . workingURL ( OoOoO )
   i1iIi1IIiIII1 = uservar . ADVANCEDFILE
  else :
   o0o0 = wiz . workingURL ( url )
   i1iIi1IIiIII1 = url
  iiiii1II ( 'Quick Configure AdvancedSettings.xml' , 'autoadvanced' , icon = IiIi11iI , themeit = OOoO )
  if os . path . exists ( I11II1i ) :
   iiiii1II ( 'View Currect AdvancedSettings.xml' , 'currentsettings' , icon = IiIi11iI , themeit = OOoO )
   iiiii1II ( 'Remove Currect AdvancedSettings.xml' , 'removeadvanced' , icon = IiIi11iI , themeit = OOoO )
  if o0o0 == True :
   if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = IiIi11iI , themeit = OOoO )
   i1oO0OO0 = wiz . openURL ( i1iIi1IIiIII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o0O0Oo00 = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1oO0OO0 )
   if len ( o0O0Oo00 ) > 0 :
    for O0Oo0o000oO , Ii11IiI , url , Ii1ii111i1 , i1i1i1I , OooOo00o in o0O0Oo00 :
     if Ii11IiI . lower ( ) == "yes" :
      oo00O00oO000o ( "[B]%s[/B]" % O0Oo0o000oO , 'advancedsetting' , url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
     else :
      iiiii1II ( O0Oo0o000oO , 'writeadvanced' , O0Oo0o000oO , url , description = OooOo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = oooOo0OOOoo0 )
   else : wiz . log ( "[Advanced Settings] ERROR: Invalid Format." )
  else : wiz . log ( "[Advanced Settings] URL not working: %s" % o0o0 )
 else : wiz . log ( "[Advanced Settings] not Enabled" )
 if 19 - 19: i11IiIiiIIIII
def O00O ( name , url ) :
 o0o0 = wiz . workingURL ( url )
 if o0o0 == True :
  if os . path . exists ( I11II1i ) : O0OOOOOoo = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to overwrite your current Advanced Settings with [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR white]Overwrite[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  else : O0OOOOOoo = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install [COLOR %s]%s[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , name ) , yeslabel = "[B][COLOR white]Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if 69 - 69: ooOo + iiIIi1IiIi11
  if O0OOOOOoo == 1 :
   file = wiz . openURL ( url )
   i1IiII = open ( I11II1i , 'w' ) ;
   i1IiII . write ( file )
   i1IiII . close ( )
   iiIIIII1i1iI . ok ( o0OOO , '[COLOR %s]AdvancedSettings.xml file has been successfully written.  Once you click okay it will force close kodi.[/COLOR]' % iIiIi11 )
   wiz . killxbmc ( True )
  else : wiz . log ( "[Advanced Settings] install canceled" ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Write Cancelled![/COLOR]" % iIiIi11 ) ; return
 else : wiz . log ( "[Advanced Settings] URL not working: %s" % o0o0 ) ; wiz . LogNotify ( '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , o0OOO ) , "[COLOR %s]URL Not Working[/COLOR]" % iIiIi11 )
 if 12 - 12: iiIIi1IiIi11 / o0o0Oo0oooo0
def ooooo0Oo0 ( ) :
 i1IiII = open ( I11II1i )
 o0I1IIIi11ii11 = i1IiII . read ( ) . replace ( '\t' , '    ' )
 wiz . TextBox ( o0OOO , o0I1IIIi11ii11 )
 i1IiII . close ( )
 if 53 - 53: OO00O0O0O00Oo * i1Ii / iIii1I11I1II1 / ooOo % oO0
def IIii ( ) :
 if os . path . exists ( I11II1i ) :
  wiz . removeFile ( I11II1i )
 else : LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]AdvancedSettings.xml not found[/COLOR]" )
 if 97 - 97: oO0 / Ooo0O + OO00O0O0O00Oo
def i111I11i1I ( ) :
 notify . autoConfig ( )
 if 85 - 85: iii11iiII * i1IIi % ooOo - OOoooooO
def I11I1ii1i ( ) :
 II11Ii111II1 = 'http://whatismyipaddress.com/'
 if not wiz . workingURL ( II11Ii111II1 ) : return 'Unknown' , 'Unknown' , 'Unknown'
 O00OOO00Ooo = wiz . openURL ( II11Ii111II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if not 'Access Denied' in O00OOO00Ooo :
  OoOOoooO000 = re . compile ( 'whatismyipaddress.com/ip/(.+?)"' ) . findall ( O00OOO00Ooo )
  OoO0o000oOo = OoOOoooO000 [ 0 ] if ( len ( OoOOoooO000 ) > 0 ) else 'Unknown'
  Oo00OO00o0oO = re . compile ( '"font-size:14px;">(.+?)</td>' ) . findall ( O00OOO00Ooo )
  iI1I1I1i1i = Oo00OO00o0oO [ 0 ] if ( len ( Oo00OO00o0oO ) > 0 ) else 'Unknown'
  OOo0O = Oo00OO00o0oO [ 1 ] + ', ' + Oo00OO00o0oO [ 2 ] + ', ' + Oo00OO00o0oO [ 3 ] if ( len ( Oo00OO00o0oO ) > 2 ) else 'Unknown'
  return OoO0o000oOo , iI1I1I1i1i , OOo0O
 else : return 'Unknown' , 'Unknown' , 'Unknown'
 if 100 - 100: I1111 % I1111
def iI1I1 ( ) :
 ii1O0ooooo000 = [ 'System.FriendlyName' ,
 'System.BuildVersion' ,
 'System.CpuUsage' ,
 'System.ScreenMode' ,
 'Network.IPAddress' ,
 'Network.MacAddress' ,
 'System.Uptime' ,
 'System.TotalUptime' ,
 'System.FreeSpace' ,
 'System.UsedSpace' ,
 'System.TotalSpace' ,
 'System.Memory(free)' ,
 'System.Memory(used)' ,
 'System.Memory(total)' ]
 OooOoOO0OO = [ ] ; OooOOO = 0
 for I1iiIiiii1111 in ii1O0ooooo000 :
  I1ii1i11i = wiz . getInfo ( I1iiIiiii1111 )
  Oooooo0O00o = 0
  while I1ii1i11i == "Busy" and Oooooo0O00o < 10 :
   I1ii1i11i = wiz . getInfo ( I1iiIiiii1111 ) ; Oooooo0O00o += 1 ; wiz . log ( "%s sleep %s" % ( I1iiIiiii1111 , str ( Oooooo0O00o ) ) ) ; xbmc . sleep ( 200 )
  OooOoOO0OO . append ( I1ii1i11i )
  OooOOO += 1
 II11ii1 = OooOoOO0OO [ 8 ] if 'Una' in OooOoOO0OO [ 8 ] else wiz . convertSize ( int ( float ( OooOoOO0OO [ 8 ] [ : - 8 ] ) ) * 1024 * 1024 )
 ii1II1II = OooOoOO0OO [ 9 ] if 'Una' in OooOoOO0OO [ 9 ] else wiz . convertSize ( int ( float ( OooOoOO0OO [ 9 ] [ : - 8 ] ) ) * 1024 * 1024 )
 i11i11II11i = OooOoOO0OO [ 10 ] if 'Una' in OooOoOO0OO [ 10 ] else wiz . convertSize ( int ( float ( OooOoOO0OO [ 10 ] [ : - 8 ] ) ) * 1024 * 1024 )
 II1Ii1I1i = wiz . convertSize ( int ( float ( OooOoOO0OO [ 11 ] [ : - 2 ] ) ) * 1024 * 1024 )
 OOooOooo0OOo0 = wiz . convertSize ( int ( float ( OooOoOO0OO [ 12 ] [ : - 2 ] ) ) * 1024 * 1024 )
 oo0o0OoOO0o0 = wiz . convertSize ( int ( float ( OooOoOO0OO [ 13 ] [ : - 2 ] ) ) * 1024 * 1024 )
 III1III11II , iI1I1I1i1i , OOo0O = I11I1ii1i ( )
 if 43 - 43: ooOo
 iiIIIiI1Ii = [ ] ; IIiiiiiIiIIi = [ ] ; iiIiiIi1 = [ ] ; I1Ii11i = [ ] ; I1iIiiiI1OOO0O00Oo = [ ] ; ii1oOOO0ooOO = [ ] ; i11IiI1iiI11 = [ ]
 if 85 - 85: oO0 - o0o0Oo0oooo0 / oO0 + iii11iiII - iiIIi1IiIi11
 IIii1III = glob . glob ( os . path . join ( O0O , '*/' ) )
 for ooooOoo0OO in sorted ( IIii1III , key = lambda OooOOO : OooOOO ) :
  Oo0O0000Oo00o = os . path . split ( ooooOoo0OO [ : - 1 ] ) [ 1 ]
  if Oo0O0000Oo00o == 'packages' : continue
  II1 = os . path . join ( ooooOoo0OO , 'addon.xml' )
  if os . path . exists ( II1 ) :
   i1IiII = open ( II1 )
   o0I1IIIi11ii11 = i1IiII . read ( )
   ii = re . compile ( "<provides>(.+?)</provides>" ) . findall ( o0I1IIIi11ii11 )
   if len ( ii ) == 0 :
    if Oo0O0000Oo00o . startswith ( 'skin' ) : i11IiI1iiI11 . append ( Oo0O0000Oo00o )
    if Oo0O0000Oo00o . startswith ( 'repo' ) : I1iIiiiI1OOO0O00Oo . append ( Oo0O0000Oo00o )
    else : ii1oOOO0ooOO . append ( Oo0O0000Oo00o )
   elif not ( ii [ 0 ] ) . find ( 'executable' ) == - 1 : I1Ii11i . append ( Oo0O0000Oo00o )
   elif not ( ii [ 0 ] ) . find ( 'video' ) == - 1 : iiIiiIi1 . append ( Oo0O0000Oo00o )
   elif not ( ii [ 0 ] ) . find ( 'audio' ) == - 1 : IIiiiiiIiIIi . append ( Oo0O0000Oo00o )
   elif not ( ii [ 0 ] ) . find ( 'image' ) == - 1 : iiIIIiI1Ii . append ( Oo0O0000Oo00o )
   if 89 - 89: iiIIi1IiIi11 . i11iIiiIii * O0
 iiiii1II ( '[B]Media Center Info:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOoOO0OO [ 0 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOoOO0OO [ 1 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , wiz . platform ( ) . title ( ) ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOoOO0OO [ 2 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 iiiii1II ( '[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOoOO0OO [ 3 ] ) , '' , icon = IiIi11iI , themeit = OOoO )
 if 44 - 44: i1IIi . ooOo / i11iIiiIii + i1Ii
 iiiii1II ( '[B]Uptime:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOoOO0OO [ 6 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOoOO0OO [ 7 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 27 - 27: iii11iiII
 iiiii1II ( '[B]Local Storage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , II11ii1 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , ii1II1II ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , i11i11II11i ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 52 - 52: OO00O0O0O00Oo % o0o0Oo0oooo0 + iIii1I11I1II1 * IIIi1i1I . IiiIII111ii
 iiiii1II ( '[B]Ram Usage:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , II1Ii1I1i ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OOooOooo0OOo0 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , oo0o0OoOO0o0 ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 95 - 95: iIii1I11I1II1 . i1Ii - OoooooooOO * I1111 / I1I1i1
 iiiii1II ( '[B]Network:[/B]' , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOoOO0OO [ 4 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , III1III11II ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , iI1I1I1i1i ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OOo0O ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , OooOoOO0OO [ 5 ] ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 74 - 74: IIIi1i1I
 iII1i1IIiI1I = len ( iiIIIiI1Ii ) + len ( IIiiiiiIiIIi ) + len ( iiIiiIi1 ) + len ( I1Ii11i ) + len ( ii1oOOO0ooOO ) + len ( i11IiI1iiI11 ) + len ( I1iIiiiI1OOO0O00Oo )
 iiiii1II ( '[B]Addons([COLOR %s]%s[/COLOR]):[/B]' % ( oOOo0O00o , iII1i1IIiI1I ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Video Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( iiIiiIi1 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Program Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( I1Ii11i ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Music Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( IIiiiiiIiIIi ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Picture Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( iiIIIiI1Ii ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Repositories:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( I1iIiiiI1OOO0O00Oo ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Skins:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( i11IiI1iiI11 ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 iiiii1II ( '[COLOR %s]Scripts/Modules:[/COLOR] [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , iIiIi11 , str ( len ( ii1oOOO0ooOO ) ) ) , '' , icon = IiIi11iI , themeit = oooOo0OOOoo0 )
 if 67 - 67: IiiIII111ii
def iIII11Iiii1 ( ) :
 oooO00Oo = '[COLOR white]ON[/COLOR]' ; ooO00o = '[COLOR red]OFF[/COLOR]'
 o0oo0 = 'true' if o0O0OOO0Ooo == 'true' else 'false'
 OoO0OOoO0Oo0 = 'true' if iiIiII1 == 'true' else 'false'
 oO00O = 'true' if OOO00O0O == 'true' else 'false'
 II111IiiiI1 = 'true' if ooOOoooooo == 'true' else 'false'
 oooOO0oo0Oo00 = 'true' if O0i1II1Iiii1I11 == 'true' else 'false'
 oOoO = 'true' if II1I == 'true' else 'false'
 iI111I1III = 'true' if IiIIIi1iIi == 'true' else 'false'
 I1iIiiiI1OOO0O00Oo = 'true' if IIII == 'true' else 'false'
 super = 'true' if iiIiI == 'true' else 'false'
 i111IiiI1Ii = 'true' if o00oooO0Oo == 'true' else 'false'
 if 72 - 72: O0 . o0o0Oo0oooo0 * Ooo0O + oO0 - I1I1i1
 oo00O00oO000o ( 'Keep Trakt Data' , 'trakt' , icon = iIIii , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Real Debrid' , 'realdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 oo00O00oO000o ( 'Keep Login Info' , 'login' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Import Save Data' , 'managedata' , 'import' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Export Save Data' , 'managedata' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( '- Click to toggle settings -' , '' , themeit = OOoO )
 iiiii1II ( 'Save Trakt: %s' % o0oo0 . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOOiiiiI )
 iiiii1II ( 'Save Real Debrid: %s' % OoO0OOoO0Oo0 . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOOiiiiI )
 iiiii1II ( 'Save Login Info: %s' % oO00O . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Sources.xml\': %s' % II111IiiiI1 . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keepsources' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Profiles.xml\': %s' % oOoO . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keepprofiles' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Advancedsettings.xml\': %s' % oooOO0oo0Oo00 . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keepadvanced' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep \'Favourites.xml\': %s' % iI111I1III . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keepfavourites' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Super Favourites: %s' % super . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keepsuper' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep Installed Repo\'s: %s' % I1iIiiiI1OOO0O00Oo . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keeprepos' , icon = I1111i , themeit = OOOiiiiI )
 iiiii1II ( 'Keep My \'WhiteList\': %s' % i111IiiI1Ii . replace ( 'true' , oooO00Oo ) . replace ( 'false' , ooO00o ) , 'togglesetting' , 'keepwhitelist' , icon = I1111i , themeit = OOOiiiiI )
 if i111IiiI1Ii == 'true' :
  iiiii1II ( 'Edit My Whitelist' , 'whitelist' , 'edit' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'View My Whitelist' , 'whitelist' , 'view' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Clear My Whitelist' , 'whitelist' , 'clear' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Import My Whitelist' , 'whitelist' , 'import' , icon = I1111i , themeit = OOOiiiiI )
  iiiii1II ( 'Export My Whitelist' , 'whitelist' , 'export' , icon = I1111i , themeit = OOOiiiiI )
 iIi1 ( 'files' , 'viewType' )
 if 40 - 40: I1111 + I1111
def o0oo0o00ooO00 ( ) :
 o0oo0 = '[COLOR white]ON[/COLOR]' if o0O0OOO0Ooo == 'true' else '[COLOR red]OFF[/COLOR]'
 IIiIiiI1i = str ( O000OOo00oo ) if not O000OOo00oo == '' else 'Trakt hasnt been saved yet.'
 iiiii1II ( '[I]Register FREE Account at http://trakt.tv[/I]' , '' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Save Trakt Data: %s' % o0oo0 , 'togglesetting' , 'keeptrakt' , icon = iIIii , themeit = OOoO )
 if o0O0OOO0Ooo == 'true' : iiiii1II ( 'Last Save: %s' % str ( IIiIiiI1i ) , '' , icon = iIIii , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = iIIii , themeit = OOoO )
 if 49 - 49: oO0 . i1Ii . i1IIi * o0o0Oo0oooo0 % iIii1I11I1II1
 for o0oo0 in traktit . ORDER :
  O0Oo0o000oO = oOOOoo00 [ o0oo0 ] [ 'name' ]
  III11I1 = oOOOoo00 [ o0oo0 ] [ 'path' ]
  OOOO0o0O = oOOOoo00 [ o0oo0 ] [ 'saved' ]
  file = oOOOoo00 [ o0oo0 ] [ 'file' ]
  iI111I = wiz . getS ( OOOO0o0O )
  O00OoOoO = traktit . traktUser ( o0oo0 )
  Ii1ii111i1 = oOOOoo00 [ o0oo0 ] [ 'icon' ] if os . path . exists ( III11I1 ) else iIIii
  i1i1i1I = oOOOoo00 [ o0oo0 ] [ 'fanart' ] if os . path . exists ( III11I1 ) else OOO00
  ii1IIIIiI11 = iI1IIIii ( 'saveaddon' , 'Trakt' , o0oo0 )
  ooO0o0oo = iI1IIIii ( 'save' , 'Trakt' , o0oo0 )
  ii1IIIIiI11 . append ( ( oooOo0OOOoo0 % '%s Settings' % O0Oo0o000oO , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' % ( IiII1IiiIiI1 , o0oo0 ) ) )
  if 79 - 79: i1Ii % I1111
  iiiii1II ( '[+]-> %s' % O0Oo0o000oO , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
  if not os . path . exists ( III11I1 ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  elif not O00OoOoO : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authtrakt' , o0oo0 , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  else : iiiii1II ( '[COLOR white]Addon Data: %s[/COLOR]' % O00OoOoO , 'authtrakt' , o0oo0 , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  if iI111I == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importtrakt' , o0oo0 , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savetrakt' , o0oo0 , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  else : iiiii1II ( '[COLOR white]Saved Data: %s[/COLOR]' % iI111I , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  if 81 - 81: i11iIiiIii + i11iIiiIii * I1111 + i1Ii
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Trakt Data' , 'savetrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Trakt Data' , 'restoretrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Import Trakt Data' , 'importtrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Trakt Data' , 'cleartrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addontrakt' , 'all' , icon = iIIii , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 32 - 32: O0 . OoooooooOO
def iiIIiiIi ( ) :
 OoO0OOoO0Oo0 = '[COLOR white]ON[/COLOR]' if iiIiII1 == 'true' else '[COLOR red]OFF[/COLOR]'
 IIiIiiI1i = str ( oo0OOo ) if not oo0OOo == '' else 'Real Debrid hasnt been saved yet.'
 iiiii1II ( '[I]http://real-debrid.com is a PAID service.[/I]' , '' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Save Real Debrid Data: %s' % OoO0OOoO0Oo0 , 'togglesetting' , 'keepdebrid' , icon = o00O0O , themeit = OOoO )
 if iiIiII1 == 'true' : iiiii1II ( 'Last Save: %s' % str ( IIiIiiI1i ) , '' , icon = o00O0O , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = o00O0O , themeit = OOoO )
 if 42 - 42: iiIIi1IiIi11 + iIii1I11I1II1
 for II1IiiIII in debridit . ORDER :
  O0Oo0o000oO = iiIiIIIiiI [ II1IiiIII ] [ 'name' ]
  III11I1 = iiIiIIIiiI [ II1IiiIII ] [ 'path' ]
  OOOO0o0O = iiIiIIIiiI [ II1IiiIII ] [ 'saved' ]
  file = iiIiIIIiiI [ II1IiiIII ] [ 'file' ]
  iI111I = wiz . getS ( OOOO0o0O )
  O00OoOoO = debridit . debridUser ( II1IiiIII )
  Ii1ii111i1 = iiIiIIIiiI [ II1IiiIII ] [ 'icon' ] if os . path . exists ( III11I1 ) else o00O0O
  i1i1i1I = iiIiIIIiiI [ II1IiiIII ] [ 'fanart' ] if os . path . exists ( III11I1 ) else OOO00
  ii1IIIIiI11 = iI1IIIii ( 'saveaddon' , 'Debrid' , II1IiiIII )
  ooO0o0oo = iI1IIIii ( 'save' , 'Debrid' , II1IiiIII )
  ii1IIIIiI11 . append ( ( oooOo0OOOoo0 % '%s Settings' % O0Oo0o000oO , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' % ( IiII1IiiIiI1 , II1IiiIII ) ) )
  if 41 - 41: II111iiii * OOoooooO
  iiiii1II ( '[+]-> %s' % O0Oo0o000oO , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
  if not os . path . exists ( III11I1 ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  elif not O00OoOoO : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authdebrid' , II1IiiIII , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  else : iiiii1II ( '[COLOR white]Addon Data: %s[/COLOR]' % O00OoOoO , 'authdebrid' , II1IiiIII , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  if iI111I == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importdebrid' , II1IiiIII , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savedebrid' , II1IiiIII , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  else : iiiii1II ( '[COLOR white]Saved Data: %s[/COLOR]' % iI111I , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  if 68 - 68: IiiIII111ii - ooOo
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Real Debrid Data' , 'savedebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Real Debrid Data' , 'restoredebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Import Real Debrid Data' , 'importdebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Real Debrid Data' , 'cleardebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addondebrid' , 'all' , icon = o00O0O , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 41 - 41: IIIi1i1I
def I11II1 ( ) :
 oO00O = '[COLOR white]ON[/COLOR]' if OOO00O0O == 'true' else '[COLOR red]OFF[/COLOR]'
 IIiIiiI1i = str ( ooOOO00Ooo ) if not ooOOO00Ooo == '' else 'Login data hasnt been saved yet.'
 iiiii1II ( '[I]Several of these addons are PAID services.[/I]' , '' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Save Login Data: %s' % oO00O , 'togglesetting' , 'keeplogin' , icon = ii1iii1i , themeit = OOoO )
 if OOO00O0O == 'true' : iiiii1II ( 'Last Save: %s' % str ( IIiIiiI1i ) , '' , icon = ii1iii1i , themeit = OOoO )
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , icon = ii1iii1i , themeit = OOoO )
 if 46 - 46: o0o0Oo0oooo0
 for oO00O in loginit . ORDER :
  O0Oo0o000oO = iiI1IIIi [ oO00O ] [ 'name' ]
  III11I1 = iiI1IIIi [ oO00O ] [ 'path' ]
  OOOO0o0O = iiI1IIIi [ oO00O ] [ 'saved' ]
  file = iiI1IIIi [ oO00O ] [ 'file' ]
  iI111I = wiz . getS ( OOOO0o0O )
  O00OoOoO = loginit . loginUser ( oO00O )
  Ii1ii111i1 = iiI1IIIi [ oO00O ] [ 'icon' ] if os . path . exists ( III11I1 ) else ii1iii1i
  i1i1i1I = iiI1IIIi [ oO00O ] [ 'fanart' ] if os . path . exists ( III11I1 ) else OOO00
  ii1IIIIiI11 = iI1IIIii ( 'saveaddon' , 'Login' , oO00O )
  ooO0o0oo = iI1IIIii ( 'save' , 'Login' , oO00O )
  ii1IIIIiI11 . append ( ( oooOo0OOOoo0 % '%s Settings' % O0Oo0o000oO , 'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=login)' % ( IiII1IiiIiI1 , oO00O ) ) )
  if 83 - 83: i11iIiiIii * OO00O0O0O00Oo
  iiiii1II ( '[+]-> %s' % O0Oo0o000oO , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = OOoO )
  if not os . path . exists ( III11I1 ) : iiiii1II ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  elif not O00OoOoO : iiiii1II ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , 'authlogin' , oO00O , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  else : iiiii1II ( '[COLOR white]Addon Data: %s[/COLOR]' % O00OoOoO , 'authlogin' , oO00O , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ii1IIIIiI11 )
  if iI111I == "" :
   if os . path . exists ( file ) : iiiii1II ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , 'importlogin' , oO00O , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
   else : iiiii1II ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , 'savelogin' , oO00O , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  else : iiiii1II ( '[COLOR white]Saved Data: %s[/COLOR]' % iI111I , '' , icon = Ii1ii111i1 , fanart = i1i1i1I , menu = ooO0o0oo )
  if 49 - 49: Ooo0O * IIIi1i1I + I1I1i1 - i11iIiiIii
 if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
 iiiii1II ( 'Save All Login Data' , 'savelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Recover All Saved Login Data' , 'restorelogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Import Login Data' , 'importlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Saved Login Data' , 'clearlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iiiii1II ( 'Clear All Addon Data' , 'addonlogin' , 'all' , icon = ii1iii1i , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 74 - 74: Ooo0O / iIii1I11I1II1 . II111iiii - I1111
def O0Oo0 ( ) :
 if o0OIiII < 17 :
  iIIIi1IiI11I1 = os . path . join ( OOOO , wiz . latestDB ( 'Addons' ) )
  try :
   os . remove ( iIIIi1IiI11I1 )
  except Exception , i1OoOO :
   wiz . log ( "Unable to remove %s, Purging DB" % iIIIi1IiI11I1 )
   wiz . purgeDb ( iIIIi1IiI11I1 )
 else :
  xbmc . log ( "Requested Addons.db be removed but doesnt work in Kod17" )
  if 71 - 71: IiiIII111ii - O0 - iiIIi1IiIi11 . iii11iiII % Ooo0O
def Oo00oO ( ) :
 IIii1III = glob . glob ( os . path . join ( O0O , '*/' ) )
 ooo0ii1iIIi11 = [ ] ; iI1IIIII1Ii = [ ]
 for ooooOoo0OO in sorted ( IIii1III , key = lambda OooOOO : OooOOO ) :
  Oo0O0000Oo00o = os . path . split ( ooooOoo0OO [ : - 1 ] ) [ 1 ]
  if Oo0O0000Oo00o in Iii1I1I11iiI1 : continue
  elif Oo0O0000Oo00o in OOo0 : continue
  elif Oo0O0000Oo00o == 'packages' : continue
  II1 = os . path . join ( ooooOoo0OO , 'addon.xml' )
  if os . path . exists ( II1 ) :
   i1IiII = open ( II1 )
   o0I1IIIi11ii11 = i1IiII . read ( )
   o0O0Oo00 = wiz . parseDOM ( o0I1IIIi11ii11 , 'addon' , ret = 'id' )
   if 13 - 13: II111iiii
   o0o000Oo = Oo0O0000Oo00o if len ( o0O0Oo00 ) == 0 else o0O0Oo00 [ 0 ]
   try :
    Iii111IiIii = xbmcaddon . Addon ( id = o0o000Oo )
    ooo0ii1iIIi11 . append ( Iii111IiIii . getAddonInfo ( 'name' ) )
    iI1IIIII1Ii . append ( o0o000Oo )
   except :
    pass
 if len ( ooo0ii1iIIi11 ) == 0 :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]No Addons To Remove[/COLOR]" % iIiIi11 )
  return
 if o0OIiII > 16 :
  OOOo = iiIIIII1i1iI . multiselect ( "%s: Select the addons you wish to remove." % o0OOO , ooo0ii1iIIi11 )
 else :
  OOOo = [ ] ; O0OOOOOoo = 0
  oO0o0O0o0OO00 = [ "-- Click here to Continue --" ] + ooo0ii1iIIi11
  while not O0OOOOOoo == - 1 :
   O0OOOOOoo = iiIIIII1i1iI . select ( "%s: Select the addons you wish to remove." % o0OOO , oO0o0O0o0OO00 )
   if O0OOOOOoo == - 1 : break
   elif O0OOOOOoo == 0 : break
   else :
    iIiiiIi = ( O0OOOOOoo - 1 )
    if iIiiiIi in OOOo :
     OOOo . remove ( iIiiiIi )
     oO0o0O0o0OO00 [ O0OOOOOoo ] = ooo0ii1iIIi11 [ iIiiiIi ]
    else :
     OOOo . append ( iIiiiIi )
     oO0o0O0o0OO00 [ O0OOOOOoo ] = "[B][COLOR %s]%s[/COLOR][/B]" % ( oOOo0O00o , ooo0ii1iIIi11 [ iIiiiIi ] )
 if OOOo == None : return
 if len ( OOOo ) > 0 :
  wiz . addonUpdates ( 'set' )
  for OooooOo in OOOo :
   IIIiiiIiI ( iI1IIIII1Ii [ OooooOo ] , ooo0ii1iIIi11 [ OooooOo ] , True )
   if 80 - 80: IIIi1i1I % IIIi1i1I % O0 - i11iIiiIii . iiIIi1IiIi11 / O0
  xbmc . sleep ( 500 )
  if 13 - 13: ooOo + O0 - oO0 % Ooo0O / IiiIII111ii . i1IIi
  if I11i1I1I == 1 : OOOO00OoooO = 1
  elif I11i1I1I == 2 : OOOO00OoooO = 0
  else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR white]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
  if OOOO00OoooO == 1 : wiz . reloadFix ( 'remove addon' )
  else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
  if 7 - 7: oO0 / II111iiii - i11IiIiiIIIII + i1IIi + IiiIII111ii
def i11i11i ( ) :
 if os . path . exists ( ooOOOo0oo0O0 ) :
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , 'removedata' , 'all' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , 'removedata' , 'uninstalled' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , 'removedata' , 'empty' , themeit = oooOo0OOOoo0 )
  iiiii1II ( '[COLOR red][B][REMOVE][/B][/COLOR] %s Addon_Data' % o0OOO , 'resetaddon' , themeit = oooOo0OOOoo0 )
  if O0O0ooOOO == 'No' : iiiii1II ( wiz . sep ( ) , '' , themeit = OOoO )
  IIii1III = glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*/' ) )
  for ooooOoo0OO in sorted ( IIii1III , key = lambda OooOOO : OooOOO ) :
   Oo0O0000Oo00o = ooooOoo0OO . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   Ii1ii111i1 = os . path . join ( ooooOoo0OO . replace ( ooOOOo0oo0O0 , O0O ) , 'icon.png' )
   i1i1i1I = os . path . join ( ooooOoo0OO . replace ( ooOOOo0oo0O0 , O0O ) , 'fanart.png' )
   iiI1iI = Oo0O0000Oo00o
   Ooo00O0 = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' , 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' , 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' , 'script.' : '[COLOR white][SCRIPT] [/COLOR]' , 'service.' : '[COLOR white][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' , 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for OoO0OOoO0 in Ooo00O0 :
    iiI1iI = iiI1iI . replace ( OoO0OOoO0 , Ooo00O0 [ OoO0OOoO0 ] )
   if Oo0O0000Oo00o in Iii1I1I11iiI1 : iiI1iI = '[COLOR white][B][PROTECTED][/B][/COLOR] %s' % iiI1iI
   else : iiI1iI = '[COLOR red][B][REMOVE][/B][/COLOR] %s' % iiI1iI
   iiiii1II ( ' %s' % iiI1iI , 'removedata' , Oo0O0000Oo00o , icon = Ii1ii111i1 , fanart = i1i1i1I , themeit = oooOo0OOOoo0 )
 else :
  iiiii1II ( 'No Addon data folder found.' , '' , themeit = OOoO )
 iIi1 ( 'files' , 'viewType' )
 if 5 - 5: i1IIi . i1IIi
def o0o0oo0Ooo ( ) :
 iiiii1II ( "[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]" , '' , icon = IiIi11iI )
 IIii1III = glob . glob ( os . path . join ( O0O , '*/' ) )
 OooOOO = 0
 for ooooOoo0OO in sorted ( IIii1III , key = lambda OooOOO : OooOOO ) :
  Oo0O0000Oo00o = os . path . split ( ooooOoo0OO [ : - 1 ] ) [ 1 ]
  if Oo0O0000Oo00o in Iii1I1I11iiI1 : continue
  if Oo0O0000Oo00o in OOo0 : continue
  iI1i = os . path . join ( ooooOoo0OO , 'addon.xml' )
  if os . path . exists ( iI1i ) :
   OooOOO += 1
   IIii1III = ooooOoo0OO . replace ( O0O , '' ) [ 1 : - 1 ]
   i1IiII = open ( iI1i )
   o0I1IIIi11ii11 = i1IiII . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o0O0Oo00 = wiz . parseDOM ( o0I1IIIi11ii11 , 'addon' , ret = 'id' )
   i11I1II = wiz . parseDOM ( o0I1IIIi11ii11 , 'addon' , ret = 'name' )
   try :
    I1iI11iii = o0O0Oo00 [ 0 ]
    O0Oo0o000oO = i11I1II [ 0 ]
   except :
    continue
   try :
    Iii111IiIii = xbmcaddon . Addon ( id = I1iI11iii )
    OO00O0oOO = "[COLOR white][Enabled][/COLOR]"
    i11I = "false"
   except :
    OO00O0oOO = "[COLOR red][Disabled][/COLOR]"
    i11I = "true"
    pass
   Ii1ii111i1 = os . path . join ( ooooOoo0OO , 'icon.png' ) if os . path . exists ( os . path . join ( ooooOoo0OO , 'icon.png' ) ) else iiiiiIIii
   i1i1i1I = os . path . join ( ooooOoo0OO , 'fanart.jpg' ) if os . path . exists ( os . path . join ( ooooOoo0OO , 'fanart.jpg' ) ) else OOO00
   iiiii1II ( "%s %s" % ( OO00O0oOO , O0Oo0o000oO ) , 'toggleaddon' , IIii1III , i11I , icon = Ii1ii111i1 , fanart = i1i1i1I )
   i1IiII . close ( )
 if OooOOO == 0 :
  iiiii1II ( "No Addons Found to Enable or Disable." , '' , icon = IiIi11iI )
 iIi1 ( 'files' , 'viewType' )
 if 56 - 56: iiIIi1IiIi11 . OO00O0O0O00Oo
def I1i1ii ( ) :
 III1II1i = [ 'Every Startup' , 'Every Day' , 'Every Three Days' , 'Every Weekly' ]
 O0000oo00oOOO = iiIIIII1i1iI . select ( "[COLOR %s]How often would you list to Auto Clean on Startup?[/COLOR]" % iIiIi11 , III1II1i )
 if not O0000oo00oOOO == - 1 :
  wiz . setS ( 'autocleanfeq' , str ( O0000oo00oOOO ) )
  wiz . LogNotify ( '[COLOR %s]Auto Clean Up[/COLOR]' % oOOo0O00o , '[COLOR %s]Fequency Now %s[/COLOR]' % ( iIiIi11 , III1II1i [ O0000oo00oOOO ] ) )
  if 98 - 98: IIIi1i1I . OoooooooOO
def Oo000 ( ) :
 iiiii1II ( 'Convert Text Files to 0.1.7' , 'converttext' , themeit = OOOiiiiI )
 iiiii1II ( 'Create QR Code' , 'createqr' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Notifications' , 'testnotify' , themeit = OOOiiiiI )
 iiiii1II ( 'Test Update' , 'testupdate' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run' , 'testfirst' , themeit = OOOiiiiI )
 iiiii1II ( 'Test First Run Settings' , 'testfirstrun' , themeit = OOOiiiiI )
 iiiii1II ( 'Test APk' , 'testapk' , themeit = OOOiiiiI )
 if 97 - 97: O0 / iii11iiII + I1I1i1 . IIIi1i1I % o0o0Oo0oooo0 - o0o0Oo0oooo0
 iIi1 ( 'files' , 'viewType' )
 if 33 - 33: i11IiIiiIIIII % II111iiii + I1111
 if 93 - 93: i1IIi . i1Ii / ooOo + i1Ii
 if 58 - 58: oO0 + O0 . Ooo0O + o0o0Oo0oooo0 - I1111 - o0o0Oo0oooo0
 if 41 - 41: Ooo0O / i1IIi / Ooo0O - iiIIi1IiIi11 . I1I1i1
def Oooooooo00o00 ( name , type , theme = None , over = False ) :
 if over == False :
  O0oo00OOOO = wiz . checkBuild ( name , 'url' )
  if O0oo00OOOO == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Unabled to find build[/COLOR]" % iIiIi11 )
   return
  IiIi1II111I = wiz . workingURL ( O0oo00OOOO )
  if IiIi1II111I == False :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Build Zip Error: %s[/COLOR]" % ( iIiIi11 , IiIi1II111I ) )
   return
 if type == 'gui' :
  if name == O000oo0O :
   if over == True : o00o = 1
   else : o00o = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to apply the guifix for:' % iIiIi11 , '[COLOR %s]%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR white]Apply Fix[/COLOR][/B]' )
  else :
   o00o = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , "[COLOR %s][COLOR %s]%s[/COLOR] community build is not currently installed." % ( iIiIi11 , oOOo0O00o , name ) , "Would you like to apply the guiFix anyways?.[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR white]Apply Fix[/COLOR][/B]' )
  if o00o :
   IIi1i1 = wiz . checkBuild ( name , 'gui' )
   o0O0Ooo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( IIi1i1 ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading GuiFix:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
   iIiiIi11IIi = os . path . join ( o0o0OOO0o0 , '%s_guisettings.zip' % o0O0Ooo )
   try : os . remove ( iIiiIi11IIi )
   except : pass
   downloader . download ( IIi1i1 , iIiiIi11IIi , oo00 )
   xbmc . sleep ( 500 )
   Ii1i1i1111 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
   oo00 . update ( 0 , Ii1i1i1111 , '' , 'Please Wait' )
   extract . all ( iIiiIi11IIi , oOo00Oo00O , oo00 , title = Ii1i1i1111 )
   oo00 . close ( )
   wiz . defaultSkin ( )
   wiz . lookandFeelData ( 'save' )
   if I11i1I1I == 1 : OOOO00OoooO = 1
   elif I11i1I1I == 2 : OOOO00OoooO = 0
   else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Gui fix has been installed.  Would you like to Reload the profile or Force Close Kodi?[/COLOR]" % iIiIi11 , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR white]Force Close[/COLOR][/B]" )
   if OOOO00OoooO == 1 : wiz . reloadFix ( )
   else : iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]To save changes you now need to force close Kodi, Press OK to force close Kodi[/COLOR]" % iIiIi11 ) ; wiz . killxbmc ( 'true' )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]GuiFix: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'fresh' :
  O0oO00oOOooO ( name )
 elif type == 'normal' :
  if oO0o00oOOooO0 == 'normal' :
   if o0O0OOO0Ooo == 'true' :
    traktit . autoUpdate ( 'all' )
    wiz . setS ( 'traktlastsave' , str ( I1IiiiiI ) )
   if iiIiII1 == 'true' :
    debridit . autoUpdate ( 'all' )
    wiz . setS ( 'debridlastsave' , str ( I1IiiiiI ) )
   if OOO00O0O == 'true' :
    loginit . autoUpdate ( 'all' )
    wiz . setS ( 'loginlastsave' , str ( I1IiiiiI ) )
  IiI = int ( o0OIiII ) ; Iii1iiI = int ( float ( wiz . checkBuild ( name , 'kodi' ) ) )
  if not IiI == Iii1iiI :
   if IiI == 16 and Iii1iiI <= 15 : ooOOO0OooOo = False
   else : ooOOO0OooOo = True
  else : ooOOO0OooOo = False
  if ooOOO0OooOo == True :
   ii1IiiII = iiIIIII1i1iI . yesno ( "%s - [COLOR red]WARNING!![/COLOR]" % o0OOO , '[COLOR %s]There is a chance that the skin will not appear correctly' % iIiIi11 , 'When installing a %s build on a Kodi %s install' % ( wiz . checkBuild ( name , 'kodi' ) , o0OIiII ) , 'Would you still like to install: [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR white]Yes, Install[/COLOR][/B]' )
  else :
   if not over == False : ii1IiiII = 1
   else : ii1IiiII = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to Download and Install:' % iIiIi11 , '[COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR white]Yes, Install[/COLOR][/B]' )
  if ii1IiiII :
   wiz . clearS ( 'build' )
   IIi1i1 = wiz . checkBuild ( name , 'url' )
   o0O0Ooo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( IIi1i1 ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , '' , 'Please Wait' )
   iIiiIi11IIi = os . path . join ( o0o0OOO0o0 , '%s.zip' % o0O0Ooo )
   try : os . remove ( iIiiIi11IIi )
   except : pass
   wiz . add_one ( name )
   downloader . download ( IIi1i1 , iIiiIi11IIi , oo00 )
   xbmc . sleep ( 500 )
   Ii1i1i1111 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) )
   oo00 . update ( 0 , Ii1i1i1111 , '' , 'Please Wait' )
   Oo0oO , II1ii1ii11I1 , o0ooOO0o = extract . all ( iIiiIi11IIi , o00 , oo00 , title = Ii1i1i1111 )
   if int ( float ( Oo0oO ) ) > 0 :
    wiz . fixmetas ( )
    wiz . lookandFeelData ( 'save' )
    wiz . defaultSkin ( )
    if 7 - 7: iIii1I11I1II1 * I1111 / o0o0Oo0oooo0 % OO00O0O0O00Oo - I1I1i1 - iii11iiII
    wiz . setS ( 'buildname' , name )
    wiz . setS ( 'buildversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'buildtheme' , '' )
    wiz . setS ( 'latestversion' , wiz . checkBuild ( name , 'version' ) )
    wiz . setS ( 'lastbuildcheck' , str ( OOI1iI1ii1II ) )
    wiz . setS ( 'installed' , 'true' )
    wiz . setS ( 'extract' , str ( Oo0oO ) )
    wiz . setS ( 'errors' , str ( II1ii1ii11I1 ) )
    wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( Oo0oO , II1ii1ii11I1 ) )
    try : os . remove ( iIiiIi11IIi )
    except : pass
    if int ( float ( II1ii1ii11I1 ) ) > 0 :
     o00o = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s v%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , Oo0oO , '%' , oOOo0O00o , II1ii1ii11I1 ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR white]View Errors[/COLOR][/B]' )
     if o00o :
      if isinstance ( II1ii1ii11I1 , unicode ) :
       o0ooOO0o = o0ooOO0o . encode ( 'utf-8' )
      wiz . TextBox ( o0OOO , o0ooOO0o )
    oo00 . close ( )
    OOo00OoO = wiz . themeCount ( name )
    if not OOo00OoO == False :
     Oooooooo00o00 ( name , 'theme' )
    if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
    if I11i1I1I == 1 : OOOO00OoooO = 1
    elif I11i1I1I == 2 : OOOO00OoooO = 0
    else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR white]Force Close[/COLOR][/B]" )
    if OOOO00OoooO == 1 : wiz . reloadFix ( )
    else : wiz . killxbmc ( True )
   else :
    if isinstance ( II1ii1ii11I1 , unicode ) :
     o0ooOO0o = o0ooOO0o . encode ( 'utf-8' )
    wiz . TextBox ( "%s: Error Installing Build" % o0OOO , o0ooOO0o )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Build Install: Cancelled![/COLOR]' % iIiIi11 )
 elif type == 'theme' :
  if theme == None :
   OOo00OoO = wiz . checkBuild ( name , 'theme' )
   iiIO0OO0o0O00oO = [ ]
   if not OOo00OoO == 'http://' and wiz . workingURL ( OOo00OoO ) == True :
    iiIO0OO0o0O00oO = wiz . themeCount ( name , False )
    if len ( iiIO0OO0o0O00oO ) > 0 :
     if iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]The Build [COLOR %s]%s[/COLOR] comes with [COLOR %s]%s[/COLOR] different themes" % ( iIiIi11 , oOOo0O00o , name , oOOo0O00o , len ( iiIO0OO0o0O00oO ) ) , "Would you like to install one now?[/COLOR]" , yeslabel = "[B][COLOR white]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" ) :
      wiz . log ( "Theme List: %s " % str ( iiIO0OO0o0O00oO ) )
      o00O = iiIIIII1i1iI . select ( o0OOO , iiIO0OO0o0O00oO )
      wiz . log ( "Theme install selected: %s" % o00O )
      if not o00O == - 1 : theme = iiIO0OO0o0O00oO [ o00O ] ; oO0o0oOo = True
      else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 ) ; return
   else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: None Found![/COLOR]' % iIiIi11 )
  else : oO0o0oOo = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to install the theme:' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , theme ) , 'for [COLOR %s]%s v%s[/COLOR]?[/COLOR]' % ( oOOo0O00o , name , wiz . checkBuild ( name , 'version' ) ) , yeslabel = "[B][COLOR white]Install Theme[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel Themes[/COLOR][/B]" )
  if oO0o0oOo :
   OoO0O0oo0o = wiz . checkTheme ( name , theme , 'url' )
   o0O0Ooo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
   if not wiz . workingURL ( OoO0O0oo0o ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Invalid Zip Url![/COLOR]' % iIiIi11 ) ; return False
   if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
   oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme ) , '' , 'Please Wait' )
   iIiiIi11IIi = os . path . join ( o0o0OOO0o0 , '%s.zip' % o0O0Ooo )
   try : os . remove ( iIiiIi11IIi )
   except : pass
   downloader . download ( OoO0O0oo0o , iIiiIi11IIi , oo00 )
   xbmc . sleep ( 500 )
   oo00 . update ( 0 , "" , "Installing %s " % name )
   iIi11I11 = False
   if oO0o00oOOooO0 not in [ "fresh" , "normal" ] :
    iIi11I11 = i1ioO ( iIiiIi11IIi ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    I11iiI = i1iIii1i111 ( iIiiIi11IIi ) if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] else False
    if iIi11I11 == True :
     wiz . lookandFeelData ( 'save' )
     OOooo000OooO = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
     o0o0OoOo = xbmc . getSkinDir ( )
     if 33 - 33: i1IIi / OO00O0O0O00Oo - i1IIi . Ooo0O
     skinSwitch . swapSkins ( OOooo000OooO )
     OooOOO = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and OooOOO < 150 :
      OooOOO += 1
      xbmc . sleep ( 200 )
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return
     xbmc . sleep ( 500 )
   Ii1i1i1111 = '[COLOR %s][B]Installing Theme:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , theme )
   oo00 . update ( 0 , Ii1i1i1111 , '' , 'Please Wait' )
   Oo0oO , II1ii1ii11I1 , o0ooOO0o = extract . all ( iIiiIi11IIi , o00 , oo00 , title = Ii1i1i1111 )
   wiz . setS ( 'buildtheme' , theme )
   wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( Oo0oO , II1ii1ii11I1 ) )
   oo00 . close ( )
   if oO0o00oOOooO0 not in [ "fresh" , "normal" ] :
    wiz . forceUpdate ( )
    if o0OIiII >= 17 : wiz . kodi17Fix ( )
    if I11iiI == True :
     wiz . lookandFeelData ( 'save' )
     wiz . defaultSkin ( )
     o0o0OoOo = wiz . getS ( 'defaultskin' )
     skinSwitch . swapSkins ( o0o0OoOo )
     OooOOO = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and OooOOO < 150 :
      OooOOO += 1
      xbmc . sleep ( 200 )
      if 18 - 18: Ooo0O / O0 + iiIIi1IiIi11
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     wiz . lookandFeelData ( 'restore' )
    elif iIi11I11 == True :
     skinSwitch . swapSkins ( o0o0OoOo )
     OooOOO = 0
     xbmc . sleep ( 1000 )
     while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and OooOOO < 150 :
      OooOOO += 1
      xbmc . sleep ( 200 )
      if 65 - 65: i1IIi . oO0 / OOoooooO
     if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
      wiz . ebi ( 'SendClick(11)' )
     else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return
     wiz . lookandFeelData ( 'restore' )
    else :
     wiz . ebi ( "ReloadSkin()" )
     xbmc . sleep ( 1000 )
     wiz . ebi ( "Container.Refresh" )
  else :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Theme Install: Cancelled![/COLOR]' % iIiIi11 )
   if 11 - 11: i1Ii * OOoooooO / OOoooooO - iii11iiII
def OoO0o0OOOO ( name , url ) :
 if not wiz . workingURL ( url ) :
  LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Invalid URL for Build[/COLOR]' % iIiIi11 ) ; return
 type = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to preform a [COLOR %s]Fresh Install[/COLOR] or [COLOR %s]Normal Install[/COLOR] for:[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , name ) , yeslabel = "[B][COLOR white]Fresh Install[/COLOR][/B]" , nolabel = "[B][COLOR red]Normal Install[/COLOR][/B]" )
 if type == 1 :
  O0oO00oOOooO ( 'third' , True )
 wiz . clearS ( 'build' )
 o0O0Ooo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
 oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , '' , 'Please Wait' )
 iIiiIi11IIi = os . path . join ( o0o0OOO0o0 , '%s.zip' % o0O0Ooo )
 try : os . remove ( iIiiIi11IIi )
 except : pass
 downloader . download ( url , iIiiIi11IIi , oo00 )
 xbmc . sleep ( 500 )
 Ii1i1i1111 = '[COLOR %s][B]Installing:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name )
 oo00 . update ( 0 , Ii1i1i1111 , '' , 'Please Wait' )
 Oo0oO , II1ii1ii11I1 , o0ooOO0o = extract . all ( iIiiIi11IIi , o00 , oo00 , title = Ii1i1i1111 )
 if int ( float ( Oo0oO ) ) > 0 :
  wiz . fixmetas ( )
  wiz . lookandFeelData ( 'save' )
  wiz . defaultSkin ( )
  if 39 - 39: oO0 / i1IIi * i1Ii - ooOo
  wiz . setS ( 'installed' , 'true' )
  wiz . setS ( 'extract' , str ( Oo0oO ) )
  wiz . setS ( 'errors' , str ( II1ii1ii11I1 ) )
  wiz . log ( 'INSTALLED %s: [ERRORS:%s]' % ( Oo0oO , II1ii1ii11I1 ) )
  try : os . remove ( iIiiIi11IIi )
  except : pass
  if int ( float ( II1ii1ii11I1 ) ) > 0 :
   o00o = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , name ) , 'Completed: [COLOR %s]%s%s[/COLOR] [Errors:[COLOR %s]%s[/COLOR]]' % ( oOOo0O00o , Oo0oO , '%' , oOOo0O00o , II1ii1ii11I1 ) , 'Would you like to view the errors?[/COLOR]' , nolabel = '[B][COLOR red]No Thanks[/COLOR][/B]' , yeslabel = '[B][COLOR white]View Errors[/COLOR][/B]' )
   if o00o :
    if isinstance ( II1ii1ii11I1 , unicode ) :
     o0ooOO0o = o0ooOO0o . encode ( 'utf-8' )
    wiz . TextBox ( o0OOO , o0ooOO0o )
 oo00 . close ( )
 if o0OIiII >= 17 : wiz . addonDatabase ( IiII1IiiIiI1 , 1 )
 if I11i1I1I == 1 : OOOO00OoooO = 1
 elif I11i1I1I == 2 : OOOO00OoooO = 0
 else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR white]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR red]Force Close[/COLOR][/B]" )
 if OOOO00OoooO == 1 : wiz . reloadFix ( )
 else : wiz . killxbmc ( True )
 if 74 - 74: O0 - II111iiii + i1IIi . OO00O0O0O00Oo . oO0
def i1ioO ( path ) :
 OoO0O = zipfile . ZipFile ( path )
 for OoOo00o0OO in OoO0O . infolist ( ) :
  if '/settings.xml' in OoOo00o0OO . filename :
   return True
 return False
 if 98 - 98: i11iIiiIii / ooOo * I1I1i1 / OO00O0O0O00Oo
def i1iIii1i111 ( path ) :
 OoO0O = zipfile . ZipFile ( path )
 for OoOo00o0OO in OoO0O . infolist ( ) :
  if '/guisettings.xml' in OoOo00o0OO . filename :
   return True
 return False
 if 67 - 67: i11IiIiiIIIII % IIIi1i1I
def iiIii1I ( apk , url , Brackets ) :
 wiz . log ( apk )
 wiz . log ( url )
 if wiz . platform ( ) == 'android' :
  o00o = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to download and install:" % iIiIi11 , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , apk ) , yeslabel = "[B][COLOR white]Download[/COLOR][/B]" , nolabel = "[B][COLOR red]Cancel[/COLOR][/B]" )
  if not o00o : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: Install Cancelled[/COLOR]' % iIiIi11 ) ; return
  ii1iiIi = apk
  if not os . path . exists ( o0o0OOO0o0 ) : os . makedirs ( o0o0OOO0o0 )
  if not wiz . workingURL ( url ) == True : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]APK Installer: Invalid Apk Url![/COLOR]' % iIiIi11 ) ; return
  oo00 . create ( o0OOO , '[COLOR %s][B]Downloading:[/B][/COLOR] [COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , ii1iiIi ) , '' , 'Please Wait' )
  iIiiIi11IIi = os . path . join ( o0o0OOO0o0 , "%s.apk" % apk . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' ) )
  try : os . remove ( iIiiIi11IIi )
  except : pass
  downloader . download ( url , iIiiIi11IIi , oo00 )
  xbmc . sleep ( 100 )
  oo00 . close ( )
  if "Brackets" in Brackets :
   i11ii1i1i = zipfile . ZipFile ( iIiiIi11IIi )
   for file in i11ii1i1i . namelist ( ) :
    if file . endswith ( '.apk' ) :
     with open ( os . path . join ( o0o0OOO0o0 , os . path . basename ( file ) ) , 'wb' ) as i1IiII :
      iIIi1 = file . split ( '/' ) [ 1 ]
      i1IiII . write ( i11ii1i1i . read ( file ) )
      xbmc . sleep ( 500 )
      i1IiII . close ( )
      try :
       os . remove ( iIiiIi11IIi )
      except :
       pass
      iIiiIi11IIi = os . path . join ( o0o0OOO0o0 , iIIi1 )
  iiIIIII1i1iI . ok ( o0OOO , "Launching the APK to be installed" , "Follow the install process to complete." )
  notify . apkInstaller ( apk )
  wiz . ebi ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + iIiiIi11IIi + '")' )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]ERROR: None Android Device[/COLOR]' % iIiIi11 )
 if 9 - 9: OoooooooOO + I1I1i1 + IiiIII111ii % IiiIII111ii % Ooo0O . i1Ii
 if 76 - 76: OoooooooOO - II111iiii % o0o0Oo0oooo0 + IIIi1i1I + iIii1I11I1II1 . o0o0Oo0oooo0
 if 16 - 16: I1I1i1 . i11IiIiiIIIII
 if 50 - 50: OOoooooO * o0o0Oo0oooo0 + oO0 - i11iIiiIii + Ooo0O * oO0
def i11II ( name , url , ) :
 if "NULL" in url :
  iiIIIII1i1iI . ok ( o0OOO , "[COLOR ghostwhite]Not a valid selection, please try again.[/COLOR]" )
  sys . exit ( 1 )
  if 69 - 69: OO00O0O0O00Oo - i1IIi % iiIIi1IiIi11 . iii11iiII - iii11iiII
 I1IiI = xbmcgui . DialogProgress ( )
 I1IiI . create ( o0OOO , "" , "" , 'ROM: ' + name )
 o0O0Ooo = name . replace ( '\\' , '' ) . replace ( '/' , '' ) . replace ( ':' , '' ) . replace ( '*' , '' ) . replace ( '?' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( '|' , '' )
 iIiiIi11IIi = os . path . join ( o0o0OOO0o0 , '%s.zip' % o0O0Ooo )
 downloader . download ( url , iIiiIi11IIi , I1IiI )
 I1IiI . update ( 0 )
 extract . all ( iIiiIi11IIi , iI , I1IiI )
 iiIIIII1i1iI . ok ( o0OOO , "[COLOR yellow]Download complete, ROM Location: [/COLOR][COLOR white]" + iI + "[/COLOR]" )
 if 65 - 65: iii11iiII + II111iiii
 if 61 - 61: i11iIiiIii * IIIi1i1I % Ooo0O * OO00O0O0O00Oo - OoooooooOO - I1111
 if 83 - 83: OOoooooO / iii11iiII
 if 39 - 39: i1Ii + i11IiIiiIIIII
 if 9 - 9: ooOo % i11IiIiiIIIII . Ooo0O * ooOo
def OoO0oO0oo0O ( part , whole ) :
 return 100 * float ( part ) / float ( whole )
 if 82 - 82: OoooooooOO . IiiIII111ii
def iI1IIIii ( type , add , name ) :
 if type == 'saveaddon' :
  III1ii = [ ]
  iII1ii = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  o0oOoO00 = add . replace ( 'Debrid' , 'Real Debrid' )
  II11I = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  III1ii . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  III1ii . append ( ( OOoO % 'Save %s Data' % o0oOoO00 , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , iII1ii , II11I ) ) )
  III1ii . append ( ( OOoO % 'Restore %s Data' % o0oOoO00 , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , iII1ii , II11I ) ) )
  III1ii . append ( ( OOoO % 'Clear %s Data' % o0oOoO00 , 'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' % ( IiII1IiiIiI1 , iII1ii , II11I ) ) )
 elif type == 'save' :
  III1ii = [ ]
  iII1ii = urllib . quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
  o0oOoO00 = add . replace ( 'Debrid' , 'Real Debrid' )
  II11I = urllib . quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
  name = name . replace ( 'url' , 'URL Resolver' )
  III1ii . append ( ( oooOo0OOOoo0 % name . title ( ) , ' ' ) )
  III1ii . append ( ( OOoO % 'Register %s' % o0oOoO00 , 'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' % ( IiII1IiiIiI1 , iII1ii , II11I ) ) )
  III1ii . append ( ( OOoO % 'Save %s Data' % o0oOoO00 , 'RunPlugin(plugin://%s/?mode=save%s&name=%s)' % ( IiII1IiiIiI1 , iII1ii , II11I ) ) )
  III1ii . append ( ( OOoO % 'Restore %s Data' % o0oOoO00 , 'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % ( IiII1IiiIiI1 , iII1ii , II11I ) ) )
  III1ii . append ( ( OOoO % 'Import %s Data' % o0oOoO00 , 'RunPlugin(plugin://%s/?mode=import%s&name=%s)' % ( IiII1IiiIiI1 , iII1ii , II11I ) ) )
  III1ii . append ( ( OOoO % 'Clear Addon %s Data' % o0oOoO00 , 'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' % ( IiII1IiiIiI1 , iII1ii , II11I ) ) )
 elif type == 'install' :
  III1ii = [ ]
  II11I = urllib . quote_plus ( name )
  III1ii . append ( ( oooOo0OOOoo0 % name , 'RunAddon(%s, ?mode=viewbuild&name=%s)' % ( IiII1IiiIiI1 , II11I ) ) )
  III1ii . append ( ( OOoO % 'Fresh Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)' % ( IiII1IiiIiI1 , II11I ) ) )
  III1ii . append ( ( OOoO % 'Normal Install' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % ( IiII1IiiIiI1 , II11I ) ) )
  III1ii . append ( ( OOoO % 'Apply guiFix' , 'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)' % ( IiII1IiiIiI1 , II11I ) ) )
  III1ii . append ( ( OOoO % 'Build Information' , 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)' % ( IiII1IiiIiI1 , II11I ) ) )
 III1ii . append ( ( oooOo0OOOoo0 % '%s Settings' % o0OOO , 'RunPlugin(plugin://%s/?mode=settings)' % IiII1IiiIiI1 ) )
 return III1ii
 if 94 - 94: I1111 + i1Ii + OOoooooO
def OOoOooO00 ( state ) :
 o0o00OOOO = [ 'includevideo' , 'includeall' , 'includebob' , 'includephoenix' , 'includespecto' , 'includegenesis' , 'includeexodus' , 'includeonechan' , 'includesalts' , 'includesaltslite' ]
 i11iIi1iIIIIi = [ 'Include Video Addons' , 'Include All Addons' , 'Include Bob' , 'Include Phoenix' , 'Include Specto' , 'Include Genesis' , 'Include Exodus' , 'Include One Channel' , 'Include Salts' , 'Include Salts Lite HD' ]
 if state in [ 'true' , 'false' ] :
  for OoOo00o0OO in o0o00OOOO :
   wiz . setS ( OoOo00o0OO , state )
 else :
  if not state in [ 'includevideo' , 'includeall' ] and wiz . getS ( 'includeall' ) == 'true' :
   try :
    OoOo00o0OO = i11iIi1iIIIIi [ o0o00OOOO . index ( state ) ]
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o , OoOo00o0OO ) )
   except :
    wiz . LogNotify ( "[COLOR %s]Toggle Cache[/COLOR]" % oOOo0O00o , "[COLOR %s]Invalid id: %s[/COLOR]" % ( iIiIi11 , state ) )
  else :
   I1111iiiII1Ii = 'true' if wiz . getS ( state ) == 'false' else 'false'
   wiz . setS ( state , I1111iiiII1Ii )
   if 80 - 80: I1I1i1 % i1Ii
def iIi ( url ) :
 if 'watch?v=' in url :
  o0I1IIIi11ii11 , IiI1i111i = url . split ( '?' )
  iiiI1i1111II = IiI1i111i . split ( '&' )
  for OoOo00o0OO in iiiI1i1111II :
   if OoOo00o0OO . startswith ( 'v=' ) :
    url = OoOo00o0OO [ 2 : ]
    break
   else : continue
 elif 'embed' in url or 'youtu.be' in url :
  o0I1IIIi11ii11 = url . split ( '/' )
  if len ( o0I1IIIi11ii11 [ - 1 ] ) > 5 :
   url = o0I1IIIi11ii11 [ - 1 ]
  elif len ( o0I1IIIi11ii11 [ - 2 ] ) > 5 :
   url = o0I1IIIi11ii11 [ - 2 ]
 wiz . log ( "YouTube URL: %s" % url )
 yt . PlayVideo ( url )
 if 38 - 38: Ooo0O % oO0 - iiIIi1IiIi11 * iIii1I11I1II1 / O0
def I1iI11IiiI11i ( ) :
 IIIiIIIi11I = wiz . Grab_Log ( True )
 II1O0o00 = wiz . Grab_Log ( True , True )
 I1I1i1i = 0 ; Oo0oOO0O00 = IIIiIIIi11I
 if not II1O0o00 == False and not IIIiIIIi11I == False :
  I1I1i1i = iiIIIII1i1iI . select ( o0OOO , [ "View %s" % IIIiIIIi11I . replace ( iI11iiiI1II , "" ) , "View %s" % II1O0o00 . replace ( iI11iiiI1II , "" ) ] )
  if I1I1i1i == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
 elif IIIiIIIi11I == False and II1O0o00 == False :
  wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
  return
 elif not IIIiIIIi11I == False : I1I1i1i = 0
 elif not II1O0o00 == False : I1I1i1i = 1
 if 55 - 55: OOoooooO % Ooo0O % I1I1i1
 Oo0oOO0O00 = IIIiIIIi11I if I1I1i1i == 0 else II1O0o00
 I1IiO00Ooo0ooo0 = wiz . Grab_Log ( False ) if I1I1i1i == 0 else wiz . Grab_Log ( False , True )
 if 74 - 74: i11IiIiiIIIII
 wiz . TextBox ( "%s - %s" % ( o0OOO , Oo0oOO0O00 ) , I1IiO00Ooo0ooo0 )
 if 58 - 58: iIii1I11I1II1 * I1111 * OO00O0O0O00Oo * OOoooooO . OoooooooOO
def oo0o0ooooo ( log = None , count = None , all = None ) :
 if log == None :
  IIIiIIIi11I = wiz . Grab_Log ( True )
  II1O0o00 = wiz . Grab_Log ( True , True )
  if not II1O0o00 == False and not IIIiIIIi11I == False :
   I1I1i1i = iiIIIII1i1iI . select ( o0OOO , [ "View %s: %s error(s)" % ( IIIiIIIi11I . replace ( iI11iiiI1II , "" ) , oo0o0ooooo ( IIIiIIIi11I , True , True ) ) , "View %s: %s error(s)" % ( II1O0o00 . replace ( iI11iiiI1II , "" ) , oo0o0ooooo ( II1O0o00 , True , True ) ) ] )
   if I1I1i1i == - 1 : wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]View Log Cancelled![/COLOR]' % iIiIi11 ) ; return
  elif IIIiIIIi11I == False and II1O0o00 == False :
   wiz . LogNotify ( '[COLOR %s]View Log[/COLOR]' % oOOo0O00o , '[COLOR %s]No Log File Found![/COLOR]' % iIiIi11 )
   return
  elif not IIIiIIIi11I == False : I1I1i1i = 0
  elif not II1O0o00 == False : I1I1i1i = 1
  log = IIIiIIIi11I if I1I1i1i == 0 else II1O0o00
 if log == False :
  if count == None :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Log File not Found[/COLOR]" % iIiIi11 )
   return False
  else :
   return 0
 else :
  if os . path . exists ( log ) :
   i1IiII = open ( log , mode = 'r' ) ; o0I1IIIi11ii11 = i1IiII . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) ; i1IiII . close ( )
   o0O0Oo00 = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( o0I1IIIi11ii11 )
   if not count == None :
    if all == None :
     OooOOO = 0
     for OoOo00o0OO in o0O0Oo00 :
      if IiII1IiiIiI1 in OoOo00o0OO : OooOOO += 1
     return OooOOO
    else : return len ( o0O0Oo00 )
   if len ( o0O0Oo00 ) > 0 :
    OooOOO = 0 ; I1IiO00Ooo0ooo0 = ""
    for OoOo00o0OO in o0O0Oo00 :
     if all == None and not IiII1IiiIiI1 in OoOo00o0OO : continue
     else :
      OooOOO += 1
      I1IiO00Ooo0ooo0 += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % ( OooOOO , OoOo00o0OO . replace ( '                                          ' , '\n' ) . replace ( '\\\\' , '\\' ) . replace ( o00 , '' ) )
    if OooOOO > 0 :
     wiz . TextBox ( o0OOO , I1IiO00Ooo0ooo0 )
    else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
   else : wiz . LogNotify ( o0OOO , "No Errors Found in Log" )
  else : wiz . LogNotify ( o0OOO , "Log File not Found" )
  if 6 - 6: oO0 - IIIi1i1I * i11iIiiIii + o0o0Oo0oooo0 / OOoooooO % iii11iiII
II11IiIIiiI = 10
OOo0oOOOOoo0 = 92
ooOO0OOO00o = 1
OoOoO0ooooO0 = 2
IIII1ii1 = 3
OOO0O0OOo = 4
Iii1 = 104
OOoOi1IiiI = 105
O0OOO0 = 107
o0OIi = 7
IIi1iiI = 110
o0o = 100
oOO00OO0o0O = 108
if 35 - 35: I1I1i1 * iiIIi1IiIi11 - iIii1I11I1II1 + I1I1i1 . OoooooooOO
def ii111iI1i1 ( default = None ) :
 class ii111iI1i1 ( xbmcgui . WindowXMLDialog ) :
  def __init__ ( self , * args , ** kwargs ) :
   self . default = kwargs [ 'default' ]
   if 80 - 80: I1111 / i1Ii * ooOo % i1Ii
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . upload = 201
   self . kodi = 202
   self . kodiold = 203
   self . wizard = 204
   self . okbutton = 205
   i1IiII = open ( self . default , 'r' )
   self . logmsg = i1IiII . read ( )
   i1IiII . close ( )
   self . titlemsg = "%s: %s" % ( o0OOO , self . default . replace ( iI11iiiI1II , '' ) . replace ( o0 , '' ) )
   self . showdialog ( )
   if 95 - 95: O0 / i11IiIiiIIIII . OO00O0O0O00Oo
  def showdialog ( self ) :
   self . getControl ( self . title ) . setLabel ( self . titlemsg )
   self . getControl ( self . msg ) . setText ( wiz . highlightText ( self . logmsg ) )
   self . setFocusId ( self . scrollbar )
   if 17 - 17: i11IiIiiIIIII
  def onClick ( self , controlId ) :
   if controlId == self . okbutton : self . close ( )
   elif controlId == self . upload : self . close ( ) ; uploadLog . Main ( )
   elif controlId == self . kodi :
    o0OO0OO000OO = wiz . Grab_Log ( False )
    O00o0000OO = wiz . Grab_Log ( True )
    if o0OO0OO000OO == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , O00o0000OO . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( o0OO0OO000OO ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . kodiold :
    o0OO0OO000OO = wiz . Grab_Log ( False , True )
    O00o0000OO = wiz . Grab_Log ( True , True )
    if o0OO0OO000OO == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , O00o0000OO . replace ( iI11iiiI1II , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( o0OO0OO000OO ) )
     self . setFocusId ( self . scrollbar )
   elif controlId == self . wizard :
    o0OO0OO000OO = wiz . Grab_Log ( False , False , True )
    O00o0000OO = wiz . Grab_Log ( True , False , True )
    if o0OO0OO000OO == False :
     self . titlemsg = "%s: View Log Error" % o0OOO
     self . getControl ( self . msg ) . setText ( "Log File Does Not Exists!" )
    else :
     self . titlemsg = "%s: %s" % ( o0OOO , O00o0000OO . replace ( o0 , '' ) )
     self . getControl ( self . title ) . setLabel ( self . titlemsg )
     self . getControl ( self . msg ) . setText ( wiz . highlightText ( o0OO0OO000OO ) )
     self . setFocusId ( self . scrollbar )
     if 61 - 61: i1Ii % i1IIi - iiIIi1IiIi11 . OOoooooO - Ooo0O + Ooo0O
  def onAction ( self , action ) :
   if action == II11IiIIiiI : self . close ( )
   elif action == OOo0oOOOOoo0 : self . close ( )
 if default == None : default = wiz . Grab_Log ( True )
 II1ii1Ii = ii111iI1i1 ( "LogViewer.xml" , I1ii11iIi11i . getAddonInfo ( 'path' ) , 'DefaultSkin' , default = default )
 II1ii1Ii . doModal ( )
 del II1ii1Ii
 if 31 - 31: iiIIi1IiIi11 - o0o0Oo0oooo0 . o0o0Oo0oooo0 - IIIi1i1I + Ooo0O / i11iIiiIii
def IIIiiiIiI ( addon , name , over = False ) :
 if not over == False :
  o00o = 1
 else :
  o00o = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Are you sure you want to delete the addon:' % iIiIi11 , 'Name: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , name ) , 'ID: [COLOR %s]%s[/COLOR][/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR white]Remove Addon[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' )
 if o00o == 1 :
  ooooOoo0OO = os . path . join ( O0O , addon )
  wiz . log ( "Removing Addon %s" % addon )
  wiz . cleanHouse ( ooooOoo0OO )
  xbmc . sleep ( 200 )
  try : shutil . rmtree ( ooooOoo0OO )
  except Exception , i1OoOO : wiz . log ( "Error removing %s" % addon , xbmc . LOGNOTICE )
  o0ooOo00O ( addon , name , over )
 if over == False :
  wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]%s Removed[/COLOR]" % ( iIiIi11 , name ) )
  if 90 - 90: iIii1I11I1II1 + o0o0Oo0oooo0
def o0ooOo00O ( addon , name = None , over = False ) :
 if addon == 'all' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR white]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   wiz . cleanHouse ( ooOOOo0oo0O0 )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'uninstalled' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] addon data stored in you Userdata folder for uninstalled addons?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR white]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   O0oOoo0o000O0 = 0
   for ooooOoo0OO in glob . glob ( os . path . join ( ooOOOo0oo0O0 , '*' ) ) :
    Oo0O0000Oo00o = ooooOoo0OO . replace ( ooOOOo0oo0O0 , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
    if Oo0O0000Oo00o in Iii1I1I11iiI1 : pass
    elif os . path . exists ( os . path . join ( O0O , Oo0O0000Oo00o ) ) : pass
    else : wiz . cleanHouse ( ooooOoo0OO ) ; O0oOoo0o000O0 += 1 ; wiz . log ( ooooOoo0OO ) ; shutil . rmtree ( ooooOoo0OO )
   wiz . LogNotify ( '[COLOR %s]Clean up Uninstalled[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , O0oOoo0o000O0 ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Addon Data[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 elif addon == 'empty' :
  if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to remove [COLOR %s]ALL[/COLOR] empty addon data folders in you Userdata folder?[/COLOR]' % ( iIiIi11 , oOOo0O00o ) , yeslabel = '[B][COLOR white]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
   O0oOoo0o000O0 = wiz . emptyfolder ( ooOOOo0oo0O0 )
   wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]%s Folders(s) Removed[/COLOR]' % ( iIiIi11 , O0oOoo0o000O0 ) )
  else : wiz . LogNotify ( '[COLOR %s]Remove Empty Folders[/COLOR]' % oOOo0O00o , '[COLOR %s]Cancelled![/COLOR]' % iIiIi11 )
 else :
  IiIIIiI = os . path . join ( oOo00Oo00O , 'addon_data' , addon )
  if addon in Iii1I1I11iiI1 :
   wiz . LogNotify ( "[COLOR %s]Protected Plugin[/COLOR]" % oOOo0O00o , "[COLOR %s]Not allowed to remove Addon_Data[/COLOR]" % iIiIi11 )
  elif os . path . exists ( IiIIIiI ) :
   if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you also like to remove the addon data for:[/COLOR]' % iIiIi11 , '[COLOR %s]%s[/COLOR]' % ( oOOo0O00o , addon ) , yeslabel = '[B][COLOR white]Remove Data[/COLOR][/B]' , nolabel = '[B][COLOR red]Don\'t Remove[/COLOR][/B]' ) :
    wiz . cleanHouse ( IiIIIiI )
    try :
     shutil . rmtree ( IiIIIiI )
    except :
     wiz . log ( "Error deleting: %s" % IiIIIiI )
   else :
    wiz . log ( 'Addon data for %s was not removed' % addon )
 wiz . refresh ( )
 if 19 - 19: I1111 . OoooooooOO * I1111 + i1Ii + OoooooooOO
def i11iiI ( type ) :
 if type == 'build' :
  OooOOO = O0oO00oOOooO ( 'restore' )
  if OooOOO == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Local Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
  wiz . skinToDefault ( )
 wiz . restoreLocal ( type )
 if 67 - 67: oO0 + IiiIII111ii
def o0O00OooooO ( type ) :
 if type == 'build' :
  OooOOO = O0oO00oOOooO ( 'restore' )
  if OooOOO == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]External Restore Cancelled[/COLOR]" % iIiIi11 ) ; return
 wiz . restoreExternal ( type )
 if 77 - 77: ooOo % OOoooooO
def oO0oo ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  if wiz . checkBuild ( name , 'url' ) :
   name , O0OOO0OOooo00 , oO0o00oOOooO0 , OOOoO000 , oOOOO , Ii , Ii1ii111i1 , i1i1i1I , ii1iii1I1I , oOoo000 , OooOo00o , IiI11i1IIiiI = wiz . checkBuild ( name , 'all' )
   oOoo000 = 'Yes' if oOoo000 . lower ( ) == 'yes' else 'No'
   I1IiO00Ooo0ooo0 = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , name )
   I1IiO00Ooo0ooo0 += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , O0OOO0OOooo00 )
   if not Ii == "http://" :
    o00o0o000Oo = wiz . themeCount ( name , False )
    I1IiO00Ooo0ooo0 += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , ', ' . join ( o00o0o000Oo ) )
   I1IiO00Ooo0ooo0 += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , oOOOO )
   I1IiO00Ooo0ooo0 += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , oOoo000 )
   I1IiO00Ooo0ooo0 += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % ( iIiIi11 , oOOo0O00o , OooOo00o )
   wiz . TextBox ( o0OOO , I1IiO00Ooo0ooo0 )
  else : wiz . log ( "Invalid Build Name!" )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 100 - 100: i1IIi - i11iIiiIii . OO00O0O0O00Oo * I1111
def oOIIII ( name ) :
 if wiz . workingURL ( I1I1i1I ) == True :
  ooOOo = wiz . checkBuild ( name , 'preview' )
  if ooOOo and not ooOOo == 'http://' : iIi ( ooOOo )
  else : wiz . log ( "[%s]Unable to find url for video preview" % name )
 else : wiz . log ( "Build text file not working: %s" % WORKINGURL )
 if 5 - 5: O0
def o0oo0Oo ( plugin ) :
 iI1i = os . path . join ( O0O , plugin , 'addon.xml' )
 if os . path . exists ( iI1i ) :
  I1iIiiiI1 = open ( iI1i , mode = 'r' ) ; i1oO0OO0 = I1iIiiiI1 . read ( ) ; I1iIiiiI1 . close ( ) ;
  o0O0Oo00 = wiz . parseDOM ( i1oO0OO0 , 'import' , ret = 'addon' )
  i1i1I1II = [ ]
  for I1iIII1IiiI in o0O0Oo00 :
   if not 'xbmc.python' in I1iIII1IiiI :
    i1i1I1II . append ( I1iIII1IiiI )
  return i1i1I1II
 return [ ]
 if 66 - 66: i1Ii + iIii1I11I1II1
def o0Oo00oOO ( do ) :
 if do == 'import' :
  O0oo = os . path . join ( o0 , 'temp' )
  if not os . path . exists ( O0oo ) : os . makedirs ( O0oo )
  I1iIiiiI1 = iiIIIII1i1iI . browse ( 1 , '[COLOR %s]Select the location of the SaveData.zip[/COLOR]' % iIiIi11 , 'files' , '.zip' , False , False , o00 )
  if not I1iIiiiI1 . endswith ( '.zip' ) :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Import Data Error![/COLOR]" % ( iIiIi11 ) )
   return
  o0000O00oO0O = os . path . join ( O0ooO0Oo00o , 'SaveData.zip' )
  i11I = xbmcvfs . copy ( I1iIiiiI1 , o0000O00oO0O )
  wiz . log ( "%s" % str ( i11I ) )
  extract . all ( xbmc . translatePath ( o0000O00oO0O ) , O0oo )
  o0oo0 = os . path . join ( O0oo , 'trakt' )
  oO00O = os . path . join ( O0oo , 'login' )
  II1IiiIII = os . path . join ( O0oo , 'debrid' )
  OooOOO = 0
  if os . path . exists ( o0oo0 ) :
   OooOOO += 1
   IiiI111I11 = os . listdir ( o0oo0 )
   if not os . path . exists ( traktit . TRAKTFOLD ) : os . makedirs ( traktit . TRAKTFOLD )
   for OoOo00o0OO in IiiI111I11 :
    oO0Ooooo000 = os . path . join ( traktit . TRAKTFOLD , OoOo00o0OO )
    I1ii1i11i = os . path . join ( o0oo0 , OoOo00o0OO )
    if os . path . exists ( oO0Ooooo000 ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , OoOo00o0OO ) , yeslabel = "[B][COLOR white]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( oO0Ooooo000 )
    shutil . copy ( I1ii1i11i , oO0Ooooo000 )
   traktit . importlist ( 'all' )
   traktit . traktIt ( 'restore' , 'all' )
  if os . path . exists ( oO00O ) :
   OooOOO += 1
   IiiI111I11 = os . listdir ( oO00O )
   if not os . path . exists ( loginit . LOGINFOLD ) : os . makedirs ( loginit . LOGINFOLD )
   for OoOo00o0OO in IiiI111I11 :
    oO0Ooooo000 = os . path . join ( loginit . LOGINFOLD , OoOo00o0OO )
    I1ii1i11i = os . path . join ( oO00O , OoOo00o0OO )
    if os . path . exists ( oO0Ooooo000 ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , OoOo00o0OO ) , yeslabel = "[B][COLOR white]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( oO0Ooooo000 )
    shutil . copy ( I1ii1i11i , oO0Ooooo000 )
   loginit . importlist ( 'all' )
   loginit . loginIt ( 'restore' , 'all' )
  if os . path . exists ( II1IiiIII ) :
   OooOOO += 1
   IiiI111I11 = os . listdir ( II1IiiIII )
   if not os . path . exists ( debridit . REALFOLD ) : os . makedirs ( debridit . REALFOLD )
   for OoOo00o0OO in IiiI111I11 :
    oO0Ooooo000 = os . path . join ( debridit . REALFOLD , OoOo00o0OO )
    I1ii1i11i = os . path . join ( II1IiiIII , OoOo00o0OO )
    if os . path . exists ( oO0Ooooo000 ) :
     if not iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % ( iIiIi11 , oOOo0O00o , OoOo00o0OO ) , yeslabel = "[B][COLOR white]Yes Replace[/COLOR][/B]" , nolabel = "[B][COLOR red]No Skip[/COLOR][/B]" ) : continue
     else : os . remove ( oO0Ooooo000 )
    shutil . copy ( I1ii1i11i , oO0Ooooo000 )
   debridit . importlist ( 'all' )
   debridit . debridIt ( 'restore' , 'all' )
  wiz . cleanHouse ( O0oo )
  wiz . removeFolder ( O0oo )
  os . remove ( o0000O00oO0O )
  if OooOOO == 0 : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Failed[/COLOR]" % iIiIi11 )
  else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Save Data Import Complete[/COLOR]" % iIiIi11 )
 elif do == 'export' :
  Iii1Iiii = xbmc . translatePath ( O0ooO0Oo00o )
  dir = [ traktit . TRAKTFOLD , debridit . REALFOLD , loginit . LOGINFOLD ]
  traktit . traktIt ( 'update' , 'all' )
  loginit . loginIt ( 'update' , 'all' )
  debridit . debridIt ( 'update' , 'all' )
  I1iIiiiI1 = iiIIIII1i1iI . browse ( 3 , '[COLOR %s]Select where you wish to export the savedata zip?[/COLOR]' % iIiIi11 , 'files' , '' , False , True , o00 )
  I1iIiiiI1 = xbmc . translatePath ( I1iIiiiI1 )
  i1i1Ii1IiIII = os . path . join ( Iii1Iiii , 'SaveData.zip' )
  I1IIii11 = zipfile . ZipFile ( i1i1Ii1IiIII , mode = 'w' )
  for IIii1III in dir :
   if os . path . exists ( IIii1III ) :
    IiiI111I11 = os . listdir ( IIii1III )
    for file in IiiI111I11 :
     I1IIii11 . write ( os . path . join ( IIii1III , file ) , os . path . join ( IIii1III , file ) . replace ( o0 , '' ) , zipfile . ZIP_DEFLATED )
  I1IIii11 . close ( )
  if I1iIiiiI1 == Iii1Iiii :
   iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , i1i1Ii1IiIII ) )
  else :
   try :
    xbmcvfs . copy ( i1i1Ii1IiIII , os . path . join ( I1iIiiiI1 , 'SaveData.zip' ) )
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , os . path . join ( I1iIiiiI1 , 'SaveData.zip' ) ) )
   except :
    iiIIIII1i1iI . ok ( o0OOO , "[COLOR %s]Save data has been backed up to:[/COLOR]" % ( iIiIi11 ) , "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , i1i1Ii1IiIII ) )
    if 22 - 22: OOoooooO / OOoooooO - IiiIII111ii % i11IiIiiIIIII . iii11iiII + i1Ii
def Oo0000O0OOooO ( url ) :
 iIi1I1 = urllib2 . Request ( url )
 iIi1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0oOoo0OoO0O = urllib2 . urlopen ( iIi1I1 )
 i1oO0OO0 = O0oOoo0OoO0O . read ( )
 O0oOoo0OoO0O . close ( )
 return i1oO0OO0
 if 64 - 64: i1IIi % oO0 / IiiIII111ii % OoooooooOO
def I1iii1 ( url ) :
 if url == 'http://' : return False
 try :
  iIi1I1 = urllib2 . Request ( url )
  iIi1I1 . add_header ( 'User-Agent' , USER_AGENT )
  O0oOoo0OoO0O = urllib2 . urlopen ( iIi1I1 )
  O0oOoo0OoO0O . close ( )
 except Exception , i1OoOO :
  return i1OoOO
 return True
 if 19 - 19: IIIi1i1I % OoooooooOO . OoooooooOO
 if 40 - 40: O0 . OO00O0O0O00Oo / iIii1I11I1II1 * I1I1i1
 if 73 - 73: Ooo0O - iiIIi1IiIi11 . IIIi1i1I % i1IIi . O0
 if 15 - 15: OOoooooO . iIii1I11I1II1 * ooOo % i11IiIiiIIIII
def O0oO00oOOooO ( install = None , over = False ) :
 if o0O0OOO0Ooo == 'true' :
  traktit . autoUpdate ( 'all' )
  wiz . setS ( 'traktlastsave' , str ( I1IiiiiI ) )
 if iiIiII1 == 'true' :
  debridit . autoUpdate ( 'all' )
  wiz . setS ( 'debridlastsave' , str ( I1IiiiiI ) )
 if OOO00O0O == 'true' :
  loginit . autoUpdate ( 'all' )
  wiz . setS ( 'loginlastsave' , str ( I1IiiiiI ) )
 if over == True : ii1IiiII = 1
 elif install == 'restore' : ii1IiiII = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing the local backup?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR white]Continue[/COLOR][/B]' )
 elif install : ii1IiiII = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings" , "Before installing [COLOR %s]%s[/COLOR]?" % ( oOOo0O00o , install ) , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR white]Continue[/COLOR][/B]' )
 else : ii1IiiII = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Do you wish to restore your" % iIiIi11 , "Kodi configuration to default settings?[/COLOR]" , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR white]Continue[/COLOR][/B]' )
 if ii1IiiII :
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   OOooo000OooO = 'skin.confluence' if o0OIiII < 17 else 'skin.estuary'
   if 21 - 21: I1111 - ooOo . OoooooooOO
   if 6 - 6: iIii1I11I1II1 - iIii1I11I1II1 % I1I1i1 / iIii1I11I1II1 * OO00O0O0O00Oo
   skinSwitch . swapSkins ( OOooo000OooO )
   OooOOO = 0
   xbmc . sleep ( 1000 )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) and OooOOO < 150 :
    OooOOO += 1
    xbmc . sleep ( 200 )
    wiz . ebi ( 'SendAction(Select)' )
   if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
    wiz . ebi ( 'SendClick(11)' )
   else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Skin Swap Timed Out![/COLOR]' % iIiIi11 ) ; return False
   xbmc . sleep ( 1000 )
  if not wiz . currSkin ( ) in [ 'skin.confluence' , 'skin.estuary' ] :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Skin Swap Failed![/COLOR]' % iIiIi11 )
   return
  wiz . addonUpdates ( 'set' )
  iIio0oooo0OOo00 = os . path . abspath ( o00 )
  oo00 . create ( o0OOO , "[COLOR %s]Calculating files and folders" % iIiIi11 , '' , 'Please Wait![/COLOR]' )
  OOO0 = sum ( [ len ( IiiI111I11 ) for I1Ii1 , O0oo0oOoO00 , IiiI111I11 in os . walk ( iIio0oooo0OOo00 ) ] ) ; i1ii1iIi = 0
  oo00 . update ( 0 , "[COLOR %s]Gathering Excludes list." % iIiIi11 )
  Iii1I1I11iiI1 . append ( 'My_Builds' )
  Iii1I1I11iiI1 . append ( 'archive_cache' )
  if IIII == 'true' :
   I1iIiiiI1OOO0O00Oo = glob . glob ( os . path . join ( O0O , 'repo*/' ) )
   for OoOo00o0OO in I1iIiiiI1OOO0O00Oo :
    I1I1Ii = os . path . split ( OoOo00o0OO [ : - 1 ] ) [ 1 ]
    if not I1I1Ii == Iii1I1I11iiI1 :
     Iii1I1I11iiI1 . append ( I1I1Ii )
  if iiIiI == 'true' :
   Iii1I1I11iiI1 . append ( 'plugin.program.super.favourites' )
  if o00oooO0Oo == 'true' :
   iI1IIII1 = ''
   i111IiiI1Ii = wiz . whiteList ( 'read' )
   if len ( i111IiiI1Ii ) > 0 :
    for OoOo00o0OO in i111IiiI1Ii :
     try : O0Oo0o000oO , id , IIii1III = OoOo00o0OO
     except : pass
     if IIii1III . startswith ( 'pvr' ) : iI1IIII1 = id
     I1iIII1IiiI = o0oo0Oo ( IIii1III )
     for Oo0o in I1iIII1IiiI :
      if not Oo0o in Iii1I1I11iiI1 :
       Iii1I1I11iiI1 . append ( Oo0o )
      OoO000oo000o0 = o0oo0Oo ( Oo0o )
      for i1Ii1I1Ii11iI in OoO000oo000o0 :
       if not i1Ii1I1Ii11iI in Iii1I1I11iiI1 :
        Iii1I1I11iiI1 . append ( i1Ii1I1Ii11iI )
     if not IIii1III in Iii1I1I11iiI1 :
      Iii1I1I11iiI1 . append ( IIii1III )
    if not iI1IIII1 == '' : wiz . setS ( 'pvrclient' , IIii1III )
  if wiz . getS ( 'pvrclient' ) == '' :
   for OoOo00o0OO in Iii1I1I11iiI1 :
    if OoOo00o0OO . startswith ( 'pvr' ) :
     wiz . setS ( 'pvrclient' , OoOo00o0OO )
  oo00 . update ( 0 , "[COLOR %s]Clearing out files and folders:" % iIiIi11 )
  i1ii111i = wiz . latestDB ( 'Addons' )
  for i1ii1i1Ii11 , O0O0Oo0O0oo , IiiI111I11 in os . walk ( iIio0oooo0OOo00 , topdown = True ) :
   O0O0Oo0O0oo [ : ] = [ O0oo0oOoO00 for O0oo0oOoO00 in O0O0Oo0O0oo if O0oo0oOoO00 not in Iii1I1I11iiI1 ]
   for O0Oo0o000oO in IiiI111I11 :
    i1ii1iIi += 1
    IIii1III = i1ii1i1Ii11 . replace ( '/' , '\\' ) . split ( '\\' )
    OooOOO = len ( IIii1III ) - 1
    if O0Oo0o000oO == 'sources.xml' and IIii1III [ - 1 ] == 'userdata' and ooOOoooooo == 'true' : wiz . log ( "Keep Sources: %s" % os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
    elif O0Oo0o000oO == 'favourites.xml' and IIii1III [ - 1 ] == 'userdata' and IiIIIi1iIi == 'true' : wiz . log ( "Keep Favourites: %s" % os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
    elif O0Oo0o000oO == 'profiles.xml' and IIii1III [ - 1 ] == 'userdata' and II1I == 'true' : wiz . log ( "Keep Profiles: %s" % os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
    elif O0Oo0o000oO == 'advancedsettings.xml' and IIii1III [ - 1 ] == 'userdata' and O0i1II1Iiii1I11 == 'true' : wiz . log ( "Keep Advanced Settings: %s" % os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
    elif O0Oo0o000oO in Ooo0oOooo0 : wiz . log ( "Keep Log File: %s" % O0Oo0o000oO , xbmc . LOGNOTICE )
    elif O0Oo0o000oO . endswith ( '.db' ) :
     try :
      if O0Oo0o000oO == i1ii111i and o0OIiII >= 17 : wiz . log ( "Ignoring %s on v%s" % ( O0Oo0o000oO , o0OIiII ) , xbmc . LOGNOTICE )
      else : os . remove ( os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) )
     except Exception , i1OoOO :
      if not O0Oo0o000oO . startswith ( 'Textures13' ) :
       wiz . log ( 'Failed to delete, Purging DB' , xbmc . LOGNOTICE )
       wiz . log ( "-> %s" % ( str ( i1OoOO ) ) , xbmc . LOGNOTICE )
       wiz . purgeDb ( os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) )
    else :
     oo00 . update ( int ( wiz . percentage ( i1ii1iIi , OOO0 ) ) , '' , '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % ( iIiIi11 , oOOo0O00o , O0Oo0o000oO ) , '' )
     try : os . remove ( os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) )
     except Exception , i1OoOO :
      wiz . log ( "Error removing %s" % os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) , xbmc . LOGNOTICE )
      wiz . log ( "-> / %s" % ( str ( i1OoOO ) ) , xbmc . LOGNOTICE )
   if oo00 . iscanceled ( ) :
    oo00 . close ( )
    wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Fresh Start Cancelled[/COLOR]" % iIiIi11 )
    return False
  for i1ii1i1Ii11 , O0O0Oo0O0oo , IiiI111I11 in os . walk ( iIio0oooo0OOo00 , topdown = True ) :
   O0O0Oo0O0oo [ : ] = [ O0oo0oOoO00 for O0oo0oOoO00 in O0O0Oo0O0oo if O0oo0oOoO00 not in Iii1I1I11iiI1 ]
   for O0Oo0o000oO in O0O0Oo0O0oo :
    oo00 . update ( 100 , '' , 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % ( oOOo0O00o , O0Oo0o000oO ) , '' )
    if O0Oo0o000oO not in [ "Database" , "userdata" , "temp" , "addons" , "addon_data" ] :
     shutil . rmtree ( os . path . join ( i1ii1i1Ii11 , O0Oo0o000oO ) , ignore_errors = True , onerror = None )
   if oo00 . iscanceled ( ) :
    oo00 . close ( )
    wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Fresh Start Cancelled[/COLOR]" % iIiIi11 )
    return False
  oo00 . close ( )
  wiz . clearS ( 'build' )
  if over == True :
   return True
  elif install == 'restore' :
   return True
  elif install :
   Oooooooo00o00 ( install , 'normal' , over = True )
  else :
   if I11i1I1I == 1 : OOOO00OoooO = 1
   elif I11i1I1I == 2 : OOOO00OoooO = 0
   else : OOOO00OoooO = iiIIIII1i1iI . yesno ( o0OOO , "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % ( iIiIi11 , oOOo0O00o , oOOo0O00o ) , yeslabel = "[B][COLOR red]Reload Profile[/COLOR][/B]" , nolabel = "[B][COLOR white]Force Close[/COLOR][/B]" )
   if OOOO00OoooO == 1 : wiz . reloadFix ( 'fresh' )
   else : wiz . addonUpdates ( 'reset' ) ; wiz . killxbmc ( True )
 else :
  if not install == 'restore' :
   wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , '[COLOR %s]Fresh Install: Cancelled![/COLOR]' % iIiIi11 )
   wiz . refresh ( )
   if 62 - 62: i11IiIiiIIIII / oO0
   if 85 - 85: ooOo + iiIIi1IiIi11 - iiIIi1IiIi11 . OoooooooOO - iIii1I11I1II1
   if 8 - 8: i11iIiiIii * I1I1i1 / oO0 . IiiIII111ii
   if 31 - 31: i11iIiiIii - OOoooooO / oO0 - IiiIII111ii
def iiIiIi1111iI1 ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]No, Cancel[/COLOR][/B]' , yeslabel = '[B][COLOR white]Clear Cache[/COLOR][/B]' ) :
  wiz . clearCache ( )
  if 11 - 11: oO0 . oO0 + II111iiii * o0o0Oo0oooo0 . i1Ii
  if 10 - 10: iiIIi1IiIi11 * IiiIII111ii - OOoooooO . i11IiIiiIIIII - iii11iiII
def oOO0O00OoOo ( ) :
 if iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to clear cache, packages and thumbnails?[/COLOR]' % iIiIi11 , nolabel = '[B][COLOR red]Cancel Process[/COLOR][/B]' , yeslabel = '[B][COLOR white]Clean All[/COLOR][/B]' ) :
  wiz . clearCache ( )
  wiz . clearPackages ( 'total' )
  I1i1I11 ( 'total' )
  if 9 - 9: ooOo
def I1i1I11 ( type = None ) :
 oOoo0 = wiz . latestDB ( 'Textures' )
 if not type == None : O0OOOOOoo = 1
 else : O0OOOOOoo = iiIIIII1i1iI . yesno ( o0OOO , '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % ( iIiIi11 , oOoo0 ) , "They will repopulate on the next startup[/COLOR]" , nolabel = '[B][COLOR red]Don\'t Delete[/COLOR][/B]' , yeslabel = '[B][COLOR white]Delete Thumbs[/COLOR][/B]' )
 if O0OOOOOoo == 1 :
  try : wiz . removeFile ( os . join ( OOOO , oOoo0 ) )
  except : wiz . log ( 'Failed to delete, Purging DB.' ) ; wiz . purgeDb ( oOoo0 )
  wiz . removeFolder ( oOoOooOo0o0 )
  if 26 - 26: i1Ii / iIii1I11I1II1 - iIii1I11I1II1
 else : wiz . log ( 'Clear thumbnames cancelled' )
 wiz . redoThumbs ( )
 if 57 - 57: i1Ii
def IiI11I1Ii11II ( ) :
 oo0ooOoOOoO = [ ] ; ii1iiIi = [ ]
 for Oo0000o , iI1IiiiIIiiII , IiiI111I11 in os . walk ( o00 ) :
  for i1IiII in fnmatch . filter ( IiiI111I11 , '*.db' ) :
   if i1IiII != 'Thumbs.db' :
    oOo000o = os . path . join ( Oo0000o , i1IiII )
    oo0ooOoOOoO . append ( oOo000o )
    dir = oOo000o . replace ( '\\' , '/' ) . split ( '/' )
    ii1iiIi . append ( '(%s) %s' % ( dir [ len ( dir ) - 2 ] , dir [ len ( dir ) - 1 ] ) )
 if o0OIiII >= 16 :
  O0OOOOOoo = iiIIIII1i1iI . multiselect ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , ii1iiIi )
  if O0OOOOOoo == None : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  elif len ( O0OOOOOoo ) == 0 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else :
   for oOII1i1i1I1iII in O0OOOOOoo : wiz . purgeDb ( oo0ooOoOOoO [ oOII1i1i1I1iII ] )
 else :
  O0OOOOOoo = iiIIIII1i1iI . select ( "[COLOR %s]Select DB File to Purge[/COLOR]" % iIiIi11 , ii1iiIi )
  if O0OOOOOoo == - 1 : wiz . LogNotify ( "[COLOR %s]Purge Database[/COLOR]" % oOOo0O00o , "[COLOR %s]Cancelled[/COLOR]" % iIiIi11 )
  else : wiz . purgeDb ( oo0ooOoOOoO [ oOII1i1i1I1iII ] )
  if 48 - 48: iii11iiII . iii11iiII + i11iIiiIii + oO0 % O0
  if 67 - 67: OOoooooO / i11IiIiiIIIII * ooOo % OoooooooOO
  if 46 - 46: i1Ii
  if 12 - 12: I1I1i1 + o0o0Oo0oooo0 . iIii1I11I1II1 % OOoooooO + i1IIi . OOoooooO
def III ( ) :
 oO0o00oOOooO0 = wiz . workingURL ( O0O0OOOOoo )
 if oO0o00oOOooO0 == True :
  try :
   id , I1IiO00Ooo0ooo0 = wiz . splitNotify ( O0O0OOOOoo )
   if id == False : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Notification: Not Formated Correctly[/COLOR]" % iIiIi11 ) ; return
   notify . notification ( I1IiO00Ooo0ooo0 , True )
  except Exception , i1OoOO :
   wiz . log ( "Error on Notifications Window: %s" % str ( i1OoOO ) , xbmc . LOGERROR )
 else : wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Invalid URL for Notification[/COLOR]" % iIiIi11 )
 if 96 - 96: i11iIiiIii - i11iIiiIii % I1I1i1 * iii11iiII * o0o0Oo0oooo0 - I1111
def I1iiIiII ( ) :
 if O000oo0O == "" :
  notify . updateWindow ( )
 else :
  notify . updateWindow ( O000oo0O , oo0OooOOo0 , O00oO , wiz . checkBuild ( O000oo0O , 'icon' ) , wiz . checkBuild ( O000oo0O , 'fanart' ) )
  if 39 - 39: I1111 % IIIi1i1I / i1Ii * iiIIi1IiIi11 * IIIi1i1I . IIIi1i1I
def i1iIIiiIiII ( ) :
 notify . firstRun ( )
 if 20 - 20: OOoooooO . I1111 * iiIIi1IiIi11
def OOii11Ii1IiiI1 ( ) :
 notify . firstRunSettings ( )
 if 83 - 83: OOoooooO + i1IIi * OoooooooOO * IIIi1i1I
 if 83 - 83: iIii1I11I1II1 - OOoooooO - OO00O0O0O00Oo / I1111 - O0
 if 81 - 81: IiiIII111ii - IIIi1i1I * oO0 / OO00O0O0O00Oo
 if 21 - 21: I1111
 if 63 - 63: i11IiIiiIIIII . O0 * i11IiIiiIIIII + iIii1I11I1II1
def Ii1iIi ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 OOo0OOOoOOo = sys . argv [ 0 ]
 if not mode == None : OOo0OOOoOOo += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OOo0OOOoOOo += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOo0OOOoOOo += "&url=" + urllib . quote_plus ( url )
 IIIooo0o0O = True
 if themeit : display = themeit % display
 IiiiIIi11II = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : IiiiIIi11II . addContextMenuItems ( menu , replaceItems = overwrite )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = True )
 return IIIooo0o0O
 if 55 - 55: i11IiIiiIIIII
def ooooooo00oO0OO ( name , url , mode , iconimage , fanart , description ) :
 if 30 - 30: I1I1i1 + OoooooooOO + iii11iiII / II111iiii * Ooo0O
 OOo0OOOoOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIooo0o0O = True
 IiiiIIi11II = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = False )
 if 59 - 59: IiiIII111ii / o0o0Oo0oooo0 * I1111 * iiIIi1IiIi11 % IIIi1i1I
def oo00O00oO000o ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 OOo0OOOoOOo = sys . argv [ 0 ]
 if not mode == None : OOo0OOOoOOo += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OOo0OOOoOOo += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOo0OOOoOOo += "&url=" + urllib . quote_plus ( url )
 IIIooo0o0O = True
 if themeit : display = themeit % display
 IiiiIIi11II = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : IiiiIIi11II . addContextMenuItems ( menu , replaceItems = overwrite )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = True )
 return IIIooo0o0O
 if 61 - 61: Ooo0O - O0 - OoooooooOO
def iiiii1II ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 OOo0OOOoOOo = sys . argv [ 0 ]
 if not mode == None : OOo0OOOoOOo += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OOo0OOOoOOo += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOo0OOOoOOo += "&url=" + urllib . quote_plus ( url )
 IIIooo0o0O = True
 if themeit : display = themeit % display
 IiiiIIi11II = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : IiiiIIi11II . addContextMenuItems ( menu , replaceItems = overwrite )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = False )
 return IIIooo0o0O
 if 4 - 4: II111iiii - IIIi1i1I % Ooo0O * i11iIiiIii
def Oo0 ( name , url , mode , iconimage ) :
 OOo0OOOoOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 IIIooo0o0O = True
 IiiiIIi11II = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : name } )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = True )
 return IIIooo0o0O
 if 18 - 18: Ooo0O % O0
def iIi1i ( name , url , mode , iconimage , fanart , description , installRating ) :
 OOo0OOOoOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&installRating=" + urllib . quote_plus ( installRating )
 IIIooo0o0O = True
 IiiiIIi11II = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Premiered" : installRating } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = False )
 return IIIooo0o0O
 if 66 - 66: iIii1I11I1II1 % i11iIiiIii / ooOo
def IIIIIiiI11i1 ( display , mode = None , name = None , url = None , menu = None , description = o0OOO , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , themeit = None ) :
 OOo0OOOoOOo = sys . argv [ 0 ]
 if not mode == None : OOo0OOOoOOo += "?mode=%s" % urllib . quote_plus ( mode )
 if not name == None : OOo0OOOoOOo += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOo0OOOoOOo += "&url=" + urllib . quote_plus ( url )
 IIIooo0o0O = True
 if themeit : display = themeit % display
 IiiiIIi11II = xbmcgui . ListItem ( display , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : display , "Plot" : description } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : IiiiIIi11II . addContextMenuItems ( menu , replaceItems = overwrite )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = False )
 return IIIooo0o0O
 if 43 - 43: ooOo / iiIIi1IiIi11 / OOoooooO + iIii1I11I1II1 + OoooooooOO
def oOo0O ( display , mode , name = None , url = None , menu = None , overwrite = True , fanart = OOO00 , icon = iiiiiIIii , description = None , themeit = None ) :
 OOo0OOOoOOo = '%s?mode=%s' % ( sys . argv [ 0 ] , urllib . quote_plus ( mode ) )
 if not name == None : OOo0OOOoOOo += "&name=" + urllib . quote_plus ( name )
 if not url == None : OOo0OOOoOOo += "&url=" + urllib . quote_plus ( url )
 if not description == None : OOo0OOOoOOo += "&description=" + urllib . quote_plus ( description )
 IIIooo0o0O = True
 if themeit : display = themeit % display
 IiiiIIi11II = xbmcgui . ListItem ( description , iconImage = "DefaultFolder.png" , thumbnailImage = icon )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : description , "Plot" : o0OOO } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 if not menu == None : IiiiIIi11II . addContextMenuItems ( menu , replaceItems = overwrite )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = False )
 return IIIooo0o0O
 if 33 - 33: II111iiii - i1Ii - OOoooooO
def oO00oOoo00o0 ( name , url , mode , iconimage , fanart , description ) :
 OOo0OOOoOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 IIIooo0o0O = True
 IiiiIIi11II = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = False )
 return IIIooo0o0O
 if 41 - 41: IIIi1i1I / iii11iiII + iiIIi1IiIi11 + OOoooooO
def iiiiii1Ii ( name , url , mode , iconimage , fanart , description ) :
 if 20 - 20: OO00O0O0O00Oo + OO00O0O0O00Oo * II111iiii * iIii1I11I1II1 % O0 * ooOo
 OOo0OOOoOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIooo0o0O = True
 IiiiIIi11II = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = True )
 return IIIooo0o0O
 if 62 - 62: OoooooooOO / o0o0Oo0oooo0 . i1Ii . i1Ii % OOoooooO
 if 42 - 42: I1I1i1 . iii11iiII - OOoooooO
 if 33 - 33: II111iiii / O0 / i1Ii - i11IiIiiIIIII - i1IIi
def IiIiiI ( name , url , mode , iconimage , fanart , description ) :
 OOo0OOOoOOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIooo0o0O = True
 IiiiIIi11II = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiiiIIi11II . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiiiIIi11II . setProperty ( "Fanart_Image" , fanart )
 if mode == 90 :
  IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = False )
 else :
  IIIooo0o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0OOOoOOo , listitem = IiiiIIi11II , isFolder = True )
 return IIIooo0o0O
 if 53 - 53: ooOo % OoooooooOO + OO00O0O0O00Oo - Ooo0O / i1Ii * I1I1i1
def ooo0O ( ) :
 Ii1iiIIi1i = [ ]
 iIiiiI1I = sys . argv [ 2 ]
 if len ( iIiiiI1I ) >= 2 :
  iIII1I1ii = sys . argv [ 2 ]
  iiIIi11ii1Ii = iIII1I1ii . replace ( '?' , '' )
  if ( iIII1I1ii [ len ( iIII1I1ii ) - 1 ] == '/' ) :
   iIII1I1ii = iIII1I1ii [ 0 : len ( iIII1I1ii ) - 2 ]
  OO0iiiii1iiIIii = iiIIi11ii1Ii . split ( '&' )
  Ii1iiIIi1i = { }
  for oOo0 in range ( len ( OO0iiiii1iiIIii ) ) :
   II1IIii1I11I = { }
   II1IIii1I11I = OO0iiiii1iiIIii [ oOo0 ] . split ( '=' )
   if ( len ( II1IIii1I11I ) ) == 2 :
    Ii1iiIIi1i [ II1IIii1I11I [ 0 ] ] = II1IIii1I11I [ 1 ]
    if 17 - 17: O0
  return Ii1iiIIi1i
  if 31 - 31: i11IiIiiIIIII + II111iiii * Ooo0O + Ooo0O . i11IiIiiIIIII
iIII1I1ii = ooo0O ( )
oO0o00oOOooO0 = None
O0Oo0o000oO = None
O0Oo00o00OoO = None
Ooooo0OoO0 = None
i1i1i1I = None
OooOo00o = None
II1i1I1111I1I = None
IiI11i1IIiiI = None
try :
 II1i1I1111I1I = int ( iIII1I1ii [ "fav_mode" ] )
except :
 pass
try : O0Oo00o00OoO = urllib . unquote_plus ( iIII1I1ii [ "mode" ] )
except : pass
try : O0Oo0o000oO = urllib . unquote_plus ( iIII1I1ii [ "name" ] )
except : pass
try : oO0o00oOOooO0 = urllib . unquote_plus ( iIII1I1ii [ "url" ] )
except : pass
try : Ooooo0OoO0 = urllib . unquote_plus ( iIII1I1ii [ "iconimage" ] )
except : pass
try : i1i1i1I = urllib . unquote_plus ( iIII1I1ii [ "fanart" ] )
except : pass
try : OooOo00o = urllib . unquote_plus ( iIII1I1ii [ "description" ] )
except : pass
if 27 - 27: Ooo0O * OOoooooO + i11iIiiIii / ooOo - IIIi1i1I
print "Mode: " + str ( O0Oo00o00OoO )
print "URL: " + str ( oO0o00oOOooO0 )
print "Name: " + str ( O0Oo0o000oO )
print "IconImage: " + str ( Ooooo0OoO0 )
if 44 - 44: IiiIII111ii * OOoooooO / o0o0Oo0oooo0
wiz . log ( '[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % ( O0oo0OO0 , O0Oo00o00OoO if not O0Oo00o00OoO == '' else None , O0Oo0o000oO , oO0o00oOOooO0 ) )
if 69 - 69: OOoooooO . iii11iiII - ooOo
def IiIi ( ) :
 if 44 - 44: II111iiii . II111iiii + iii11iiII * IiiIII111ii
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   oO0o00oOOooO0 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   oO00oOoo00o0 ( file , oO0o00oOOooO0 , 'read' , iiiiiIIii , iiiiiIIii , '' )
   if 16 - 16: II111iiii
def oooOO0OO0 ( ) :
 iiI1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 for file in os . listdir ( Ii11iii11I ) :
  if file . endswith ( ".zip" ) :
   oO0o00oOOooO0 = xbmc . translatePath ( os . path . join ( Ii11iii11I , file ) )
   IiIiiI ( file , oO0o00oOOooO0 , 'dell' , iiiiiIIii , iiiiiIIii , '' )
   if 58 - 58: iIii1I11I1II1 / ooOo - oO0 . I1I1i1 - Ooo0O
def iIi1 ( content , viewType ) :
 if 88 - 88: I1111 . OO00O0O0O00Oo / i11IiIiiIIIII
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if ADDON . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % ADDON . getSetting ( viewType ) )
  if 47 - 47: I1111 + oO0 . OOoooooO
  if 43 - 43: ooOo - I1I1i1 / I1I1i1 . II111iiii - IiiIII111ii
  if 40 - 40: iiIIi1IiIi11 . o0o0Oo0oooo0 * O0
  if 6 - 6: ooOo - II111iiii . ooOo + i11IiIiiIIIII . iii11iiII
  if 74 - 74: i1IIi
  if 15 - 15: i1IIi + i1Ii % ooOo / i11iIiiIii * o0o0Oo0oooo0
  if 69 - 69: i11iIiiIii
def iIi1 ( content , viewType ) :
 if wiz . getS ( 'auto-view' ) == 'true' :
  ooO = wiz . getS ( viewType )
  if ooO == '50' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : ooO = '55'
  if ooO == '500' and o0OIiII >= 17 and I1IIiiIiii == 'skin.estuary' : ooO = '50'
  wiz . ebi ( "Container.SetViewMode(%s)" % ooO )
  if 84 - 84: iIii1I11I1II1 . OOoooooO + iiIIi1IiIi11
if O0Oo00o00OoO == None : i1iiIiI1Ii1i ( )
if 85 - 85: iii11iiII % IIIi1i1I * IIIi1i1I + OoooooooOO
elif O0Oo00o00OoO == 'wizardupdate' : wiz . wizardUpdate ( )
elif O0Oo00o00OoO == 'builds' : OoO00 ( )
elif O0Oo00o00OoO == 'viewbuild' : oOOo000oOoO0 ( O0Oo0o000oO , IiI11i1IIiiI )
elif O0Oo00o00OoO == 'buildinfo' : oO0oo ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'buildpreview' : oOIIII ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'install' : Oooooooo00o00 ( O0Oo0o000oO , oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'theme' : Oooooooo00o00 ( O0Oo0o000oO , IiI11i1IIiiI , O0Oo00o00OoO , oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'viewthirdparty' : iiiI ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'installthird' : OoO0o0OOOO ( O0Oo0o000oO , oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'editthird' : IiIII1i1i ( O0Oo0o000oO ) ; wiz . refresh ( )
if 82 - 82: i11IiIiiIIIII / o0o0Oo0oooo0 - iii11iiII / OOoooooO
elif O0Oo00o00OoO == 'pro' : Main_Menu ( )
if 50 - 50: iii11iiII + I1111 . i11iIiiIii + oO0 + i11iIiiIii
elif O0Oo00o00OoO == 'maint' : iIiiIIi1iiII ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'speed' : OOoo0oo ( )
elif O0Oo00o00OoO == 'kodi17fix' : wiz . kodi17Fix ( )
elif O0Oo00o00OoO == 'advancedsetting' : i111Iii ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'autoadvanced' : i111I11i1I ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'removeadvanced' : IIii ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'asciicheck' : wiz . asciiCheck ( )
elif O0Oo00o00OoO == 'backupbuild' : wiz . backUpOptions ( 'build' )
elif O0Oo00o00OoO == 'backupgui' : wiz . backUpOptions ( 'guifix' )
elif O0Oo00o00OoO == 'backuptheme' : wiz . backUpOptions ( 'theme' )
elif O0Oo00o00OoO == 'backupaddon' : wiz . backUpOptions ( 'addondata' )
elif O0Oo00o00OoO == 'oldThumbs' : wiz . oldThumbs ( )
elif O0Oo00o00OoO == 'clearbackup' : wiz . cleanupBackup ( )
elif O0Oo00o00OoO == 'convertpath' : wiz . convertSpecial ( o00 )
elif O0Oo00o00OoO == 'currentsettings' : ooooo0Oo0 ( )
elif O0Oo00o00OoO == 'fullclean' : oOO0O00OoOo ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'clearcache' : iiIiIi1111iI1 ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'clearpackages' : wiz . clearPackages ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'clearcrash' : wiz . clearCrash ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'clearthumb' : I1i1I11 ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'checksources' : wiz . checkSources ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'checkrepos' : wiz . checkRepos ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'freshstart' : O0oO00oOOooO ( )
elif O0Oo00o00OoO == 'forceupdate' : wiz . forceUpdate ( )
elif O0Oo00o00OoO == 'forceprofile' : wiz . reloadProfile ( wiz . getInfo ( 'System.ProfileName' ) )
elif O0Oo00o00OoO == 'forceclose' : wiz . killxbmc ( )
elif O0Oo00o00OoO == 'forceskin' : wiz . ebi ( "ReloadSkin()" ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'hidepassword' : wiz . hidePassword ( )
elif O0Oo00o00OoO == 'unhidepassword' : wiz . unhidePassword ( )
elif O0Oo00o00OoO == 'enableaddons' : o0o0oo0Ooo ( )
elif O0Oo00o00OoO == 'toggleaddon' : wiz . toggleAddon ( O0Oo0o000oO , oO0o00oOOooO0 ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'togglecache' : OOoOooO00 ( O0Oo0o000oO ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'toggleadult' : wiz . toggleAdult ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'changefeq' : I1i1ii ( ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'uploadlog' : uploadLog . Main ( )
elif O0Oo00o00OoO == 'viewlog' : ii111iI1i1 ( )
elif O0Oo00o00OoO == 'viewwizlog' : ii111iI1i1 ( I11iii1Ii )
elif O0Oo00o00OoO == 'viewerrorlog' : oo0o0ooooo ( all = True )
elif O0Oo00o00OoO == 'clearwizlog' : i1IiII = open ( I11iii1Ii , 'w' ) ; i1IiII . close ( ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Wizard Log Cleared![/COLOR]" % iIiIi11 )
elif O0Oo00o00OoO == 'purgedb' : IiI11I1Ii11II ( )
elif O0Oo00o00OoO == 'fixaddonupdate' : O0Oo0 ( )
elif O0Oo00o00OoO == 'removeaddons' : Oo00oO ( )
elif O0Oo00o00OoO == 'removeaddon' : IIIiiiIiI ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'removeaddondata' : i11i11i ( )
elif O0Oo00o00OoO == 'removedata' : o0ooOo00O ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'resetaddon' : O0oOoo0o000O0 = wiz . cleanHouse ( o0 , ignore = True ) ; wiz . LogNotify ( "[COLOR %s]%s[/COLOR]" % ( oOOo0O00o , o0OOO ) , "[COLOR %s]Addon_Data reset[/COLOR]" % iIiIi11 )
elif O0Oo00o00OoO == 'systeminfo' : iI1I1 ( )
elif O0Oo00o00OoO == 'restorezip' : i11iiI ( 'build' )
elif O0Oo00o00OoO == 'restoregui' : i11iiI ( 'gui' )
elif O0Oo00o00OoO == 'restoreaddon' : i11iiI ( 'addondata' )
elif O0Oo00o00OoO == 'restoreextzip' : o0O00OooooO ( 'build' )
elif O0Oo00o00OoO == 'restoreextgui' : o0O00OooooO ( 'gui' )
elif O0Oo00o00OoO == 'restoreextaddon' : o0O00OooooO ( 'addondata' )
elif O0Oo00o00OoO == 'writeadvanced' : O00O ( O0Oo0o000oO , oO0o00oOOooO0 )
if 31 - 31: IIIi1i1I * OO00O0O0O00Oo . o0o0Oo0oooo0 * i11IiIiiIIIII
elif O0Oo00o00OoO == 'apk1' : O0O0o0o0o ( )
elif O0Oo00o00OoO == 'apkgame' : IiIIiIIIiIii ( oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'select' : I1iIi1iiiIiI ( oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'grab' : Ii1I11I ( O0Oo0o000oO , oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'rom' : OOO0o0OO0OO ( oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'apkscrape1' : APK ( )
elif O0Oo00o00OoO == 'apkscrape' : OOO0oOoO0O ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'apkshow' : OOooo0O ( oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'intellaunch' : i1II ( )
elif O0Oo00o00OoO == 'intelselect' : iIiiIiiIi ( O0Oo0o000oO , oO0o00oOOooO0 , Ooooo0OoO0 , i1i1i1I , OooOo00o )
elif O0Oo00o00OoO == 'emurom' : o0oo0000 ( )
elif O0Oo00o00OoO == 'roms' : IiI1i111IiIiIi1 ( )
elif O0Oo00o00OoO == 'snes' : I1IiooooOoO0O ( )
elif O0Oo00o00OoO == 'nes' : iIiIIi ( )
elif O0Oo00o00OoO == 'gen' : IIii1 ( )
elif O0Oo00o00OoO == 'atr' : i11IiIIi11I ( )
elif O0Oo00o00OoO == 'n64' : iiIIi ( )
elif O0Oo00o00OoO == 'tbg' : i1II11Iii1I ( )
elif O0Oo00o00OoO == 'nds' : OO0OoOo0OOO ( )
elif O0Oo00o00OoO == 'ps' : I1Iii1I ( )
elif O0Oo00o00OoO == 'apkinstall' : iiIii1I ( O0Oo0o000oO , oO0o00oOOooO0 , "None" )
elif O0Oo00o00OoO == 'rominstall' : i11II ( O0Oo0o000oO , oO0o00oOOooO0 , )
if 28 - 28: i1Ii + ooOo - Ooo0O % iii11iiII . i11IiIiiIIIII + ooOo
elif O0Oo00o00OoO == 'youtube' : oooo ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'viewVideo' : iIi ( oO0o00oOOooO0 )
if 72 - 72: IiiIII111ii / Ooo0O / IIIi1i1I * o0o0Oo0oooo0 + iii11iiII
elif O0Oo00o00OoO == 'addons' : O00o0O ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'addoninstall' : iIiI ( O0Oo0o000oO , oO0o00oOOooO0 )
if 58 - 58: I1I1i1 % ooOo . ooOo * I1111 - i1Ii . OoooooooOO
elif O0Oo00o00OoO == 'savedata' : iIII11Iiii1 ( )
elif O0Oo00o00OoO == 'togglesetting' : wiz . setS ( O0Oo0o000oO , 'false' if wiz . getS ( O0Oo0o000oO ) == 'true' else 'true' ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'managedata' : o0Oo00oOO ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'whitelist' : wiz . whiteList ( O0Oo0o000oO )
if 10 - 10: OO00O0O0O00Oo
elif O0Oo00o00OoO == 'trakt' : o0oo0o00ooO00 ( )
elif O0Oo00o00OoO == 'savetrakt' : traktit . traktIt ( 'update' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'restoretrakt' : traktit . traktIt ( 'restore' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'addontrakt' : traktit . traktIt ( 'clearaddon' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'cleartrakt' : traktit . clearSaved ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'authtrakt' : traktit . activateTrakt ( O0Oo0o000oO ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'updatetrakt' : traktit . autoUpdate ( 'all' )
elif O0Oo00o00OoO == 'importtrakt' : traktit . importlist ( O0Oo0o000oO ) ; wiz . refresh ( )
if 48 - 48: iiIIi1IiIi11 * i1IIi % OoooooooOO * IiiIII111ii * I1111
elif O0Oo00o00OoO == 'realdebrid' : iiIIiiIi ( )
elif O0Oo00o00OoO == 'savedebrid' : debridit . debridIt ( 'update' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'restoredebrid' : debridit . debridIt ( 'restore' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'addondebrid' : debridit . debridIt ( 'clearaddon' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'cleardebrid' : debridit . clearSaved ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'authdebrid' : debridit . activateDebrid ( O0Oo0o000oO ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'updatedebrid' : debridit . autoUpdate ( 'all' )
elif O0Oo00o00OoO == 'importdebrid' : debridit . importlist ( O0Oo0o000oO ) ; wiz . refresh ( )
if 7 - 7: iiIIi1IiIi11 . IiiIII111ii . iiIIi1IiIi11 - OO00O0O0O00Oo
elif O0Oo00o00OoO == 'login' : I11II1 ( )
elif O0Oo00o00OoO == 'savelogin' : loginit . loginIt ( 'update' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'restorelogin' : loginit . loginIt ( 'restore' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'addonlogin' : loginit . loginIt ( 'clearaddon' , O0Oo0o000oO )
elif O0Oo00o00OoO == 'clearlogin' : loginit . clearSaved ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'authlogin' : loginit . activateLogin ( O0Oo0o000oO ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'updatelogin' : loginit . autoUpdate ( 'all' )
elif O0Oo00o00OoO == 'importlogin' : loginit . importlist ( O0Oo0o000oO ) ; wiz . refresh ( )
if 33 - 33: OOoooooO + OoooooooOO - I1111 / i1IIi / OoooooooOO
elif O0Oo00o00OoO == 'contact' : notify . contact ( oOO0O00Oo0O0o )
elif O0Oo00o00OoO == 'settings' : wiz . openS ( O0Oo0o000oO ) ; wiz . refresh ( )
elif O0Oo00o00OoO == 'opensettings' : id = eval ( oO0o00oOOooO0 . upper ( ) + 'ID' ) [ O0Oo0o000oO ] [ 'plugin' ] ; OOO0IIIIii11II1I = wiz . addonId ( id ) ; OOO0IIIIii11II1I . openSettings ( ) ; wiz . refresh ( )
if 48 - 48: oO0 - O0 . I1111
elif O0Oo00o00OoO == 'developer' : Oo000 ( )
elif O0Oo00o00OoO == 'converttext' : wiz . convertText ( )
elif O0Oo00o00OoO == 'createqr' : wiz . createQR ( )
elif O0Oo00o00OoO == 'testnotify' : III ( )
elif O0Oo00o00OoO == 'testupdate' : I1iiIiII ( )
elif O0Oo00o00OoO == 'testfirst' : i1iIIiiIiII ( )
elif O0Oo00o00OoO == 'testfirstrun' : OOii11Ii1IiiI1 ( )
elif O0Oo00o00OoO == 'testapk' : notify . apkInstaller ( 'SPMC' )
if 38 - 38: O0
elif O0Oo00o00OoO == 'guide' : TvGuide ( )
if 79 - 79: i1IIi . IIIi1i1I
elif O0Oo00o00OoO == 'recreateaddon' : ReCreate_Addon_ini ( )
elif O0Oo00o00OoO == 'getlistplay' : Get_List_playlinks ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'resolve' : RESOLVER ( oO0o00oOOooO0 )
elif O0Oo00o00OoO == 'streams' : Streams_Menu ( )
elif O0Oo00o00OoO == 'liveevent' : Live_Events ( O0Oo0o000oO )
elif O0Oo00o00OoO == 'addonopen' : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
