#TO find the vowels and consonants in the given strings.
a=input("Enter the string: ")
vowel=0
consonant=0
space=0
for i in a:
    if i.lower() in "aeiou":
        vowel=vowel+1
    elif i ==" ":
        space=space+1    
    else:
        consonant=consonant+1
        print(i,end="")
print("The given string contains",vowel,"vowels and",consonant-space,"consonants.")