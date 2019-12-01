#Write a program to print the sum of all natural numbers with recursion.
def sum(x):
    if x==1:
        return x
    else:
        return x+sum(x-1)

#Write a program to print the sum of all natural numbers.
def sum(x):
    sumn=0
    for i in range(1,x+1):
        sumn=sumn+i
    return sumn

x=int(input(""))
print(sum(x))