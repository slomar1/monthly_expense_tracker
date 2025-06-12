import pandas
import matplotlib
import csv
import os
from datetime import date


# Mark current year and define path for file with that year.
current_year = date.today().year
csv_path = f"{current_year}_data.csv"


# Check if CSV file exists.
def check_for_csv(path):

    return os.path.exists(path)


# Create CSV file if it doesn't exist
def create_csv(path):
    
    if not check_for_csv(path):  # Check if the file doesn't exist.
        with open(path, "w") as csvfile:
            pass  # File created, but no data added yet.

create_csv(csv_path)