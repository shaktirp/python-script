import requests
import json
from env_variables import _SETTINGS

_URLS = {
    "register": "https://sunburst.sunsetwx.com/v1/register",
    "login": "https://sunburst.sunsetwx.com/v1/login",
    "coordinates": "https://sunburst.sunsetwx.com/v1/coordinates",
    "quality": "https://sunburst.sunsetwx.com/v1/quality"
}

_ERRORMSGS = {
    "tokenInvalid": "Token not valid",
    "tokenCallError": "Could not get new token",
    "coordinatesError": "Error in getting coordinates",
    "qualityError": "Error in getting quality"
}

def getJson():
    with open("data.json") as json_file:
        data = json.load(json_file)
        return data

def postJson(newToken):
    data = getJson()
    data["token"] = newToken
    with open("data.json", "w") as outputFile:
        json.dump(data, outputFile)

def getNewToken():
    data = [
        ("email", _SETTINGS["email"]),
        ("password", _SETTINGS["password"])
    ]

    resp = requests.post(_URLS["login"], data=data)

    if resp.status_code in (200, 201):
        postJson(resp.json()["token"])
    else:
        print(_ERRORMSGS["tokenCallError"])

def getCoordinates(city, token):
    headers = {
        "Authorization": "Bearer " + token
    }

    params = {
        "location": city
    }

    resp = requests.get(_URLS["coordinates"], headers=headers, params=params)

    if resp.status_code in (200,201):
        x_coordinate = resp.json()["features"][0]["geometry"]["coordinates"][0]
        y_coordinate = resp.json()["features"][0]["geometry"]["coordinates"][1]
        coords = str(x_coordinate) + "," + str(y_coordinate)
        return coords
    elif resp.status_code == 401:
        return _ERRORMSGS["tokenInvalid"]
    else:
        print(_ERRORMSGS["coordinatesError"])
        return

def getQuality(coords, timeOfDay, token):
    headers = {
        "Authorization": "Bearer " + token
    }

    params = {
        "coords": coords,
        "type": timeOfDay
    }

    resp = requests.get(_URLS["quality"], headers=headers, params=params)

    if resp.status_code in (200,201):
        props = resp.json()["features"][0]["properties"]
        return props
    else:
        print(_ERRORMSGS["qualityError"])
        return {}

def main():
    _DATA = getJson()
    coords = getCoordinates(_DATA["city"], _DATA["token"])
    if coords == _ERRORMSGS["tokenInvalid"]:
        print("Getting new token")
        getNewToken()
        _DATA = getJson()
        coords = getCoordinates(_DATA["city"], _DATA["token"])

    return {
        "sunset": getQuality(coords, "sunset", _DATA["token"]),
        "sunrise": getQuality(coords, "sunrise", _DATA["token"])
    }
