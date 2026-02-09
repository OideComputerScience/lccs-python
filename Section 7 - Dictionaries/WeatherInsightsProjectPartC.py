import requests

# -----------------------------
# Function: Get multi-day data
# -----------------------------
def get_forecast(latitude, longitude):
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )
    response = requests.get(url)
    return response.json()

# -----------------------------
# Function: Analyse forecast
# -----------------------------
def analyse_forecast(data):
    daily = data["daily"]   # dictionary containing lists

    max_temps = daily["temperature_2m_max"]
    min_temps = daily["temperature_2m_min"]

    highest = max(max_temps)
    lowest = min(min_temps)
    average = sum(max_temps) / len(max_temps)

    return {
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "days": len(max_temps)
    }

# -----------------------------
# Function: Display summary
# -----------------------------
def display_summary(results):
    print("5‑Day Weather Summary")
    print("---------------------")
    print("Highest temperature:", results["highest"], "°C")
    print("Lowest temperature:", results["lowest"], "°C")
    print("Average max temp:", round(results["average"], 1), "°C")
    print("Days analysed:", results["days"])

# -----------------------------
# Main Program
# -----------------------------
def main():
    latitude = 51.9
    longitude = -8.5

    data = get_forecast(latitude, longitude)
    results = analyse_forecast(data)
    display_summary(results)

main()
