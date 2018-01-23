import requests
import json
from env_variables import _SETTINGS

_URLS = {
    "register": "https://sunburst.sunsetwx.com/v1/register",
    "login": "https://sunburst.sunsetwx.com/v1/login",
    "coordinates": "https://sunburst.sunsetwx.com/v1/coordinates",
    "quality": "https://sunburst.sunsetwx.com/v1/quality"
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
        getCoordinates()
        return resp.json()["token"]

    return

def getCoordinates():
    headers = {
        "Authorization": "Bearer " + _DATA["token"]
    }

    params = {
        "location": _DATA["city"]
    }

    resp = requests.get(_URLS["coordinates"], headers=headers, params=params)

    if resp.status_code in (200,201):
        x_coordinate = resp.json()["features"][0]["geometry"]["coordinates"][0]
        y_coordinate = resp.json()["features"][0]["geometry"]["coordinates"][1]
        coords = str(x_coordinate) + "," + str(y_coordinate)
        getQuality(coords, "sunrise")
        getQuality(coords, "sunset")
    elif resp.status_code == 401:
        getNewToken()
    else:
        print("Error in getting coordinates")

def getQuality(coords, timeOfDay):
    headers = {
        "Authorization": "Bearer " + _DATA["token"]
    }

    params = {
        "coords": coords,
        "type": timeOfDay
    }

    resp = requests.get(_URLS["quality"], headers=headers, params=params)

    if resp.status_code in (200,201):
        props = resp.json()["features"][0]["properties"]
        print(props["type"], props["valid_at"], props["quality"], props["temperature"])
    else:
        print("Error in getting quality")

def main():
    

_DATA = getJson()
