#Finding HCF by EUCLID
first=int(input(""))
second=int(input(""))
temp=0
if first>second:
    temp=first
    first=second
    second=temp
if second%first==0:
    print(first,"is the HCF")
else:
    if(first%(second%first))==0:
        print(second%first,"is the HCF")


#Finding HCF part 2
first=int(input(""))
second=int(input(""))
HCF=0
i=1
while i<=first and i<=second:
    if first%i==0 and second%i==0:
        HCF=i
    i+=1
print("The HCF would be",HCF)