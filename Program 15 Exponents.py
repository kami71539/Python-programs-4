print(2**3)
def exponents(base,power):
    i=1
    for index in range(power):
        i=i*base
    return i
a=int(input(""))
b=int(input(""))
print(a, "raised to the power of" ,b,"would give us", exponents(a,b))
