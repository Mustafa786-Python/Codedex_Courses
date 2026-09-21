"""
Create a drive_thru.py program with your favorite fast food chain's menu.

Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!

For example, if you called the function with:

Argument value 1, it could return '🍔 Cheeseburger'.
Argument value 2, it could return '🍟 Fries'.
Argument value 3, it could return '🥤 Soda'.
Argument value 4, it could return '🍦 Ice Cream'.
Argument value 5, it could return '🍪 Cookie'.
Make sure to call this function a few times to make sure that it works!

Lastly, let's do the following:

Create a welcome menu and put that in a welcome() function.
Create a main program that takes in user input with input().
"""


def get_item(x):
    if x == 1:
        menu = "🍔 Cheeseburger"
    elif x == 2:
        menu = "🍟 Fries"
        return menu
    elif x == 3:
        menu = "🥤 Soda"
        return menu
    elif x == 4:
        menu = "🍦 Ice Cream"
        return menu
    elif x == 5:
        menu = "🍪 Cookie"
        return menu
    else:
        menu = "Sorry, out of list"
        return menu


def welcome():
    print("""

Press 1, for  '🍔 Cheeseburger'.
Press 2, for  '🍟 Fries'.
Press 3, for  '🥤 Soda'.
Press 4, for  '🍦 Ice Cream'.
Press 5, for  '🍪 Cookie'.
""")


welcome()


option = int(input("What do you want to order: "))
print(get_item(option))
