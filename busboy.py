from route_cache_creator import create_dictionary

routes_dict = create_dictionary()


testMode = True


def parse_coords(locationString):
    from geopy.geocoders import GoogleV3
    key = "AIzaSyD-Ho0sPmcPzQiPDvooQGexPxZf5Xj4xI0"
    geolocator = GoogleV3(key)
    location = geolocator.geocode(locationString)

    if testMode:
        print("TESTMODE ENABLED: coordinates of " + locationString + ":")
        print((location.latitude, location.longitude), end="\n")

    return str(location.latitude) + ", " + str(location.longitude)


def get_data(locationCoords):
    import requests
    url = "https://transloc-api-1-2.p.rapidapi.com/stops.json"
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

    import json

    # honestly this code chunk is horrible but i don't know how to do
    # it better and i'm too lazy to figure out how
    json_object = response.json()
    dump = json.dumps(json_object, indent=1)
    loaded_json = json.loads(dump)
    data = loaded_json["data"]  # response itself also contains a bunch of other irrelevant stuff that isn't needed

    return data


# given a dataset, returns a list of all entries with the field
def load_data(data, field):
    # print(response.text)
    # print(response.json())
    field_data = []

    for entry in data:
        # print(entry[field])
        field_data.append(entry[field])

    return field_data


# finds routes that are accessible to both locations
# start and end should both be lists of routes from start/end
def find_common_stops(start, end):
    start_routes = parse_route_names(start)
    end_routes = parse_route_names(end)
    common_routes = []

    for route in start_routes:
        if route in end_routes and route not in common_routes:
            common_routes.append(route)
    return common_routes

# given a dataset of stops, all the routes that they access
def get_routes(stops_data):
    # print(stops_data)
    routes_data = load_data(stops_data, "routes")  # should be list of lists?
    unique_routes = []
    for routeSet in routes_data:
        for route in routeSet:
            if route not in unique_routes:
                unique_routes.append(route)
    # print(routes_data)
    # print(unique_routes)
    return unique_routes


def parse_route_names(routes):
    # print("KEYS")
    # print(routes_dict.keys(), end="\n")

    for route in routes:
        if route in routes_dict.keys():
            # print("MATCH FOUND")
            routes[routes.index(route)] = routes_dict[route]
    # print("PARSED ROUTES")
    # print(routes, end="\n")
    return routes



