import phonenumbers
import opencage
import folium

# calling number variable from myphone file
from myphone import number


# calling geocoder  from phonenumbers file
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")

print(location)

# calling service provider name from phonenumbers file
from phonenumbers import carrier

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

# Make account on opencage data website to access this feature
from opencage.geocoder import OpenCageGeocode


key ='# Enter your opencage data API key (use paid version for better experience)'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 900000)
folium.Marker([lat, lng], popup=location).add_to(myMap)


myMap.save("find_location.html")