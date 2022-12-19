print('''
██████╗░██╗░░██╗██╗███╗░░██╗███████╗░█████╗░
██╔══██╗██║░░██║██║████╗░██║██╔════╝██╔══██╗
██████╔╝███████║██║██╔██╗██║█████╗░░██║░░██║
██╔═══╝░██╔══██║██║██║╚████║██╔══╝░░██║░░██║
██║░░░░░██║░░██║██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░''')
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
target = input("ENTER YOUR TARGET PHONENUMBER :")
country = phonenumbers.parse(target )
locations = geocoder.description_for_number(country , "en")
print("THE TARGET COUNTRY LOACTIONS  IS  :" + locations)
sim_pro = phonenumbers.parse(target)
print("YOUR TARGET SIM PROVIDER IS :" + carrier.name_for_number(sim_pro , "en"))
time = timezone.time_zones_for_number(country)
print( 'this is the target time zobe' + str(time))




