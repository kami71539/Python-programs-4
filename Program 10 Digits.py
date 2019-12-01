#Finding whether the given number is 2 digit or not.
number=int(input("ENter the number."))
if number>9 and number<100:
    print("The number is indeed of 2 digit.")
else:
    print("The number is not of 2 digits.")

a=320
b=a/10#Absolute Quotient will come in decimal.
c=a//10#Quotient
d=a%10 #remainder

#finding how many digits does the number contains.
number=int(input("Enter the number; "))
count=0
while number>0:
    count=count+1
    number=number//10
print("The number contains",count,"digits")