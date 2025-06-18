import os
import csv


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


# Check if CSV file exists at the given path
# Arg: the file path (str)
# Returns: bool, True if file exists, False if not
def check_for_csv(path):

    return os.path.exists(path)


# Create CSV file if it doesn't exist
# If file is created, adds header to file
# Args: path for new file (str). Header to write (list)
def create_csv(path, header, init_data):

    if not check_for_csv(path):
        with open(path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerow(init_data)

