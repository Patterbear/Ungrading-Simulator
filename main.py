import tkinter as tk
from tkinter import messagebox, PhotoImage, StringVar
import platform
from random import random, choice, randint


"""
This is the where the main loop occurs

Also contains the splash screen, which has two buttons: Start and options
Start will launch the game, so everything to do with the sim itself must be in the function it calls.*/
"""


class Character:
    def __init__(self, name="Default Character", avatar=None, gender="Other"):  # Default values included
        self.name = name
        self.avatar = avatar  # We can make an avatar class when the character customisation is complete
        self.gender = gender
        self.intelligence = round(random(), 2)  # Intelligence begins as random value between 0 and 1
        self.confidence = 5  # Neutral confidence
        self.level = 1

    def __str__(self):
        return "name: " + self.name + ", gender: " + self.gender + ", intelligence: " \
               + str(self.intelligence) + ", confidence: " + str(self.confidence) + ", level: " + str(self.level)


class CreateCharacter:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.startGame = None
        self.app = None

        self.avatar_label = tk.Label(self.frame, text="Avatar:", font=(gameFont, 15))
        self.avatar_label.grid(column=2, row=1)

        profile_image = tk.PhotoImage(file="assets/default_character.gif")
        self.profile_image = tk.Label(self.frame, image=profile_image)  # THIS WILL BE REPLACED BY THE CUSTOM PICTURE
        self.profile_image.image = profile_image
        self.profile_image.grid(column=2, row=2)

        self.change_avatar_button = tk.Button(self.frame, text="Customise", command=self.customise_avatar, font=(gameFont, 15))
        self.change_avatar_button.grid(column=2, row=3)

        self.name_label = tk.Label(self.frame, text="Full Name:", font=(gameFont, 15))
        self.name_label.grid(column=1, row=4)

        self.name_var = tk.StringVar()
        self.name_input = tk.Entry(self.frame, font=(gameFont, 20), textvariable=self.name_var)
        self.name_input.grid(column=2, row=4)

        self.gender_label = tk.Label(self.frame, text="Gender:", font=(gameFont, 15))
        self.gender_label.grid(column=1, row=5)

        self.gender_var = StringVar(self.frame)
        gender_options = ["Male", "Female", "Other"]
        self.gender_var.set(gender_options[2])

        self.gender_input = tk.OptionMenu(self.frame, self.gender_var, *gender_options)
        self.gender_input.grid(column=2, row=5)

        tk.Label(self.frame).grid(column=2, row=6)

        self.save_character_button = tk.Button(self.frame, text="Done", command=self.save_character, font=(gameFont, 20))
        self.save_character_button.grid(column=2, row=7)

        self.avatar = profile_image

        self.frame.pack()

    def customise_avatar(self):

        print("Avatar creation.")

        #  AVATAR CUSTOMISATION HERE

        return None

    def save_character(self):
        # character = Character(name_var.get(), self.profile_image, gender_var.get())
        character = Character(self.name_var.get(), self.profile_image, self.gender_var.get())  # THIS WORKS 12/02
        print(character)

        self.startGame = tk.Toplevel(self.master)
        self.startGame.geometry("1920x1080")
        self.startGame.title("Ungrading Simulator")
        self.startGame.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = UngradingSimulator(self.startGame, character)


class Launcher:
    # Launcher constructor method
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # self.start_button = tk.Button(self.frame, text="Start Game", command=self.start, font=(gameFont, 50))
        self.start_button = tk.Button(self.frame, text="Start Game", command=self.create_character, font=(gameFont, 50))
        self.start_button.pack()

        self.options_button = tk.Button(self.frame, text="Options", command=self.options, font=(gameFont, 50))
        self.options_button.pack()

        # These are just to avoid Pycharm warnings
        self.startGame = None
        self.optionsScreen = None
        self.app = None
        self.eventScreen = None
        self.createCharacter = None

        self.frame.pack()

    # Method to open the game window
    def start(self):
        #  print("Start Game")
        test_character = Character("Test Test", None, str(choice(['Male', 'Female', 'Other'])))  # Test character
        print(test_character)
        self.startGame = tk.Toplevel(self.master)
        self.startGame.geometry("1920x1080")
        self.startGame.title("Ungrading Simulator")
        self.startGame.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = UngradingSimulator(self.startGame, test_character)

    def create_character(self):
        self.createCharacter = tk.Toplevel(self.master)
        self.createCharacter.geometry("764x480")
        self.createCharacter.iconphoto(False, tk.PhotoImage(file='app_icon.png'))
        self.createCharacter.title("Create Character")
        self.app = CreateCharacter(self.createCharacter)

    # Method to open options window
    def options(self):
        self.optionsScreen = tk.Toplevel(self.master)
        self.optionsScreen.geometry("500x700")
        self.optionsScreen.title("Options")
        self.optionsScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = OptionsScreen(self.optionsScreen)


