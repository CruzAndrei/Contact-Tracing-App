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


    login_frame.pack(pady=10)
    login_frame.pack_propagate(False)

    login_frame.configure(height=400, width=250)


root.mainloop()