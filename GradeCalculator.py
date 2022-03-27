import tkinter
from cgitb import text
from logging import root
from textwrap import fill
from tkinter import *
from tkinter import ttk
from turtle import heading
from main import set_game_font
import random
from PIL import Image, ImageTk

g_skill_level = 0
g_total_activities = 0


def run(avatar, skill_level, total_activities, awareness):

    global g_skill_level
    global g_total_activities
    global g_avatar
    global g_awareness

    g_skill_level = skill_level
    g_total_activities = total_activities
    g_awareness = awareness

    if avatar is None:
        g_avatar = "assets/default_character.gif"
    else:
        g_avatar = avatar

    gameFont = set_game_font()

    root = tkinter.Toplevel()
    root.title('Grade Calculator')
    root.geometry('500x600')

    # Function to calculate final score and place it on the screen
    def calculate():

        # Final grade calculated using skill level and a degree of randomness (0-5%)
        g_achieved = (g_skill_level*10) + random.randint(0, 6)

        # The degree of randomness could put the score over 100%, so this ensures it doesn't
        if g_achieved > 100:
            g_achieved = 100

        # Determines colour of grade label based on grade (green for good, yellow for ok and red for bad)
        if g_achieved >= 70:
            score_colour = 'green'
        elif g_achieved <= 69 and g_achieved > 50:
            score_colour = 'yellow'
        else:
            score_colour = 'red'

        Label(root, font=(gameFont, 18)).pack()
        Label(root, text="You scored: " + str(g_achieved) + "%", font=(gameFont, 40), bg=score_colour).pack()#place(x=190,y=275)
        Label(root, font=(gameFont, 18)).pack()
        Button(root, text='End Game', font=(gameFont, 15), command=quit).pack()
        Button(root, text='Get my grade', font=(gameFont, 20), state="disabled").place(x=152, y=330)

    heading_label = Label(root, text='Self Assessment', font=(gameFont, 18))
    heading_label.pack()

    img = ImageTk.PhotoImage(Image.open(g_avatar))
    profile_image = Label(root, image=img)
    profile_image.pack()

    # Character's awareness (confidence) determines how close their prediction is to the final grade
    character_prediction = int(g_awareness*((g_skill_level*10) + random.randint(0, 6)))

    # Prediction could technically be over 100%, this ensures it isn't
    if character_prediction > 100:
        character_prediction = 100

    character_dialogue = Label(root, bg='white', font=(gameFont, 18), text='"I reckon I achieved a grade of of ' + str(character_prediction) + '%"')
    character_dialogue.pack()

    Label(root, font=(gameFont, 18)).pack()

    calculate_button = Button(root, text='Get my grade', font=(gameFont, 20), command=calculate).pack()

    root.mainloop()
