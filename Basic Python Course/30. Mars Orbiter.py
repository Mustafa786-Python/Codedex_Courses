"""
Define a function named distance_to_miles() that converts a distance from kilometers to miles. It should:

Take in one parameter named distance (the distance in kilometers).
Print the distance in miles.
After, call the function and use 10000 as the argument.
"""


def distance_to_miles(kilometer):
    miles = f"{kilometer/1.609} miles"
    return miles


print(distance_to_miles(10000))
