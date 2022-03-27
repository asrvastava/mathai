import pymysql
import sqlite3
import basic
import numpy

def create(host,password,username):
    server=pymysql.connect(host=host,user=username,password=password)
    a=server.cursor()
    basic.speak("what is the name of  database you want to create ")
    print("what is the name of database create")
    db=basic.takecommand()
    k=a.execute("create %s",(db))
    if k==True:
        basic.speak("do you also want to create a table sir ")
        m=basic.takecommand()
        if "yes" in m:
            basic.speak("what is the name of tables do you want to create ")
            table=basic.takecommand()
            basic.speak("how many entity for coloum sir")
            column=basic.takecommand()
            int(column)
            a=numpy.array([25])
            for n in column:
                a[n]=basic.takecommand()

            b=numpy.array([25])
            for k in column:
                b[k]=basic.takecommand()   

            for f in column:

                a.execute("create table %s (%s %s,)",(table,a[f],m[f]))

            exit()    

        
def query(host,password,username):
    server=pymysql.connect(host=host,user=username,password=password)
    a=server.cursor()
    
    basic.speak("which type of query you want to do")
    q=basic.takecommand().lower()
    if 'select'in  q :
        basic.speak("which table you want to place query")
        table=basic.takecommand()
        basic.speak("which column do you want to select")
        basic.speak("enter the column name")
        column=basic.takecommand()
        basic.speak("which entity do you want on which you want to do query")
        base=basic.takecommand()
        basic.speak("value of that entity")
        value=basic.takecommand()
            
        basic.speak("do you want add more specification for query yes or no")
        extra=basic.takecommand().lower
        if "yes" in extra:
            basic.speak("with which coperatorr you want to add specification or /and")
            n=basic.takecommand().lower()
            if "and" in n:
                basic.speak("which entity do you want on which you want to do query")
                base1=basic.takecommand()
                basic.speak("value of that entity")
                value1=basic.takecommand()
                return a.execute("select %s from %s where %s=%s and %s=%s",(column,table,base,value,base1,value1))

            if "or" in n:
                basic.speak("which entity do you want on which you want to do query")
                base1=basic.takecommand()
                basic.speak("value of that entity")
                value1=basic.takecommand()
                return a.execute("select %s from %s where %s=%s or %s=%s",(column,table,base,value,base1,value1))
        else:
            return a.execute("select %s from %s where %s=%s",(column,table,base,value))

def update(host,username,password):
    server=pymysql.connect(host=host,user=username,password=password)
    a=server.cursor()
    basic.speak("enter table name")
    table=input("enter table name")
    basic.speak("enter target entity")
    entity=input("enter target entity")
    basic.speak("enter value of entity")
    value=input("enter value of entity")
    basic.speak("enter new value")
    nvalue=input("enter new value")
    try:
        a.execute('update %s set value=%s where %s=5s',(table,nvalue,entity,value,))
    except Exception:
        print(Exception)    

def delete(host,username,password):
    server=pymysql.connect(host=host,user=username,password=password)
    a=server.cursor()
    basic.speak("enter table name you want to delete")
    table=input("enter table name you want to delete")
    basic.speak("enter target entity")
    entity=input("enter target entity")
    basic.speak("enter value of entity")
    value=input("enter value of entity")
    a.execute('delete from %s where %s=%s',(table,entity,value,))

def  orderby(host,username,password):
    server=pymysql.connect(host=host,user=username,password=password)
    a=server.cursor()
    basic.speak("enter target entity")
    entity=input("enter target entity")
    basic.speak("enter table name")
    table=input("enter table name")
    basic.speak("order by ascending or descending order")
    order=input('ASC for ascending or DESC for decending order')
    if order=='ASC' or order=="asc":
        a.execute('select %s from %s ORDERBY %s ASC',(entity,table,entity,))

    if order=='DESC' or order=="desc": 
        a.execute('select %s from %s ORDERBY %s DESC',(entity,table,entity,))
    


def droptable(host,username,password):
    server=pymysql.connect(host=host,user=username,password=password)
    a=server.cursor()
    basic.speak("enter table name")
    table=input("enter table name")
    a.execute('DROP %s',(table))
    
