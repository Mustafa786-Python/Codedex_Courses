"""
Let’s go back to fruits! 🫐🍇🍌🍓🍒

Grocery shopping is great until you forget what was on your list. 😥

Before you head out, your best friend ask you to pick up some fruit for her too. Let's combine the lists!

Create two sets representing your favorite fruits and your best friend's favorite fruits.
Print the union of the two sets.
Print the intersection of the two sets.
Have fun with it, check if the same fruit is in both sets or see the <difference> in both sets.

Remember: tomatoes are fruits! 🍅
"""

my_fruits = {"Mango", "Strawbeeet", "Banana"}
friends_fruits = {"Apricot", "Grape", "Banana"}

fruits_set_uni = my_fruits.union(friends_fruits)
fruits_set_int = my_fruits.intersection(friends_fruits)

print(f"""Union: {fruits_set_uni}
Intersection: {fruits_set_int}""")
