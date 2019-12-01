# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:35:15 2019

@author: Kamran
"""

#To find the avg of all the even numbers in the user input array.
def even(x):
    if x%2==0:
        return True
x=[]
y=5
z=0
evenn=0
v=0
for i in range(y):
    w=int(input(""))
    x.append(w)
    if even(x[i]):
       z=z+x[i]
       evenn=evenn+1
    else :
        v=v+x[i]
print("avg",z/evenn)
print(v)