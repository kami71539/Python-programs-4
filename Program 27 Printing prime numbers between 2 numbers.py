low=int(input("Enter lower limit: "))
high=int(input("Enter upper limit: "))
flag=False
while low<high:
    flag=False
    for i in range(2,low):
        if low%i==0:
            flag=True
            break
    if flag==False:
        print(low,end="],[")
    low=low+1