"""
Monthly Expense Tracker - Main Program
Current version: 0.8
Roadmap: See readme.md for feature implementation plan
"""


# Imports
import csv
import os
from utils import create_csv, get_number, ask_to_continue, get_month, get_year, get_last_row_data


# Constants
csv_path = f"data.csv"
csv_header = ["Month", "Income", "Spent", "Net", "Savings"]\


# Initialize csv file and get starting savings
def initialize_tracker():

     # Check if CSV exists and has data
    if os.path.exists(csv_path):
        last_date, last_savings = get_last_row_data(csv_path)
        print(f"\nResuming from last saved month: {last_date}")

        # Extract year and month from last date
        start_year, start_month = map(int, last_date.split('-'))

        # Calculate next month
        start_month += 1
        if start_month > 12:
            start_month = 1
            start_year += 1

        savings = last_savings

    else:
        # New File setup
        savings = get_number("\nHow much do you have saved up?: ")
        start_year = get_year("\nPlease type in the year you are starting count from: ")
        start_month = get_month("What month of the  year will you be stating off with? ")

        # Create CSV with header only
        create_csv(csv_path, csv_header)


    # Add data to csv per month
    while True:

        # Get monthly data
        month_made = get_number("How much did you make this month?: ")
        rent = get_number("How much have you spent on housing (rent, utilities, etc.) this month?: ")
        food = get_number("How much have you spent on groceries this month?: ")
        gas = get_number("How much have you spent on transportation (gas, maintenece, public transport, etc.) this month?: ")
        outside = get_number("How much have you spent on lesuire (restaurants, takeout, clothing, etc.) this month?: ")
        edu = get_number("How much have you spent on education (courses, books, etc.) this month?: ")
        other = get_number("How much money have you spent miscellaneously (gym, entertainment, grooming, etc.) this month?: ")

        # Calculate monthly totals
        month_spent = rent + food + gas + outside + edu + other
        print(f"\nYou have spent ${month_spent:.2f} in total this month. ")
        month_net = month_made - month_spent
        print(f"\nYou have made a net total of ${month_net:.2f} this month. ")
        savings += month_net
        print(f"\nTaking your net balance into account, your total savings now lie at ${savings:.2f}. ")

        # create new row for current month
        current_date = f"{start_year}-{start_month}"
        current_row = [current_date, month_made, month_spent, month_net, savings]

        # Append to csv
        with open(csv_path, "a", newline="") as month_file:
            writer = csv.writer(month_file)
            writer.writerow(current_row)

        # Ask user to continue to next month or break
        if not ask_to_continue("\nWould you like to log data for another month or stop? y/n: "):
            print("\nThank you for trying my monthly expense tracker. " \
            "All data saved to csv file within the program.")
            break
        
        # Increment for next month if user wants
        pass
        start_month += 1
        if start_month > 12:
            start_month = 1
            start_year  += 1
    

# Run main.py
if __name__ == "__main__":
    print("\nHello. Welcome to my monthly expense tracker, where you will" \
    "be able log your financial data per month")
    initialize_tracker()