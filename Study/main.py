from tkinter import *

root = Tk()
root.geometry('1920x1080')
root.title('Study')

Whichpage = 0

text_file1 = open("des.txt", 'r')
description = text_file1.read()

ButtonCanvas = Canvas(root, width=50, height=50)
ButtonCanvas.grid(row=0, column=0, padx=0)

Content_welcome = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_welcome.grid(row=0, column=1, padx=40, pady=0)

Content_welcome.create_text(500,200, text="Welcome to Ungrading", font=('DIN Condensed','25','bold'))
Content_welcome.create_text(500, 320, text=description)

Content_T1 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T2 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T3 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T4 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T5 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')

Done = Canvas(root, width=1000, height=100, bg="white", bd=1, highlightthickness=1, highlightbackground='white')
Done.grid(row=1, column=1)

def t1():

    global Whichpage
    Whichpage = 1

    Content_T1.grid(row=0, column=1, padx=40, pady=0)
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid_forget()
    Content_welcome.grid_forget()

    Content_T1.create_text(500,20, text="This is topic 1", font=('DIN Condensed','25','bold'))
    Content_T1.create_text(60, 40, text="This is topic 1")

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

    Content_T2.create_text(500, 20, text="This is topic 2", font=('DIN Condensed', '25', 'bold'))
    Content_T2.create_text(60, 40, text="This is topic 2")

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

    Content_T3.create_text(500, 20, text="This is topic 3", font=('DIN Condensed', '25', 'bold'))
    Content_T3.create_text(60, 40, text="This is topic 3")

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

    Content_T4.create_text(500, 20, text="This is topic 4", font=('DIN Condensed', '25', 'bold'))
    Content_T4.create_text(60, 40, text="This is topic 4")

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

    Content_T5.create_text(500, 20, text="This is topic 5", font=('DIN Condensed', '25', 'bold'))
    Content_T5.create_text(60, 40, text="This is topic 5")

    done_button.grid(row=0, column=0, pady=0)
    undone_button.grid(row=0, column=1, pady=0, padx=10)

done_colour = '#6fa5e6'

def method_done(whichone):
    whichone.config(font=('DIN Condensed', '25', 'bold'),highlightbackground='green' )

def method_Undone(whichone):
    whichone.config(font=('DIN Condensed', '25', 'bold'), highlightbackground='#6fa5e6')

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

Space1 = Label(ButtonCanvas, text="")
Space1.grid(row=0, column=0, pady=0, padx=150)

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

done_button = Button(Done, text="Done", width=20, height=2, highlightbackground=done_colour, command=done_button);
done_button.config(font=('DIN Condensed','25','bold'))


undone_button = Button(Done, text="Incomplete", width=20, height=2, highlightbackground=done_colour, command=undone_button);
undone_button.config(font=('DIN Condensed','25','bold'))



root.mainloop()
