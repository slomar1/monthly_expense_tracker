import os
import csv
import pandas as pd


# Prompt user for valid numberical input
# Arg: prompt to display to user (str)
# Returns: float, valid number from user
def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, not letters or symbols.")


# Prompt user for valid year input
# Arg: prompt to display to user (str)
# Returns: int, valid year from user
def get_year(prompt):
     
     while True:
        try:
            year = int(input(prompt))
            if year < 0 or year > 9999:
                print("Please neter a valid year, from 0 AD to 9999 AD. ")
            else:
                return year
        except ValueError:
            print("Please enter a number, not letters or symbols.")


# Prompt user for valid month input
# Arg: prompt to display to user (str)
# Returns: int, valid month from user
def get_month(prompt):
     
     while True:
        try:
            month = int(input(prompt))
            if month < 1 or month > 12:
                print("Please enter a valid month, from 1 to 12.")
            else:
                return month
        except ValueError:
            print("Please enter a number, not letters or symbols.")
    

# Prompt user to add another month or stop program
# Arg: prompt to display to user (str)
def ask_to_continue(prompt):

    while True:
        response = input(prompt).strip().lower()
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid input. Please type 'y' for yes, 'n' for no: ")

    
# Create CSV file if it doesn't exist
# If file is created, adds header to file
# Args: path for new file (str). Header to write (list)
def create_csv(path, header):

    with open(path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)


# Get last row data from CSV with pandas
# Args: path for new file (str)
def get_last_row_data(path):

    try:
        df = pd.read_csv(path)

        # Get last row
        last_row = df.iloc[-1]

        # Extract date and savings
        last_date = last_row["Month"]
        last_savings = last_row ["Savings"]

        return last_date, last_savings
    
    except Exception as e:
        print(f"Error reading data: {e}")
        return None, None