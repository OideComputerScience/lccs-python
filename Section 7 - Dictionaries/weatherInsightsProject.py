import requests

# -----------------------------
# Function: Get weather data
# -----------------------------
def get_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()          # JSON → Python dictionary
    return data # a python dictionary will be returned

# -----------------------------
# Function: Display results - extract key values of temperature, weather and wind speed. 
# -----------------------------
def display_weather(data):
    weather = data["current_weather"]     # nested dictionary
    temp = weather["temperature"]
    wind = weather["windspeed"]

    print("Current Weather")
    print("----------------")
    print("Temperature (°C):", temp)
    print("Wind Speed (km/h):", wind)
    
'''a) Analyse the weather by passing another variable to this function called ideal_temp
This variable should be an ideal temp. If the temp is less than or greater than this
use a print statement to say whether it is ideal or not.
Don't forget to modify the calling function. 
b)If the wind speed is greater than 20 display it is very windy otherwise
state they are normal. 
c) Complete in main function
d) Create a new function called get_forecast that accepts latitude and longitude data.
It gets multi-day data from the following URL url = ( "https://api.open-meteo.com/v1/forecast?" f"latitude={latitude}&longitude={longitude}" "&daily=temperature_2m_max,temperature_2m_min" "&timezone=auto" )
(Or modify the URL in get_weather_data().
Create another new function to analyse_forecast(data)
Store the data in lists of dictionaries.
Find the max, min and average temp.
Create another function called display summary to display the results. 
    ''' 
# -----------------------------
# Main Program
# -----------------------------
def main():
    # Hard‑coded location (Cork)
    latitude = 51.9
    longitude = -8.5

    data = get_weather_data(latitude, longitude)
'''c) ask the user to enter their ideal temperature in degrees Celsuis.
pass this value to the display_weather function below.
Dont forget to modify the function to accept 2 input parameters. '''
    display_weather(data)

main()
