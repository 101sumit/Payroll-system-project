from tkinter import *
import tkinter.messagebox
import emp_backend
import welcome
class Employee:

    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database")
        self.root.geometry("1450x800+0+0")
        self.root.config(bg="cadet blue")
        emp_id=StringVar()
        emp_name = StringVar()
        dept_id=StringVar()
        emp_contact = StringVar()
        emp_cnic = StringVar()
        emp_dob = StringVar()
        #emp_image = StringVar()
        emp_Gender = StringVar()
        emp_email = StringVar()
        emp_hiredate = StringVar()
        emp_status = StringVar()

        #*********************function*************************#
        def iExit():
            iExit=tkinter.messagebox.askyesno("Employee Database Management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return
        def ClearData():
            self.txtemp_id.delete( 0, END )
            self.txtemp_name.delete( 0, END )
            self.txtemp_contact.delete(0,END)
            self.txtemp_DOB.delete( 0, END )
            self.txtemp_gender.delete( 0, END )

            self.txtemp_hiredate.delete( 0, END )


        def addData():
            if(len(emp_id.get())!=0):
                emp_backend.add_emp_rec( emp_id.get(), emp_name.get(),emp_contact.get(),emp_dob.get(), emp_Gender.get(), emp_hiredate.get())
                emplist.delete(0,END)
                emplist.insert(END,emp_id.get(),emp_name.get(),emp_contact.get(),emp_dob.get(),emp_Gender.get(),emp_hiredate.get())

        def DisplayData():
             emplist.delete(0,END)
             all_data = emp_backend.view_emp_record()
             for row in all_data:
                 emplist.insert(END,row,str(""))
             if len(all_data)==0:
                 emplist.insert( END,"TABLE IS EMPTY", str( "" ) )



        def  eventData(event):
            global sd
            searchemp=emplist.curselection()[0]
            sd=emplist.get(searchemp)

            self.txtemp_contact.delete( 0, END )
            self.txtemp_contact.insert( END,sd[1])

            self.txtemp_id.delete( 0, END )
            self.txtemp_id.insert( END,sd[2])


            self.txtemp_name.delete( 0, END )
            self.txtemp_name.inserte(END,sd[3])


            self.txtemp_DOB.delete( 0, END )
            self.txtemp_DOB.inserte(END,sd[6])

            self.txtemp_hiredate.delete( 0, END )
            self.txtemp_hiredate.inserte(END,sd[7])


            self.txtemp_gender.delete( 0, END )
            self.txtemp_gender.inserte(END,sd[9])

        def deleteData():
            if(len(emp_id.get())!=0):
                emp_backend.deleteRec( emp_id.get() )
                DisplayData()

        def searchDatabase():
            emplist.delete(0,END)
            all_data=emp_backend.searchData( emp_id.get(), emp_name.get(), emp_contact.get(),
                                               emp_dob.get(), emp_Gender.get(),emp_hiredate.get() )
            for row in all_data:
                emplist.insert(END,row,str(""))
            if len(all_data)==0:
                emplist.insert( END, "data is not found", str( "" ) )
        def back():
            jump_to_main()

        def update():
            if (len( emp_id.get() ) != 0):
                emp_backend.UpdateData( emp_id.get(), emp_name.get(), emp_contact.get(), emp_dob.get(),
                                         emp_Gender.get(), emp_hiredate.get() )
                emplist.delete( 0, END )
                emplist.insert( END, emp_id.get(), emp_name.get(), emp_contact.get(), emp_dob.get(), emp_Gender.get(),
                                emp_hiredate.get() )

        #*****************************************frames title ******************#
        MainFrame=Frame(self.root,bg="cadet blue",height=700)
        MainFrame.grid()

        TitFrame=Frame(MainFrame,bd=2,padx=4,pady=8,bg="Ghost White",relief=RIDGE)
        TitFrame.pack()
        ButtonFrame = Frame(MainFrame, padx=5, pady=20, bg="cadet blue", relief=RIDGE)
        ButtonFrame.pack( side=BOTTOM )

        DataFrameDisplay = Frame( MainFrame,padx=2, pady=3, bg="Ghost White", relief=RIDGE,
                                  bd=7 )
        DataFrameDisplay.pack( side=RIGHT )

        DataFrame = Frame(MainFrame,padx=5,width=300, pady=2, bg="Ghost White", relief=RIDGE,bd=7 )
        DataFrame.pack(side=LEFT)



        #******************************************data frame  end***************************************#
        # *********************************************list box&scrolling widget****************************************#
        scrollbar=Scrollbar(DataFrameDisplay)
        scrollbar.grid(row=0,column=1,sticky='ns')

        emplist=Listbox(DataFrameDisplay,width=70,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        emplist.bind('<<ListboxSelect>>',eventData)
        emplist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=emplist.yview)

        #*********************************************list box&scrolling widget end****************************************#




        self.lblTit = Label( TitFrame, font=('arial', 20, 'bold'), width=80, height=1,text="Employee Database Management", bg="Ghost White", bd=2 )
        self.lblTit.grid()

      #***********************  titel lable for *********************************#
        self.lblemp_id = Label(DataFrame,font=('arial',14, 'bold'),text="Employee ID",padx=20,pady=10,bg="Ghost White",bd=3)
        self.lblemp_id.grid(row=0,column=0,sticky=W)
        self.txtemp_id=Entry(DataFrame,font=('arial',16,'bold'),textvariable=emp_id,width=30,bd=5)
        self.txtemp_id.grid(row=0,column=4)

        self.lblemp_name = Label(DataFrame, font=('arial', 14, 'bold'), text="Name", padx=20, pady=10,bg="Ghost White" ,bd=3)
        self.lblemp_name.grid(row=2,column=0,sticky=W)
        self.txtemp_name = Entry(DataFrame, font=('arial', 16, 'bold'), textvariable=emp_name, width=30, bd=5 )
        self.txtemp_name.grid( row=2, column=4 )


        self.lblemp_contact = Label( DataFrame, font=('arial', 14, 'bold'), text="Contact", padx=20, pady=10,bg="Ghost White",bd=3)
        self.lblemp_contact.grid(row=4,column=0,sticky=W)
        self.txtemp_contact = Entry( DataFrame, font=('arial', 16, 'bold'), textvariable=emp_contact, width=30, bd=5 )
        self.txtemp_contact.grid( row=4, column=4 )

        self.lblemp_DOB = Label( DataFrame, font=('arial', 14, 'bold'), text="DOB", padx=20, pady=10,bg="Ghost White", bd=3 )
        self.lblemp_DOB.grid(row=8,column=0,sticky=W)
        self.txtemp_DOB = Entry( DataFrame, font=('arial', 16, 'bold'), textvariable=emp_dob, width=30, bd=5 )
        self.txtemp_DOB.insert( 0, 'YYYY-MM-DD' )
        self.txtemp_DOB.bind( "<Button-1>", lambda event: clear_entry( event, self.txtemp_DOB ) )
        self.txtemp_DOB.grid( row=8, column=4 )






        def clear_entry(event, entry):
            entry.delete( 0, END )


        self.lblemp_gender = Label( DataFrame, font=('arial', 14, 'bold'), text="Gender", padx=20, pady=10,bg="Ghost White", bd=3 )
        self.lblemp_gender.grid(row=12,column=0,sticky=W)
        self.txtemp_gender = Entry( DataFrame, font=('arial', 16, 'bold'), textvariable=emp_Gender, width=30, bd=5 )

        self.txtemp_gender.grid( row=12, column=4 )



        self.lblemp_hiredate = Label( DataFrame, font=('arial', 14, 'bold'), text="hiredate", padx=20, pady=10,bg="Ghost White", bd=3 )
        self.lblemp_hiredate.grid(row=16,column=0,sticky=W)
        self.txtemp_hiredate = Entry( DataFrame, font=('arial', 16, 'bold'), textvariable=emp_hiredate, width=30, bd=5)
        self.txtemp_hiredate.insert(0,'YYYY-MM-DD')
        self.txtemp_hiredate.bind( "<Button-1>", lambda event: clear_entry( event, self.txtemp_hiredate ) )


        self.txtemp_hiredate.grid( row=16, column=4 )





#*****************************************BOTTON**************************************#
        self.btnaddData=Button(ButtonFrame,text="Add New",font=('arial',8,'bold'),height=1,width=10,padx=5,bd=4,command=addData)
        self.btnaddData.grid(row=20,column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial',8, 'bold'), height=1, width=5,padx=5, bd=4,command=DisplayData )
        self.btnDisplayData.grid( row=20, column=1 +1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial',8, 'bold'), height=1, width=10, bd=4,padx=5 ,command=ClearData)
        self.btnClearData.grid( row=20, column=2+2 )

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial',8, 'bold'), height=1, width=5,padx=5, bd=4,command=deleteData)
        self.btnDeleteData.grid( row=20, column=3+3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial',8, 'bold'), height=1,padx=5, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid( row=20, column=4 +4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial',8, 'bold'), height=1,padx=5,bd=4, width=10,command=update)
        self.btnUpdateData.grid( row=20, column=5 +5)

        self.btnExit = Button(ButtonFrame,text="Exit", font=('arial',8, 'bold'), height=1, width=10,padx=5, bd=4 ,command=iExit)
        self.btnExit.grid( row=20, column=6 +6)

        self.btnExit = Button( ButtonFrame, text="back", font=('arial', 8, 'bold'), height=1, width=10, padx=5, bd=4,
                               command=back )
        self.btnExit.grid( row=20, column=7 + 7 )


def run_employee():
    root = Tk()
    application=Employee(root)
    root.mainloop()
def jump_to_main():
    welcome.run_welcome()

if  __name__=='__main__':
    root=Tk()
    application=Employee(root)
    root.mainloop()

