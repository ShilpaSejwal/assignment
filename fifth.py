#1 leap year

year = int(input("enter a year"))
if(year%4)==0:
    print("this is a leap year")
else:
    print("this is not leap year")


#2 to check dimensions

length = int(input("enter the length"))
breadth = int(input("enter the beadth"))
if (length == breadth):
    print("this is square")
else:
    print("this is rectangle")


#3 old and young people

a = int(input("enter age of first person"))
b =  int(input("enter age of second person"))
c =  int(input("enter age of third person"))
if(a>b and a>c):
    print("first is oldest")
    if(b>c):
         print("third is youngest")
    else:
        print("second is youngest")

elif(b>a and b>c):
    print("second is oldest")
    if(a>c):
        print("third is youngest")
    else:
        print("first is youngest")

else:
    print("thrd is oldest")
    if(b>a):
         print("first is youngest")
    else:
        print("second is youngest")



#4 prize

points = int(input("enter points earned upto 200"))
if(points>0 and points<=50):
    print("no prize")
elif(points>51 and points<=150):
    print("you won wooden dog")
elif(points>151 and points<=180):
    print("you won book")
elif(points>181 and points<=200):
    print("you won chocolates")



#5 cost pay

quantity = int(input("enter quantity of items"))
cost = quantity * 10
if cost > 1000:
    print("10% discount")
    discount = (cost*10)/100
    update = cost - discount
    print("you need to pay" ,(update))
else:
    print("you need to pay " ,(cost))
