#Comparing 3 numbers.
print("Enter the 3 numbers needed to be compared")
a=int(input(""))
b=int(input(""))
c=int(input(""))
if a!=b and a!=c and b!=c:
    if a>b and a>c:
        print(a, "is the largest")
    elif b>a and b>c:
        print(b, "is the largest")
    else:
        print(c, "is the largest")
    if a>b and a<c or a<b and a>c:
        print(a, "comes in the middle")
    elif b>a and b<c or b>a and b>c:
        print(b, "comes in the middle")
    else:
        print(c, "comes in the middle")
    if a<b and a<c:
        print(a,"is smallest")
    elif b<a and b<c:
        print(b,"is smallest")
    else:
        print(c,"is smallest")
else:
    print("2 of these 3 nums are equal.")