import tkinter
from cgitb import text
from logging import root
from textwrap import fill
from tkinter import *
from turtle import heading
from main import set_game_font

g_skill_level = 0
g_total_activities = 0


def run(skill_level, total_activities):

    global g_skill_level
    global g_total_activities

    g_skill_level = skill_level
    g_total_activities = total_activities

    gameFont = set_game_font()

    root = tkinter.Toplevel()
    root.title('Grade Calculator')
    root.geometry('400x400')
    root.configure(background='light grey')

    def calculate():
        c_level= int(label1_entry.get())
        skill = g_skill_level
        a_completed = g_total_activities
        s_grade = int(label4_entry.get())
        total = (c_level + skill + a_completed)
        g_achieved=(total+s_grade+100/10,'%')
        Label(root, text=total, font='Gamefont 18 bold').place(x=190,y=235)
        Label(root, text=g_achieved, font='Gamefont 18 bold').place(x=190,y=275)

    heading_label = Label(root, text='Self Assessment ', font='Gamefont 18 bold',bg='grey',fg='black').pack()
    label1 = Label(root, text='Confidence Level ',font='Gamefont 8 bold').place(x=15,y=30)
    label2 = Label(root, text='S K I L L  L E V E L ',font='Gamefont 8 bold').place(x=40,y=105)
    label3 = Label(root, text='C O M P L E T E D  A C T I V I T I E S ',font='Gamefont 8 bold').place(x=1.5,y=140)
    label4 = Label(root, text='S U G G E S T E D  G R A D E  ',font='Gamefont 8 bold').place(x=30,y=195)
    label5 = Label(root, text='T O T A L',font='Gamefont 8 bold').place(x=80,y=240)
    label6 = Label(root, text='G R A D E  A C H I E V E D',font='Gamefont 8 bold',).place(x=40,y=280)

    label1_entry = Entry(root,font="8",width='15',bd='2')
    label1_entry.place(x=190,y=70)

    label2_entry = Label(root, font="10", width='15', text=str(skill_level))
    label2_entry.place(x=190,y=105)

    label3_entry = Label(root, font="10", width='15', text=str(total_activities))
    label3_entry.place(x=190,y=140)

    label4_entry = Entry(root,font="10",width='15',bd='2')
    label4_entry.place(x=190,y=195)

    calculate_button = Button(root,text='Calculate ',font=(gameFont, 10),bg='white',fg='black',command=calculate).place(x=50,y=320)
    exit_button = Button(root,text='Exit ',font='Gamefont 10 bold',bg='white',fg='black', width= '15',command=exit).place(x=220,y=320)
    root.mainloop()