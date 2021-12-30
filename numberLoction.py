import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder

key = "c26408c63fa44d14b72a01f8912012c5"
sumNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(sumNumber,"he")
print(yourLocation)

# get service provider

from phonenumbers import carrier
service_provider  = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode


geocoder = OpenCageGeocode(key)
query = str(yourLocation)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng],zoom_start = 18)
folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)
# save map in html file
myMap.save("myLocation.html")
