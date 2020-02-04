from busboy import *

def main():
    # location = input("location?")

    location = "balz-dobie"
    #balz coordinates: (38.0340393, -78.5173214)
    #monroe coordinates: (38.034837, -78.5064309)

    startroutes = routes_from_location(location)
    endroutes = routes_from_location("monroe hall uva")

    print("common routes: " + str(find_common_stops(startroutes, endroutes)))
    parse_route_names([4013586, 4013584, 4013594, 4013698, 4013590, 4013700, 4013696])


def routes_from_location(location):
    location_coords = parse_coords(location)
    stop_data = get_data(location_coords)
    stop_names = load_data(stop_data, "name")

    #print(stop_names)

    routes = parse_route_names(get_routes(stop_data))

    return routes


if __name__ == '__main__':
    main()
