import data_handler as dh
import routes_handler as rh
from iso8601 import parse_date
from datetime import datetime, timezone

from push_notifs import *

def main():
    test_arrivals()
    #test_routes()
def test_arrivals():
    data = dh.get_arrivals("4235112") # Alderman @ AFC
    # print(data)
    # print(type(read_field(data,"arrivals"))) # "list"
    arrivals_data = dh.read_field(data,"arrivals")

    #print(json.dumps(arrivals_data, indent=4))

    for thing in arrivals_data:
        for arrival in thing: # i don't know why this second loop is necessary but it is
            arrival_time = str(arrival["arrival_at"])
            time = parse_date(arrival_time)
            now = datetime.now(timezone.utc)
            diff = time-now
            mins = round(diff.total_seconds() / 60)
            print("arriving: " + str(time))
            print("now: " + str(now))
            print("diff: " + str(diff))
            print("mins: " + str(mins) + "\n")
            notify("", "Alderman @ AFC", mins)
def test_routes():
    location = "balz-dobie"
    # balz coordinates: (38.0340393, -78.5173214)
    # monroe coordinates: (38.034837, -78.5064309)
    location = input("location?")
    # startroutes = routes_from_location(location)
    # endroutes = routes_from_location("monroe hall uva")
    print(routes_from_location(location))
    # print("common routes: " + str(find_common_stops(startroutes, endroutes)))
    # parse_route_names([4013586, 4013584, 4013594, 4013698, 4013590, 4013700, 4013696])


def routes_from_location(location):
    location_coords = dh.parse_coords(location)
    stop_data = dh.get_stops(location_coords)
    stop_names = dh.read_field(stop_data, "name")

    print(stop_names)

    routes = rh.parse_route_names(rh.get_routes(stop_data))

    return routes


if __name__ == '__main__':
    main()
