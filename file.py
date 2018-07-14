# question 1

with open("web.txt",'r') as f:
    data=f.readlines()
    for line in data:
        print(line)
    l = len(data)
    n = int(input("enter the value of n to print last n lines"))
    if (n<=1):
        print(data[n:1])
    else:
        print("n is not in range")

     
        
#question 2

l=[]
with open('web.txt','r') as f:
    data = f.readlines()
    word = []
    for line in data:
        word+=line.split()

    d={}
    for k in word:
        if k in d:
            d[k]+=1

        else:
            d[k]=1
    print(d)


# question 3

with open('try.txt','r') as d:
    with open('new.txt','w') as d1:
        for line in d:
            d1.write(line)

# question 4


#line in second file.
'''
a.txt
hi how are you!!
hope you are doing good!!
b.txt
i m fine!!
what about you?
'''

with open('web.txt','r') as f1, open('try.txt','r')as f2, open('new.txt','w') as f3:
    a=f1.readlines()
    b=f2.readlines()
    for line1,line2 in zip(a,b):
        line4=line1+line2
        f3.write(line4)

f4=open('new.txt','r')
print(f4.read())
f4.close()


# quetion 5

with open('try.txt','w') as f:
    for i in range(5):
        x=int(input("enter number" ))
        f.write("%d"%(x))

with open('try.txt','r') as f:
    data = f.readlines()

    for no in data:
        l=no.split()
    l.sort()

with open('new.txt','w') as f:
    for i in l:
        f.write("%s"%(i))

    


