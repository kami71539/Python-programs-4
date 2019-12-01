#Nested Loops
for i in range(10):
    for j in range(10):
        print(j,end="")
    print("")
    print(i)



number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
    ]
print(number_grid[1][2])
for row in number_grid:
    print (row)
    for coloumn in row:
        print(coloumn)
    