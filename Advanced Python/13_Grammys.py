"""
For many, music is so personal. We have created a playlist of songs that have won the “Song of the Year” 🏆 Grammy award in the past 5 years.

Let's play around with the data!

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)] 

First, use the filter() function to pick out the songs that are longer than 5 minutes (i.e., 5.00).

Next, use map() to convert all the durations of the songs in your playlist from minutes to seconds.

Lastly, add up the total playtime of the playlist with reduce().

Since map(), filter(), and reduce() all use function parameters, it may be helpful to define separate named functions for them:

A longer_than_five_minutes() function for filter().
A minutes_to_seconds() function for map().
An add_durations() function for reduce().
"""

from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55),
            ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

# Functions


def longer_than_five_minutes(x): return x[1] > 5
def minutes_to_seconds(x): return x[1] * 60
def add_durations(x, y): return x + y


above_five = filter(longer_than_five_minutes, playlist)
print(f"\033[1mFilter\033[0m")
print(list(above_five))

five_time = map(minutes_to_seconds, playlist)
print(f"\033[1mMap\033[0m")
print(list(five_time))

total = reduce(add_durations, map(minutes_to_seconds, playlist))
print(f"\033[1mReduce\033[0m")
print(f"{total:.2f}s")
