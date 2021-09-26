# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:14:49 2021

@author: pc
"""

#Number of inputs in a list
N=int(input()) 

#Taking input for first list: list_A
list_A=input().split(", ")

#Taking input for second list: list_B
list_B=input().split(", ")

#Checking the two lists
print("liast_A: ",list_A)
print("list_B: ",list_B)

#Converting lists to sets
set_A=set(list_A)
set_B=set(list_B)

#Printing common elements
print(set_A & set_B)    

#Printing the common values as integers
set_C=set_A & set_B
for i in set_C:
    print(i)