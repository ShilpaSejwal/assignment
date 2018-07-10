# question 1
'''
 name and handle the exception
a=3
if a<4:
    a=a/(a-3)
    print(a)
    
ZeroDivisionError: division by zero
'''

a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)

except ZeroDivisionError as e:
    print("error is ",e)



# question 2
'''
l=[1,2,3]
print(l[3])

IndexError: list index out of range
'''

l=[1,2,3]
try:
    print(l[3])

except IndexError as e:
    print("error is ",e)



# question 3

try:
    raise NameError("Hi there") #raise error
except NameError:
    print("an exception")
    raise #to  determine whether the exception was raised or not

'''
an exception
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/python/exception.py", line 43, in <module>
    raise NameError("Hi there") #raise error
NameError: Hi there
'''


#question 4

def AbyB(a , b):
    try:
             c = ((a+b) / (a-b))
    except ZeroDivisionError:
         print ("a/b result in 0")
    else:
         print(c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

'''
output

-5.0
a/b result in 0

'''

#question 5


#import error

try:
    from threading import XY
    print("hi")
except ImportError as e:
    print("error is",e)


#value error

try:
  n=int(input("enter a valid number"))
  print(n)

except ValueError as e:
    print("value is wrong",e)



#index error

l=[1,2,3]
try:
    print(l[3])
except IndexError as e:
    print("error is",e)



#question 6

class Error(Exception):

    def agetoosmall(self,warning):
        print(warning)

x= True
while x:
    try:
        age = int(input("enter valid age"))
        if age<18:
            raise Error()

    except Error as e:
        e.agetoosmall("age is not valid")

    else:
        x=False

    


