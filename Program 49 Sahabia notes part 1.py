a=[1,2,3,"hello",2.52]
del a[3]
print(a)
a=[1,2,3,"hello",[1,"b",451,["a","b","c"],540,51,5],2.50]
a[4][3][1]=0
print(len(a))
b=[1,2,3,"hello",2.52]
c=a+b
print(c)
print(a*3)
print(4 in a)
for x in a:
    print(x)
a=[1,2,3,"hello"]
b=[5,8,9]
print(b)
print(a+b)
a.extend(b)

print(a),
a=[1,2,1,3,"hello",2.52]
print(a.count(1))
print(a.index("hello"))
a=[1,2,3]
a.insert(2,"world")
print(a)
print(1+2)
a=[]
b=int(input("Alright let's do this. "))
for i in range(b):
    c=input("Enter elements: ")
    a.append(c)
print(a)

a=[1,2,3,4,5]
type(a)
print(a[:5])
b=[6,7,8,9,0]
print(a+b)
c=a+b
c.sort()
print(c)

a={1,2,3,4,5}
b={6,7,4,9,5}
print("Union ",a|b)#print(a.union(b))
print("Intersection" ,a&b)#print(a.intersect(b))
print("Difference " ,a-b)
print("Difference 2" ,b-a)
print("Difference 3" ,a.difference(b))
print("Difference 4" ,b.difference(a))
print("raise to the power" ,a^b)
print("symmetric" ,a.symmetric_difference(b),"This is the symmetric difference between the two.")#INtersection ka ulta.

a=[1,2,[1,223,4,34,45],34,54]
a[2].append(5)
print(a)
#a[2][2].add(5)