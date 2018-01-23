from twilio.rest import Client
from time import gmtime, strftime
from env_variables import _SETTINGS
from sunsetwx import *

client = Client(_SETTINGS["SID"], _SETTINGS["token"])

def getMsg(type, time, quality, temprature):
    return type + ": " + time + " | " + quality + " | " + str(temprature) + "C"

qualityObj = main()

sunsetMsg = getMsg("sunset", qualityObj["sunset"]["valid_at"], qualityObj["sunset"]["quality"], qualityObj["sunset"]["temperature"])
sunriseMsg = getMsg("sunrise", qualityObj["sunrise"]["valid_at"], qualityObj["sunrise"]["quality"], qualityObj["sunrise"]["temperature"])

print(sunsetMsg, sunriseMsg)
# client.messages.create(to=_SETTINGS["to_number"],
#                        from_=_SETTINGS["from_number"],
#                        body=sunsetMsg)
#
# client.messages.create(to=_SETTINGS["to_number"],
#                        from_=_SETTINGS["from_number"],
#                        body=sunriseMsg)
