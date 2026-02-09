# LCCS computerscience@oide.ie
# Feb 2026
# A program to demonstrate dictionary indexing - errors

d = {
    "OMG" : "Oh My God!",
    "LOL" : "Laugh out Loud",
    "IMHO" : "In My Humble Opinion",
}

print(d)
#print(d["LOL"])
#print(d['LOLL']) # syntax error: Key does not exist
#print)d['omg']) #to demonstrate keys are case sensitive.
#########################
# Alternative way to add an element to a dictionary
# d = {
#     "OMG":"Oh My God!",
#     "LOL":"Laugh Out Loud"
#     }
# 
# d["IMHO"] = "In My Humble Opinion"
#We can print an entire list
#print(d)
#######################################
'''
#We can use dictionaries with a combination of data types.
#for example it does not have to be all strings as above.
numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}
print(numbers)
'''

'''
#we can also have keys that are unrelated to each other.
#A dictionary can have a mixture of datatypes. 
#For example look at the student details below.

student= {
    "id":"abc123",
    "age": 17,
    "grant": False,
    "gpa": 76.2
    }
    
print(student)
'''
#################
'''
#keys can also be variables.
#We have already declared dictionary d above.
#  now we will declare a variable called key and assign the string "OMG" to it.
key = "OMG" #declares a variable
value = d[key] #teh contents of key is the index
print(value)
'''