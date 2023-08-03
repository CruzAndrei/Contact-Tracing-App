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
    login_frame.pack(pady=10)
    login_frame.pack_propagate(False)

    login_frame.configure(height=400, width=250)


root.mainloop()