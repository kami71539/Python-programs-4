#Printing text after specific lines.
text=str(input("Enter Text: "))
text_number=int(input("Enter number of text you'd like to print; "))
line_number=1
for i in range(0,text_number):
    print(text)
    for j in range(0,line_number):
        print("1")
    line_number=line_number+1
print(text)