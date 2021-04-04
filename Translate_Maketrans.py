# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:44:37 2021

@author: pc
"""

#translate() and #makerans() method

'''
translate() helps to change or convert a string.
A string is said to be changed or converted in following scenarios: -
1. We insert or replace a character or word in a string.
2. We delete a character or word in a string.

translate() and maketrans() helps to help make character level translation 

translate() works on translation table or table.
To create the table we use maketrans() method.
'''

'''
maketrans() method returns a translation table.
string.maketrans(x,y,z)
-> x is mandatory
-> y and z are optional
'''

str="abcde"
dict1={"a":"1","b":"2","c":"3","d":"4","e":"5"}
t=str.maketrans(dict1)
'''
We get a dictionary with key and value. Key has ASCII value of characters in str
We corresponding values given in dict1 (translation table).
'''
print(t)

print("ASCII value of a: ",ord("a"))
print("ASCII value of b: ",ord("b"))
print("ASCII value of c: ",ord("c"))
print("Using translate() method: ",str.translate(t))

'''
Considering the situation that translating table has data for only three characters
'''
dict2={"a":"1","b":"2","c":"3"}
t=str.maketrans(dict2)
print(t)
print("Using translate() method: ",str.translate(t))

'''
Considering the situation that there are repeat characters in the string, the result will show data with unique keys only
'''
str1="abcac"
t=str1.maketrans(dict2)
print(t)
print("Using translate() method: ",str1.translate(t))
'''
makeTrans() with two arguments, both strings must be of equal length
'''

str="Hi welcome to Python maketrans() method with two arguments"
str1="abcde"
str2="12345"
t=str.maketrans(str1,str2)
'''
We get ordinal values in both keys and values
'''
print(t)
print("For ordinal value 49, corresponding character value is ",chr(49))
print("For ordinal value 53, corresponding character value is ",chr(53))
print("For ordinal value 101, corresponding character value is ",chr(101))
print("Using translate() method: ",str.translate(t))
'''
makeTrans() with three arguments
'''

str="Hi welcome to Python$&* maketrans() method with three arguments"
str1="abcde"
str2="12345"
str3="($&"
t=str.maketrans(str1,str2,str3)
'''
We will see 40: None, 36:None, 38 None, which means the characters 
in string str3 have no replacement values and thus they will be deleted 
and not replaced.

'''
print(t)
print("For ordinal value 40, corresponding character value is ",chr(40))
print("For ordinal value 36, corresponding character value is ",chr(36))
print("For ordinal value 38, corresponding character value is ",chr(38))
print("Using translate() method: ",str.translate(t))
