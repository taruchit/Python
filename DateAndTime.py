# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 00:47:14 2021

@author: pc
"""

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Printing today's date
today=date.today()
print("Today's date is: ", today)

#Printing date's individual components
print("Today's day",today.day)
print("Today's month",today.month)
print("Today's year",today.year)

#Printing weekday number
print("Today's weekday",today.weekday())
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print("Which day is today: ",days[today.weekday()])

#Printing date and time
today=datetime.now()
print("Today's date and time': ",today)

#Printing the current time
t=datetime.time(datetime.now())
print("Current time: ",t)

#Printing the current year
now=datetime.now()
print(now.strftime("The current (full) year is: %Y"))
print(now.strftime("The current's last two digits: %y"))

#Printing the current day
print(now.strftime("The current day is: %A"))
print(now.strftime("The current day in shortform is: %a"))

#Printing the current month
print(now.strftime("The current month is: %B"))
print(now.strftime("The current month in short form is: %b"))

#Pringting today's complete datedate
print(now.strftime("Today's date mm/dd/yy: %D"))

#Printing only date
print(now.strftime("Date: %d"))

#Printing current time
print(now.strftime("Current time: %X"))

#Printing today's date
print(now.strftime("Printing today's date: %x"))

#Printing day month date and time in short form
print(now.strftime("Today's day, month, date and time in short form: %c"))

#Printing whether current time is AM or PM
print(now.strftime("AM or PM: %p"))

#Printing current time
print(now.strftime("Current time as per 12 hour window: %I:%M:%S %p"))
print(now.strftime("Current time as per 24 hour window: %H:%M"))


#Printing a basic timedelta
print("Basic timedelta: ",timedelta(days=365, hours=5, minutes=1))

now=datetime.now()
#Printing the date after an year
print("One year later: "+str(now+timedelta(days=365)))

#Using timedelata with two arguments
print("Date after 4 weeks and 4 days: "+str(now+timedelta(days=4, weeks=4)))

#Printing the date 1 week ago
print("One week ago, the date was: "+str(now-timedelta(weeks=1)))

#Printing the number of days between current date and birthday date
today=date.today()
birthdayDate = date(today.year,9,1)
print("Birthday date: ",birthdayDate)
if today<birthdayDate:
    print("Number of days for the birthday: ",(birthdayDate-today).days)
elif today==birthdayDate:
    print("Today is the birthday.")
else:
    print("Birthday for this year happend %d days ago" %((today-birthdayDate).days))
    
