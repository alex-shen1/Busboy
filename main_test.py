from busboy import *

def main():
    # location = input("location?")

    location = "balz-dobie"
    location_coords = parse_coords(location)
    stop_data = get_data(location_coords)
    stop_names = load_data(stop_data, "name")

    print(stop_names)

    get_routes(stop_data)

    # parse_route_names([4013586, 4013584, 4013594, 4013698, 4013590, 4013700, 4013696])


if __name__ == '__main__':
    main()
