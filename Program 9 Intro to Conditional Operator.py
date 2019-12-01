#Using onditional operator to check whether you are eligible to vote or not.
a=int(input("Enter your age: "))
c=("You are eligible to vote.")
d=("You are not eligible to vote.")
print(c) if a>18 else print(d)