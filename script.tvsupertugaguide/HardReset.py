import time
import os
import xbmc
import xbmcgui
import xbmcaddon

databasePath = xbmc.translatePath('special://userdata/addon_data/script.tvsupertugaguide')
d = xbmcgui.Dialog()

			
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "guides.ini" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "addons.ini" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "addons2.ini" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "guide.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "amylist.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "franca.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "alemanha.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "italia.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "uk.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "usa.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
						
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "master.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "settings.xml" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "master.db" in name:
			try:
				os.remove(os.path.join(root,name))
			except: 
				d = xbmcgui.Dialog()
				d.ok('Hard Reset', 'Error Removing ' + str(name),'','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
				pass
		else:
			continue
			
			

d = xbmcgui.Dialog()			
d.ok('tvsupertugaguide guide Hard reset', 'Please restart for ','the changes to take effect','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
