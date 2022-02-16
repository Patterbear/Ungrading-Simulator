from cgitb import text
from logging import root
from textwrap import fill
from tkinter import *
from turtle import heading

root = Tk()
root.title('S E L F A S S E S S M E N T')
root.geometry('400x400')
root.configure(background='light grey')

def calculate():
    c_level= int(label1_entry.get())
    skill_level= int(label2_entry.get())
    a_completed= int(label3_entry.get())
    s_grade= int(label4_entry.get())
    total = (c_level + skill_level + a_completed)
    g_achieved=(total+s_grade+100/10,'%')
    Label(root, text=total, font='Gamefont 18 bold').place(x=190,y=235)
    Label(root, text=g_achieved, font='Gamefont 18 bold').place(x=190,y=275)

heading_label = Label(root, text='S E L F  A S S E S S M E N T ', font='Gamefont 18 bold',bg='grey',fg='black').pack()
label1 = Label(root, text='S T U D E N T  N A M E ',font='Gamefont 8 bold').place(x=50,y=70)
label2 = Label(root, text='S K I L L  L E V E L ',font='Gamefont 8 bold').place(x=60,y=105)
label3 = Label(root, text='E V I D E N C E ',font='Gamefont 8 bold').place(x=70,y=145)
label4 = Label(root, text='S U G G E S T E D  G R A D E  ',font='Gamefont 8 bold').place(x=30,y=195)
label5 = Label(root, text='T O T A L',font='Gamefont 8 bold').place(x=80,y=240)
label6 = Label(root, text='G R A D E  A C H I E V E D',font='Gamefont 8 bold',).place(x=40,y=280)

label1_entry = Entry(root,font="8",width='15',bd='2')
label1_entry.place(x=190,y=70)

label2_entry = Entry(root,font="10",width='15',bd='2')
label2_entry.place(x=190,y=105)

label3_entry = Entry(root,font="10",width='15',bd='2')
label3_entry.place(x=190,y=140)

label4_entry = Entry(root,font="10",width='15',bd='2')
label4_entry.place(x=190,y=195)

#label5_entry = Entry(root,font="10",width='15',bd='2')
#label5_entry.place(x=190,y=240)

calculate_button = Button(root,text='C A L C U L A T E ',font='Gamefont 10 bold',bg='white',fg='black',command=calculate).place(x=50,y=320)
exit_button = Button(root,text='E X I T ',font='Gamefont 10 bold',bg='white',fg='black', width= '15',command=exit).place(x=220,y=320)
mainloop()