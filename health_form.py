#Contract Tracing App Form

from tkinter import *
from tkinter import filedialog

def save_info():
    vax_info = vax.get()
    symptom_info = symptom.get()
    exposure_info = exposure.get()
    covid_info = covid.get()
    tester_info = tester.get()
    date_info = date.get()

    print(vax_info, symptom_info, exposure_info, covid_info, tester_info,date_info)

    file = open("user.txt", "w")
    file.write(vax_info)
    file.write(symptom_info)
    file.write(exposure_info)
    file.write(covid_info)
    file.write(tester_info)
    file.write(date_info)
    file.close()
    print("User has been registered successfully")

    vax_entry.delete(0, END)
    symptom_entry.delete(0, END)
    exposure_entry.delete(0,END)
    covid_entry.delete(0,END)
    tester_entry.delete(0,END)
    date_entry.delete(0, END)

screen = Tk()
screen.geometry("500x600")
screen.title("Health Decleration Form")
heading = Label(text="Personal Information", bg="grey", fg="black", width="500", height="3")
heading()

vax_type = Label(text= "Type of Vaccination: ")
pos_symptopm = Label(text= "What kind of symptom did you experience this past week: ")
covid_exposure = Label(text= "Is there a possiblity that you made contact with someone with a confirmed case?")
symptom_exposure = Label(text = "Did you have contact with someone with possible covid-19 symptom, such as loss of smell, sore throat, fever, etc?")
covid_tester = Label(text="Have you had a swab test for Covid-19 for the past weeks?")
date_today = Label(text="Today's Date:")

vax_type.place(x=15, y=100)
pos_symptopm.place(x=15, y=160)
covid_exposure.place(x=15, y=230)
symptom_exposure.place(x=15, y=310)
covid_tester.place(x=15, y=390)
date_today.place(x=15, y=480)

vax = StringVar()
symptom = StringVar()
exposure = StringVar()
covid = StringVar()
tester = StringVar()
date = StringVar()

vax_entry = Entry(textvariable= vax, width= "30")
symptom_entry = Entry(textvariable= symptom, width= "30")
exposure_entry = Entry(textvariable= exposure, width= "30")
covid_entry = Entry(textvariable= covid, width= "30")
tester_entry = Entry(textvariable= tester, width= "30")
date_entry = Entry(textvariable= date, width="30")

vax_entry.place(x=15, y=130)
symptom_entry.place(x=15, y=200)
exposure_entry.place(x=15, y=270)
covid_entry.place(x=15, y=350)
tester_entry.place(x=15, y=430)
date_entry.place(x=15, y=500)

register = Button(screen, text = "Register", width= "50", height="2")
register.place(x=15, y=550)

screen.mainloop()
