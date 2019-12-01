#Write a program to convert then print the vowel in uppercase of the given string.
string=str(input(""))
length=len(string)
for i in string:
    if i.lower() in "aeiou":
        string=string+i.upper()
    else:
        string=string+i
print(string[length:])
