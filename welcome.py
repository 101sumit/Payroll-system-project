from tkinter import *
import payment_frontend
import employee_front

class main_class:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome Page Interface")
        self.root.minsize(width = 1370, height = 700)
        self.root.maxsize(width = 1370, height = 700)

        button2 = Label(self.root, text = "welcome to payroll system", width = 150, height = 2, font=('arial', 20, 'bold'),bg="cyan",relief=RAISED)
        button2.pack(padx = 1, pady = 50 )

        username_frame = Frame(self.root)
        label = Label(username_frame, text="Username")
        label.pack(side=LEFT)
        button5 = Button(self.root, text = "PAY SALARY", width = 15, height = 5,font=('arial', 12, 'bold'),bg="#856ff8",command=self.goto_payment)
        button5.place(x=400,y=200)

        button5 =Button( self.root, text="EMPLOYEE DATA", width=15, height=5,font=('arial', 12, 'bold') ,bg="yellow",command=self.goto_employee)
        button5.place( x=700, y=200 )

        #button5 =Button( self.root, text="Structure of Salary", width=15, height=5,font=('arial', 12, 'bold'),bg="gray")
        #button5.place( x=800, y=200 )
    def goto_payment(self):
        self.root.destroy()
        payment_frontend.run_payment1()
    def goto_employee(self):
        self.root.destroy()
        employee_front.run_employee()


def run_welcome():
    root = Tk()
    application = main_class( root )
    root.mainloop()


if  __name__=='__main__':
    root=Tk()
    application=main_class(root)
    root.mainloop()
