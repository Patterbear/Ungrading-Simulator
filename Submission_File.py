from cgitb import text
from distutils import command
from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from turtle import width

# creating a window
main = Tk()
main.title("Ungrading Simulator")
#main.iconbitmap("Images/app_icon.png")
main.geometry('800x800')

font1 = font.Font(family='Calibri Bold', size=25)
font2 = font.Font(family='Calibri Bold', size=14)
font3 = font.Font(family="Arial Bold", size=20)

mylabel = Label(main, text='File Submission Page/Request Feedback', font=font1, width=500)
mylabel.pack()

# creating a frame
tframe = Frame(main)
tframe.pack()
bframe = Frame(main)
bframe.pack(side=BOTTOM)


# Commands
# Print
def sub_message():
    return messagebox.askokcancel("Thanks for submitting Activity 1", "You have shown good understanding in Activity 1. Therefore, you are awarded 73% in Activity 1")



# def take_input1():
#     inputValue = name_input.get("1.0",END)
#     print(inputValue)


# CREATING WIDGETS/BUTTONS
submit_btn = Button(bframe, text='Submit', fg='Black', width=20, height=1, font=font2, borderwidth=2,
                    command=sub_message)
submit_btn.pack(side=RIGHT)
cancel_btn = Button(bframe, text='Close', fg='Black', width=20, height=1, font=font2, borderwidth=2, command=main.quit)
cancel_btn.pack(side=RIGHT)
main_btn= Button (bframe, text= "Main Menu", fg="Black", width=20, height=1, font= font2, borderwidth=2, command= main.quit)
main_btn.pack(side=RIGHT)
# Name Labels
name_label = Label(main, text="Full Name", font=font2)
name_label.place(x=40, y=60)

name_input = Entry(main, width=40)
name_input.place(x=140, y=65)

# Upload Label
upload_label = Label(main, text="Upload", font=font3)
upload_label.place(x=40, y=120)


# Dropdown Menu
def show():
    mylabel1 = Label(main, text=opt.get())
    mylabel1.place(x=180, y=185)


options = ["Activity 1",
           "Activity 2",
           "Activity 3",
           "Activity 4",
           "Activity 5"]

opt = StringVar()
opt.set("No file chosen")

drop = OptionMenu(main, opt, *options)
drop.pack()
drop.place(x=40, y=180)

# Choose file btn
file_btn = Button(main, text='Choose File', fg='Black', width=11, height=1, font=font2, borderwidth=1, command=show)
file_btn.place(x=40, y=220)

# Write Submission
comment_label = Label(main, text="Comments", font=font2)
comment_label.place(x=40, y=300)


def take_input():
    inputValue = comment_box.get("1.0", "end-1c")
    print(inputValue)


comment_box = Text(main, height=10, width=80)
comment_box.place(x=40, y=340)

click_btn = Button(main, height=1, width=10, text="Click", command=lambda: take_input())
click_btn.pack()
click_btn.place(x=40, y=520)



mainloop()
