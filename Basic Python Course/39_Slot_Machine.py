import random


#Creating Function
def play():
    symbols = ['🍒', ' 🍇', '🍉', '7️⃣']

   

    results = random.choices(symbols, k=3)

    if results == ['7️⃣', '7️⃣', '7️⃣']:
        print(results)
        print("Jackpot! 💰")

    else:
        print(results)
        print("Thanks for playing")
    print("-" * 40)

print("-" * 40)
print(f"\033[1m         Welcome to Slot Machine!\033[0m")

#Asking for play
while True:
    ask = input("Do you want to: (Y / N ): ").strip().upper()
    if ask == "N" or ask == "Y":
        break
    else:
        print("Only Y / N ")

#Applying Condition
if ask == "Y":
    while True:
        play()

        while True:
            ask2 = input("Do you want to play again: (Y / N ): ").strip().upper()
            if ask2 == "N" or ask2 == "Y":
                break

        #Breaking Outerloop
        if ask2 == "N":
            break

else:
    print("Thanks for Coming")