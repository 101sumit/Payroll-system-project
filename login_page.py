from tkinter import *
import admin_backend
from tkinter import *
from tkinter import messagebox
import itertools
import welcome
class LoginPage:
    def __init__(self, root):
        row=admin_backend.check_admin_presant()
        row = list( itertools.chain( *row ) )
        print(row)
        print(len(row))
        admin_backend.admin_create()
        password=StringVar()
        con_password = StringVar()
        username=StringVar()
        self.login_screen=root

        def searchDatabase():
            all_data = admin_backend.searchData(username.get(),password.get())
            if len(all_data)==0:
                messagebox.showwarning( "Warning", "Wrong UserId or Password" )
            else:
                #messagebox.showwarning( 'Log in',"you are log in successfully")
                open_welcome()

        def add_admin():
            admin_backend.adminRec(username.get(),password.get())
            open_welcome()
        self.login_screen.minsize( width=1370, height=700 )
        self.login_screen.maxsize( width=1370, height=700 )
        def pass_match():
            if password.get()==con_password.get() and len(password.get())!=0 and len(username.get())!=0:
                add_admin()
            else:
                messagebox.showwarning( "error","password is not matching" )


#...........................log in..........................
        def login():
            self.login_screen.title( "Login" )
            self.login_screen.geometry( "1450x750" )
            Label( self.login_screen, text="Please Enter Login details", width=150, height=2,
                   font=('arial', 20, 'bold'), bg="cyan", pady=10, relief=RAISED ).pack()
            Label( self.login_screen, text="" ).pack()
            Label( self.login_screen, text="Username", width=15, font=('arial', 20, 'bold'), pady=10, bg="cyan",
                   relief=RAISED ).pack()
            username_login_entry = Entry( self.login_screen, textvariable=username, width=40, bd=10 )
            username_login_entry.pack()
            Label( self.login_screen, text="" ).pack()
            Label( self.login_screen, text="Password", width=15, font=('arial', 20, 'bold'), bg="cyan", pady=10,
                   relief=RAISED ).pack()
            password__login_entry = Entry( self.login_screen, textvariable=password, show='*', width=40, bd=10 )
            password__login_entry.pack()
            Label( self.login_screen, text="" ).pack()
            Button( self.login_screen, text="Login", width=10, height=1, bg="yellow", command=searchDatabase ).pack()
            self.login_screen.mainloop()
        def Register():
            self.login_screen.title( "Register" )
            self.login_screen.geometry( "1450x750" )
            Label( self.login_screen, text="Please Enter signup details", width=150, height=2,
                   font=('arial', 20, 'bold'), bg="cyan", pady=10, relief=RAISED ).pack()
            Label( self.login_screen, text="" ).pack()
            Label( self.login_screen, text="Username", width=15, font=('arial', 20, 'bold'), pady=10, bg="cyan",
                   relief=RAISED ).pack()
            username_login_entry = Entry( self.login_screen, textvariable=username, width=40, bd=10 )
            username_login_entry.pack()
            Label( self.login_screen, text="" ).pack()
            Label( self.login_screen, text="Password", width=15, font=('arial', 20, 'bold'), bg="cyan", pady=10,
                   relief=RAISED ).pack()
            password__login_entry = Entry( self.login_screen, textvariable=password, show='*', width=40, bd=10 )
            password__login_entry.pack()
            Label( self.login_screen, text="" ).pack()

            Label( self.login_screen, text="Confirm Password", width=15, font=('arial', 20, 'bold'), bg="cyan", pady=10,
                   relief=RAISED ).pack()
            self.con_password__login_entry = Entry( self.login_screen, textvariable=con_password, show='*', width=40, bd=10 )
            self.con_password__login_entry.pack()
            Label( self.login_screen, text="" ).pack()

            Button( self.login_screen, text="Login", width=10, height=1, bg="yellow", command=pass_match).pack()

            self.login_screen.mainloop()
        if len(row)!=0:
            login()
        else:
            Register()

#.......................register............................

def open_welcome():
    root.destroy()
    welcome.run_welcome()

if  __name__=='__main__':
    root=Tk()
    application=LoginPage(root)
    root.mainloop()
