#import needed library by running command in terminal "pip install time" and
#"pip install datetime"
#this program runs a reminder one time if you want to go for everyday you need to add few things.
#this is called daily reminder since it reminds us for only maximum time of 24 hours of a day.
from time import sleep
from datetime import datetime

# Get reminder details
reminder = input("What shall I remind you about? ")
rem_time = input("Please enter the time for the reminder (HHMM format): ")

# Validate time input
try:
    rem_time = datetime.strptime(rem_time, "%H%M")  # Convert input to datetime object
except ValueError:
    print("Please enter the correct time in HHMM format!")
    exit()

# Get current time
now = datetime.now()
time_now = now.strftime("%H%M")

# Convert times to minutes for comparison
rem_minutes = rem_time.hour * 60 + rem_time.minute
now_minutes = now.hour * 60 + now.minute

# Calculate time difference
diff_time = rem_minutes - now_minutes
if diff_time < 0:
    diff_time += 1440  # Adjust for next day

print(f"Reminder set for {rem_time.strftime('%H:%M')}. It will trigger in {diff_time} minutes.")

# Wait until the time arrives
sleep(diff_time * 60)

# Trigger the reminder
print("\n⏰ Reminder:", reminder)
