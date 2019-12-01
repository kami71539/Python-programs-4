#Printing factorial without recursion.
def factorial(x):
    factorial=1
    for i in range(x,0,-1):
        factorial=factorial*i
    return factorial
x=int(input(""))
print(factorial(x))