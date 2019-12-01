#To find the avg sum of prime numbers between 2 given numbers.
def prime(x,y):
    sump=0
    count=0
    while x<y:
        flag=0
        for i in range(2,x//2+1):
            if(x%i==0):
                flag=1
        if flag==0:
            print(x,end=" ")
            sump=sump+x
            count=count+1
        x=x+1
    print("\nThe sum of all prime numbers would be",sump)
    print("The avg of all prime numbers would be",sump/count)
    
    
x=int(input(""))
y=int(input(""))
print("The list of all prime numbers would be",end=" ")
prime(x,y)