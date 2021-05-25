# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 22:38:09 2021

@author: pc
"""
#Importing a calendar module
import calendar

#Creating a plain text calendar
c=calendar.TextCalendar(calendar.SUNDAY)
st=c.formatmonth(2017,1,0,0)
print(st)

#Creating a HTML formatted calendar
hc=calendar.HTMLCalendar(calendar.SUNDAY)
st=hc.formatmonth(2017,1)
print(st) #Returns the HTML tags

#Loop over days of a month
#Zeroes mean that the day of the week is an overlapping month or other month
#It will return numbers that represent each day of the month
for i in c.itermonthdays(2017, 8):
    print(i)
    
#Getting months and days as per current system's settings
for name in calendar.month_name:
    print(name)
    
for day in calendar.day_name:
    print(day)
    
#To get dates of first Monday in each month.
print("Getting date for first Monday in every month")
for m in range(1,13):
    cal=calendar.monthcalendar(2021, m)
    weekone=cal[0]
    weektwo=cal[1]
    '''print("Weekone: ",weekone)
    print("Weektwo",weektwo)'''
    if weekone[calendar.MONDAY]!=0:
        meetday=weekone[calendar.MONDAY]
    else:
        meetday=weektwo[calendar.MONDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))    
                

