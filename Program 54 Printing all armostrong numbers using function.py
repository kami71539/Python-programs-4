#TO print all the 3 digit armostrong numbers.
def armostrong(x):
    sum=0
    remainder=0
    x1=x
    while x>0:
        remainder=x%10
        sum=sum+remainder*remainder*remainder
        x=x//10
    if sum==x1:
        return True
    else:
        return False
for x in range(1,1000):
    if armostrong(x):
        print(x)