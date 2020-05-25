from route_cache_creator import create_dictionary
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(os.path.join('.env'))
TRANSLOC_API_KEY = os.getenv("TRANSLOC_API_KEY")

routes_dict = create_dictionary()


testMode = True

# runs a string through Google API and returns a string holding geo coordinates
def parse_coords(locationString):
    from geopy.geocoders import GoogleV3
    key = "AIzaSyD-Ho0sPmcPzQiPDvooQGexPxZf5Xj4xI0"
    geolocator = GoogleV3(key)
    location = geolocator.geocode(locationString)

    if testMode:
        print("TESTMODE ENABLED: coordinates of " + locationString + ":")
        print((location.latitude, location.longitude), end="\n")

    return str(location.latitude) + ", " + str(location.longitude)

# given a string of coordinates, returns data for all stops within 300 meters
def get_stops(locationCoords):
    url = "https://transloc-api-1-2.p.rapidapi.com/stops.json"
    # PRESET — Balz-Dobie
    # querystring = {"callback": "call", "geo_area": "38.033963, -78.517397 | 300", "agencies": "347"}
    # PRESET — Monroe Hall
    # querystring = {"callback": "call", "geo_area": "38.034778, -78.506495 | 300", "agencies": "347"}

    querystring = {"callback": "call", "geo_area": "" + locationCoords + " | 300", "agencies": "347"}
    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': TRANSLOC_API_KEY
    }
    response = requests.request("GET", url, headers=headers, params=querystring)


    # honestly this code chunk is horrible but i don't know how to do
    # it better and i'm too lazy to figure out how
    json_object = response.json()
    dump = json.dumps(json_object, indent=1)
    loaded_json = json.loads(dump)
    data = loaded_json["data"]  # response itself also contains a bunch of other irrelevant stuff that isn't needed

    return data


# given a dataset, returns a list of all entries with the field
def read_field(data, field):
    # print(response.text)
    # print(response.json())
    field_data = []

    for entry in data:
        # print(entry[field])
        field_data.append(entry[field])

    return field_data

def get_arrivals(stop):
    url = "https://transloc-api-1-2.p.rapidapi.com/arrival-estimates.json"

    querystring = {"stops":"4235112","callback":"call","agencies":"347"}

    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': TRANSLOC_API_KEY
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_object = response.json()
    dump = json.dumps(json_object, indent=1)
    loaded_json = json.loads(dump)
    data = loaded_json["data"]  # response itself also contains a bunch of other irrelevant stuff that isn't needed

    return data






