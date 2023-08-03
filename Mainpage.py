import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import sqlite3

root =tk.Tk()
root.geometry('500x600')
root.title('Contact Tracing App')

def create_database():
    if not os.path.exists("accounts_data.db"):
        connection = sqlite3.connect("accounts_data.db")

        cursor = connection.cursor()
        cursor.execute("""
             
        CREATE TABLE accounts(
                       
        username text,
        password text,
        mobile text,
        email text                

        )
        
        """)

        connection.commit()
        connection.close()

def register_account(username, password, mobile, email):
    try: 
        connection = sqlite3.connect("accounts_data.db")

        cursor = connection.cursor()
        cursor.execute(f"""

        INSERT INTO accounts VALUES('{username}', '{password}', '{mobile}', '{email}')
            
        """)

        connection.commit()

        cursor.execute("""
        SELECT * FROM accounts
        """)

        connection.commit()
        print(cursor.fetchall())

        connection.close()
        return True
    
    except Exception as error:
        return False
    
def check_existence1(username):
    connection = sqlite3.connect("accounts_data.db")

    cursor = connection.cursor()
    cursor.execute(f"""

    SELECT username FROM accounts WHERE username == "{username}"

    """)

    connection.commit()

    response = cursor.fetchall()
    print(response)
    return response


    connection.close()

def check_existence2(username,password):
    connection = sqlite3.connect("accounts_data.db")

    cursor = connection.cursor()
    cursor.execute(f"""

    SELECT username FROM accounts WHERE username == "{username}" AND  password == "{password}"

    """)

    connection.commit()

    response = cursor.fetchall()
    print(response)
    return response


    connection.close()

def message_box(msg):
    message_frame = tk.Frame(root, relief=tk.SOLID,
                             highlightthickness=2, highlightbackground="gray")
    close_btn = tk.Button(message_frame, text="X", font=("bold", 12),
                          bd= 0, command=lambda: message_frame.destroy())
    close_btn.pack(side=tk.TOP, anchor=tk.E)

    message_lb = tk.Label(message_frame, text=msg, font=("bold",15))
    message_lb.pack(pady=20)
    message_frame.place(x=120, y=80, width=300, height=350)

