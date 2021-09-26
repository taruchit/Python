# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:29:25 2021

@author: pc
"""

#Computing factorial
def computeFactorial(N):
    if N==0 or N==1:
        return 1
    else:
        return N*computeFactorial(N-1)

#Number of testcases
T=int(input())

#User input and output
data=0
for i in range(T):
    data=int(input())
    res=computeFactorial(data)
    print(res)
