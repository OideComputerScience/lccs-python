import requests

# -----------------------------
# Function: Get weather data
# -----------------------------
def get_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    return response.json()

# -----------------------------
# Function: Analyse weather
# -----------------------------
def analyse_weather(data, ideal_temp):
    weather = data["current_weather"]
    temp = weather["temperature"]
    wind = weather["windspeed"]

    # Simple comparisons
    temp_ok = temp >= ideal_temp
    windy = wind > 20

    return {
        "temp": temp,
        "wind": wind,
        "temp_ok": temp_ok,
        "windy": windy
    }

# -----------------------------
# Function: Display report
# -----------------------------
def display_report(results):
    print("Weather Report")
    print("--------------")
    print("Temperature:", results["temp"], "°C")
    print("Wind Speed:", results["wind"], "km/h")

    if results["temp_ok"]:
        print("It is warm enough for outdoor activities.")
    else:
        print("It is colder than your ideal temperature.")

    if results["windy"]:
        print("Warning: It is quite windy.")
    else:
        print("Wind levels are normal.")

# -----------------------------
# Main Program
# -----------------------------
def main():
    # User chooses ideal temperature
    ideal = float(input("Enter your ideal temperature (°C): "))

    # Hard‑coded location (Cork)
    data = get_weather_data(51.9, -8.5)

    results = analyse_weather(data, ideal)
    display_report(results)

main()
