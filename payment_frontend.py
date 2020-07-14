import time
import datetime
from tkinter import *
from tkinter import messagebox
import transaction_tab_back_end
import itertools
import emp_backend
import welcome
import tkinter.messagebox
id_name=[]
class Employee:

    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database")
        self.root.geometry("1450x750")
        self.root.config(bg="cadet blue")
        transaction_tab_back_end.transaction_table()
        emp_id=StringVar()

        def get_name():
            tuple = emp_backend.get_name(txtemp_id.get())
            id_name= list( itertools.chain( *tuple ) )
            if len(id_name)==0:
                messagebox.showerror( "Title", "This employee is not exist in our data base" )
                self.goto_payment1()
            else:
                self.goto_payment2( id_name )

            #self.txtemp_name.insert( END, row[0] )
            #self.txtemp_id.insert( END, row[0])
            '''print(id_name)
            print(id_name[0])
            print(id_name[)'''
            self.goto_payment2(id_name)

        TitFrame=Frame(self.root,bd=2,padx=4,pady=8,bg="Ghost White",relief=RIDGE)

        self.lblTit = Label(self.root, font=('arial', 20, 'bold'), width=80, height=3,text="Employee Database Management", bg="yellow", bd=2)
        self.lblTit.place(x=10,y=0)
        i=1
      #***********************  titel lable for dataframe left*********************************#
        self.lblemp_id = Label(self.root,font=('arial',14, 'bold'),text="Employee ID = ",padx=2,pady=2,bg="Ghost White",bd=3)
        self.lblemp_id.place(x=200,y=200)
        txtemp_id=Entry(self.root,font=('arial',16,'bold'),textvariable=emp_id,width=10,bd=5)
        txtemp_id.place(x=400,y=200)
        button5 = Button( self.root, text="PAY SALARY", width=15, height=1, font=('arial', 12, 'bold'), bg="#856ff8",command=get_name)
        button5.place( x=400, y=300)

    def goto_payment2(self,id_name1):
        self.root.destroy()
        run_payment2(id_name1)
    def goto_payment1(self):
        self.root.destroy()
        run_payment1()

        #...................................fetch fromemployee tble............................




















