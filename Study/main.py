from tkinter import *

root = Tk()
root.geometry('1920x1080')
root.title('Study')


ButtonCanvas = Canvas(root, width=50, height=50)
ButtonCanvas.grid(row=0, column=0, padx=0)


Content_T1 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T2 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T3 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T4 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')
Content_T5 = Canvas(root, width=1000, height=550, bg="white", bd=1, highlightthickness=1, highlightbackground='black')



def t1():
    Content_T1.grid(row=0, column=1, padx=40, pady=0)
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid_forget()

    Content_T1.create_text(500,20, text="This is topic 1", font=('DIN Condensed','25','bold'))
    Content_T1.create_text(60, 40, text="This is topic 1")

def t2():
    Content_T1.grid_forget()
    Content_T2.grid(row=0, column=1, padx=40, pady=0)
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid_forget()

    Content_T2.create_text(500, 20, text="This is topic 2", font=('DIN Condensed', '25', 'bold'))
    Content_T2.create_text(60, 40, text="This is topic 2")


def t3():
    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid(row=0, column=1, padx=40, pady=0)
    Content_T4.grid_forget()
    Content_T5.grid_forget()

    Content_T3.create_text(500, 20, text="This is topic 3", font=('DIN Condensed', '25', 'bold'))
    Content_T3.create_text(60, 40, text="This is topic 3")


def t4():
    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid(row=0, column=1, padx=40, pady=0)
    Content_T5.grid_forget()

    Content_T4.create_text(500, 20, text="This is topic 4", font=('DIN Condensed', '25', 'bold'))
    Content_T4.create_text(60, 40, text="This is topic 4")



def t5():
    Content_T1.grid_forget()
    Content_T2.grid_forget()
    Content_T3.grid_forget()
    Content_T4.grid_forget()
    Content_T5.grid(row=0, column=1, padx=40, pady=0)

    Content_T5.create_text(500, 20, text="This is topic 5", font=('DIN Condensed', '25', 'bold'))
    Content_T5.create_text(60, 40, text="This is topic 5")


Space1 = Label(ButtonCanvas, text="")
Space1.grid(row=0, column=0, pady=0, padx=150)

topic1 = Button(ButtonCanvas, text="Topic 1", width=20, height=2, highlightbackground='#ffffff', command=t1);
topic1.config(font=('DIN Condensed','25','bold'))
topic1.grid(row=1, column=0, pady=40, padx=35)

topic2_button = Button(ButtonCanvas, text="Topic 2", width=20, height=2, highlightbackground='#ffffff', command=t2);
topic2_button.config(font=('DIN Condensed','25','bold'))
topic2_button.grid(row=2, column=0, pady=35)

topic3_button = Button(ButtonCanvas, text="Topic 3", width=20, height=2, highlightbackground='#ffffff', command=t3);
topic3_button.config(font=('DIN Condensed','25','bold'))
topic3_button.grid(row=3, column=0, pady=35)

topic4_button = Button(ButtonCanvas, text="Topic 4", width=20, height=2, highlightbackground='#ffffff', command=t4);
topic4_button.config(font=('DIN Condensed','25','bold'))
topic4_button.grid(row=4, column=0, pady=35)

topic5_button = Button(ButtonCanvas, text="Topic 5", width=20, height=2, highlightbackground='#ffffff', command=t5);
topic5_button.config(font=('DIN Condensed','25','bold'))
topic5_button.grid(row=5, column=0, pady=35)

root.mainloop()