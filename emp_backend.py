import mysql.connector

def employeedata():
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    s="create table if not exists employee(emp_id int primary key,emp_name varchar(50) not null," \
      "emp_contact varchar(50) not null unique," \
      "emp_dob date," \
      "emp_Gender varchar(2),emp_hiredate date)"
    cur.execute(s)
    mydb.commit()
    mydb.close()
def get_name(id):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    cur.execute( "select emp_id,emp_name ,emp_contact from employee where emp_id=%s", (id,) )
    name_id = cur.fetchall()
    return name_id


def add_emp_rec(emp_id,emp_name,emp_contact,emp_dob,emp_Gender,emp_hiredate):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur=mydb.cursor()
    s = "INSERT INTO employee values(%s,%s,%s,%s,%s,%s)"
    b=(emp_id,emp_name,emp_contact,emp_dob,emp_Gender,emp_hiredate)
   # cur.execute("INERT INTO employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(emp_id,emp_name,dept_id,emp_contact,emp_cnic,emp_dob,emp_Gender,emp_email,emp_hiredate,emp_status))
    cur.execute(s,b)
    mydb.commit()
    mydb.close()
def view_emp_record():
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur=mydb.cursor()
    cur.execute("select * from employee")
    row=cur.fetchall()
    mydb.commit()
    mydb.close()
    return row

def deleteRec(id):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur=mydb.cursor()
    cur.execute("DELETE from employee where emp_id=%s",(id,))
    mydb.commit()
    mydb.close()

def searchData(emp_id="",emp_name="",dept_id="",emp_contact="",emp_cnic="",emp_dob="",emp_Gender="",emp_email="",emp_hiredate="",emp_status=""):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    a="select  * from employee where emp_id=%s OR emp_name=%s OR emp_contact=%s OR emp_dob=%s OR emp_Gender=%s OR  emp_hiredate=%s"
    b=(emp_id,emp_name,emp_contact,emp_dob,emp_Gender,emp_hiredate)
    cur.execute(a,b)
    row=cur.fetchall()
    mydb.commit()
    mydb.close()
    return row

def UpdateData(id,emp_name="",emp_contact="",emp_dob="",emp_Gender="",emp_hiredate=""):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()

    cur.execute("UPDATE  employee SET  emp_name=%s ,"
                "emp_contact=%s , emp_dob=%s ,emp_Gender=%s,emp_hiredate=%s where emp_id=%s",(emp_name,emp_contact,emp_dob,emp_Gender,emp_hiredate,id))
    mydb.commit()
    mydb.close()

def fatchData(emp_id):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    a="select emp_name from employee where emp_id=%s"
    b=(emp_id,)
    cur.execute(a,b)
    row=cur.fetchall()
    mydb.commit()
    mydb.close()
    return row


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>salary_table<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def fatchData_salary(emp_id):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement')
    cur = mydb.cursor()
    a="select *from  salary where emp_id=%s"
    b=(emp_id,)
    cur.execute(a,b)
    row=cur.fetchall()
    mydb.commit()
    mydb.close()
    return row
















