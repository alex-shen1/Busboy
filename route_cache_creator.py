import os

# this is the same as get_data in busboy but with different parameters on the request
def get_data():
    import requests
    url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"
    querystring = {"callback": "call", "agencies": "347"}
    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': os.getenv("TRANSLOC_API_KEY")
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    import json

    # honestly this code chunk is horrible but i don't know how to do
    # it better and i'm too lazy to figure out how
    json_object = response.json()
    dump = json.dumps(json_object, indent=1)
    # print(dump)
    loaded_json = json.loads(dump)
    data = loaded_json["data"]  # response itself also contains a bunch of other irrelevant stuff that isn't needed

    return data


def create_cache():
    routes_data = get_data()
    with open("routes.txt", "w+") as routes_file:
        for route in routes_data["347"]:  # 347 = UVA's "agency id"
            routes_file.write(route["short_name"] + "=" + route["route_id"] + "\n")


def create_dictionary():
    routes_dict = {}
    with open("routes.txt", "r") as routes_file:
        n = 1
        for line in routes_file:
            separator = line.index("=")
            route_name = (line[:separator])
            id = (line[separator + 1:len(line) - 1])  # need the -1 to remove \n character
            routes_dict[id] = route_name
    # print(routes_dict)
    return routes_dict


def main():
    create_cache()
    create_dictionary()


if __name__ == '__main__':
    main()
