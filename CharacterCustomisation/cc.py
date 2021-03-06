from tkinter import *
from PIL import ImageTk, Image

profile_image_location = None
current_tie = 3
current_suit = 1
current_hair = 1
current_shirt = 3


def run():

    global profile_image_location
    global current_suit
    global current_tie
    global current_hair
    global current_shirt


    root = Toplevel()
    root.geometry('1920x1080')
    root.title('Character Customization')
    root.configure(background='white')
    MainCanvas = Canvas(root, width=1920, height=1080, bg="white")
    MainCanvas.pack(pady=20)

    # Main two images on the first frame

    # Image1
    MalePhoto = Image.open('CharacterCustomisation/male.png')
    # resize image 1
    resized = MalePhoto.resize((350,350), Image.ANTIALIAS)
    P1 = ImageTk.PhotoImage(resized)

    # Image2
    FemalePhoto = Image.open('CharacterCustomisation/female.png')
    # Resize image 2
    resized = FemalePhoto.resize((350,350), Image.ANTIALIAS)
    P2 = ImageTk.PhotoImage(resized)

    # Functions to change between frames (main, male cus, female cus)
    def mc():
        maleCanvas.pack()
        MainCanvas.pack_forget()


    def fc():
        femaleCanvas.pack()
        MainCanvas.pack_forget()

    def back():
        femaleCanvas.pack_forget()
        maleCanvas.pack_forget()
        MainCanvas.pack()

    def confirm_profile():
        root.quit()
        return profile_image_location


    # Buttons of the main frame for option (male or female)

    male_button = Button(MainCanvas, image=P1, command=mc)
    female_button = Button(MainCanvas, image=P2, command=fc)

    male_button.grid(row=0, column=0, pady=220)
    female_button.grid(row=0, column=1)

    # Male Customization Frmae (canvas)
    maleCanvas = Canvas(root, width=1920, height=1080, bg="white")

    # changing male items

    current_tie = 3
    current_suit = 1

    def changeitem(ITEM):
        global profile_image_location
        if ITEM in range (3,5):
            global current_tie
            current_tie = ITEM

        if ITEM in range (1,3):
            global current_suit
            current_suit = ITEM

        if current_suit == 1 and current_tie == 3:
            black_suit_blue_tie.grid_forget()
            blue_suit_black_tie.grid_forget()
            blue_suit_blue_tie.grid_forget()
            black_suit_black_tie.grid(row=0, column=2, padx=100, rowspan=50)
            profile_image_location = "CharacterCustomisation/allblack.gif"

        elif current_suit == 1 and current_tie == 4:
            blue_suit_blue_tie.grid_forget()
            blue_suit_black_tie.grid_forget()
            black_suit_black_tie.grid_forget()
            black_suit_blue_tie.grid(row=0, column=2, padx=100, rowspan=50)
            profile_image_location = "CharacterCustomisation/BlackB-BlueT.gif"

        elif current_suit == 2 and current_tie == 4:
            black_suit_black_tie.grid_forget()
            black_suit_blue_tie.grid_forget()
            blue_suit_black_tie.grid_forget()
            blue_suit_blue_tie.grid(row=0, column=2, padx=100, rowspan=50)
            profile_image_location = "CharacterCustomisation/MaleBlueBlazerBlueTie.gif"

        elif current_suit == 2 and current_tie == 3:
            blue_suit_blue_tie.grid_forget()
            black_suit_blue_tie.grid_forget()
            black_suit_black_tie.grid_forget()
            blue_suit_black_tie.grid(row=0, column=2, padx=100, rowspan=50)
            profile_image_location = "CharacterCustomisation/BluBlazBlackTie.gif"


    # Item images of male (IMPORTING)
    # Image 1
    mi1 = Image.open('CharacterCustomisation/MaleBlackBlazer .png')
    # resize image 1
    resized = mi1.resize((350,350), Image.ANTIALIAS)
    MBB = ImageTk.PhotoImage(resized)

    # Image 2
    mi2 = Image.open('CharacterCustomisation/MaleBlazerBlue.png')
    # resize image 2
    resized = mi2.resize((350,350), Image.ANTIALIAS)
    MBBLUE = ImageTk.PhotoImage(resized)

    # Image 3
    mi3 = Image.open('CharacterCustomisation/TieBlack.png')
    # resize image 3
    resized1 = mi3.resize((350,350), Image.ANTIALIAS)
    TieBlack = ImageTk.PhotoImage(resized1)

    # Image 4
    mi4 = Image.open('CharacterCustomisation/TieBlue.png')
    # resize image 4
    resized2 = mi4.resize((350,350), Image.ANTIALIAS)
    TieBlue = ImageTk.PhotoImage(resized2)

    # fixed problem (speak to me)
    def A1():
        a = 1
        changeitem(a)


    def A2():
        a = 2
        changeitem(a)


    def A3():
        a = 3
        changeitem(a)


    def A4():
        a = 4
        changeitem(a)

    # Change image into buttons
    blackSuit = Button(maleCanvas, image=MBB, command=A1)
    blueSuit = Button(maleCanvas, image=MBBLUE, command=A2)
    TieBlack1 = Button(maleCanvas, image=TieBlack, command=A3)
    TieBlue1 = Button(maleCanvas, image=TieBlue, command=A4)

    # Changing of profile picture (importing)
    mi5 = Image.open('CharacterCustomisation/male.png')
    # resize image 5
    resized3 = mi5.resize((350,350), Image.ANTIALIAS)
    Profile = ImageTk.PhotoImage(resized3)

    mi6 = Image.open('CharacterCustomisation/BlackB-BlueT.png')
    # resize image 5
    resized4 = mi6.resize((350,350), Image.ANTIALIAS)
    Profile2 = ImageTk.PhotoImage(resized4)

    mi7 = Image.open('CharacterCustomisation/BluBlazBlackTie.png')
    # resize image 5
    resized5 = mi7.resize((350,350), Image.ANTIALIAS)
    Profile3 = ImageTk.PhotoImage(resized5)

    mi8 = Image.open('CharacterCustomisation/MaleBlueBlazerBlueTie.png')
    # resize image 5
    resized6 = mi8.resize((350,350), Image.ANTIALIAS)
    Profile4 = ImageTk.PhotoImage(resized6)

    # CHANGING IMAGES INTO BUTTONS (Male)
    black_suit_black_tie = Button(maleCanvas, image=Profile)
    black_suit_blue_tie = Button(maleCanvas, image=Profile2)
    blue_suit_black_tie = Button(maleCanvas, image=Profile3)
    blue_suit_blue_tie = Button(maleCanvas, image=Profile4)

    blackSuit.grid(row=0, column=1, pady=50, padx=50)
    blueSuit.grid(row=1, column=1)
    TieBlack1.grid(row=0, column=0)
    TieBlue1.grid(row=1, column=0)


    # Back button
    backimage = Image.open('CharacterCustomisation/backbutton.jpg')
    resized7 = backimage.resize((90,35), Image.ANTIALIAS)
    bb = ImageTk.PhotoImage(resized7)


    # confrim button
    confrim_image = Image.open('CharacterCustomisation/confrim.jpg')
    confrim_image_resize = confrim_image.resize((125,35), Image.ANTIALIAS)
    confrim_image_button = ImageTk.PhotoImage(confrim_image_resize)

    back_button = Button(maleCanvas, image=bb, command=back)
    back_button.place(x=1260, y=771)


    # FEMALE Customization (canvas)
    femaleCanvas = Canvas(root, width=1920, height=1080, bg="white")



    current_shirt = 1
    current_hair = 3

    def female_changeitem(female_item):
        global profile_image_location
        if female_item in range(3, 5):
            global current_hair
            current_hair = female_item

        if female_item in range(1, 3):
            global current_shirt
            current_shirt = female_item


        if current_shirt == 1 and current_hair == 3:
            profile2_f.grid_forget()
            profile3_f.grid_forget()
            profile4_f.grid_forget()
            profile1_f.grid(row=0, column=2, padx=100, rowspan=50)
            profile_image_location = "CharacterCustomisation/BLACKhairblackshirt.gif"

        elif current_shirt == 1 and current_hair == 4:
            profile1_f.grid_forget()
            profile3_f.grid_forget()
            profile4_f.grid_forget()
            profile2_f.grid(row=0, column=2, padx=100, rowspan=50)
            profile_image_location = "CharacterCustomisation/BrownHair-BlackShirr.gif"

        elif current_shirt == 2 and current_hair == 3:
            profile1_f.grid_forget()
            profile2_f.grid_forget()
            profile4_f.grid_forget()
            profile3_f.grid(row=0, column=2, padx=100, rowspan=50)
            profile_image_location = "CharacterCustomisation/BlackHair-OrangeShirt.gif"

        elif current_shirt == 2 and current_hair == 4:
            profile3_f.grid_forget()
            profile2_f.grid_forget()
            profile1_f.grid_forget()
            profile4_f.grid(row=0, column=2, padx=100, rowspan=50)
            profile_image_location = "CharacterCustomisation/BrownHair-OrangeShirt.gif"


    def f1():
        f = 1
        female_changeitem(f)


    def f2():
        f = 2
        female_changeitem(f)


    def f3():
        f = 3
        female_changeitem(f)


    def f4():
        f = 4
        female_changeitem(f)


    # Four item for female displaying on feamle canvas

    f_image_1 = Image.open('CharacterCustomisation/Female-Black-HaIr.png')
    f_image_1_resize = f_image_1.resize((350,350), Image.ANTIALIAS)
    black_hair = ImageTk.PhotoImage(f_image_1_resize)

    f_image_2 = Image.open('CharacterCustomisation/Female-Blonde-HaIr.png')
    f_image_2_resize = f_image_2.resize((350,350), Image.ANTIALIAS)
    blonde_hair = ImageTk.PhotoImage(f_image_2_resize)

    f_image_3 = Image.open('CharacterCustomisation/BlackShirtT.png')
    f_image_3_resize = f_image_3.resize((350,350), Image.ANTIALIAS)
    black_shirt = ImageTk.PhotoImage(f_image_3_resize)

    f_image_4 = Image.open('CharacterCustomisation/OrangeShirt.png')
    f_image_4_resize = f_image_4.resize((350,350), Image.ANTIALIAS)
    pink_shirt = ImageTk.PhotoImage(f_image_4_resize)

    female_black_shirt_button = Button(femaleCanvas, image=black_shirt, command=f1)
    female_pink_shirt_button = Button(femaleCanvas, image=pink_shirt, command=f2)
    female_black_hair_button = Button(femaleCanvas, image=black_hair, command=f3)
    female_blonde_hair_button = Button(femaleCanvas, image=blonde_hair, command=f4)


    female_black_hair_button.grid(row=0, column=0, pady=50, padx=50)
    female_blonde_hair_button.grid(row=1, column=0)
    female_black_shirt_button.grid(row=0, column=1)
    female_pink_shirt_button.grid(row=1, column=1)


    # Female profile images

    f_profile_1 = Image.open('CharacterCustomisation/BLACKhairblackshirt.png')
    f_profile_1_resize = f_profile_1.resize((350,350), Image.ANTIALIAS)
    profile1_female = ImageTk.PhotoImage(f_profile_1_resize)

    f_profile_2 = Image.open('CharacterCustomisation/BrownHair-BlackShirr.png')
    f_profile_2_resize = f_profile_2.resize((350,350), Image.ANTIALIAS)
    profile2_female = ImageTk.PhotoImage(f_profile_2_resize)

    f_profile_3 = Image.open('CharacterCustomisation/BlackHair-OrangeShirt.png')
    f_profile_3_resize = f_profile_3.resize((350,350), Image.ANTIALIAS)
    profile3_female = ImageTk.PhotoImage(f_profile_3_resize)

    f_profile_4 = Image.open('CharacterCustomisation/BrownHair-OrangeShirt.png')
    f_profile_4_resize = f_profile_4.resize((350,350), Image.ANTIALIAS)
    profile4_female = ImageTk.PhotoImage(f_profile_4_resize)


    profile1_f = Button(femaleCanvas, image=profile1_female)
    profile2_f = Button(femaleCanvas, image=profile2_female)
    profile3_f= Button(femaleCanvas, image=profile3_female)
    profile4_f = Button(femaleCanvas, image=profile4_female)

    back_button2 = Button(femaleCanvas, image=bb, command=back)
    back_button2.place(x=1260, y=771)

    confrim_button1 = Button(femaleCanvas, image=confrim_image_button, command=confirm_profile)
    confrim_button1.place(x=1120, y=771)

    confrim_button2 = Button(maleCanvas, image=confrim_image_button, command=confirm_profile)
    confrim_button2.place(x=1120, y=771)

    root.mainloop()