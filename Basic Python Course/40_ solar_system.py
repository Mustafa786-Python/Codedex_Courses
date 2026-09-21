

from math import pi , sqrt
from random import choice

planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]

random_planets = choice(planets)

r = 0

if random_planets == "Mercury":
    r = 2440
elif random_planets == "Venus":
    r = 6052
elif random_planets == "Earth":
    r = 6371
elif random_planets == "Mars":
    r = 3390
elif random_planets == "Saturn":
    r = 58232
else:
    print("Oops! An error occurred.")

print(f"The area of {random_planets} is {round(4*pi*(r**2), -5)}")
