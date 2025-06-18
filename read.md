This is  reworked, expanded version of my monthly expense tracker.
This one actually uses some data tools.
Forgive the embarrassing code, I am still just learining.

I finally fixed the import issue.
Here's a new roadmap of the things I need to do:


Phase 1: Core Functionality (✅)

    Initialize CSV with Header and Month 0 Data (✅)
        Modify create_csv to write header (✅ in session 1)
        Add "Month 0" row with initial savings data when creating new file (✅ in session 2)

    Monthly Data Collection (✅)
        Implement function to collect monthly income/expense data (✅ in session 2)
        Calculate monthly savings: previous savings + income - expenses (✅ in session 2)
        Comprehensive input validation (✅ in session 3)

    CSV Appending System (✅)
        Create function to append new monthly data to CSV (✅ in session 2)
        Automatically increment month number based on existing data (✅ in session 2)
        Handle first month after initial savings (Month 1) (✅ in session 2)
        Add text to guide the user (✅ in session 2)


Phase 2: Time Management (✅)

    Date-Based Tracking
        Implement actual month/year tracking (✅ in session 3)
        Allow manual date entry for month and year (✅ in session 3)
        Carry over final savings from previous year (✅ in session 3)


Phase 3: Data Analysis

    CSV Reading & Basic Stats
        Add ability to add from last month instead of restarting with new file
        Implement pandas CSV reading
        Show monthly averages

    Data Visualization
        Create savings trend line graph
        Generate income vs expense bar charts
        Add monthly comparison visuals