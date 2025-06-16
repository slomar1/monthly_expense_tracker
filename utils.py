import os


# Check if CSV file exists.
def check_for_csv(path):

    return os.path.exists(path)


# Create CSV file if it doesn't exist
def create_csv(path):
    
    if not check_for_csv(path):
        with open(path, "w") as csvfile:
            pass  # File created, but no data added yet.


# Get a valid number from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, not letters or symbols.")
