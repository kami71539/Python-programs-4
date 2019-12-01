number=int(input("Enter Number: "))
for i in range(2,number):
    if(number%i==0):
        flag=True
        break
    else:
        flag=False
if flag:
    print("The number is not prime.")
    print(i,"times",number//i,"is",number)
else:
    print("The number is prime.")
