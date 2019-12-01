# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:10:41 2019

@author: Kamran
"""

#To find all the armostrong numebrs in the given array.
def armo(a):
    sum=0
    a2=a
    while a>0:
        r=a%10
        a=a//10
        sum=sum+r*r*r
    if sum==a2:
        return True 
a=[]
d=[]
b=2
for i in range(b):
    c=int(input(""))
    a.append(c)
print(a)
for i in range(b):
    if armo(a[i]):
        d.append(a[i])
print(d)