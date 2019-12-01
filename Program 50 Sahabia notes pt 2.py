a={
'a':5,
'b':6,
'c':7
}
print(a.get('b',"Nothing"))
a['d']=8
print(a)
del a['a']
print(a)
#Nested List.
a={'Name':{'first':'Aman','last':'Sharma'},
'Age':20,
'occup':{'Manager','HR','Teacher'}}
print(a['Name']['last'])
print(a['occup'])

a=input('')
d=dict()
for c in a:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)

a=5#global
def display():
    a=10#local
    print("In display funtion a =",a)
def show():
    a=20#local
    print("In show funtion a =",a)
def function():
    #global a
    a=30
    print("In funtion a =",a)
display()
show()
function()
print(a)

c=1
while c!=1:
    print(c)
    