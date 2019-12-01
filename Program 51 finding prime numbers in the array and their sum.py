#To find all the prime numbers in an array.
def isprime(x):
    prime=True
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            prime=False
    if prime==True:
        return True
a=[]
b=[]
c=10
for i in range(c):
    d=int(input(""))
    a.append(d)
print("The array is",a)
for i in range(c):
    if isprime(a[i]):
        b.append(a[i])
print("The prime element(s) in the array:-",b)
b=sum(b)
print("The sum would be :-",b)
