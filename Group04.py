from cgitb import text
from re import L
from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

#creating a window
root = Tk()
root.geometry('800x700')

bgimg= tk.PhotoImage(file = r"C:\Users\bilal\OneDrive\Pictures\Chelsea\pcodLqgKi.png")
label1 = Label( root, image = bgimg)
label1.place(x = 1.5, y = 3)

myFont = font.Font(family='Calibri Bold', size=25)
myFont2 = font.Font(family='Calibri Bold', size=11)

mylabel = Label(root, text = 'Help Menu', font=myFont, width=500)
mylabel.pack()



#creating a frame
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

def message():
    return messagebox.askokcancel('Ungrading Methodology', 'Ungrading works through the student completing various activties/challenges to develop their learning process. This process will then outcome your grade through providing evidence and demonstration of your learning.')

def message2():
    return messagebox.askokcancel('The Simulator', 'Welcome to the Ungrading Simulator help page. This simulator is designed to teach you how ungrading works through completing different activities in order to level up. The main purpose is to actually enjoy the learning process and you being able to define your own grade with evidence. ')

def message3():
    return messagebox.askokcancel('Achieving Grades','Students will achieve grades through providing evidence of their completed tasks. The complexity of tasks will be a strong indicator of the grade youll achieve. Generally, the more complex the tasks, the higher the grade youll achieve. ')

def message4():
    return messagebox.askokcancel('Feedback','Feedback will allow the student to improve on what they have learnt. If the feedback is acted upon correctly, the student will get a higher grade and will develop their learning further')

def message5():
    lb = Label(root, text = 'Hello ' + e.get())
    lb.pack()

#CREATING WIDGETS/BUTTONS
btn1 = Button(topframe,text='Ungrading Methodology', fg='Black', width=25, height=2, font = myFont2, borderwidth= 3, command= message )
btn1.pack(side=LEFT)
btn2 = Button(topframe,text='The Simulator', fg='Black',width=25, height=2, font = myFont2, borderwidth= 3, command= message2)
btn2.pack(side=LEFT)
btn3 = Button(topframe,text='Achieving Grades', fg='Black', width=25, height=2, font = myFont2, borderwidth= 3, command= message3)
btn3.pack(side=LEFT)
btn4 = Button(topframe,text='Feedback', fg='Black', width=25, height=2, font= myFont2, borderwidth= 3, command= message4 )
btn4.pack(side=LEFT)
btn_quit = Button(bottomframe,text='Exit', fg='Black', width=25, height=2, font= myFont2, borderwidth= 5,  command= root.quit )
btn_quit.pack(side=RIGHT)
btn5 = Button(bottomframe, text='<<', width=25, height= 2, font= myFont2, borderwidth= 5, command=message5,)
btn5.pack(side=LEFT)
btn6 = Button(bottomframe, text='>>', width=25, height= 2, font= myFont2, borderwidth= 5, command=message5,)
btn6.pack(side=LEFT)

root.mainloop()

