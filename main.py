import pandas
import matplotlib
import csv
from datetime import date

from utils import create_csv, get_number


# Mark current year and define path for file with that year.
current_year = date.today().year
csv_path = f"{current_year}_data.csv"


# Create CSV if it doesn't exist
create_csv(csv_path)


# Main program
savings = get_number("How much do you have saved up? ")
savings_history = [savings]
print(savings_history)