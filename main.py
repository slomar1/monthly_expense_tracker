"""
Monthly Expense Tracker - Main Program
Roadmap: See README.md for feature implementation plan
"""


# Imports
from utils import create_csv, get_number


# Constants
csv_path = f"data.csv"
csv_header = ["Month", "Gained", "Spent", "Savings"]


# Initialize csv file and get starting savings
def initialize_tracker():

    # Get initial settings
    initial_savings = get_number("How much do you have saved up? ")

    # Create CSV with header if doesn't exist
    create_csv(csv_path, csv_header)

initialize_tracker()