#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu

#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import gui, xbmcgui, settings
import utils, urllib2, base64

settings.showTOS()
settings.setUrl()
addon_id = 'script.tvsupertugaguide'
un = base64.decodestring(b'dXNlcm5hbWU=')
up = base64.decodestring(b'cGFzc3dvcmQ=')
ae = base64.decodestring('QXV0aG9yaXphdGlvbiBFcnJvciAhISEgUGxlYXNlIENoZWNrIFlvdXIgVXNlcm5hbWUgYW5kIFBhc3N3b3Jk')

try:
	w = gui.TVGuide()
	w.doModal()
	del w

except urllib2.HTTPError, e:
		if e.code == 401:
			utils.notify(addon_id, ae)
		else:
		    utils.notify(addon_id, e)		
