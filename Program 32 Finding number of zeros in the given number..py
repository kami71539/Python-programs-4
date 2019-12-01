#To find the number of zeros in the given number.
number=int(input(""))
zero=0
while number>0:
    remainder=number%10
    number=number//10
    if remainder==0:
        zero=zero+1
print(zero)