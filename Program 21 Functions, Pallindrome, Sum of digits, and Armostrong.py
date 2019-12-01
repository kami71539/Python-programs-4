#Adding digits of the number entered.
def sum(number):
    sum=0
    while number>0:
        remainder=number%10
        sum=sum+remainder
        number=number//10
    print("The sum of all the digits of the number would be",sum)

#To check whether the given 3 digit number is a pallindrome or not.
def pallindrome(number):
    sum=0
    number2=number
    c=100
    while number>0:
        remainder=number%10
        sum=sum+remainder*c
        c=c//10
        number=number//10
    if sum==number2:
        print("The given number("+str(number2)+") is a pallindrome.")
    else:
        print("The given number ("+str(number2)+") is not a pallindrome.")

#Check whether the givne number is an armostrong or not.
def armostrong(number):
    sum=0
    number2=number
    c=100
    while number>0:
        remainder=number%10
        sum=sum+(remainder*remainder*remainder)
        number=number//10
    if sum==number2:
        print("The given number ("+str(number2)+") is an armostong number.")
    else:
        print("The given number ("+str(number2)+") is not an armostong number.")
    
number=int(input("Enter the number : "))
sum(number)
pallindrome(number)
armostrong(number)