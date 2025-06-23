"""
Monthly Expense Tracker - Main Program
Current version: 0.9
Roadmap: See readme.md for feature implementation plan
"""


# Imports
import csv
import os
from utils import create_csv, get_number, ask_to_continue, get_month, get_year, get_last_row_data
from visualization import plot_savings_trend, plot_income_vs_expenses


# Constants
csv_path = "data.csv"
csv_header = ["Month", "Income", "Spent", "Net", "Savings"]\



# Initialize the expense tracker workflow
# Checks for existing data file
# Resumes from last entry or starts new
# Handles monthly data collection
def initialize_tracker():

     # Check if CSV exists and offers resume option
    if os.path.exists(csv_path):
        last_date, last_savings = get_last_row_data(csv_path)

        if ask_to_continue(f"\nResume from last entry ({last_date})? (y/n): "):
            start_year, start_month = map(int, last_date.split('-'))

            # Calculate next month
            start_month += 1
            if start_month > 12:
                start_month = 1
                start_year += 1
            
            savings = last_savings


    else:
        # New File setup
        print("Starting new tracking session. ")
        create_csv(csv_path, csv_header)

        savings = get_number("\nHow much do you have saved up?: ")
        start_year = get_year("\nPlease type in the year you are starting count from: ")
        start_month = get_month("What month of the  year will you be stating off with? ")


    # Add data to csv per month
    while True:

        # Get monthly data
        print(f"Please input the following data for {start_year}-{start_month}. ")

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

        # Offer visualization
        if ask_to_continue("Would you like to end the program and View financial visualizations? (y/n): "):
            print(f"All data saved to: {os.path.abspath(csv_path)}")
            plot_savings_trend(csv_path)
            plot_income_vs_expenses(csv_path)
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