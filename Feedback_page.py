import tkinter
from cgitb import text
from distutils import command
from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import random
import sqlite3


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

    with sqlite3.connect("assets/databases/SaveSlots.db") as db:
        c = db.cursor()
    c.execute("SELECT name, topic FROM Activity;")
    OptionList=c.fetchall()
    variable = tk.StringVar(main)
    variable.set(OptionList[0])

    menu = tk.OptionMenu(main, value_inside, *OptionList)
    menu.config(width=25, font=('Helvetica', 12))
    menu.pack()
    menu.place(x=20,y=90)


    #TODO Need to hookup requestFeedback to database so when each day is incremented can check if feedback is due?
    def requestFeedback():
        return messagebox.showinfo("Feedback", "Your feedback on " + value_inside.get() + " will arrive soon")


    #TODO Need to implement feedback into database from showFeedback function into Feedback table
    def showFeedback():

        p = value_inside.get()
        if "Click" in p:
            print("got here")
            return messagebox.showinfo("Select Task", "Please select a task")
        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute("SELECT feedback FROM Feedback, Activity WHERE Activity.id=? AND Activity.feedbackid=Feedback.id;", p)
        myline=c.fetchall()
        myline=str(myline)
        if len(myline)==0:
            c.execute("SELECT message FROM Feedback;")
            db.commit()
            result=c.fetchall()
            myline = random.choice(result)
            c.execute("SELECT id FROM Feedback WHERE message=?;", myline)
            db.commit()
            feedback_id=c.fetchall()
            c.execute("INSERT INTO Activity (feedbackid) VALUES(?) WHERE id=?;",feedback_id, p)
            db.commit()
            myline=str(myline)
        feedback_label = Label(main, text="Feedback", font=font2)
        feedback_label.place(x=40, y=160)

        feedback_box = Text(main, height=10, width=80)
        feedback_box.place(x=40, y=180)
        feedback_box.insert(tk.END, myline[2:len(myline)-3])
        feedback_box.configure(state=DISABLED)

        #TODO Add notes feature for students per task? and table for notes in database :)
        request_btn = Button(main, text='Exit', fg='Black', width=9, height=1, font=font2, borderwidth=1, command=close)
        request_btn.place(x=40, y=650)

    def close():
        db.close()
        main.destroy()



    request_btn = Button(main, text='Request Feedback', fg='Black', width=15, height=1, font=font2, borderwidth=1, command=requestFeedback)
    request_btn.place(x=400, y=90)

    view_btn = Button(main, text='View Feedback', fg='Black', width=15, height=1, font=font2, borderwidth=1, command=showFeedback)
    view_btn.place(x=600, y=90)

    mainloop()

