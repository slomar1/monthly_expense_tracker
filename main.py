import pandas
import matplotlib
import csv
from datetime import date
from file_utils import check_for_csv, create_csv


# Mark current year and define path for file with that year.
current_year = date.today().year
csv_path = f"{current_year}_data.csv"


# Create CSV if it doesn't exist
create_csv(csv_path)