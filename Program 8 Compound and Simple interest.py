#To find the compound interest and simple interest.
print("Enter the Principal, Rate and Time.")
principal=float(input("Principal: "))
rate=float(input("Rate: "))
time=float(input("Time: "))
m=(1+rate/100)
n=pow(m,time)
compound_interest=(principal*n)-principal
simple_interest=(principal*rate*time)/100
print("The compound interest would be:",round(compound_interest,1),"and simple interest would be",simple_interest)