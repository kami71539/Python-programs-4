#Write a program to create 2 strings and print the comman character.
string1=input("")
string2=input("")
c=0
for a in string1:
    for b in string2:
        if a==b:
            print(a,end=" ")
            c=c+1
            break
print("")
if c==0:
    print("No common characters")
elif c==1:
    print("There is",c,"common character.")
else:
    print("There are",c,"common characters")
    