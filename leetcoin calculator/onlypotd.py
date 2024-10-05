from datetime import datetime, timedelta

def calculate_target_date(A: int, T: int, s: int) -> str:
    today = datetime.now()
    current_amount = A
    daily_income = 11
    
    # Initialize the current day counter
    days_since_start = 0
    
    while current_amount < T:
        # Increment day by day
        today += timedelta(days=1)
        days_since_start += 1  # Count days from the start
        
        # Add daily 11 rupees
        current_amount += daily_income
        
        # Check for 25th or 30th of the month to add bonuses
        if today.day == 25:
            current_amount += 25
        elif today.day == 30:
            current_amount += 50
            
        # Add the 30-day cycle bonus (30 rupees every 30 days since start date)
        if (days_since_start+s) % 30 == 0:
            current_amount += 30
    
    # Return the date when the target is reached
    return today.strftime("%Y-%m-%d")

# Example usage
s = int(input("Enter current streak\n")) # Initial days saved
A = int(input("Enter current leetcoins\n"))  # Current amount saved
T = int(input("Enter targetf leetcoins\n"))  # Target amount to reach
target_date = calculate_target_date(A, T, s)
print(f"You will reach {T} rupees on: {target_date}")
