#printing fibonacci series upto n terms.
n=int(input("Upto what term would you like to print? "))
first=0
second=1
fib=0
for i in range(n+1):
    fib=first+second
    first=second
    second=fib
    print(first,end=" ")
