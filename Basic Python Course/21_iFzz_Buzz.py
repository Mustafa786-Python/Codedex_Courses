"""
FizzBuzz
Prints numbers 1 to 100, but:
  - multiples of 3 print "Fizz"
  - multiples of 5 print "Buzz"
  - multiples of both 3 and 5 print "FizzBuzz"
"""

for num in range(1, 100 + 1):
    if num % 15 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 15 == 0:
        print("Buzz")

    else:
        print(num)