# The game window/class
class UngradingSimulator:
    # Constructor method
    def __init__(self, master, character):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.character = character

        # self.testLabel = tk.Label(self.frame, text="Ungrading Simulator goes here.", font=(gameFont, 20))
        # self.testLabel.pack()

        display = tk.PhotoImage(file="assets/black_image.gif")
        self.display = tk.Label(self.frame, image=display)
        self.display.image = display
        self.display.pack()

        self.testEventButton = tk.Button(self.frame, text="Test Event", command=self.event, font=(gameFont, 20))
        self.testEventButton.pack()

        self.level_up_button = tk.Button(self.frame, text="Level Up test", command=self.levelUp, font=(gameFont, 20))
        self.level_up_button.pack()

        self.view_character_button = tk.Button(self.frame, text="View Profile", command=self.view_character, font=(gameFont, 20))
        self.view_character_button.pack()

        # Ignore these they just stop Pycharm from moaning
        self.eventScreen = None
        self.app = None
        self.level_up_string = None
        self.level_up_box = None
        self.characterScreen = None

        self.frame.pack()
        self.user_level = 0  # user's level will be automatically 0, they've not learned anything

    # Method to call and configure an event (will pick a random one later)
    def event(self):
        self.eventScreen = tk.Toplevel(self.master)
        self.eventScreen.geometry("764x480")
        self.eventScreen.title("Event")
        self.eventScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon

        event_text = "Your professor was assassinated. You get an extra " + str(randint(1, 5)) + "days to submit."
        event_title = "Professor is dead!"

        self.app = Event(self.eventScreen, event_text, event_title)

    # method that when triggered will increase user_level by 1 and notify the user they have levelled up
    def levelUp(self):
        # self.user_level+=1
        self.character.level += 1
        # print(self.character.level)
        self.level_up_string = "Good job! You have levelled up to level "+str(self.character.level)
        self.level_up_box = tk.messagebox.showinfo("You have levelled up!", message=self.level_up_string)

    def view_character(self):
        self.characterScreen = tk.Toplevel(self.master)
        self.characterScreen.geometry("500x700")
        self.characterScreen.title(self.character.name)
        self.characterScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))
        self.app = ViewCharacter(self.characterScreen, self.character)


# Character profile
class ViewCharacter:
    def __init__(self, master, character):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.character = character

        profile_image = tk.PhotoImage(file="assets/default_character.gif")
        self.profile_image = tk.Label(self.frame, image=profile_image)  # THIS WILL BE REPLACED BY THE CUSTOM PICTURE
        self.profile_image.image = profile_image
        self.profile_image.pack()

        self.name_label = tk.Label(self.frame, text="Name: " + self.character.name, font=(gameFont, 20))
        self.name_label.pack()

        self.gender_label = tk.Label(self.frame, text="Gender: " + self.character.gender, font=(gameFont, 20))
        self.gender_label.pack()

        self.level_label = tk.Label(self.frame, text="Skill Level: " + str(self.character.level), font=(gameFont, 20))
        self.level_label.pack()

        self.frame.pack()


# Options screen
class OptionsScreen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.changes = []

        self.testLabel = tk.Label(self.frame, text="Options go here.", font=(gameFont, 20))
        self.testLabel.pack()

        self.DoneButton = tk.Button(self.frame, text="Done", font=(gameFont, 20), command=self.done)
        self.DoneButton.pack()

        self.frame.pack()

    def done(self):

        # Saving changes occurs here

        self.master.destroy()


# Simple event class, displays event title and text
class Event:
    def __init__(self, master, event_title, event_text):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.eventTitleLabel = tk.Label(self.frame, text=event_title, font=(gameFont, 15))
        self.eventTitleLabel.pack()

        self.eventTextLabel = tk.Label(self.frame, text=event_text, font=(gameFont, 15))
        self.eventTextLabel.pack()

        self.eventQuitButton = tk.Button(self.frame, text="Continue", font=(gameFont, 15), command=self.quit)
        self.eventQuitButton.pack()

        self.frame.pack()

    def quit(self):
        self.master.destroy()


# Main method, Creates the root screen and begins the main loop
def main():

    root = tk.Tk()
    app = Launcher(root)
    root.geometry("1280x720")
    root.title("Splash Screen")
    root.option_add('*Dialog.msg.font', 'Helvetica 15')  # Sets dialogue message font
    root.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon

    root.mainloop()


# Method to set the games font based on the OS
def set_game_font():
    if platform.system() == "Linux":  # Linux builds
        return "Helvetica"
    elif platform.system() == "Darwin":  # MacOS
        return "Gill Sans"
    elif platform.system() == "Windows":  # Microsoft Windows
        return "Segoe UI"
    else:
        return "Arial"  # In case the system cannot be identified


# Runs main method
if __name__ == "__main__":
    global gameFont
    gameFont = set_game_font()

    main()
