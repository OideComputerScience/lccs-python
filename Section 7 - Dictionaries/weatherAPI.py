import requests
#This is an example of the open meteo api
url = "https://api.open-meteo.com/v1/forecast?latitude=51.9&longitude=-8.5&current_weather=true"
response = requests.get(url)

data = response.json()   # ← JSON becomes a Python dictionary
#Now data is a dictionary and you can explore it
print(data.keys())
print(data["current_weather"])
#Demonstrate dictionary access and manipulation
# Extract the current temperature
weather = data["current_weather"]
temperature = weather["temperature"]

print("Current temperature:", temperature)
#Or combine values
wind = weather["windspeed"]
print(f"It is {temperature}°C with wind speed {wind} km/h")

#Add a function to process teh dictionary
#This converts temp to fahrenheit
def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Use it with the API data
temp_c = data["current_weather"]["temperature"]
temp_f = to_fahrenheit(temp_c)

print("Temperature in Fahrenheit:", temp_f)

