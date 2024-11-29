# Time, Scheduling, and Program Automation

import time
import subprocess
import webbrowser
from datetime import datetime, timedelta
import schedule
import sys
import calendar

# ------------------- Time and Scheduling -------------------

# Measure Execution Time
start_time = time.time()
for _ in range(1000000): pass
print(f"Execution Time: {time.time() - start_time} seconds")

# Pause Execution
time.sleep(2)  # Pauses for 2 seconds

# Current Date and Time
now = datetime.now()
print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Calculate Future and Past Dates
future_date = now + timedelta(days=10)
past_date = now - timedelta(days=10)
print(f"Future Date: {future_date}, Past Date: {past_date}")

# Check Leap Year
print(f"Is 2024 a Leap Year? {calendar.isleap(2024)}")

# Schedule Task (Using `schedule` library)
def print_task():
    print("Task executed!")

schedule.every(10).seconds.do(print_task)

# Keep the scheduler running in the background
def run_scheduler():
    print("Scheduler running... Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

# Uncomment the following line to run the scheduler
# run_scheduler()

# ------------------- Automating Program Launch -------------------

# Open a Website
webbrowser.open("https://www.python.org")

# Open a File
try:
    if sys.platform == "win32":
        subprocess.run(['start', 'example.txt'], shell=True)
    elif sys.platform == "darwin":  # macOS
        subprocess.run(['open', 'example.txt'])
    else:  # Linux
        subprocess.run(['xdg-open', 'example.txt'])
except FileNotFoundError:
    print("File not found!")

# Run a System Command and Capture Output
result = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)
print(f"Command Output: {result.stdout.strip()}")

# Error Handling Example
try:
    subprocess.run(['nonexistentprogram'])
except FileNotFoundError:
    print("Program not found!")

# Automate Recurring Task with Time
while True:
    print("Recurring task every 15 seconds...")
    time.sleep(15)
    break  # Remove this line for infinite loop
