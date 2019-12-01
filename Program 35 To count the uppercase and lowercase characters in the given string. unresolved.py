#To count the uppercase and lowercase characters in the given string.
string=input("")
j='a'
lower=0
upper=0
space=0
for i in string:
    for j in range(65,92):
        if chr(j) in i:
            upper=upper+1
        elif j==" ":
            space=space+1
    for j in range(97,123):
        if chr(j) in i:
            lower=lower+1
            #print(chr(j))
print("There are",lower-space,"lower characters and",upper,"upper characters.")