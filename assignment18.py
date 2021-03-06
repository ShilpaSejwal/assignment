#Question1
import pymysql as pm

try:
    con=pm.connect(host='localhost', database='sahil', user='root', password='India@123',port=3304)
    cursor=con.cursor()
    
    query1 = 'create table Book(Book_ID int(5) primary key,Title_ID int(5),Location varchar(10),Genre varchar(10))'
    query2 = 'create table Titles(Title_ID int(5) primary key,ISBN int(5),Publisher_ID int(10),Publication_Year int(10))'
    query3 = 'create table Publishers(Publisher_ID int(5) primary key,Name varchar(10),Street_Address varchar(10),Suit_Number int(10),Zip_Code_ID int(5))'
    query4 = 'create table Zipcodes(Zipcode_ID int(5) primary key,City varchar(10),State varchar(10),Zip_Code int(5))'
    query5 = 'create table Authors_Titles(Author_Title_ID int(5) primary key,Author_ID int(5),Title_ID int(5))'
    query6 = 'create table Authors(Author_ID int(5) primary key,FirstName varchar(10),MiddleName varchar(10),LastName varchar(10))'
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    cursor.execute(query6)
    print("connection established")

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print("problem",e)

finally:
    cursor.close()
    con.close()


#Question2

import pymysql as pm
try:
    con=pm.connect(host='localhost', database='sahil', user='root', password='India@123',port=3304)
    cursor = con.cursor()

    query1_mul = "insert into Book values(%s,%s,%s,%s)"
    data = [(1,20,'New Delhi','Comedy'),
            (2,21, 'Haryana', 'Fiction'),
            (3,22, 'Mumbai', 'Action')]
    cursor.executemany(query1_mul,data)

    con.commit()
    print("Data inserted in table")

except pm.DatabaseError as e:
    if con:
        con.rollback()
    print("problem",e)

finally:
    cursor.close()
    con.close()

#Question3
import pymysql as pm

try:
    con = pm.connect(host='localhost', database='sahil', user='root' ,password='India@123',port=3304)
    cursor = con.cursor()

    query1_select = 'select * from Book'
    cursor.execute(query1_select)
    

    data = cursor.fetchall()
    for row in data:
        print("Book_ID: {}, Title_ID: {}, Location: {}, Genre: {} ".format(row[0] ,row[1] ,row[2] ,row[3]))

    # update
    query1 = "update Book set Location='Rajasthan' where Book_ID= 1 "
    cursor.execute(query1)
    query2 = "update Book set Title_ID=Title_ID+3 where Book_ID= 1 "
    cursor.execute(query2)

    query1_select = 'select * from Book'
    cursor.execute(query1_select)
    

    data = cursor.fetchall()
    for row in data:
       print("Book_ID: {}, Title_ID: {}, Location: {}, Genre: {} ".format(row[0], row[1], row[2], row[3]))

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print("problem" ,e)

finally:
    con.close()
