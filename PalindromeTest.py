# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:39:47 2021

@author: pc
"""

#User input
data=input()

#Reversing the string
Rdata=data[::-1]
print(Rdata)

if(data.lower()==Rdata.lower()):
    print("Palindrome")
else:
    print("Not palindrome")