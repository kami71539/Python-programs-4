number=int(input("Enter the number : "))
#Adding digits of the number entered.
#To check whether the given 3 digit number is a pallindrome or not.
#To check whether the given number is an armostrong or not.
sum=0
sum1=0
number2=number
sum2=0
c=100
while number>0:
        remainder=number%10
        sum=sum+remainder
        sum1=sum1+remainder*c
        sum2=sum2+(remainder*remainder*remainder)
        number=number//10
        c=c//10

print("The sum of all the digits of the number would be",sum)

if sum1==number2:
        print("The given number("+str(number2)+") is a pallindrome.")
else:
        print("The given number ("+str(number2)+") is not a pallindrome.")
        
if sum2==number2:
        print("The given number ("+str(number2)+") is an armostong number.")
else:
        print("The given number ("+str(number2)+") is not an armostong number.")



        
 




