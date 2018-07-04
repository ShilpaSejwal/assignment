#1


for i in range (10):
    a = int(input("enter a number:"))
    print("number is :" ,a)


#2

x=10
while(x>0):
    print("hello")



#3

l1 = []
for x in range(5):
    y = int(input("enter the value"))
    l1.append(y)

print(l1)
l2=[]
for x in l1:
    z= x*x
    l2.append(z)
print(l2)


#4

l1=[1,2,'shilpa',4.7,9,'apple']
print(l1)
l2=[]
l3=[]
l4=[]
for x in l1:
    if type(x) == int:
        l2.append(x)
    elif type(x) == str:
        l3.append(x)
    elif type(x) == float:
        l4.append(x)

print("list of integers" ,l2)
print("list of strings" ,l3)
print("list of floats" ,l4)


#5


even=[]
odd=[]

for x in range (1,101):
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("list of even " ,even)
print("list of odd" ,odd)



#6

a=1
while (a<=4):
    print("*"*a)
    a=a+1



#7

d = {}
for i in range(5):
    name = input("enter name")
    age = input("enter age")

    d[name] = [age]
    print(d)



#8

l1 = []
for x in range(5):
    s = input("enter elements")
    l1.append(s)
    print(l1)

   
d = input("enter element to be deleted")
for x in l1:
    if x == d:
        l1.remove(x)
else:
    print("element not present")
print("the list is:" ,l1)

