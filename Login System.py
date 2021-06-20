from tkinter import *
from tkinter import messagebox as ms
import sqlite3

with sqlite3.connect('Logdb.db') as db:
    c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL,password TEXT NOT NULL)")
db.commit()
db.close()


class main:
    def __init__(self, master):
        self.master = master
        # username and password for login page
        self.username = StringVar()
        self.password = StringVar()
        # username and password for create account page
        self.n_username = StringVar()
        self.n_password = StringVar()

        self.widgets()

    def login(self):
        # with this method, the user login if had an account
        with sqlite3.connect('Logdb.db') as db:
            c = db.cursor()
        find_user = 'SELECT * FROM user WHERE username=? and password=?'
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Logged in'
            self.head['pady'] = 150
            self.logou.pack()
        else:
            ms.showerror("Oops!", "Username Not Found.")

    def logout(self):
        self.head['text'] = 'LOGIN'
        self.head['pady'] = 10
        self.logou.pack_forget()
        self.logf.pack()
        self.username.set('')
        self.password.set('')

    def new_user(self):
        # with this method , the user create an account
        with sqlite3.connect('Logdb.db') as db:
            c = db.cursor()
        find_user = 'SELECT * FROM user WHERE username=?'
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken! try a diffrent one')
        else:
            ms.showinfo('Success', 'Account Created!')
            self.log()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()

        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master, text="LOGIN", font=('', 35), pady=10)
        self.head.pack()
        # create a frame for widgets of loginpage
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text="Username: ", font=('', 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text="Password: ", font=('', 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text="Login", bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text="Create Account", font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2, column=1)
        self.logf.pack()
        # create a frame for widgets of create account page
        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text="Username: ", font=('', 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text="Password: ", font=('', 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text="Create Account", bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text="Go To Login", font=('', 15), padx=5, pady=5, command=self.log).grid(row=2, column=1)
        self.logou = Frame(self.master, padx=10, pady=10)
        Button(self.logou, text="Logout", font=('', 15), padx=5, pady=5, command=self.logout).grid(row=5, column=5)

root = Tk()
main(root)
root.mainloop()
