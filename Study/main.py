from tkinter import *

root = Tk()
root.geometry('1920x1080')
root.title('Study')

# Varibale which will be used to mark topics as done and incomplete
Whichpage = 0

# This section of the code reads txt files
des_txt = open("des.txt", 'r')
description = des_txt.read()

topic1_txt = open("topic1.txt", 'r')
topic_1 = topic1_txt.read()

topic2_txt = open("topic2.txt", 'r')
topic_2 = topic2_txt.read()

topic3_txt = open("topic3.txt", 'r')
topic_3 = topic3_txt.read()

topic4_txt = open("topic4.txt", 'r')
topic_4 = topic4_txt.read()

topic5_txt = open("topic5.txt", 'r')
topic_5 = topic5_txt.read()

# Canvas for all the topics button
ButtonCanvas = Canvas(root, width=50, height=50)
ButtonCanvas.grid(row=0, column=0, padx=0)

# Welcome canvas, this displays description
Content_welcome = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_welcome.grid(row=0, column=1, padx=40, pady=0)
Content_welcome.create_text(500,100, text="Project Management", font=('DIN Condensed','25','bold'))
Content_welcome.create_text(500, 280, text=description)

# Main canvas for each topic
Content_T1 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T2 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T3 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T4 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T5 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')

# Canvas which will hold 'Done' and 'Incomplete' button for each topic
Done = Canvas(root, width=1000, height=100, bg="white", bd=1, highlightthickness=1, highlightbackground='white')
Done.grid(row=1, column=1)

# Functions of each topic, implimented to hide and display correct content on the main screen.
def t1():

    global Whichpage
    Whichpage = 1

    Content_T1.grid(row=0, column=1, padx=40, pady=0)
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid_forget()
    Content_welcome.grid_forget()

    Content_T1.create_text(500,20, text="Topic 1 - What is a project? ", font=('DIN Condensed','25','bold'))
    Content_T1.create_text(345, 280, text=topic_1)

    done_button.grid(row=0, column=0, pady=0)
    undone_button.grid(row=0, column=1, pady=0, padx=10)

def t2():

    global Whichpage
    Whichpage = 2

    Content_T1.grid_forget()
    Content_T2.grid(row=0, column=1, padx=40, pady=0)
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid_forget()
    Content_welcome.grid_forget()

    Content_T2.create_text(500, 20, text="Topic 2 - Project life cycle", font=('DIN Condensed', '25', 'bold'))
    Content_T2.create_text(320, 280, text=topic_2)

    done_button.grid(row=0, column=0, pady=0)
    undone_button.grid(row=0, column=1, pady=0, padx=10)

def t3():

    global Whichpage
    Whichpage = 3

    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid(row=0, column=1, padx=40, pady=0)
    Content_T4.grid_forget()
    Content_T5.grid_forget()
    Content_welcome.grid_forget()

    Content_T3.create_text(500, 20, text="Topic 3 - Project Constraints", font=('DIN Condensed', '25', 'bold'))
    Content_T3.create_text(345, 280, text=topic_3)

    done_button.grid(row=0, column=0, pady=0)
    undone_button.grid(row=0, column=1, pady=0, padx=10)

def t4():
    global Whichpage
    Whichpage = 4

    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid(row=0, column=1, padx=40, pady=0)
    Content_T5.grid_forget()
    Content_welcome.grid_forget()

    Content_T4.create_text(500, 20, text="Topic 4 - Project Scheduling", font=('DIN Condensed', '25', 'bold'))
    Content_T4.create_text(345, 280, text=topic_4)

    done_button.grid(row=0, column=0, pady=0)
    undone_button.grid(row=0, column=1, pady=0, padx=10)


def t5():
    global Whichpage
    Whichpage = 5

    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid(row=0, column=1, padx=40, pady=0)
    Content_welcome.grid_forget()

    Content_T5.create_text(500, 20, text="Topic 5 - Project Resourcing/Costs", font=('DIN Condensed', '25', 'bold'))
    Content_T5.create_text(345, 280, text=topic_5)

    done_button.grid(row=0, column=0, pady=0)
    undone_button.grid(row=0, column=1, pady=0, padx=10)

# Default colour for buttons
done_colour = '#6fa5e6'

# Changes colour of topic button to be 'marked'
def method_done(whichone):
    whichone.config(font=('DIN Condensed', '25', 'bold'),highlightbackground='green' )

# changes colour to default when topic is 'unmarked'
def method_Undone(whichone):
    whichone.config(font=('DIN Condensed', '25', 'bold'), highlightbackground='#6fa5e6')

# This works out which is the CURRENT selected page the user is on, so the page can be marked as done
def done_button():
    global Whichpage

    if Whichpage == 1:
        y= topic1
    elif Whichpage == 2:
        y = topic2_button
    elif Whichpage == 3:
        y = topic3_button
    elif Whichpage == 4:
        y = topic4_button
    elif Whichpage == 5:
        y = topic5_button

    method_done(y)

# Similar to Done function, this is to mark a topic as incomplete
def undone_button():
    global Whichpage

    if Whichpage == 1:
        y= topic1
    elif Whichpage == 2:
        y = topic2_button
    elif Whichpage == 3:
        y = topic3_button
    elif Whichpage == 4:
        y = topic4_button
    elif Whichpage == 5:
        y = topic5_button

    method_Undone(y)

# Extra space to fix positioning
Space1 = Label(ButtonCanvas, text="")
Space1.grid(row=0, column=0, pady=0, padx=150)

# TOPIC buttons
topic1 = Button(ButtonCanvas, text="Topic 1", width=20, height=2, highlightbackground=done_colour, command=t1);
topic1.config(font=('DIN Condensed','25','bold'))
topic1.grid(row=1, column=0, pady=40, padx=35)

topic2_button = Button(ButtonCanvas, text="Topic 2", width=20, height=2, highlightbackground=done_colour, command=t2);
topic2_button.config(font=('DIN Condensed','25','bold'))
topic2_button.grid(row=2, column=0, pady=35)

topic3_button = Button(ButtonCanvas, text="Topic 3", width=20, height=2, highlightbackground='#6fa5e6', command=t3);
topic3_button.config(font=('DIN Condensed','25','bold'))
topic3_button.grid(row=3, column=0, pady=35)

topic4_button = Button(ButtonCanvas, text="Topic 4", width=20, height=2, highlightbackground='#6fa5e6', command=t4);
topic4_button.config(font=('DIN Condensed','25','bold'))
topic4_button.grid(row=4, column=0, pady=35)

topic5_button = Button(ButtonCanvas, text="Topic 5", width=20, height=2, highlightbackground='#6fa5e6', command=t5);
topic5_button.config(font=('DIN Condensed','25','bold'))
topic5_button.grid(row=5, column=0, pady=35)

# Done and inComplete buttons
done_button = Button(Done, text="Done", width=20, height=2, highlightbackground=done_colour, command=done_button);
done_button.config(font=('DIN Condensed','25','bold'))


undone_button = Button(Done, text="Incomplete", width=20, height=2, highlightbackground=done_colour, command=undone_button);
undone_button.config(font=('DIN Condensed','25','bold'))


root.mainloop()
