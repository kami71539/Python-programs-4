#TO find whether the given number is prime.
def prime(x):
    flag=0
    for i in range (2,(x//2)+1):
        if(x%i==0):
            flag=1
    if flag==0:
        print(x,"is a prime number")
    else:
        print(x,"is not a prime number")
x=int(input(""))
prime(x)
        