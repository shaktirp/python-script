from twilio.rest import Client
from time import gmtime, strftime
from env_variables import _SETTINGS
from sunsetwx import *

# client = Client(_SETTINGS["SID"], _SETTINGS["token"])
#
# body = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - Hello from Python! "
#
# print(body)

# client.messages.create(to=_SETTINGS["to_number"],
#                        from_=_SETTINGS["from_number"],
#                        body=body)

getCoordinates()
