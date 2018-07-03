#1

l = [input("enter values")
for i in range (5)]
print(l)

#2

nl = ['google','apple','facebook','microsoft','tesla']
c = l+nl
print (c)

#3

l = ["a","b","b","c","b","a"]
print(l)
print(l.count("a"))
print(l.count("b"))

#4

l = [5,7,9,3,2,6,8,1]
l.sort()
print(l)


#5

l1 = [4,7,5,9,8,3,1]
l2 = [9,5,2,1,6,9,0]
l3 = l1+l2
l3.sort()
print(l3)


#6
#stack

l1 = []
l1.append(1)
print(l1)
l1.append(4)
print(l1)
l1.append(7)
print(l1)
print(l1.pop(-1))
print("now the list is" ,l1)
print(l1.pop(-1))
print("now the list is" ,l1)


#queue

l1=[]
l1.append(5)
print(l1)
l1.append(9)
print(l1)
l1.append(7)
print(l1)
print(l1.pop(0))
print("now the list is" ,l1)
print(l1.pop(0))
print("now the list is" ,l1)



#7

l1 = [1,2,3,5,7,9]
even=0
odd=0
for x in l1:
    if x%2==0:
        even+=1
    else:
        odd+=1
print("even numbers =" ,even)
print("odd numbers =" ,odd)



