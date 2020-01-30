import requests

IL_id = 4013700
OL_id = 4013698
CGS_id = 4013586
NL_id = 4013584

url = "https://transloc-api-1-2.p.rapidapi.com/stops.json"

def parseCoords(location):
    from geopy.geocoders import GoogleV3
    key = "AIzaSyD-Ho0sPmcPzQiPDvooQGexPxZf5Xj4xI0"
    geolocator = GoogleV3(key)
    location = geolocator.geocode(location)

    #print((location.latitude, location.longitude))

    return(str(location.latitude) + ", " + str(location.longitude))


def getData(locationCoords):
    # PRESET — Balz-Dobie
    # querystring = {"callback": "call", "geo_area": "38.033963, -78.517397 | 300", "agencies": "347"}
    # PRESET — Monroe Hall
    # querystring = {"callback": "call", "geo_area": "38.034778, -78.506495 | 300", "agencies": "347"}

    querystring = {"callback": "call", "geo_area": "" + locationCoords + " | 300", "agencies": "347"}

    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': "c96a129019msh032ff6b90f063edp12836cjsn86ac9b68c0ab"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response

def loadData(response):
    # print(response.text)

    # print(response.json())
    import json

    json_object = response.json()
    dump = json.dumps(json_object, indent=1)

    test = json.loads(dump)
    # print(test)
    # print("spacer")

    # print(test["rate_limit"])

    # for key in test.keys():
    #     print("this is a key: " + key)
    #     print((test[key]))

    data = test["data"]

    # print(data)


    for entry in data:
        print(entry["name"])


def main():
    print("python main function")
    location = input("location?")
    locationCoords = parseCoords(location)
    loadData(getData(locationCoords))


if __name__ == '__main__':
    main()
