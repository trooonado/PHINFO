# PRINTING MY LOGO 
print(""""
██████╗░██╗░░██╗██╗███╗░░██╗███████╗░█████╗░
██╔══██╗██║░░██║██║████╗░██║██╔════╝██╔══██╗
██████╔╝███████║██║██╔██╗██║█████╗░░██║░░██║
██╔═══╝░██╔══██║██║██║╚████║██╔══╝░░██║░░██║
██║░░░░░██║░░██║██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
verson=1.20.2 
created by satya@hacker""""")

#STARTING THE CODING 

#importing module

import phonenumbers
from phonenumbers import geocoder , carrier
from opencage.geocoder import OpenCageGeocode
import folium 
from phonenumbers import timezone

#tracking country

number = input("ENTER THE NUMBER :")
num =  phonenumbers.parse(number)
locktions = geocoder.description_for_number(num , "en")
print('THE COUNTER OF THE NUMBER :' + locktions)

#service provider 
sim_pro = phonenumbers.parse(number)
print('THE SIM PROVIDERS OF THE NUMBER :' + carrier.name_for_number(sim_pro ,'en'))

# time zone
time_zone = timezone.time_zones_for_number(num)
print('THE TIME ZONE OF THE NUMBER :' + str(time_zone))

# chaking the number true or false

troo_or_false = phonenumbers.is_possible_number(num)
print("THE NUMBER :" + str(troo_or_false))

# api key 

api_key = '583f481cb0164d59aac1c4a777735f2c'
geocoder = OpenCageGeocode(api_key)
query = str(locktions)
result = geocoder.geocode(query)
print(result)

#printing the latitude and longitude 

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

#locating the location into the map 

map = folium.Map(loactions=[lat, lng] , zoom_start=9)
folium.Marker([lat, lng] ,popup=locktions).add_to((map))
map.save('LOACTION.html')


# THE ENG OF COD 