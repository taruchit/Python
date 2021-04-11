# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 00:09:02 2021

@author: pc
"""

a,b=10,20

# Type 1

if a>b:
    print("a is greater than b")
    
elif b>a:
    print("b is greater than a")
    
else:
    print("a and b are equal")
    

# Type 2

sentence="a and b are equal" if(a==b) else "a is not equal to b"
print(sentence)