from twilio.rest import Client
from time import gmtime, strftime
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
        "SID": process.env.SID,
        "token": process.env.token,
        "to_number": process.env.to_number,
        "from_number": process.env.from_number
    }

client = Client(_SETTINGS["SID"], _SETTINGS["token"])

body = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - Hello from Python! "

print(body, _SETTINGS)

client.messages.create(to=_SETTINGS["to_number"],
                       from_=_SETTINGS["from_number"],
                       body=body)
