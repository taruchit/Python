# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:43:00 2021

@author: pc
"""

# Declaring a variable and initializing it

temp=10

# Printing the varaible

print(temp)

#Redeclaring the same variable with different data type

temp="Python"
print(temp)

#Variables of same data type can be combined
a=2
b=3
print(a+b) # Successful

a="Python"
b="3"
print(a+b) # Successful

#Variables of different data types cannot be combined
a="Python"
b=3
print(a+b) #Error

#To combine a string and int varaible, we need to use str() method with int
a="Python"
b=3
print(a+str(b))

#Global varaiable and Local varaible
var1="Global variable"
def printMethod():
    var1="Local variable"
    print(var1)

printMethod() # Prints Local varaible
print(var1)  # Prints Global variable

var2="Global variable"
def globalPrintMethod():
    global var2
    var2="Local variable"
    print(var2)
globalPrintMethod() # Prints Local variable
print(var2)  # Prints Local variable







