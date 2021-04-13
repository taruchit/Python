# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:34:50 2021

@author: pc
"""

# While loop

x=0
print("Executing While loop")
while x<5:
    print(x)
    x=x+1
    
# For loop

print("Executing For loop")
for x in range(1,11):
    print(x)
    
    
# Using For loop over a collection

print("Executing For loop over a collection")
weekend=["Saturday","Sunday"]
for i in weekend:
    print(i)
    

#Using enumerate method in for loop

print("The enumerate() method helps to get the index number of value.")
weekday=["Monday","Tuesday","Wednesday","Thursday","Friday"]
for i,d in enumerate(weekday):
    print(i, d)