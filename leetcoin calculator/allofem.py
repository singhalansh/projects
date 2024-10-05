from datetime import datetime, timedelta

def is_weekend(date):
    # Check if the date is a Saturday (5) or Sunday (6)
    return date.weekday() in [5, 6]

def calculate_weekend_bonus(date):
    # Find out which weekend it is in the current month
    day = date.day
    if is_weekend(date):
        # Calculate the week number (1st weekend, 2nd weekend, etc.)
        week_number = (day - 1) // 7 + 1
        if week_number == 1 or week_number == 3:
            return 5  # 1st and 3rd weekends
        elif week_number == 2 or week_number == 4:
            return 40  # 2nd and 4th weekends
    return 0  # No bonus if it's not a weekend

def calculate_target_date(A: int, T: int, s: int) -> str:
    today = datetime.now()
    current_amount = A
    daily_income = 11
    
    # Initialize the current day counter
    days_since_start = 0
    
    while current_amount < T:
        # Increment the day by 1
        today += timedelta(days=1)
        days_since_start += 1  # Count days since the start of saving
        
        # Add daily income
        current_amount += daily_income
        
        # Check for the 25th and 30th of the month
        if today.day == 25:
            current_amount += 25
        elif today.day == 30:
            current_amount += 50
            
        # Add the 30-day cycle bonus
        if (days_since_start + s) % 30 == 0:
            current_amount += 30
        
        # Check for weekend bonuses
        current_amount += calculate_weekend_bonus(today)
    
    # Return the date when the target is reached
    return today.strftime("%Y-%m-%d")

# Example usage
s = int(input("Enter the number of days ago you started saving: "))  # Initial days saved
A = int(input("Enter your current amount of rupees: "))  # Current amount saved
T = int(input("Enter the target amount of rupees: "))  # Target amount to reach

target_date = calculate_target_date(A, T, s)
print(f"You will reach {T} rupees on: {target_date}")
