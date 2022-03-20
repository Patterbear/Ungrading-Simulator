from tkinter import *

root = Tk()
root.geometry('1920x1080')
root.title('Activities')

#identify current selected page
global page_number

# Canvas for buttons on the left
ButtonCanvas = Canvas(root, width=50, height=50)
ButtonCanvas.grid(row=0, column=0, padx=0)

# Text in the question field (Used for saving answer)
default_text_page1_q1 = ""
default_text_page1_q2 = ""

default_text_page2_q1 = ""
default_text_page2_q2 = ""

default_text_page3_q1 = ""
default_text_page3_q2 = ""

default_text_page4_q1 = ""
default_text_page4_q2 = ""

default_text_page5_q1 = ""
default_text_page5_q2 = ""


# Main content hiding/displaying of each page depending on which activity button is selected
def t1():
    Content_T1.grid(row=0, column=1, padx=40, pady=0)
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid_forget()
    Content_welcome.grid_forget()
    Content_T1.create_text(500,20, text="Topic 1 - Activity", font=('DIN Condensed','25','bold'))


# Questions AND Answers for Page 1

    question1 = "what is 1+1? "
    question1_answer = "2"

    question2 = "what is 2+2? "
    question2_answer = "4"

    # Question number
    Content_T1.create_text(60,105, text="Question 1 ", font=('DIN Condensed', '25', 'bold'))
    Content_T1.create_text(60, 305, text="Question 2 ", font=('DIN Condensed', '25', 'bold'))

    # Questions
    Content_T1.create_text(55, 130, text=question1)
    t1a = Entry(Content_T1, width=30)
    global default_text_page1_q1
    t1a.insert(END, default_text_page1_q1)
    t1a.place(x=10, y=140)

    Content_T1.create_text(55, 330, text=question2)
    t1b = Entry(Content_T1, width=30)
    global default_text_page1_q2
    t1b.insert(END, default_text_page1_q2)
    t1b.place(x=10, y=340)


    # implement awareness awards here
    # Checking of the answer
    def checking_Answer():

        if t1a.get() == question1_answer:
            print("Correct, Question 1a")

            global default_text_page1_q1
            default_text_page1_q1 = t1a.get()

        else:
            print("Question 1a is wrong")
            default_text_page1_q1 = t1a.get()

        if t1b.get() == question2_answer:
            print("Correct, Question 1b")
            global default_text_page1_q2
            default_text_page1_q2 = t1b.get()

        else:
            print("Question 1b is wrong")
            default_text_page1_q2 = t1b.get()

    confirm_button = Button(Content_T1, text="Confirm", command=checking_Answer)
    confirm_button.place(x=120,y=170)

    confirm_button2 = Button(Content_T1, text="Confirm", command=checking_Answer)
    confirm_button2.place(x=120, y=370)


def t2():

    global page_number
    page_number = 2

    Content_T1.grid_forget()
    Content_T2.grid(row=0, column=1, padx=40, pady=0)
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid_forget()
    Content_welcome.grid_forget()

    Content_T2.create_text(500, 20, text="This is topic 2", font=('DIN Condensed', '25', 'bold'))
    Content_T2.create_text(60, 40, text="This is topic 2")


def t3():

    global page_number
    page_number = 3

    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid(row=0, column=1, padx=40, pady=0)
    Content_T4.grid_forget()
    Content_T5.grid_forget()
    Content_welcome.grid_forget()

    Content_T3.create_text(500, 20, text="This is topic 3", font=('DIN Condensed', '25', 'bold'))
    Content_T3.create_text(60, 40, text="This is topic 3")


def t4():
    global page_number
    page_number = 4

    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid(row=0, column=1, padx=40, pady=0)
    Content_T5.grid_forget()
    Content_welcome.grid_forget()

    Content_T4.create_text(500, 20, text="This is topic 4", font=('DIN Condensed', '25', 'bold'))
    Content_T4.create_text(60, 40, text="This is topic 4")



def t5():
    global page_number
    page_number = 5

    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid(row=0, column=1, padx=40, pady=0)
    Content_welcome.grid_forget()

    Content_T5.create_text(500, 20, text="This is topic 5", font=('DIN Condensed', '25', 'bold'))
    Content_T5.create_text(60, 40, text="This is topic 5")

done_colour = '#6fa5e6'

def method_done(whichone):
    whichone.config(font=('DIN Condensed', '25', 'bold'),highlightbackground='green' )

def method_Undone(whichone):
    whichone.config(font=('DIN Condensed', '25', 'bold'), highlightbackground='#6fa5e6')

def done_button():
    global page_number

    if page_number == 1:
        y= topic1
    elif page_number == 2:
        y = topic2_button
    elif page_number == 3:
        y = topic3_button
    elif page_number == 4:
        y = topic4_button
    elif page_number == 5:
        y = topic5_button

    method_done(y)

def undone_button():
    global page_number

    if page_number == 1:
        y= topic1
    elif page_number == 2:
        y = topic2_button
    elif page_number == 3:
        y = topic3_button
    elif page_number == 4:
        y = topic4_button
    elif page_number == 5:
        y = topic5_button

    method_Undone(y)




# Buttons for activities
Space1 = Label(ButtonCanvas, text="")
Space1.grid(row=0, column=0, pady=10, padx=150)

topic1 = Button(ButtonCanvas, text="Topic 1 - Activity", width=20, height=2, highlightbackground='#6fa5e6', command=t1);
topic1.config(font=('DIN Condensed','25','bold'))
topic1.grid(row=1, column=0, pady=40, padx=35)

topic2_button = Button(ButtonCanvas, text="Topic 2 - Activity", width=20, height=2, highlightbackground='#6fa5e6', command=t2);
topic2_button.config(font=('DIN Condensed','25','bold'))
topic2_button.grid(row=2, column=0, pady=35)

topic3_button = Button(ButtonCanvas, text="Topic 3 - Activity", width=20, height=2, highlightbackground='#6fa5e6', command=t3);
topic3_button.config(font=('DIN Condensed','25','bold'))
topic3_button.grid(row=3, column=0, pady=35)

topic4_button = Button(ButtonCanvas, text="Topic 4 - Activity", width=20, height=2, highlightbackground='#6fa5e6', command=t4);
topic4_button.config(font=('DIN Condensed','25','bold'))
topic4_button.grid(row=4, column=0, pady=35)

topic5_button = Button(ButtonCanvas, text="Topic 5 - Activity", width=20, height=2, highlightbackground='#6fa5e6', command=t5);
topic5_button.config(font=('DIN Condensed','25'))
topic5_button.grid(row=5, column=0, pady=35)

# Welcome Frame,
Content_welcome = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_welcome.grid(row=0, column=1, padx=40, pady=0)
Content_welcome.create_text(500,250, text="Activities", font=('DIN Condensed','25','bold'))
Content_welcome.create_text(500, 270, text="Description")

# Canvas for every single activties
Content_T1 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T2 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T3 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T4 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T5 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')








root.mainloop()
