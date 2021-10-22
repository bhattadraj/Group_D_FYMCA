import os
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from pymsgbox import *

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="#57BC90")


def Open():
    from subprocess import call

    call(["python", "Open_Photo.py"])


wlcm = tk.Label(root, width=95, height=2, text="LUNG DISEASE DETECTION SYSTEM",
                background="black", foreground="white", font=("Times New Roman", 19, "bold"))
wlcm.place(x=0, y=0)

# co = tk.Label(root, text="---------------------------------Choose the Option Below---------------------------------",
#               width=85, height=2, background="black", foreground="white", font=("Times New Roman", 19, "bold"))
# co.place(x=0, y=150)

# co = tk.Label(root, text="Contact US:\n 020 123456", width=20, height=2,
#               background="white", foreground="black", font=("Times New Roman", 19, "bold"))
# co.place(x=5, y=550)


Disease = tk.Button(root, text="Disease Detection", command=Open, width=25, height=3,
                    background="white", foreground="black", font=("Times New Roman", 14, "bold"))
Disease.place(x=550, y=325)


root.mainloop()


# os module is needed
print("--------- Using os.listdir")
n = 0
files = os.listdir(r'D:\Project\Full Code\Full Code\CT SCAN DATA')
for fn in files:
    if fn.startswith('B'):
        n += 1
        print(fn)
print("count = {}".format(n))
