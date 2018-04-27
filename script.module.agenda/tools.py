import xbmc
import xbmcaddon

# Write something on XBMC log
def log(message):
    xbmc.log("Agenda Desportiva " + message)

# Write this module messages on XBMC log
def debug(message):
    debug_enabled = getSetting('debug_enabled')
    if debug_enabled == 'true':
        xbmc.log("Agenda Desportiva [DEBUG] "+message)

def getSetting(settingName):
    settingValue = xbmcaddon.Addon().getSetting(settingName)
    return settingValue