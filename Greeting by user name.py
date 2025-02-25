# install datetime library by running "pip install datetime" in terminal.
#this program gives user greeting by given name and time of the system.
name = input("Enter your name : ")
print ("Hello ", name)
from datetime import datetime
now = datetime.now()
Time = now.strftime("%H")
Time = int(Time)
if Time <12 :

    print ("Good Morning, ", name)
elif Time >= 12:
    if Time <18:
        print ("Good Afternoon, ", name)
    else:
        print("Good evening, ", name)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print (dt_string)