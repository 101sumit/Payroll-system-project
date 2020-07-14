import mysql.connector
import itertools

from mysql.connector import Error

def admin_create():
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS admin(admin_user varchar(20) PRIMARY KEY,pasword text)")
    mydb.commit()
    mydb.close()


def adminRec(admin,password):
        mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
        cur = mydb.cursor()
        cur = mydb.cursor()
        cur.execute("INSERT INTO admin VALUES(%s,%s)",(admin,password))
        mydb.commit()
        mydb.close()
def check_admin_presant():
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    cur.execute( "select * from admin")
    row = cur.fetchall()
    return row


def searchData(user,pas):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    cur.execute("select * from admin where admin_user =%s and pasword=%s",(user,pas))
    rows=cur.fetchall()
    mydb.close()
    return rows


def dataUpdate(admin="",pasword=""):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    tuple0 =searchData()
    tuple0_list_admin = list(itertools.chain(*tuple0))
    cur.execute("update admin set admin_user=%s,pasword=%s where admin_user=%s",(admin,pasword,tuple0_list_admin[0]))
    mydb.commit()
    mydb.close()

