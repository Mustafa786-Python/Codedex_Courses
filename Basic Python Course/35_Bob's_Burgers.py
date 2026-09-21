"""
In the last exercise, we created a Restaurant class.

In a new file called bobs_burgers.py, create an instance of the Restaurant class called bobs_burgers with the following attributes:

'Bob\'s Burgers'
'American Diner'
4.7
False
Once you do that, create two more instances of the Restaurant class with your favorite dinner spots nearby.

Then, use print(vars()) to output each of the three restaurants!
"""


class Restaurant:
    name = ""
    category = ""
    rating = 0.00
    delivery = True

bobs_burgers = Restaurant()

bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

kabab_jees = Restaurant()

kabab_jees.name = "Kabab Jees"
kabab_jees.category = "Kabab"
kabab_jees.rating = 4.5
kabab_jees.delivery = True

shaheen_shin = Restaurant()

shaheen_shin.name = "Shahheen Shinwari"
shaheen_shin.category = "Tikka"
shaheen_shin.rating = 5
shaheen_shin.delivery = True

print(vars(bobs_burgers))
print(vars(kabab_jees))
print(vars(shaheen_shin))


