#Finding Interest by using functions
def c_interest(p,r,t):
    m=(1+r/100)
    n=pow(m,t)
    i=p*n-p
    print("The compound interest would be:",end='')
    print(i)
    
def s_interest(p,r,t):
    return (p*r*t)/100
    
    
p=float(input("Enter the Principal: "))
r=float(input("Enter the rate: "))
t=float(input("Enter the time: "))
c_interest(p,r,t)
print("The simple interest would be: ",end="")
print(s_interest(p,r,t))