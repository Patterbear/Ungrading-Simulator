import tkinter
from cgitb import text
from distutils import command
from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import random


def run():
    #window
    main = tkinter.Toplevel()
    main.title("Ungrading Simulator")
    main.geometry('800x800')

    # font1 = font.Font(family='Calibri Bold', size=25)
    font2 = font.Font(family='Calibri Bold', size=12)
    font3 = font.Font(family="Arial Bold", size=20)

    topLabel = Label(main, text='Feedback', font=font3, width=500)
    topLabel.pack()

    value_inside = tkinter.StringVar(main)
    value_inside.set("Click to choose a task")

    OptionList = [
        "Task1",
        "Task2",
        "Task3",
        "Task4"
    ]

    variable = tk.StringVar(main)
    variable.set(OptionList[0])

    menu = tk.OptionMenu(main, value_inside, *OptionList)
    menu.config(width=25, font=('Helvetica', 12))
    menu.pack()
    menu.place(x=20,y=90)


    #TODO Need to hookup requestFeedback to database so when each day is incremented can check if feedback is due?
    def requestFeedback():
        z = random.randint(2,7)
        return messagebox.showinfo("Feedback", "Your feedback on " + value_inside.get() + " will arrive in " + str(z) + " days")


    #TODO Need to implement feedback into database from showFeedback function into Feedback table
    def showFeedback():

        p = value_inside.get()
        print(p)
        if "Click" in p:
            print("got here")
            return messagebox.showinfo("Select Task", "Please select a task")

        # def random_line(afile):
        #     line = next(afile)
        #     for num, aline in enumerate(afile, 2):
        #         if random.randrange(num):
        #             continue
        #         line = aline
        #     return line



        # random_line("Feedbacks.txt")

        lines = open('Feedbacks').read().splitlines()
        myline = random.choice(lines)
        print(myline)

        feedback_label = Label(main, text="Feedback", font=font2)
        feedback_label.place(x=40, y=160)

        feedback_box = Text(main, height=10, width=80)
        feedback_box.place(x=40, y=180)
        feedback_box.insert(tk.END, myline)
        feedback_box.configure(state=DISABLED)

        notes_label = Label(main, text="User notes", font=font2)
        notes_label.place(x=40, y=400)

        notes_box = Text(main, height=10, width=80)
        notes_box.place(x=40, y=420)

        #TODO Add notes feature for students per task? and table for notes in database :)
        request_btn = Button(main, text='Save notes', fg='Black', width=9, height=1, font=font2, borderwidth=1)
        request_btn.place(x=40, y=650)


    request_btn = Button(main, text='Request Feedback', fg='Black', width=15, height=1, font=font2, borderwidth=1, command=requestFeedback)
    request_btn.place(x=400, y=90)

    view_btn = Button(main, text='View Feedback', fg='Black', width=15, height=1, font=font2, borderwidth=1, command=showFeedback)
    view_btn.place(x=600, y=90)

    mainloop()

