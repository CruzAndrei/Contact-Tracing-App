import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import sqlite3

root =tk.Tk()
root.geometry('500x600')
root.title('Contact Tracing App')

def login_page():
    login_frame = tk.Frame(root)

    username_lb = tk.Label(login_frame, text="Enter Username: ", font=("bold", 12))
    username_lb.place(x=60, y=20)

    username = tk.Entry(login_frame, font=("bold", 15),
                        bd=0, highlightcolor="#158aff",
                        highlightthickness=2, highlightbackground="gray")
    username.place(x=50, y=60, width=150, height=30)

    password_lb= tk.Label(login_frame, text="Enter Password: ", font=("bold",12))
    password_lb.place(x=60, y=120)

    password = tk.Entry(login_frame, font=("bold", 15),
                        bd=0, highlightcolor="#158aff",
                        highlightthickness=2, highlightbackground="gray",show ="*")
    password.place(x=50, y=160, width=150, height=30)
    
    login_btn = tk.Button(login_frame, text="Login", font=('bold',12),
                        bg="#158aff", fg="white")
    login_btn.place(x=50, y=220, width=150)

    register_btn = tk.Button(login_frame, text="Register",
                             font=("bold", 12), bg="#158aff",
                             bd=0, underline=True)
    register_btn.place(x=90, y=260 )


    login_frame.pack(pady=10)
    login_frame.pack_propagate(False)

    login_frame.configure(height=400, width=250)

def register_page():
    register_frame = tk.Frame(root)
    username_lb = tk.Label(register_frame, text="Enter Username: ", font=("bold", 12))
    username_lb.place(x=60, y=20)
    username = tk.Entry(register_frame, font=("bold", 15),
                        bd=0, highlightcolor="#158aff",
                        highlightthickness=2, highlightbackground="gray")
    username.place(x=50, y=60, width=150, height=30)

    password_lb= tk.Label(register_frame, text="Enter Password: ", font=("bold",12))
    password_lb.place(x=60, y=120)

    password = tk.Entry(register_frame, font=("bold", 15),
                        bd=0, highlightcolor="#158aff",
                        highlightthickness=2, highlightbackground="gray")
    password.place(x=50, y=160, width=150, height=30)

    mobile_number= tk.Label(register_frame, text="Mobile Number: ", font=("bold",12))
    mobile_number.place(x=60, y=220)

    mobile = tk.Entry(register_frame, font=("bold", 15),
                        bd=0, highlightcolor="#158aff",
                        highlightthickness=2, highlightbackground="gray")
    mobile.place(x=50, y=250, width=150, height=30)

    email_add= tk.Label(register_frame, text="Email Address: ", font=("bold",12))
    email_add.place(x=60, y=310)

    email = tk.Entry(register_frame, font=("bold", 15),
                        bd=0, highlightcolor="#158aff",
                        highlightthickness=2, highlightbackground="gray")
    email.place(x=50, y=340, width=150, height=30)

    register_btn = tk.Button(register_frame, text="Register",
                             font=("bold", 12), bg="#158aff",
                             bd=0, underline=True)
    register_btn.place(x=50, y=405, width=150 )


    register_frame.pack()
    register_frame.pack_propagate(False)
    register_frame.configure(height=600, width=250)

login_page()
root.mainloop()