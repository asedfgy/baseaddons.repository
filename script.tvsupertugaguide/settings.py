#      Copyright (C) 2015 Justin Mills
#      
#
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
import xbmcgui, utils

addon_id = 'script.tvsupertugaguide'
dlg = xbmcgui.Dialog()


def showTOS():
	tos = utils.get_setting(addon_id,'tos')== "true"
#	if tos == False:
#		utils.set_setting(addon_id, 'tos', 'true')
#		dlg.ok('IVUE TV Guide TOS','By using Ivue Guide you agree to the terms and conditions found at https://www.facebook.com/groups/tecbox')

def setSettings(username,password,userid):
       username = utils.set_setting(addon_id, 'tvsupertuga', username)
       password = utils.set_setting(addon_id, 'tvsupertuga', password)
       userid = utils.set_setting(addon_id, 'userid', userid)

def setUrl():
	user = utils.set_setting(addon_id, 'userurl', 'https://raw.githubusercontent.com/programacaotv/programacaotv/master/guide/') 
	url = utils.set_setting(addon_id, 'mainurl', 'https://raw.githubusercontent.com/programacaotv/programacaotv/master/guide/')
	logos = utils.set_setting(addon_id, 'logos', 'https://raw.githubusercontent.com/programacaotv/programacaotv/master/logos/')	
	   
