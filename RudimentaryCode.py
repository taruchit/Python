# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:17:41 2021

@author: pc
"""

#Printing a line
print("Today is a good day")

#Arithmetic operations
print("Addition: ",(4+2))
print("Subtraction: ",(4-2))
print("Multiplication: ",(4*2))
print("Division: ",(4/2))
print("Modulus: ",(4%2))

#Taking user input and storing in the variable
name=input("What is your name?")

#Displaying the vartiable's content
print("Nice to meet you: ",name)

#Getting the variable type
print(type(name))

#Defining a method
def main():
    print("Inside main method")

#Calling a method    
if __name__=="__main__":
    main()