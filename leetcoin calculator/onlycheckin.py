from datetime import datetime, timedelta

def days_to_target(S, A, T, d=1, p=30, b=30):
    """
    Calculate the number of days needed to reach the target amount T.
    
    S: Initial days saved (so far)
    A: Current total amount saved
    T: Target amount to reach
    d: Daily savings (default is 1)
    p: Period of bonus (default is 30)
    b: Bonus amount after every 'p' days (default is 30)
    """
    
    # Calculate remaining amount to reach the target
    remaining_amount = T - A
    days_needed = 0  # Additional days needed
    
    # Simulate day-by-day savings until the target is reached
    total_saved = A  # Start with the current amount saved
    
    while total_saved < T:
        days_needed += 1
        total_saved += d  # Add daily savings
        
        # Check if it's time for a bonus (every 'p' days)
        if (S + days_needed) % p == 0:
            total_saved += b
    
    return days_needed

# Current date (today's date)
current_date = datetime.today()

# Example Inputs
S = int(input("Enter current streak")) # Initial days saved
A = int(input("Enter current leetcoins"))  # Current amount saved
T = int(input("Enter targer leetcoins"))  # Target amount to reach

# Using the function to calculate the number of days needed
days_needed = days_to_target(S, A, T)

# Calculate the target date by adding the required days to the current date
target_date = current_date + timedelta(days=days_needed)

# Output results
print(f"Number of days needed to reach the target: {days_needed}")
print(f"Target date to reach the target amount: {target_date.strftime('%Y-%m-%d')}")
