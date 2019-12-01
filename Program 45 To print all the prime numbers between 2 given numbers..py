#To print all prime numbers between 2 given numbers.
def prime(x,y):
    while x<y:
        flag=0
        for i in range(2,x//2+1):
            if(x%i==0):
                flag=1
        if flag==0:
            print(x,end=" ")
        x=x+1
    
    
x=int(input(""))
y=int(input(""))
print("The list of all prime numbers would be",end=" ")
prime(x,y)