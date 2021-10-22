import tkinter as tk
#from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
window = tk.Tk()
window.geometry("1920x1080")
window.title("REGISTRATION FORM")
window.configure(background="#57BC90")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
# database code
db = sqlite3.connect('DATA.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS DOCTOR_DATA"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()


def password_check(passwd):

    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val


def insert():

    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('DATA.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM DOCTOR_DATA WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if(fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif(addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif(email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile))) < 10 or len(str((mobile))) > 10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif((time > 100) or (time < 16)):
        ms.showinfo("Message", "Please Enter valid age")
    elif(c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif(pwd == "") or (password_check(pwd)) != True:
        ms.showinfo("Message", "Please Enter valid password")
    elif(var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('DATA.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO DOCTOR_DATA(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                           (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')

            window.destroy()
            from subprocess import call
            call(["python", "Login.py"])


l1 = tk.Label(window, text="Registration Form", font=(
    "Times new roman", 15, "bold"), bg="#77C9D4", fg="black")
l1.place(x=250, y=50)

# that is for label1 registration

l2 = tk.Label(window, text="Full Name :", width=12, font=(
    "Times new roman", 15, "bold"), bg="#77C9D4")
l2.place(x=130, y=100)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=330, y=100)
# that is for label 2 (full name)


l3 = tk.Label(window, text="Address :", width=12, font=(
    "Times new roman", 15, "bold"), bg="#77C9D4")
l3.place(x=130, y=150)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=330, y=150)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(window, text="E-mail :", width=12,
              font=("Times new roman", 15, "bold"), bg="#77C9D4")
l5.place(x=130, y=200)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=330, y=200)
# that is for email address

l6 = tk.Label(window, text="Phone number :", width=12,
              font=("Times new roman", 15, "bold"), bg="#77C9D4")
l6.place(x=130, y=250)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=330, y=250)
# phone number
l7 = tk.Label(window, text="Gender :", width=12, font=(
    "Times new roman", 15, "bold"), bg="#77C9D4")
l7.place(x=130, y=300)
# gender
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="#57BC90",
               font=("bold", 15), variable=var, value=1).place(x=330, y=300)
tk.Radiobutton(window, text="Female", padx=20, width=5, bg="#57BC90", font=(
    "bold", 15), variable=var, value=2).place(x=330, y=350)


l8 = tk.Label(window, text="Age :", width=12, font=(
    "Times new roman", 15, "bold"), bg="#77C9D4")
l8.place(x=130, y=400)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=330, y=400)

l4 = tk.Label(window, text="User Name :", width=12, font=(
    "Times new roman", 15, "bold"), bg="#77C9D4")
l4.place(x=130, y=450)
t3 = tk.Entry(window, textvar=username, width=20, font=('', 15))
t3.place(x=330, y=450)

l9 = tk.Label(window, text="Password :", width=12, font=(
    "Times new roman", 15, "bold"), bg="#77C9D4")
l9.place(x=130, y=500)
t9 = tk.Entry(window, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=330, y=500)

l10 = tk.Label(window, text="Confirm Password:", width=13,
               font=("Times new roman", 15, "bold"), bg="#77C9D4")
l10.place(x=130, y=550)
t10 = tk.Entry(window, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=330, y=550)

btn = tk.Button(window, text="Register", bg="dark green",
                fg="white", width=15, height=2, command=insert)
btn.place(x=250, y=600)
#tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
#tologin.place(x=330, y=600)
window.mainloop()
