"""
We've all seen, perhaps bought, one of our favorite products with a "Bestseller" sticker. 🏅

Let’s write a program to read a CSV file and find the best-selling book of all time. 🔍

Download this CSV file of all-time bestselling books data!
Open the Bestseller - Sheet1.csv file in "read" mode.
Use the CSV reader to navigate through the data and find the book with the highest sales, via the sales in millions column.
Create a new file called bestseller_info.csv with the CSV writer.
In the new file, use .writerow() to add new CSV data.
Up next, let’s learn about what to do in the face of the unexpected, we'll be exploring error handling.
"""

import csv

with open("Bestseller - Sheet1.csv", "r", encoding="utf8") as file:
    reader = csv.DictReader(file)

    best_book = None
    highest_sales = 0

    for row in reader:
        sales =  float(row["sales in millions"])

        if sales > highest_sales:
            highest_sales = sales
            best_book = row

            with open("best_book.csv", "w") as file:
                writer = csv.writer(file)

                writer.writerow(["Book", "Sales", "Sales in Millions"])
                writer.writerow([f"""
{best_book["Book"]}
{best_book["Author"]}
{best_book["sales in millions"]}
"""
            ])