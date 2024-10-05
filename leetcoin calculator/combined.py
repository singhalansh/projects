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

def calculate_target_date_potd(A: int, T: int, s: int) -> str:
    """
    Calculate the date when the target will be reached, considering POTD bonuses.
    
    A: Current total amount saved
    T: Target amount to reach
    s: Streak of daily POTD completions
    """
    today = datetime.now()
    current_amount = A
    daily_income = 11  # Daily income from POTD
    
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
        if (days_since_start + s) % 30 == 0:
            current_amount += 30
    
    # Return the date when the target is reached
    return today.strftime("%Y-%m-%d")

def is_weekend(date):
    """
    Check if a given date falls on a weekend (Saturday or Sunday).
    """
    return date.weekday() in [5, 6]

def calculate_weekend_bonus(date):
    """
    Calculate the weekend bonus based on which weekend it is in the current month.
    """
    day = date.day
    if is_weekend(date):
        # Calculate the week number (1st weekend, 2nd weekend, etc.)
        week_number = (day - 1) // 7 + 1
        if week_number == 1 or week_number == 3:
            return 5  # 1st and 3rd weekends
        elif week_number == 2 or week_number == 4:
            return 40  # 2nd and 4th weekends
    return 0  # No bonus if it's not a weekend

def calculate_target_date_potd_contest(A: int, T: int, s: int) -> str:
    """
    Calculate the date when the target will be reached, considering POTD, weekend, and contest bonuses.
    
    A: Current total amount saved
    T: Target amount to reach
    s: Streak of daily POTD completions
    """
    today = datetime.now()
    current_amount = A
    daily_income = 11  # Daily income from POTD
    
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

# Menu to choose between the three sections
def main():
    print("Choose an option:\n1. Daily Check-ins\n2. POTD\n3. POTD + Contests")
    choice = int(input("Enter the number corresponding to your choice: "))

    S = int(input("Enter current streak: "))  # Streak or days saved
    A = int(input("Enter current leetcoins: "))  # Current amount saved
    T = int(input("Enter target leetcoins: "))  # Target amount to reach

    if choice == 1:
        days_needed = days_to_target(S, A, T)
        target_date = datetime.today() + timedelta(days=days_needed)
        print(f"Number of days needed to reach the target: {days_needed}")
        print(f"Target date: {target_date.strftime('%Y-%m-%d')}")
    
    elif choice == 2:
        target_date = calculate_target_date_potd(A, T, S)
        print(f"You will reach {T} leetcoins on: {target_date}")
    
    elif choice == 3:
        target_date = calculate_target_date_potd_contest(A, T, S)
        print(f"You will reach {T} leetcoins on: {target_date}")
    
    else:
        print("Invalid choice, please try again.")

# Run the main function
if __name__ == "__main__":
    main()
