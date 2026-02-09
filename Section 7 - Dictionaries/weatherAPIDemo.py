import requests

def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 1. Get live data
url = "https://api.open-meteo.com/v1/forecast?latitude=51.9&longitude=-8.5&current_weather=true"
response = requests.get(url)
data = response.json()

# 2. Extract dictionary values
weather = data["current_weather"]
temp_c = weather["temperature"]
wind = weather["windspeed"]

# 3. Use a function to manipulate the data
temp_f = to_fahrenheit(temp_c)

# 4. Display results
print("Live Weather for Cork")
print("---------------------")
print("Temperature:", temp_c, "°C")
print("Temperature:", temp_f, "°F")
print("Wind speed:", wind, "km/h")
