import pandas
import matplotlib
import csv
from datetime import date

from utils import create_csv, get_number


# Main program. Set up here so the user can input savings which will be added onto month 0 of csv.
savings = get_number("How much do you have saved up? ")


# Mark current year and define path for file with that year. Needed to create csv file and nothig else.
current_year = date.today().year
csv_path = f"{current_year}_data.csv"


# Header for csv file. Add this with the create_csv function in utils
# Includes current month user is detailing, money made and spent, total balance of savings.
header = ["Month", "Gained", "Spent", "Savings"]


"""
Here I need to add the prompts for user input askign them how much they made and spent that month
starting month 1, since month 0 should just me zero on everything except initial savings input.
Then I need to find a way for the month to end and a new month to start (month 2 and all the new made/spent data).
I need to do math to calculate the savings at the end of each month.
Starting a new month and getting the computer to recongize it might be tricky.
"""


# Create CSV if it doesn't exist
create_csv(csv_path)


# Main program
savings = get_number("How much do you have saved up? ")
savings_history = [savings]
print(savings_history)


"""
Okay I have the basic first steps here.
1. I need to add data to the 2025_data.csv file created, for now just the header.
2. I need to add the initial savings amount ('month 0, 0 spent, 0 made, x savings') maybe with same create_csv function.
3. I need to add prompts for user input asking them how much they made and spent that month.
4. I need to do math to calculate total savings balance left at the end of that month.
5. I need to add on to that file the months as the user goes on, eg. 'month 1, x spent, x made, x savings, month 2...'
and I need to perform math on the previous month's values to calculate the amout of savings for new month.
6. I need the program to be able to read the file and add to it after code is ran for a second time, eg. not
restart from zero asking for savings, just be able to continue from where user left off.
7. I then have to create a new file for 2026. wait new idea just hit. Allow user to put what month and year
they are starting from. maybe they want to begin from Feb 2023 or something. That might make it complicated as I 
will have to see it datetime knows the order of the months, but year basically allow user to start in any month of any
year and incrimentally add data from that point on
8. I need to use pandas for someting idk yet and matplotlib to visualize this data
9. finally put this project to bed and possibly start with machine learning, maybe not my mlb app yet, but a
skipping stone toward that.

Idk how realistic it is, but I'll try to implement one of these features once every day I code, so I should me finished
ideally in 8 coding sessions.
"""