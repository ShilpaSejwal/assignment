#1


tup = (1,3,'shilpa','sejwal',(1,2))
print(len(tup))


#2

tup = (1,3,6,4,7,9,8,2)
print(tup)
print("maximum value is " ,max(tup))
print("minimun value is " ,min(tup))


#3

tup = (2,5,7,9,8,1)
product = 1
for x in tup:
    product = product*x
print("product:" ,product)



#4 sets

set1= {input("enter a set") for i in range(4)}
print(set1)
set2 ={input("enter a set") for i in range(3)}
print(set2)
set3 = set1 - set2
print(set3)
set4 = set1 & set2
print(set4)
set5 = set1<=set2
print(set5)



#5 dictionary

from collections import OrderedDict

my_dict = dict()
for i in range(4):
    key = input("enter names")
    value = input("enter marks")
    my_dict[key] = value
    print (my_dict)
a = OrderedDict (sorted(my_dict.items(), key=lambda t: t[1]))
print(a)
b = dict(a)
print(b)



#6 count occurances

dict = {}
str = "MISSISSIPPI"
m = str.count('M')
i = str.count('I')
s = str.count('S')
p = str.count('P')

dict['M'] = m
dict['I'] = i
dict['S'] = s
dict['P'] = p
print(dict)

