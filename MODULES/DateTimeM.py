from datetime import datetime, timedelta

# to get current date and time
now = datetime.now()

# Extract specific parts
print("--- Current Info ---")
print(f"Right Now: {now}")
print(f"Current Year: {now.year}")
print(f"Current Month: {now.month}")

# targeting for specific day
target_date = datetime(2026, 12, 31)


# to calculates difference between two dates
time_left = target_date - now

print("\n--- Countdown ---")
print(f"Target Date: {target_date.strftime('%B %d, %Y')}")
print(f"Days remaining: {time_left.days}")

# What will the date be in exactly 100 hours?
future = now + timedelta(hours=100)
print(f"\n100 hours from now it will be: {future.strftime('%Y-%m-%d %H:%M:%S')}")