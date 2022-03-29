import tkinter
from tkinter import *
from main import set_game_font
import random
from PIL import Image, ImageTk


# Main function to run the grade calculator
# Takes in a given character's avatar, skill level and confidence
# Confidence is referred to as 'awareness' to match client specification, but they are the same.
def run(avatar, skill_level, awareness):

    global g_skill_level
    global g_avatar
    global g_awareness

    g_skill_level = skill_level
    g_awareness = awareness

    # If the character has no avatar, the default one is used
    if avatar is None:
        g_avatar = "assets/default_character.gif"
    else:
        g_avatar = avatar

    # Sets game font from main file's function
    gameFont = set_game_font()

    root = tkinter.Toplevel()
    root.title('Grade Calculator')
    root.geometry('500x600')
    root.iconphoto(False, PhotoImage(file='app_icon.png'))

    # Function to close the screen
    def close():
        root.destroy()

    # Function to calculate final score and place it on the screen
    def calculate():

        # Final grade calculated using skill level and a degree of randomness (1-5%)
        g_achieved = (g_skill_level*10) + random.randint(1, 5)

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
        Button(root, text='End Game', font=(gameFont, 15), command=close).pack()

        # Greyed out button to prevent user from trying to calculate their grade again
        Button(root, text='Get my grade', font=(gameFont, 20), state="disabled").place(x=calculate_button.winfo_x(), y=calculate_button.winfo_y())

    heading_label = Label(root, text='Self Assessment', font=(gameFont, 18))
    heading_label.pack()

    img = ImageTk.PhotoImage(Image.open(g_avatar))
    profile_image = Label(root, image=img)
    profile_image.pack()

    # Character's awareness (confidence) determines how close their prediction is to the final grade
    character_prediction = int(g_awareness*((g_skill_level*10) + random.randint(0, 5)))

    # Prediction could technically be over 100%, this ensures it isn't
    if character_prediction > 100:
        character_prediction = 100

    # Displays the character's 'prediction' dialogue below their picture
    character_dialogue = Label(root, bg='white', font=(gameFont, 18), text='"I reckon I achieved a grade of of ' + str(character_prediction) + '%"')
    character_dialogue.pack()

    Label(root, font=(gameFont, 18)).pack()

    calculate_button = Button(root, text='Get my grade', font=(gameFont, 20), command=calculate)
    calculate_button.pack()

    root.mainloop()
