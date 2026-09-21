"""
Create a new file called pokedex.py.

Next, let's define a Pokemon class with the following attributes:

entry (integer)
name (string)
type (list of strings)
description (string)
is_caught (boolean)
Note: Make sure to use the __init__() method.

Next, create an instance method called .speak() that prints a string of the sound a Pokémon makes. A Pokémon usually just says their name, so make the .speak() simply print out their name twice!

Then, create another instance method called .display_details() that prints the attributes of a Pokemon object like the following:

''
Entry Number: 25
Name: Pikachu
Type: Electric
Description: It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
Pikachu has already been caught!
''

Lastly, create three Pokemon class objects and use the .speak() or .display_details() instance methods for each one.

For more information about any Pokémon you want to add, see the Pokédex!

Are you ready to earn the next badge?

Bonus: For all the super fans, try and add more attributes to the Pokemon class definition, like level, region, height, or weight
"""


class Pokemon:
    def __init__(self, entry, name, type, description, is_caught, height, weight):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = is_caught
        self.height = height
        self.weight = weight

    def speak(self):
        print(f"{self.name.title()}! {self.name.title()}!", end="\n\n")

    def display_details(self):
        print(f"\033[1mDetails\033[0m")
        if self.is_caught:
            print(f"""Entry Number: {self.entry}
Name: {self.name.title()}
Type: {self.type}
Height: {self.height}
Weightt: {self.weight}
Description: {self.description}
{self.name.title()} has already been caught!
""")
        else:
            print(f"""Entry Number: {self.entry}
Name: {self.name}
Type: {self.type}
Height: {self.height}
Weightt: {self.weight}
Description: {self.description}
{self.name.title()} has not been caught yet!

""")


raichu = Pokemon(26, "Raichu", "Electric",
                 "It fires bolts of electricity from the tip of its tail and from the spiky tufts of fur growing out of its temples.", False, "3'03", "57.3 lbs")
raichu.speak()
raichu.display_details()

pikachu = Pokemon(25, "Pikachu", "Electric",
                  "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True, "1'04", "13.2 lbs")
pikachu.speak()
pikachu.display_details()

charmander = Pokemon(4, "Charmander", "Fire",
                     "The flame on its tail shows the strength of its life force.", False, "2'00", "18.7 lbs")
charmander.speak()
charmander.display_details()

squirtle = Pokemon(7, "Squirtle", "Water",
                   "After birth, its back swells and hardens into a shell.", True, "1'08", "19.8 lbs")
squirtle.speak()
squirtle.display_details()
