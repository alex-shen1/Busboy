import data_handler as dh

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
    routes_data = dh.read_field(stops_data, "routes")  # should be list of lists?
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
        routes[routes.index(route)] = lookup_route(route)
    # print("PARSED ROUTES")
    # print(routes, end="\n")
    return routes


def lookup_route(route):
    if route in dh.routes_dict.keys():
        # print("MATCH FOUND")
        return dh.routes_dict[route]
    return route