class paymet:
    def __init__(self,root,id_name1):
        self.root =root
        transaction_tab_back_end.transaction_table()
        self.root.title( "Employee payroll system" )
        self.root.geometry( '1350x650+0+0' )
        self.root.configure( background="powder blue" )

        Tops = Frame( self.root, width=1350, height=50, bd=8, bg="powder blue" )
        Tops.pack( side=TOP )

        f1 = Frame( self.root, width=600, height=600, bd=8, bg="powder blue" )
        f1.pack( side=LEFT )
        f2 = Frame(self.root, width=300, height=700, bd=8, bg="powder blue" )
        f2.pack( side=RIGHT )

        fla = Frame( f1, width=600, height=200, bd=8, bg="powder blue" )
        fla.pack( side=TOP )
        flb = Frame( f1, width=300, height=600, bd=8, bg="powder blue" )
        flb.pack( side=TOP )

        lblinfo = Label( Tops, font=('arial', 45, 'bold'), text="Employee Payroll  system ", bd=10, fg="green" )
        lblinfo.grid( row=0, column=0 )

        # =============================== Variables ========================================================
        self.Name = StringVar()
        self.contact = StringVar()
        self.HoursWorked = StringVar()
        self.wageshour = StringVar()
        self.Payable = StringVar()
        self.Taxable = StringVar()
        self.NetPayable = StringVar()
        self.GrossPayable = StringVar()
        self.OverTimeBonus = StringVar()
        self.Emp_id = StringVar()
        self.NINumber = StringVar()
        self.TimeOfOrder = StringVar()
        self.DateOfOrder = StringVar()

        self.DateOfOrder.set( time.strftime( "%d/%m/%Y" ) )

        # ================================ Label Widget =================================================

        lblName = Label( fla, text="Name", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue" ).grid( row=0,
                                                                                                                 column=0 )
        lblAddress = Label( fla, text="contact", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue" ).grid(
            row=0,
            column=2 )
        lblEmployer = Label( fla, text="Employee ID", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue" ).grid(
            row=1,
            column=0 )
        lblHoursWorked = Label( fla, text="Hours Worked", font=('arial', 16, 'bold'), bd=20, fg="red",
                                bg="powder blue" ).grid(
            row=1, column=2 )
        lblHourlyRate = Label( fla, text="Hourly Rate", font=('arial', 16, 'bold'), bd=20, fg="red",
                               bg="powder blue" ).grid(
            row=2, column=0 )
        lblTax = Label( fla, text="Tax", font=('arial', 16, 'bold'), bd=20, anchor='w', fg="red",
                        bg="powder blue" ).grid(
            row=3, column=0 )
        lblOverTime = Label( fla, text="OverTime Bonus", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue" ).grid(
            row=3,
            column=2 )
        lblGrossPay = Label( fla, text="GrossPay", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue" ).grid(
            row=4,
            column=0 )
        lblNetPay = Label( fla, text="Net Pay", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue" ).grid(
            row=4,
            column=2 )

        # =============================== Entry Widget =================================================

        etxname = Entry( fla, textvariable=self.Name, font=('arial', 16, 'bold'), bd=16, width=22, justify='left' )
        etxname.insert(0,id_name1[1])
        etxname.grid( row=0, column=1 )

        etxcontact = Entry( fla, textvariable=self.contact, font=('arial', 16, 'bold'), bd=16, width=22, justify='left' )
        etxcontact.insert(0,id_name1[2])
        etxcontact.grid( row=0, column=3 )

        etxemployer = Entry( fla, textvariable=self.Emp_id, font=('arial', 16, 'bold'), bd=16, width=22, justify='left' )
        etxemployer.insert(0,id_name1[0])
        etxemployer.grid( row=1, column=1 )

        etxhoursworked = Entry( fla, textvariable=self.HoursWorked, font=('arial', 16, 'bold'), bd=16, width=22,
                                justify='left' )
        etxhoursworked.grid( row=1, column=3 )

        etxwagesperhours = Entry( fla, textvariable=self.wageshour, font=('arial', 16, 'bold'), bd=16, width=22,
                                  justify='left' )
        etxwagesperhours.grid( row=2, column=1 )


        etxgrosspay = Entry( fla, textvariable=self.Payable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left' )
        etxgrosspay.grid( row=4, column=1 )

        etxnetpay = Entry( fla, textvariable=self.NetPayable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left' )
        etxnetpay.grid( row=4, column=3 )

        etxtax = Entry( fla, textvariable=self.Taxable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left' )
        etxtax.grid( row=3, column=1 )

        etxovertime = Entry( fla, textvariable=self.OverTimeBonus, font=('arial', 16, 'bold'), bd=16, width=22,
                             justify='left' )
        etxovertime.grid( row=3, column=3 )

        # =============================== Text Widget ============================================================

        payslip = Label( f2, textvariable=self.DateOfOrder, font=('arial', 21, 'bold'), fg="red", bg="powder blue" ).grid(
            row=0,
            column=0 )
        self.txtpayslip = Text( f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="green", bg="powder blue" )
        self.txtpayslip.grid( row=1, column=0 )

        # =============================== buttons ===============================================================

        btnsalary = Button( fla, text='Weekly Salary', padx=16, pady=3, bd=4, font=('arial', 16, 'bold'), width=10,
                            fg="red",
                            bg="black", command=self.weeklywages).grid( row=2, column=3)

        btnreset = Button( flb, text='Reset', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14,
                           command=self.reset,
                           fg="red", bg="powder blue" ).grid( row=0, column=1 )

        btnpayslip = Button( flb, text='View Payslip', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14,
                             command=self.enterinfo, fg="red", bg="powder blue" ).grid( row=0, column=2 )
        btnexit = Button( flb, text='back', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14,
                          command=self.back,
                          fg="red", bg="powder blue" ).grid( row=0, column=3 )
        btnexit = Button( flb, text='Exit System', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14,
                          command=exit,
                          fg="red", bg="powder blue" ).grid( row=0, column=4 )

    def back(self):
        jump_to_main()

    def exit(self):
        exit = tkinter.messagebox.askyesno( "Employee system", "Do you want to exit the system" )
        if exit > 0:
            root.destroy()
            return


    def reset(self):
        self.Name.set( "" )
        self.contact.set( "" )
        self.HoursWorked.set( "" )
        self.wageshour.set( "" )
        self.Payable.set( "" )
        self.Taxable.set( "" )
        self.NetPayable.set( "" )
        self.GrossPayable.set( "" )
        self.OverTimeBonus.set( "" )
        self.Emp_id.set( "" )
        self.NINumber.set( "" )
        self.txtpayslip.delete( "1.0", END )


    def enterinfo(self):
        self.txtpayslip.delete( "1.0", END )
        self.txtpayslip.insert( END, "\t\tPay Slip\n\n" )
        self.txtpayslip.insert( END, "Employer :\t\t" + self.Emp_id.get() + "\n\n" )
        self.txtpayslip.insert( END, "Name :\t\t" + self.Name.get() + "\n\n" )
        self.txtpayslip.insert( END, "Contact:\t\t" +self.contact.get() + "\n\n" )
        #self.txtpayslip.insert( END, "NI Number :\t\t" + self.NINumber.get() + "\n\n" )
        self.txtpayslip.insert( END, "Hours Worked :\t\t" + self.HoursWorked.get() + "\n\n" )
        self.txtpayslip.insert( END, "Wages per hour :\t\t" + self.wageshour.get() + "\n\n" )
        self.txtpayslip.insert( END, "Payable :\t\t" + self.Payable.get() + "\n\n" )
        self.txtpayslip.insert( END, "Tax Paid :\t\t" + self.Taxable.get() + "\n\n" )
        self.txtpayslip.insert( END, "Net Payable :\t\t" + self.NetPayable.get() + "\n\n" )



    def weeklywages(self):
        self.txtpayslip.delete( "1.0", END )
        hoursworkedperweek = float( self.HoursWorked.get() )
        wagesperhours = float( self.wageshour.get() )

        paydue = wagesperhours * hoursworkedperweek
        paymentdue = "INR", str( '%.2f' % (paydue) )
        self.Payable.set( paymentdue )

        tax = paydue * 0.2
        taxable = "INR", str( '%.2f' % (tax) )
        self.Taxable.set( taxable )

        netpay = paydue - tax
        netpays = "INR", str( '%.2f' % (netpay) )
        self.NetPayable.set( netpays )

        if hoursworkedperweek > 40:
            overtimehours = (hoursworkedperweek - 40) + wagesperhours * 1.5
            overtime = "INR", str( '%.2f' % (overtimehours) )
            ov=overtimehours
            self.OverTimeBonus.set( overtime )
        elif hoursworkedperweek <= 40:
            overtimepay = (hoursworkedperweek - 40) + wagesperhours * 1.5
            overtimehrs = "INR", str( '%.2f' % (overtimepay))
            ov=overtimepay
            self.OverTimeBonus.set(overtimehrs)

        transaction_tab_back_end.add_emp_rec( str( self.Emp_id.get()),
                                               hoursworkedperweek, wagesperhours ,
                                              ov,
                                              tax,netpay ,
                                              paydue )

        return

def run_payment1():
    root = Tk()
    application=Employee(root)
    root.mainloop()


def run_payment2(id_name1):
    root = Tk()
    application=paymet(root,id_name1)
    root.mainloop()
def jump_to_main():
    welcome.run_welcome()

if __name__=='__main__':
        root=Tk()
        application = Employee( root )
        root.mainloop()

