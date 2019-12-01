#To find the HCF and LCM of a number using recursion.
def HCF(x,y):
    if x%y==0:
        return y
    else:
        return HCF(y,x%y)
        
x=int(input(""))
y=int(input(""))
hcf=HCF(x,y)
lcm=(x*y)/hcf
print("The HCF is",hcf,". The LCM is",lcm)