def dashboard(username):
    
    def logout():
        dashboard_frame.destroy()
        login_page()

        root = tk.Tk()
        root.geometry("500x400")
        root.title("Contract Tracing App") 

        def home_page():
            home_frame = tk.Frame(main_frame)

            home_menu = tk.Label(home_frame, text="\n\nWelcome to your \n\nContract Tracing App\n\n", font=("bold",30))
            home_menu.pack()

            home_frame.pack(pady=20)
            
        def health_page():        
            def submit():
                import health_form

            health_frame = tk.Frame(main_frame)

            health_form = tk.Label(health_frame, text="\n\nFill Out\n\nYour Form", font=("bold",30))
            health_form.pack()

            form_btn = tk.Button(main_frame,text="Health Form",
                             font=("bold", 12), bg="#158aff",
                             bd=0, underline=True, command=submit)
            form_btn.place(x=140, y=300)

            health_frame.pack(pady=20)

        def contact_page():
            contact_frame = tk.Frame(main_frame)

            contact_details1 = tk.Label(contact_frame,text="\nEmergency Hotline\t\t911\nPNP\t\t117\nRegion 1\t\t0998-583-5732\nRegion 2\t\t0917-504-7971\nRegion3\t\t(045) 598-8580 \nCALABARZON\t\t0977-827-6112\nMIMAROPA\t\t(02) 8637-2895")
            contact_details2 = tk.Label(contact_frame,text="\nRegion 5\t\t0999-682-4775\nRegion 6\t\t(033) 336-3156\nRegion 7\t\t(032) 414-7399\nRegion 8\t\t(053) 323-3156\nRegion 9\t\t0998-280-8852 \nRegion 10\t\t0917-713-0173\nRegion 11\t\t0917-720-1674")
            contact_details3 = tk.Label(contact_frame,text="\nRegion 12\t\t(083) 228-1893\nBARMM\t\t(064) 421-4272\nCAR\t\t0917-514-9700\nCARAGA\t\t0945-237-8066\nNCR\t\t0999-881-1535")

            contact_details1.pack()
            contact_details2.pack()
            contact_details3.pack()
            

            contact_frame.pack(pady=20)

        def hide_indicators():
            home_lbl.config(bg="#c3c3c3")
            health_lbl.config(bg="#c3c3c3")
            contact_lbl.config(bg="#c3c3c3")
            covid_lbl.config(bg="#c3c3c3")

        def delete_pages():
            for frame in main_frame.winfo_children():
                frame.destroy()

        def indicate(lb, page):
            hide_indicators()
            lb.config(bg="#158aff")
            delete_pages()
            page()


            
        main_frame = tk.Frame(root, highlightbackground='blue',
                                highlightthickness=2)
        
        option_frame = tk.Frame(root, bg="#c3c3c3")
        home_btn = tk.Button(option_frame, text="Home", font=("bold", 15), fg="#158aff", bd=0, bg="#c3c3c3",
                             command=lambda: indicate(home_lbl, home_page))
        home_btn.place(x=10, y=50)
        home_lbl = tk.Label(option_frame, text="", bg="#c3c3c3")
        home_lbl.place(x=3, y=50, width=5, height=40)

        health_btn = tk.Button(option_frame, text="Health", font=("bold", 15), fg="#158aff", bd=0, bg="#c3c3c3",
                               command=lambda: indicate(health_lbl, health_page))
        health_btn.place(x=10, y=125)
        health_lbl = tk.Label(option_frame, text="", bg="#c3c3c3")
        health_lbl.place(x=3, y=125, width=5, height=40)

        contact_btn = tk.Button(option_frame, text="Contacts", font=("bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", 
                                command=lambda: indicate(contact_lbl, contact_page))
        contact_btn.place(x=10, y=200)
        contact_lbl = tk.Label(option_frame, text="", bg="#c3c3c3")
        contact_lbl.place(x=3, y=200, width=5, height=40)

        covid_btn = tk.Button(option_frame, text="COVID-19", font=("bold", 15), fg="#158aff", bd=0, bg="#c3c3c3")
        covid_btn.place(x=10, y=275)
        covid_lbl = tk.Label(option_frame, text="", bg="#c3c3c3")
        covid_lbl.place(x=3, y=275, width=5, height=40)


        option_frame.pack(side=tk.LEFT)
        option_frame.pack_propagate(False)
        option_frame.configure(width=125, height=600)
        

        main_frame.pack(side=tk.LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(width=400, height=400)       
    
    dashboard_frame = tk.Frame(root)

    welcome_lb = tk.Label(dashboard_frame, text=f'{username}\n Welcome to the App!',
                     font =("bold", 20))
    welcome_lb.pack(pady=10)

    home_btn= tk.Button(dashboard_frame,
                          text="HOME", bg="gray", fg="white",
                          font=("bold",15), width=20)
    home_btn.pack(side=tk.BOTTOM, pady=10)

    logout_btn= tk.Button(dashboard_frame,
                          text="Logout", bg="blue", fg="white",
                          font=("bold",15), width=20, command=logout)
    logout_btn.pack(side=tk.BOTTOM, pady=10)

    dashboard_frame.pack()
    dashboard_frame.pack_propagate(False)
    dashboard_frame.configure(height=400, width=300)


def login_page():

    def fwregister_page():
        login_frame.destroy()
        register_page()

    def verification2():
        if username.get() != "":
            if password.get() !="":

                if check_existence1(username.get()):
                    if check_existence2(username=username.get(),
                                       password=password.get()):
                        name = username.get()
                        login_frame.destroy()
                        dashboard(username=name)
                     
                    else:
                        message_box(msg="\n\n\n\nINCORRECT \n\n USERNAME/PASSWORD")

                else:
                    message_box(msg="\n\n\n\nINCORRECT \n\nUSERNAME/PASSWORD")

            else:
                message_box(msg="\n\n\nPassword is Required")
        else:
            message_box(msg="\n\n\nUsername is Required")                       
    

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
                        bg="#158aff", fg="white", command=verification2)
    login_btn.place(x=50, y=220, width=150)

    register_btn = tk.Button(login_frame, text="Register",
                             font=("bold", 12), bg="#158aff",
                             bd=0, underline=True, command=fwregister_page)
    register_btn.place(x=90, y=260 )


    login_frame.pack(pady=10)
    login_frame.pack_propagate(False)

    login_frame.configure(height=400, width=250)

def register_page():

    def fwrlogin_page():
        register_frame.destroy()
        login_page()
    def verification1():
        if username.get() != '':
            if password.get() != '':
                if mobile.get() != '':
                    if email.get() != '':
                        if not check_existence1(username.get()):

                            response = register_account(username=username.get(), 
                                                        password=password.get(),
                                                        mobile=mobile.get(), 
                                                        email=email.get())
                            if response:
                                username.delete(0, tk.END)
                                password.delete(0, tk.END)
                                mobile.delete(0, tk.END)
                                email.delete(0, tk.END) 
                                message_box("\n\n\n\nCreated Successfully")
                                
            else:
                message_box(msg="Password is required") 
        else:
            message_box(msg="Username is required")    

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
                             bd=0, underline=True, command=verification1)
    register_btn.place(x=50, y=405, width=150 )

    login_btn = tk.Button(register_frame, text="Login", fg="#158aff",
                           underline=True, font=("bold", 12), bd=0, command=fwrlogin_page)
    login_btn.place(x=100, y=440)


    register_frame.pack()
    register_frame.pack_propagate(False)
    register_frame.configure(height=600, width=250)
create_database()
login_page()
message_box()
check_existence1("root")
root.mainloop()