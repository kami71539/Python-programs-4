#To calc Hypotenuse of a triangle.
print("Enter the Base and Altitude of the triangle")
base=float(input("The base would be "))
alt=float(input("The alt would be "))
sum=(base*base)+(alt*alt)
from math import*
hypo=sqrt(sum)
print("The hypotenuse of the triangle would be" ,round(hypo,2))