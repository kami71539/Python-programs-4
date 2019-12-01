#To find the vowels in the given string.
count=0
a=list(input(""))
for x in a:
    if x.lower() in "aeiou":
        count=count+1
        print(x)
print("The vowels in the given string would be",count)
