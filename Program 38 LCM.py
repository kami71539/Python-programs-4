#Finding LCM.
first=int(input(""))
second=int(input(""))
HCF=0
i=1
while i<=first and i<=second:
    if first%i==0 and second%i==0:
        HCF=i
    i+=1
LCM=(first*second)//HCF
print(LCM)
