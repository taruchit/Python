# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 01:16:16 2021

@author: pc
"""

# Defining a basic function

def funcOne():
    print("Priniting a basic function")
    

# Defining a function with arguments

def funcTwo(arg1, arg2):
    print("arg1: ",arg1)
    print("arg2: ",arg2)
    
    
# Defining a function that returns a value

def funcThree(arg1):
    return arg1+arg1


# Defining a function with default argument

def funcFour(arg1,arg2=1):
    return arg1+arg2


# Defining a function that takes multiple arguments

def funcFive(*arg):
    res=0
    for x in arg:
        res=res+x
    return res

# Calling a function

funcOne()

funcTwo("Python",3)

print(funcThree(5))

print(funcFour(4))

print(funcFour(4,2))

print(funcFive(1,2,3,4,5))