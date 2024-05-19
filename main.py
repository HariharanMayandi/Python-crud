
import mysql.connector
from tabulate import tabulate

con=mysql.connector.connect(host='localhost',user='root',password='Anya@2927',database='python_db')


def insert(NAME,AGE,CITY):
    cur=con.cursor()
    sql='Insert into users(NAME,AGE,CITY) values(%s,%s,%s) '
    user=(NAME,AGE,CITY)
    cur.execute(sql,user)
    con.commit()
    print('Inserted Successfully')
    select()

def update(NAME,AGE,CITY,ID):
    cur=con.cursor()
    sql='update  users set NAME=%s,AGE=%s,CITY=%s where id=%s'
    user=(NAME,AGE,CITY,ID)
    cur.execute(sql,user)
    con.commit()
    print('Successfully updated')
    print('This is the updated Table')
    select()

def select():
    res=con.cursor()
    sql='select ID,NAME,AGE,CITY from users'
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=['ID','NAME','AGE','CITY']))



def delete(ID):
    cur=con.cursor()
    sql='delete from users where ID=%s'
    user=(ID,)
    cur.execute(sql,user)
    con.commit()
    print('Deleted successfully')
    select()

def exit():
    print('done')
    quit()

while True:
    print('Options for you:')
    print('   select type Select')
    print('   select type Update')
    print('   select type Insert')
    print('   select type Delete')
    print('   select type Exit')
    enter=input('Enter any one option from above option: ')
    entercap=enter.capitalize()
    if entercap=='Select':
        select()
    elif entercap=='Insert':
        NAME=input('Enter Name: ')
        AGE=input('Enter AGE: ')
        CITY=input("Enter City: ")
        insert(NAME,AGE,CITY)
    elif entercap == 'Update':
        ID=input('Enter Id: ')
        NAME = input('Enter Name: ')
        AGE = input('Enter AGE: ')
        CITY = input("Enter City: ")
        update(NAME,AGE,CITY,ID)
    elif entercap == 'Delete':
        ID=input('Enter Id :')
        delete(ID)
    elif entercap == 'Exit':
        exit()
    else:
        print('Enter valid option,try again')

