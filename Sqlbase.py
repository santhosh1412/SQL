import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="localhost", user='root', password="root", database='mysqldb')


def select():
    cursor01 = con.cursor()
    sql = 'select * from users'
    cursor01.execute(sql)
    res = cursor01.fetchall()
    print(tabulate(res, headers=['ID', 'NAME', 'AGE', 'CITY']))


def insert(Name, Age, City):
    cursor02 = con.cursor()
    sql = 'insert into users (Name,Age,City) values(%s,%s,%s)'
    users = (Name, Age, City)
    cursor02.execute(sql, users)
    con.commit()
    print("Data Inserted")


def update(Name,Age,City,ID):
    cursor03 = con.cursor()
    sql = 'update users set Name=%s,Age=%s,City=%s where ID=%s'
    users = (Name,Age,City,ID)
    cursor03.execute(sql, users)
    con.commit()
    print("Data Updated")


def delete(ID):
    cursor04=con.cursor()
    sql='delete from users where ID=%s'
    users=(ID,)
    cursor04.execute(sql,users)
    con.commit()
    print("Deleted")


ch = 1
while ch == 1:
    print('''
    1.View Data
    2.Insert
    3.Update
    4.Delete''')

    c = int(input("Enter your choice:"))
    if c == 1:
        select()
    elif c == 2:
        Name = input("Enter Name: ")
        Age = input("Enter Age: ")
        City = input("Enter City: ")
        insert(Name, Age, City)
    elif c == 3:
        ID=input("Enter ID: ")
        Name = input("Enter Name: ")
        Age = input("Enter Age: ")
        City = input("Enter City: ")
        update(Name, Age, City,ID)
    elif c == 4:
        ID = input("Enter ID to delete: ")
        delete(ID)
    else:
        quit()
