import os


# Check if CSV file exists.
def check_for_csv(path):

    return os.path.exists(path)


# Create CSV file if it doesn't exist
def create_csv(path):
    
    if not check_for_csv(path):
        with open(path, "w") as csvfile:
            pass  # File created, but no data added yet.