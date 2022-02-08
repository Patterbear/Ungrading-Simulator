from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image



w=Tk()
w.geometry('900x500')
w.configure(bg='#262626')
w.resizable(0,0)
w.title('Ungrading Simulator User Guide')


l1=Label(w,text='U N G R A D I N G S I M U L A T O R ',fg='white',bg='#262626')
l1.config(font=('Helvetica',40))
l1.pack(expand=True)

def message():
            return messagebox.askokcancel('Ungrading Methodology', 'Ungrading works through the student completing various activties/challenges to develop their learning. This process will influence their grade through providing evidence and demonstration of their learning.')
def message2():
    return messagebox.askokcancel('The Simulator', 'Welcome to the Ungrading Simulator user guide. This simulator is designed to teach you how ungrading works through completing different activities in order to level up. The main purpose is to actually enjoy the learning process and you being able to define your own grade with evidence. ')

def message3():
    return messagebox.askokcancel('Achieving Grades','Students will achieve grades through providing evidence of their completed tasks. The complexity of tasks will be a strong indicator of the grade youll achieve. Generally, the more complex the tasks, the higher the grade youll achieve. ')

def message4():
    return messagebox.askokcancel('Feedback','Feedback will allow the student to improve on what they have learnt. If the feedback is acted upon correctly, the student will get a higher grade and will develop their learning further')

def toggle_win():
    f1=Frame(w,width=300,height=500,bg='#12c4c0')
    f1.place(x=0,y=0)


    #creating buttons
    
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)


    bttn(0,80,'U N G R A D I N G  S I M U L A T O R','#0f9d9a','#12c4c0', message)
    bttn(0,117,'T H E  S I M U L A T O R','#0f9d9a','#12c4c0', message2)
    bttn(0,154,'A C H I E V I N G  G R A D E S','#0f9d9a','#12c4c0',message3)
    bttn(0,191,'F E E D B A C K','#0f9d9a','#12c4c0', message4)
    #bttn(0,228,'A C E R','#0f9d9a','#12c4c0',None)
    #bttn(0,265,'A C E R','#0f9d9a','#12c4c0',None)
    btn_quit = Button(text='E X I T', fg='Black', width=15, height=2, font='Helvetica', borderwidth= 0,  command= w.quit).pack()

    #
    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    

img1 = ImageTk.PhotoImage(Image.open("open.png"))

Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5,y=10)
       



w.mainloop()



