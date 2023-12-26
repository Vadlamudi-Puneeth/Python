# This is the code it won't give the current location it will give the first location of sim

import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+917702******")
phone_number2 = phonenumbers.parse("+919618******")
phone_number3 = phonenumbers.parse("+919573******")
phone_number4 = phonenumbers.parse("+917981******")

print("Phone number location\n")

# language = english

print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));
print(geocoder.description_for_number(phone_number4,"en"));
