import phonenumbers
from phonenumbers import timezone, geocoder, carrier

Number = input("Enter your phone number +__: ")  # Example: +923001234567
phone = phonenumbers.parse(Number)  # Converts string into a PhoneNumber object

car = carrier.name_for_number(phone, 'en')       # Finds mobile carrier (e.g., Jazz, Zong)
geo = geocoder.description_for_number(phone, 'en')  # Finds country/region (e.g., Pakistan)
time = timezone.time_zones_for_number(phone)     # Finds timezone(s) for that number

print(car)
print(geo)
print(time)
