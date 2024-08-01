from geopy.geocoders import Nominatim

# Function to get location details by address
def get_location_by_address(address):
    # Create a geolocator object
    geolocator = Nominatim(user_agent="GetLoc")
    
    # Perform geocoding
    location = geolocator.geocode(address)
    
    if location:
        print("Address:", location.address)
        print("Latitude =", location.latitude)
        print("Longitude =", location.longitude)
    else:
        print("Address not found")

# Function to get address by coordinates
def get_address_by_coordinates(latitude, longitude):
    # Create a geolocator object
    geolocator = Nominatim(user_agent="GetLoc")
    
    # Perform reverse geocoding
    location = geolocator.reverse((latitude, longitude), language='en')
    
    if location:
        print("Address:", location.address)
    else:
        print("Address not found")

# Example usage
print("Geocoding Example:")
get_location_by_address("NARSAMPET")

print("\nReverse Geocoding Example:")
get_address_by_coordinates(17.928122, 79.894531)
