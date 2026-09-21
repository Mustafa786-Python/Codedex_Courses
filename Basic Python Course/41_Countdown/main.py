import datetime
import bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2026, 9, 1)
born_date = datetime.date(2009, 3, 31)

time_difference = next_birthday - today
days_away = time_difference.days
days_spent = born_date - today
print(days_spent.days)

# Logic of days
if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {days_away} days away!")
