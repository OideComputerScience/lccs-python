#This is one python library that allows us to work with APIs.
import requests
#To work with APIs we need to know the URL that we are working with.
#This is a very small API call for demo purposes. 
response = requests.get("https://randomuser.me/api/")
#When you run this you will not see anything
#We can produce the result by printing as follows: 
#print(response.text)
# This is just printing raw data to the screen.
#If I try to use the following I will get an error. It is not usable as such.
#response.text[results]
'''What we received is raw data from the internet.
This is in JSON format, which is the standard format most APIs use.
JSON.
JSON looks like Python dictionaries but is not yet.
It is just a string of text that represents data. '''

#To work with this as a dictionary, Python needs to convert it.
#data=response.json()
#This is saying to take JSON data and convert it to python usable data.
#print(type(data)) #it tells us we have a class "dict" - it is a python dictionary.
#Now print the dictionary data
#print(data)
#It still looks simiar the what we had initially but it is now structured.
# This first thing to note is "results" is a list.We know it is a list because it uses []
#And within that list we have a dictionary. We know it is a dictionary because of {}
#print(type(data["results"]))
#print(type(data["results"][0]))# The type of the first element in the list

#If we want to see what keys are being used in the dictionary we can use the following:
#print(data.keys())
#This tells us the keys are called results and info.
#I am now going to access the first (and only) users info:
#user = data["results"][0] # user is a dictionary containing all the data
#print(user)
#Get the person's first name
#first = user["name"]["first"]
#print(first)
#Get hte person's last name
#last = user["name"]["last"]
#print(last)
#Get the email
#email = user["email"]
#print(email)
#Get the city
#city = user["location"]["city"]
#print(city)



