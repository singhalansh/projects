import tkinter as tk
from datetime import datetime, timedelta
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
reward_prices = {
         'Time Travel Ticket': 70,
        '30-Day Premium Subscription': 5000,
        'LeetCode T-Shirt': 6000,
        'LeetCode Cap': 5400,
        'LeetCode Kit': 7800,
        'LeetCode Laptop Sleeve': 8000,
        'LeetCode Big O Notebook': 9900,
        'LeetCode Hoodie': 9000
    }

# Function to calculate target date based on user inputs
def calculate_leetcoins_POTD(current_coins, streak, reward):
    today = datetime.now()
    
   
    reward_amount = reward_prices[reward]
    
    daily_income = 11
    current_amount = int(current_coins)
    streak = int(streak)
    
    days_since_start = 0
    while current_amount < reward_amount:
        today += timedelta(days=1)
        days_since_start += 1
        current_amount += daily_income

        # Bonuses based on days
        if today.day == 25:
            current_amount += 25
        elif today.day == 30:
            current_amount += 50

        # Add 30-day streak bonus
        if (days_since_start + streak) % 30 == 0:
            current_amount += 30

    return today.strftime(" %b %d %Y")

def calculate_leetcoins_checkin(current_coins, streak, reward):
    today = datetime.now()
    
    
    reward_amount = reward_prices[reward]
    
    daily_income = 1
    current_amount = int(current_coins)
    streak = int(streak)
    
    days_since_start = 0
    while current_amount < reward_amount:
        today += timedelta(days=1)
        days_since_start += 1
        current_amount += daily_income

        # Add 30-day streak bonus
        if (days_since_start + streak) % 30 == 0:
            current_amount += 30

    return today.strftime(" %b %d %Y")

def is_weekend(date):
    return date.weekday() in [5, 6]

def calculate_weekend_bonus(date):
    day = date.day
    if is_weekend(date):
        week_number = (day - 1) // 7 + 1
        if week_number == 1 or week_number == 3:
            return 5  # 1st and 3rd weekends
        elif week_number == 2 or week_number == 4:
            return 40  # 2nd and 4th weekends
    return 0

def calculate_leetcoins_all(current_coins, reward, streak) -> str:
    today = datetime.now()
    current_amount = current_coins
    daily_income = 11
    
    
    reward_amount = reward_prices[reward]
    
    days_since_start = 0
    
    while current_amount < reward_amount:
        today += timedelta(days=1)
        days_since_start += 1
        current_amount += daily_income
        
        if today.day == 25:
            current_amount += 25
        elif today.day == 30:
            current_amount += 50
            
        if (days_since_start + streak) % 30 == 0:
            current_amount += 30
            
        current_amount += calculate_weekend_bonus(today)
    
    return today.strftime(" %b %d %Y")

# Function for the "Calculate" button
def on_calculate():
    current_coins = int(current_coins_entry.get())
    streak = int(streak_entry.get())
    reward = reward_combobox.get()

    # Calculate target dates for the three scenarios
    date_1 = calculate_leetcoins_all(current_coins, reward, streak)
    date_2 = calculate_leetcoins_POTD(current_coins, streak, reward)
    date_3 = calculate_leetcoins_checkin(current_coins, streak, reward)

    # Update the result labels
    result_1.config(text=f"You can redeem your reward on {date_1}")
    result_2.config(text=f"You can redeem your reward on {date_2}")
    result_3.config(text=f"You can redeem your reward on {date_3}")

    # Update the checkmark statuses
    challenge_1.config(text="✔️ Daily Check-in\n✔️ Daily Challenge\n✔️ Weekly Contest\n✔️ Biweekly Contest\n")
    challenge_2.config(text="✔️ Daily Check-in\n✔️ Daily Challenge\n❌ Weekly Contest\n❌ Biweekly Contest\n")
    challenge_3.config(text="✔️ Daily Check-in\n❌ Daily Challenge\n❌ Weekly Contest\n❌ Biweekly Contest\n")

# Set up the window
root = ttk.Window(themename="superhero")
root.title("LeetCoin Calculator")

# Set up the main frame
frame = ttk.Frame(root)
frame.pack(pady=20)

# LeetCoin Calculator Label
header_label = ttk.Label(frame, text="LeetCoin Calculator", font=("Segoe UI Emoji", 20, "bold"), bootstyle=PRIMARY)
header_label.grid(row=0, column=0, columnspan=2, pady=20)

# Input section for current leetcoins
current_coins_label = ttk.Label(frame, text="Current LeetCoins", font=("Segoe UI Emoji", 12), bootstyle=INFO)
current_coins_label.grid(row=1, column=0, sticky="w", padx=10)
current_coins_entry = ttk.Entry(frame)
current_coins_entry.grid(row=1, column=1, padx=10, pady=5)

# Input section for streak
streak_label = ttk.Label(frame, text="Streak", font=("Segoe UI Emoji", 12), bootstyle=INFO)
streak_label.grid(row=2, column=0, sticky="w", padx=10)
streak_entry = ttk.Entry(frame)
streak_entry.grid(row=2, column=1, padx=10, pady=5)

# Dropdown for reward type
reward_label = ttk.Label(frame, text="Choose reward", font=("Segoe UI Emoji", 12), bootstyle=INFO)
reward_label.grid(row=3, column=0, sticky="w", padx=10)
reward_combobox = ttk.Combobox(frame, values=[
    'Time Travel Ticket', 
    '30-Day Premium Subscription', 
    'LeetCode T-Shirt', 
    'LeetCode Cap', 
    'LeetCode Kit', 
    'LeetCode Laptop Sleeve', 
    'LeetCode Big O Notebook', 
    'LeetCode Hoodie'
], state="readonly")
reward_combobox.grid(row=3, column=1, padx=10, pady=5)

# Calculate button
calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate, bootstyle=SUCCESS)
calculate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Result section (Three frames for each scenario)
result_frame = ttk.Frame(root)
result_frame.pack(pady=10)

challenge_1 = ttk.Label(result_frame, text="Result 1", font=("Segoe UI Emoji", 12), bootstyle=SUCCESS)
challenge_1.grid(row=0, column=0, padx=20)
result_1 = ttk.Label(result_frame, text="", font=("Segoe UI Emoji", 12), bootstyle=INFO)
result_1.grid(row=1, column=0, padx=20)

challenge_2 = ttk.Label(result_frame, text="Result 2", font=("Segoe UI Emoji", 12), bootstyle=SUCCESS)
challenge_2.grid(row=0, column=1, padx=20)
result_2 = ttk.Label(result_frame, text="", font=("Segoe UI Emoji", 12), bootstyle=INFO)
result_2.grid(row=1, column=1, padx=20)

challenge_3 = ttk.Label(result_frame, text="Result 3", font=("Segoe UI Emoji", 12), bootstyle=SUCCESS)
challenge_3.grid(row=0, column=2, padx=20)
result_3 = ttk.Label(result_frame, text="", font=("Segoe UI Emoji", 12), bootstyle=INFO)
result_3.grid(row=1, column=2, padx=20)

root.mainloop()
