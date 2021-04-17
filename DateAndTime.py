# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 00:47:14 2021

@author: pc
"""

from datetime import date
from datetime import time
from datetime import datetime

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

