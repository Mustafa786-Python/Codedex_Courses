"""
Imagine you have a dataset with information about your favorite sports team. 🏀🎾⚽ The goal is to use Python's data structures to organize and analyze this data.

If you can't think of any, feel free to use the Super Bowl 2024 champions, the Kansas City Chiefs. 🏈

As a data analyst for the Kansas City Chiefs you have been given a dataset containing information about the players, their positions, and some game statistics.

Let's start analyzing!

Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name,' 'position,' and 'jersey number.'
Print out a list of all player positions in the dataset.
Choose a player and update their game statistics in the dataset.
Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.
"""

players = [
    {
        "name": "Patrick Mahomes",
        "position": "Quarterback",
                "jersey_number": 15,
                "yards_gained": 300,
                "touchdowns": 3,
    },
    {
        "name": "Tyreek Hill",
        "position": "Wide Receiver",
                "jersey_number": 10,
                "yards_gained": 150,
                "touchdowns": 2,
    },
    {
        "name": "Travis Kelce",
        "position": "Tight End",
                "jersey_number": 87,
                "yards_gained": 100,
                "touchdowns": 1,
    },
]

for n in players:
    print(n["position"])

players[1]["yards_gained"] = 120
players[1]["touchdowns"] = 5

print(players[1])

avg = 0
tavg = 0
for n in players:
    avg += n["yards_gained"]
    tavg += n["touchdowns"]

print(f"The average Yards Gained are: {avg} and Touch Downs are gained {tavg}")
