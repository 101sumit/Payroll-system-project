import mysql.connector
from datetime import datetime

def transaction_table():
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur = mydb.cursor()
    s="create table if not exists transaction(trans_id int primary key AUTO_INCREMENT,emp_id int, FOREIGN KEY(emp_id) references employee(emp_id),date_of_transaction date,working_hrs decimal(9,2),hourly_rat decimal(8,2),bonus int,tax decimal(9,2),gross_salary int,net_salary int);"
    cur.execute(s)
    mydb.commit()
    mydb.close()


def add_emp_rec(emp_id,houres,hp_rate,bonus,tax,net_salary,gross):
    print(emp_id,houres,hp_rate,bonus,tax,net_salary,gross)
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur=mydb.cursor()

    now = datetime.now()
    formatted_date = now.strftime( '%Y-%m-%d %H:%M:%S' )
    # Assuming you have a cursor named cursor you want to execute this query on:

    s = "INSERT INTO transaction (emp_id,date_of_transaction,working_hrs,hourly_rat,emp_bonus,emp_tax,net_salary,gross_salary) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    b=(emp_id,formatted_date,houres,hp_rate,bonus,tax,net_salary,gross)
    cur.execute(s,b)
    mydb.commit()
    mydb.close()

def view_emp_record():
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="rasuur44", database='payrollmanagement' )
    cur=mydb.cursor()
    cur.execute("select * from transaction")
    row=cur.fetchall()
    mydb.commit()
    mydb.close()
    return row

