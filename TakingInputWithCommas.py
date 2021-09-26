# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:10:03 2021

@author: pc
"""

#Number of Testcases
T=int(input())

#User input
for i in range(T):
    data=input().split(", ")
    for j in range(len(data)):
        print(int(data[j]))
        print(type(data))
