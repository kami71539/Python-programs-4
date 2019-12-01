#Star Programs (BOX)
row=int(input("Enter row: "))
coloumn=int(input("Enter coloumn: "))
for i in range(0,row):
    for j in range(0,coloumn):
        print("*",end="")
    print(" ")
'''
*****
*****
*****
*****
*****
'''
#Printing a star pyramid.
for i in range(0,row):
    for j in range(0,i):
        print("*",end="")
    print("")
'''
*
**
***
****
*****
'''

for i in range(row,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("")
'''
*****
****
***
**
*
'''
#Numbered Triangle
for i in range(0,row):
    for j in range(0,i):
        print(i,end='')
    print("")
'''
1
22
333
4444
'''

for i in range(0,row):
    for j in range(0,i):
        print(i,end='')
    print("")
'''
0
01
012
0123
'''

for i in range(0,row):
    for j in range(0,coloumn):
        if j>=i:
            print('*',end='')
        else:
            print(end=' ')
    print("")
'''
*****
 ****
  ***
   **
    *
 '''

for i in range(row,0,-1):
    for j in range(0,coloumn):
        if j>=i:
            print('*',end='')
        else:
            print(end=' ')
    print("")
 '''
*****
 ****
  ***
   **
    *
 '''

z=1
for i in range(1,row):
    for j in range(0,i):
        print(z,end="")
        z=z+1
    print('')
       
 '''
1
23
456
78910
 '''
#Alphabetic Triangle
first=int(input("Enter alphabet"))

for i in range(0,row):
    for j in range(0,i):
        print(chr(first),end="")
        first=first+1
    print('')
       
'''
A
AB
ABC
ABCD
'''
