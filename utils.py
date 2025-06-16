import os
import csv


# Check if CSV file exists at the given path
# Arg: the file path (str)
# Returns: bool, True if file exists, False if not
def check_for_csv(path):

    return os.path.exists(path)


# Create CSV file if it doesn't exist
# If file is created, adds header to file
# Args: path for new file (str). Header (list) to write if provided
def create_csv(path, header, ):

    if not check_for_csv(path):
        with open(path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)



# Prompt user for valid numberical input
# Arg: prompt (str) to display to user
# Returns: float, calid number ffrom user
def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, not letters or symbols.")