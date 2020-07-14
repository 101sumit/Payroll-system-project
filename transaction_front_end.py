from tkinter import *
import tkinter.messagebox
import emp_backend
import itertools
class Employee:

    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database")
        self.root.geometry("1450x750")
        self.root.config(bg="cadet blue")
        emp_id=StringVar()
        def putdefault():
                tuple=emp_backend.fatchData(1)
                row=list(itertools.chain( *tuple))
                self.txtemp_name.insert(END,row[0])
                self.txtemp_id.insert(END,row[0])
                print(row)


        TitFrame=Frame(self.root,bd=2,padx=4,pady=8,bg="Ghost White",relief=RIDGE)



        #DataFrameDisplay = Frame(MainFrame,height=600,width=400,padx=18, pady=5, bg="Ghost White", relief=RIDGE, bd=7 )
        #DataFrameDisplay.pack(side=RIGHT)

        #******************************************data frame  end***************************************#
        # *********************************************list box&scrolling widget****************************************#

        #*********************************************list box&scrolling widget end****************************************#




        self.lblTit = Label(self.root, font=('arial', 20, 'bold'), width=80, height=3,text="Employee Database Management", bg="yellow", bd=2)
        self.lblTit.place(x=10,y=0)
        i=1
      #***********************  titel lable for dataframe left*********************************#
        self.lblemp_id = Label(self.root,font=('arial',14, 'bold'),text="Employee ID = ",padx=2,pady=2,bg="Ghost White",bd=3)
        self.lblemp_id.place(x=200,y=200)
        self.txtemp_id=Entry(self.root,font=('arial',16,'bold'),textvariable=emp_id,width=10,bd=5)
        self.txtemp_id.place(x=400,y=200)
        button5 = Button( self.root, text="PAY SALARY", width=15, height=1, font=('arial', 12, 'bold'), bg="#856ff8")
        button5.place( x=400, y=300)

        def goto_payment2(self):
            self.root.destroy()
            run_payment2()

        #...................................fetch fromemployee tble............................





def run_payment1():
    root = Tk()
    application=Employee(root)
    root.mainloop()

if  __name__=='__main__':
    root=Tk()
    application=Employee(root)
    root.mainloop()

