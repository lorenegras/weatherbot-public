from geopy.geocoders import Nominatim

# Sous python on peut avoir les coordonnées longitude latitude en fonction du nom de la ville
class ConvertCitytoCoords():
    def getCoord(self, city):
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(city)
        result = 'undefined'
        if(hasattr(location, 'latitude') and hasattr(location, 'longitude')):
            result = {"lat": str(location.latitude),
                    "lon": str(location.longitude)}
        return result
