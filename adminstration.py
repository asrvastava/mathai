import pymysql
import sqlite3
import basic
import numpy



def admin(email,password):



    server = pymysql.connect( host="localhost", user="root",password="Asrmath1053#")
    a = server.cursor()

    sql="USE jarvis;"
    a.execute(sql)
    try: 
    
        a.execute('SELECT name FROM password WHERE email = %s AND password = %s', (email, password,))
        r=a.fetchall() 
        
        
    except Exception as e:
        print(e)

    return r    


def forget(npassword,phone_no):
    server=pymysql.connect(host="localhost",user="root",password="Asrmath1053#")
    a=server.cursor()
    sql="use jarvis;"
    a.execute(sql)
    try:
        a.execute('update password set password= %s where phone_no=%s',(npassword,phone_no,))
        k=a.fechall()
        str(k)

    except Exception as e:
        print(e)

    return k    
