from tkinter import *


def run():

    root = Toplevel()
    root.geometry('1920x1080')
    root.title('Activities')

    #identify current selected page
    global page_number

    # Canvas for buttons on the left
    ButtonCanvas = Canvas(root, width=50, height=50)
    ButtonCanvas.grid(row=0, column=0, padx=0)

    # Text in the question field (Used for saving answer)
    global default_text_page1_q1
    global default_text_page1_q2
    global default_text_page2_q1
    global default_text_page2_q2
    global default_text_page3_q1
    global default_text_page3_q2
    global default_text_page4_q1
    global default_text_page4_q2
    global default_text_page5_q1
    global default_text_page5_q2

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

        question1 = "Name one of the characteristic of a project"
        question1_answer = ("temporary", "unique", "delivers results", "Delivers result", "not small")

        question2 = "Is decorating a room a project? "
        question2_answer = ("yes","yh","yeah")

        # Question number
        Content_T1.create_text(55,105, text="Question 1 ", font=('DIN Condensed', '25', 'bold'))
        Content_T1.create_text(55, 305, text="Question 2 ", font=('DIN Condensed', '25', 'bold'))

        # Questions
        Content_T1.create_text(142, 130, text=question1)
        t1a = Entry(Content_T1, width=30)
        global default_text_page1_q1
        t1a.insert(END, default_text_page1_q1)
        t1a.place(x=10, y=140)

        Content_T1.create_text(110, 330, text=question2)
        t1b = Entry(Content_T1, width=30)
        global default_text_page1_q2
        t1b.insert(END, default_text_page1_q2)
        t1b.place(x=10, y=340)

        # implement awareness awards here

        # Checking of the answer
        def checking_Answer():

            if t1a.get().lower() in question1_answer:
                print("Correct, Question 1a")

                global default_text_page1_q1
                default_text_page1_q1 = t1a.get()

            else:
                print("Question 1a is wrong")
                default_text_page1_q1 = t1a.get()

            if t1b.get().lower() in question2_answer:
                print("Correct, Question 1b")
                global default_text_page1_q2
                default_text_page1_q2 = t1b.get()

            else:
                print("Question 1b is wrong OR empty")
                default_text_page1_q2 = t1b.get()

        confirm_button = Button(Content_T1, text="Confirm", command=checking_Answer)
        confirm_button.place(x=120,y=170)

        confirm_button2 = Button(Content_T1, text="Confirm", command=checking_Answer)
        confirm_button2.place(x=120, y=370)


    def t2():

        Content_T1.grid_forget()
        Content_T2.grid(row=0, column=1, padx=40, pady=0)
        Content_T3.grid_forget()
        Content_T4.grid_forget()
        Content_T5.grid_forget()
        Content_welcome.grid_forget()
        Content_T2.create_text(500, 20, text="Topic 2 - Activity", font=('DIN Condensed', '25', 'bold'))

        # Questions AND Answers for Page 1

        question1 = "How many phases are they in a project? "
        question1_answer = ("4", "four")

        question2 = "Name the final phase of a project "
        question2_answer = ("closing", "closure")

        # Question number
        Content_T2.create_text(55, 105, text="Question 1 ", font=('DIN Condensed', '25', 'bold'))
        Content_T2.create_text(55, 305, text="Question 2 ", font=('DIN Condensed', '25', 'bold'))

        # Questions
        Content_T2.create_text(135, 130, text=question1)
        t2a = Entry(Content_T2, width=30)
        global default_text_page2_q1
        t2a.insert(END, default_text_page2_q1)
        t2a.place(x=10, y=140)

        Content_T2.create_text(115, 330, text=question2)
        t2b = Entry(Content_T2, width=30)
        global default_text_page2_q2
        t2b.insert(END, default_text_page2_q2)
        t2b.place(x=10, y=340)

        # implement awareness awards here

        # Checking of the answer
        def checking_Answer():

            if t2a.get().lower() in question1_answer:
                print("Correct, Question 1a")

                global default_text_page2_q1
                default_text_page2_q1 = t2a.get()

            else:
                print("Question 1a is wrong")
                default_text_page2_q1 = t2a.get()

            if t2b.get().lower() in question2_answer:
                print("Correct, Question 1b")
                global default_text_page2_q2
                default_text_page2_q2 = t2b.get()

            else:
                print("Question 1b is wrong OR empty")
                default_text_page2_q2 = t2b.get()

        confirm_button = Button(Content_T2, text="Confirm", command=checking_Answer)
        confirm_button.place(x=120, y=170)

        confirm_button2 = Button(Content_T2, text="Confirm", command=checking_Answer)
        confirm_button2.place(x=120, y=370)


    def t3():

        Content_T1.grid_forget()
        Content_T2.grid_forget()
        Content_T3.grid(row=0, column=1, padx=40, pady=0)
        Content_T4.grid_forget()
        Content_T5.grid_forget()
        Content_welcome.grid_forget()
        Content_T3.create_text(500, 20, text="Topic 3 - Activity", font=('DIN Condensed', '25', 'bold'))

        # Questions AND Answers for Page 1

        question1 = "Name the constraint - what the project is trying to achieve "
        question1_answer = "scope"

        question2 = "Which is the most important constraint? "
        question2_answer = ("all", "all 4", "all of them")

        # Question number
        Content_T3.create_text(55, 105, text="Question 1 ", font=('DIN Condensed', '25', 'bold'))
        Content_T3.create_text(55, 305, text="Question 2 ", font=('DIN Condensed', '25', 'bold'))

        # Questions
        Content_T3.create_text(190, 130, text=question1)
        t3a = Entry(Content_T3, width=30)
        global default_text_page3_q1
        t3a.insert(END, default_text_page3_q1)
        t3a.place(x=10, y=140)

        Content_T3.create_text(135, 330, text=question2)
        t3b = Entry(Content_T3, width=30)
        global default_text_page3_q2
        t3b.insert(END, default_text_page3_q2)
        t3b.place(x=10, y=340)

        # implement awareness awards here

        # Checking of the answer
        def checking_Answer():

            if t3a.get().lower() == question1_answer:
                print("Correct, Question 1a")

                global default_text_page3_q1
                default_text_page3_q1 = t3a.get()

            else:
                print("Question 1a is wrong")
                default_text_page3_q1 = t3a.get()

            if t3b.get().lower() in question2_answer:
                print("Correct, Question 1b")
                global default_text_page3_q2
                default_text_page3_q2 = t3b.get()

            else:
                print("Question 1b is wrong OR empty")
                default_text_page3_q2 = t3b.get()

        confirm_button = Button(Content_T3, text="Confirm", command=checking_Answer)
        confirm_button.place(x=120, y=170)

        confirm_button2 = Button(Content_T3, text="Confirm", command=checking_Answer)
        confirm_button2.place(x=120, y=370)


    def t4():

        Content_T1.grid_forget()
        Content_T2.grid_forget()
        Content_T3.grid_forget()
        Content_T4.grid(row=0, column=1, padx=40, pady=0)
        Content_T5.grid_forget()
        Content_welcome.grid_forget()
        Content_T4.create_text(500, 20, text="Topic 4 - Activity", font=('DIN Condensed', '25', 'bold'))

        # Questions AND Answers for Page 1

        question1 = "What does WBS stands for? "
        question1_answer = "work breakdown structure"

        question2 = "Name one type of dependencies"
        question2_answer = ("fs","finish to start", "ss", "start to start", "ff", "finish to finish", "sf", "start to finish")

        # Question number
        Content_T4.create_text(55, 105, text="Question 1 ", font=('DIN Condensed', '25', 'bold'))
        Content_T4.create_text(55, 305, text="Question 2 ", font=('DIN Condensed', '25', 'bold'))

        # Questions
        Content_T4.create_text(98, 130, text=question1)
        t4a = Entry(Content_T4, width=30)
        global default_text_page4_q1
        t4a.insert(END, default_text_page4_q1)
        t4a.place(x=10, y=140)

        Content_T4.create_text(110, 330, text=question2)
        t4b = Entry(Content_T4, width=30)
        global default_text_page4_q2
        t4b.insert(END, default_text_page4_q2)
        t4b.place(x=10, y=340)

        # implement awareness awards here

        # Checking of the answer
        def checking_Answer():

            if t4a.get().lower() == question1_answer:
                print("Correct, Question 1a")

                global default_text_page4_q1
                default_text_page4_q1 = t4a.get()

            else:
                print("Question 1a is wrong")
                default_text_page4_q1 = t4a.get()

            if t4b.get().lower() in question2_answer:
                print("Correct, Question 1b")
                global default_text_page4_q2
                default_text_page4_q2 = t4b.get()

            else:
                print("Question 1b is wrong OR empty")
                default_text_page4_q2 = t4b.get()

        confirm_button = Button(Content_T4, text="Confirm", command=checking_Answer)
        confirm_button.place(x=120, y=170)

        confirm_button2 = Button(Content_T4, text="Confirm", command=checking_Answer)
        confirm_button2.place(x=120, y=370)



    def t5():

        Content_T1.grid_forget()
        Content_T2.grid_forget()
        Content_T3.grid_forget()
        Content_T4.grid_forget()
        Content_T5.grid(row=0, column=1, padx=40, pady=0)
        Content_welcome.grid_forget()
        Content_T5.create_text(500, 20, text="Topic 5 - Activity", font=('DIN Condensed', '25', 'bold'))

        # Questions AND Answers for Page 1

        question1 = "Name the method used to fix over-utilisation "
        question1_answer = ("re-scheduling","rescheduling","moving","delaying","moving and delaying","delaying and moving")

        question2 = "What are the two types of project costs? "
        question2_answer = ("direct and indirect", "indirect and direct")

        # Question number
        Content_T5.create_text(55, 105, text="Question 1 ", font=('DIN Condensed', '25', 'bold'))
        Content_T5.create_text(55, 305, text="Question 2 ", font=('DIN Condensed', '25', 'bold'))

        # Questions
        Content_T5.create_text(150, 130, text=question1)
        t5a = Entry(Content_T5, width=30)
        global default_text_page5_q1
        t5a.insert(END, default_text_page5_q1)
        t5a.place(x=10, y=140)

        Content_T5.create_text(138, 330, text=question2)
        t5b = Entry(Content_T5, width=30)
        global default_text_page5_q2
        t5b.insert(END, default_text_page5_q2)
        t5b.place(x=10, y=340)

        # implement awareness awards here

        # Checking of the answer
        def checking_Answer():

            if t5a.get().lower() in question1_answer:
                print("Correct, Question 1a")

                global default_text_page5_q1
                default_text_page5_q1 = t5a.get()

            else:
                print("Question 1a is wrong")
                default_text_page5_q1 = t5a.get()

            if t5b.get().lower() in question2_answer:
                print("Correct, Question 1b")
                global default_text_page5_q2
                default_text_page5_q2 = t5b.get()

            else:
                print("Question 1b is wrong OR empty")
                default_text_page5_q2 = t5b.get()

        confirm_button = Button(Content_T5, text="Confirm", command=checking_Answer)
        confirm_button.place(x=120, y=170)

        confirm_button2 = Button(Content_T5, text="Confirm", command=checking_Answer)
        confirm_button2.place(x=120, y=370)

    # Buttons for activities
    done_colour = '#6fa5e6'

    Space1 = Label(ButtonCanvas, text="")
    Space1.grid(row=0, column=0, pady=10, padx=150)

    topic1 = Button(ButtonCanvas, text="Topic 1 - Activity", width=20, height=2, highlightbackground='#6fa5e6', command=t1);
    topic1.config(font=('DIN Condensed','25','bold'))
    topic1.grid(row=1, column=0, pady=40, padx=35)

    topic2_button = Button(ButtonCanvas, text="Topic 2 - Activity", width=20, height=2, highlightbackground='#6fa5e6',command=t2);
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
    Content_welcome.create_text(500, 270, text="This is the activity page, please click 'confirm' to save answer")

    # Canvas for every single activities
    Content_T1 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
    Content_T2 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
    Content_T3 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
    Content_T4 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
    Content_T5 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')

    root.mainloop()