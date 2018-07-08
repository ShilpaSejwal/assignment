#Question1

r=int(input("Enter the radius= "))
def area(r):
    ar=3.14*r*r
    return ar
print ("The area of circle= ",area(r))

#Question2

def Perfect( n ):

    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
     
    return (True if sum == n and n!=1 else False)
 
print("Below are all perfect numbers till 1000")
n = 2
for n in range (1000):
    if Perfect (n):
        print(n , " is a perfect number")

#Question3

def mul_table(n, i=1):
    print (n*i)
    if i != 10:
        mul_table(n,i+1)
mul_table(12)

#Question4

def power(a,b):
    if b == 1:
        return a
    else:
        return a * power(a,b-1)
print ("a^b= ",power(10,3))

#Question5

dict={}
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
dict[0]=factorial(n)
print (dict)
