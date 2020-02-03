from geopy.geocoders import GoogleV3

key = "AIzaSyD-Ho0sPmcPzQiPDvooQGexPxZf5Xj4xI0"
location = input("enter a location")
geolocator = GoogleV3(key)
location = geolocator.geocode(location)
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
