#Printing all factors of a number.
number=int(input(""))
for factor in range(1,number+1):
    if(number%factor==0):
        print(factor,"x",number//factor,"=",number)