# Event: LCCS Python Fundamental Skills Evening Workshop
# Date: Feb 2026
# Author: Oide Computer Science
# eMail: computerscience@oide.ie
# Purpose: Dictionary Programming Exercises 7.1
# Q1(b) solution

#Look at exercise p263/4 in Python manual 
car = dict( {
    'reg': "131 CN 6439",
    'make': "Audi",
    'model' : "A6",
    'year' : 2013,
    'kms' : 52739,
    'colour': "Silver",
    'deisel': True,
})
print(car)

#1f
currentYear=2026
print(car['kms']/(currentYear - car['year'])) # kms per year

#THE REMAINDER OF THIS EXAMPLE SHOWS ITERATION THROUGH DICTIONARIES
'''
# The keys are reg, make, .... deisel
for k in car.keys():
    print(k)

# The values are 131 CN 6439, Audi, .... True
for v in car.values():
    print(v)
'''