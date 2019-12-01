#Finding Area and Perimeter of a Rectangle/Square.
print("Enter the length and breadth of the rectangle")
length=int(input("The length would be: "))
breadth=int(input("The breadth would be: "))
Area=length*breadth
Perimeter=2*(length+breadth)
print("Area is",Area)
print("Perimeter would be:",Perimeter)


#Area and perimeter of Circle.
print("Enter the radius of the Circle.")
radius=float(input("The radius would be: "))
pi=3.14
Area=pi*radius*radius
Perimeter=2*pi*radius
print("Area is",Area)
print("Perimeter would be:",round(Perimeter,2))

#Area of a triangle using Heron and Perimeter.
print("Enter the 3 sides of a triangle")
First=float(input("First side: "))
Second=float(input("Second side: "))
Third=float(input("Third side: "))
Perimeter=First+Second+Third
Semi_Perimeter=Perimeter/2
Pre_Heron=Semi_Perimeter*(Semi_Perimeter-First)*(Semi_Perimeter-Second)*(Semi_Perimeter-Third)
from math import*
Heron=sqrt(Pre_Heron)
print("The Perimeter is",Perimeter)
print("The Area would be",round(Heron,2))
#Area of Cyllinder
print("FInding the total surface area of a Cyllinder.")
radius=float(input("The radius: "))
height=float(input("The height: "))
pi=3.14
Area=2*pi*radius*(radius+height)
print("The area is",round(Area,2))