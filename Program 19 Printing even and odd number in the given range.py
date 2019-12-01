#To print even numbers from low to high number.
low=int(input("Enter the lower limit: "))
high=int(input("ENter the higher limit: "))
for i in range(low,high):
    if(i%2==0):
        print(i,end=" ")
print("")
for i in range(low,high):
    if(i%2!=0):
        print(i,end=" ")
        
#Printing odd numbers from higher number to lower number
low=int(input("Enter the lower limit: "))
high=int(input("ENter the higher limit: "))
for i in range(high,low,-1):
    if(i%2!=0):
        print(i,end=" ")