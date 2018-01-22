from twilio.rest import Client
from time import gmtime, strftime
from os import environ
try:
    import env as _env
    env = "dev"
except Exception as e:
    env = "prod"

if env == "dev":
    _SETTINGS = {
        "SID": _env.SID,
        "token": _env.token,
        "to_number": _env.to_number,
        "from_number": _env.from_number
    }
else:
    _SETTINGS = {
        "SID": environ.get('SID'),
        "token": environ.get('token'),
        "to_number": environ.get('to_number'),
        "from_number": environ.get('from_number')
    }

client = Client(_SETTINGS["SID"], _SETTINGS["token"])

body = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - Hello from Python! "

print(body)

# client.messages.create(to=_SETTINGS["to_number"],
#                        from_=_SETTINGS["from_number"],
#                        body=body)
