import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate savings trend line chart
def plot_savings_trend(csv_path):

    df = pd.read_csv(csv_path)
        
        # Configure plot
    plt.figure(figsize=(10, 6))
    plt.plot(df["Month"], df["Savings"], marker='o', linestyle='-')
        
    # Formatting
    plt.title("Savings Trend Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Savings ($)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
        
    plt.show()


# Generate income vs expenses bar chart
def plot_income_vs_expenses(csv_path):

    df = pd.read_csv(csv_path)

    months = df["Month"]
    income = df["Income"]
    expenses = df["Spent"]

    indices = np.arange(len(months))
    bar_width = 0.35

    # Configure plot
    plt.figure(figsize=(12, 6))
    plt.bar(indices - bar_width/2, income, width=bar_width, 
            color='#2ecc71', label='Income')
    plt.bar(indices + bar_width/2, expenses, width=bar_width, 
            color='#e74c3c', label='Expenses')
    
    # Formatting
    plt.title("Income vs Expenses", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Amount ($)", fontsize=12)
    plt.xticks(indices, months, rotation=45)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()