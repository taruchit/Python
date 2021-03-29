#Importing the necessary packages
import os
import math

#Calculating Simple Interest
def sim_int(p,n,r): 
    p=int(input())
    n=int(input())
    r=int(input())
      
    si =(p*n*r)/100
    #Displaying Simple Interest
    print("The Simple Interest is",si)
    #Displaying all objects in the current namespace
    print(dir())      
   
    return si
      

def ceil_floor(a,b):
    a=input()
    b=input()
    #Coverting floating number into next higher decimal number
    print(math.ceil(eval(a)))
    #Converting floating number into previous decimal number
    print(math.floor(eval(b)))

    return a,b

from math import sqrt
def lists():
    #Creating an empty list
    lst =[]
    i=0
    ele=0
    #Taking 5 user inputs in the list
    for i in range(5):
        ele=int(input())
        #Calculating the square root of user input, converting it into float and then reducing to two points after decimal
        ele=format(float(sqrt(ele)),'.2f')
        lst.append(ele)  
    #Removing quotes from the list
    print(*lst,sep=', ')
           
    return lst
# Driver code
p=0
n=0
r=0
si=sim_int(p,n,r) 
a=0
b=0
c=ceil_floor(a,b)
e=lists()


'''

User input: -

3000
5
1
5.5+6.5-8.5
5.5+6.5-8.5
5
6
7
8
10

Output: -

The Simple Interest is 150.0
['n','p','r','si']
4
3
2.24, 2.45, 2.65, 2.83, 3.16

'''