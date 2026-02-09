import requests

response = requests.get("https://randomuser.me/api/")
data = response.json()

user = data["results"][0]

first = user["name"]["first"]
last = user["name"]["last"]
email = user["email"]
city = user["location"]["city"]
country = user["location"]["country"]

print("Random User Profile")
print("-------------------")
print("Name:", first, last)
print("Email:", email)
print("City:", city)
print("Country:", country)
