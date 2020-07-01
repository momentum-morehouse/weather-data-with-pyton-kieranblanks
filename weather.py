import requests 
#key= AN2UBpnNha0GDf5Z0xufgcxI0x9r7UWR

#Make the API call and store the response
def climate(lat,lon,name):
    url = 'https://api.climacell.co/v3/weather/realtime'

    payload = {
        "apikey":"AN2UBpnNha0GDf5Z0xufgcxI0x9r7UWR",
        "lat":lat,
        "lon":lon,
        "fields": ["temp", "precipitation"],
        "unit_system":"us",
    }

    response = requests.get(url, params=payload).json() 
    print(response["temp"]["value"]) #callingthevalue

#Step 3:  List of Tuples 
my_locations =[(42.331429, -83.045753, "Detroit"), (8.3405, 115.0920, "Bali"), (15.8700, 100.9925, "Thailand"), (19.4326, 99.1332, "Mexico"), (3.2028, 73.2207, "Maldives"), (4.6796, 55.4920, "Seychelles"), (30.5595, 22.9375, "South Africa"), (21.6940, 71.7979, "Turks & Caicos"), (13.9094, 60.9789, "St. Lucia"), (40.5532, 14.2222, "Capri"),]
#print(my_locations[0:2])

#Step4- Make request latitude and longitude (23.0506249, -82.4730905).

def get_weather_data(my_locations):
    



# for location in location_list:
#     climate(location[0],location[1],location[2]) #expects to see real numbers
# print(climate)



# def get_location_weather(temp, precipitation, name):
#  #Display information about the temperature & precipitation for locations
#     weather_details = {'temperature' : temp, 'precipitation ' : precip, 'name': country}
#     return weather_details
#     country_weather = get_location_weather(temp, precipitation, name)
#     print(country_weather)






 





