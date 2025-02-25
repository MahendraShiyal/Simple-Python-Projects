#install datetime library by running "pip install datetime" in terminal.
#this program is improved form of greeting by username.

from datetime import datetime

name = input("Enter your name: ")
now = datetime.now()
hour = now.hour  # Directly get the hour as an integer

if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print(f"{greeting}, {name}!")
print("Current Date & Time:", now.strftime("%d/%m/%Y %H:%M:%S"))
