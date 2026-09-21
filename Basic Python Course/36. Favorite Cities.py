"""
Ever wonder how many people live in New York City? What about London?

Create a favorite_cities.py program.

Let's make a City class that uses the __init__() method to define the following attributes:

name (string)
country (string)
population (integer rounded to the nearest thousand people)
landmarks (list of strings)
Next, create an object for your hometown and assign the attributes above.

Lastly, create another object for the city that you've always wanted to visit!

Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.
"""


class City:

    def __init__(self, name, country, population, landmark, nickname, founding_year, mayor):
        self.name = name
        self.country = country
        self.population = population
        self.landmark = landmark
        self.nickname = nickname
        self.founding_year = founding_year
        self.mayor = mayor


karachi = City("Karachi", "Pakistan", 25000000, "Mazaar e Quaid",
               "City of Lights", 1729, " Murtaza Wahab")
shenzen = City("Shenzen", "China", 17980000, "Ping An Finance Centre",
               "China's Silicon Valley", 1979, "Li Yun")

kar = vars(karachi)
shen = vars(shenzen)

print(type(kar))
for i in kar.items():
    print(i)
print()
print("For Shenzen")
for i in shen.items():
    print(i)
