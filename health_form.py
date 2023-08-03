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


screen.mainloop()
