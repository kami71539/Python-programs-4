#Printing multiplication table.
print("Let's create a multiplication table.")
number=int(input("Enter the number: "))
for i in range(1,11):
    print(number,"x",i,"=",number*i)