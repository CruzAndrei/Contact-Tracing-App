#Contract Tracing App Form

from tkinter import *
from tkinter import filedialog

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

screen.mainloop()
