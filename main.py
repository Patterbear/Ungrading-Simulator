import tkinter as tk
from tkinter import messagebox, PhotoImage, StringVar
import platform
from random import random, choice, randint
#import HelpPage


"""
This is the where the main loop occurs

Also contains the splash screen, which has two buttons: Start and options
Start will launch the game, so everything to do with the sim itself must be in the function it calls.*/
"""


class UserGuide:
    def __init__(self, master):

        HelpPage.main()



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

#uk
class CreateCharacter:
    def __init__(self, master, parent):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.parent = parent

        self.startGame = None
        self.app = None
        self.character = None

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
        self.character = Character(self.name_var.get(), self.profile_image, self.gender_var.get())  # THIS WORKS 12/02
        print(self.character)

        """ self.master.startGame = tk.Toplevel(self.parent.startGame)
        self.parent.startGame.geometry("1920x1080")
   

        self.parent.startGame.title("Ungrading Simulator")
        self.parent.startGame.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.parent.app = UngradingSimulator(self.parent.startGame, self.character)
        # self.master.destroy()"""

        self.parent.start(self.character)
        self.done()

    def done(   self):
        self.master.destroy()


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
    def start(self, character):
        #  print("Start Game")
        # test_character = Character("Test Test", None, str(choice(['Male', 'Female', 'Other'])))  # Test character
        # print(test_character)
        self.startGame = tk.Toplevel(self.master)
        self.startGame.geometry("1920x1080")
        self.startGame.title("Ungrading Simulator")
        self.startGame.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = UngradingSimulator(self.startGame, character)

    def create_character(self):
        self.createCharacter = tk.Toplevel(self.master)
        self.createCharacter.geometry("764x480")
        self.createCharacter.iconphoto(False, tk.PhotoImage(file='app_icon.png'))
        self.createCharacter.title("Create Character")
        self.app = CreateCharacter(self.createCharacter, self)

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

        self.user_guide_button = tk.Button(self.frame, text="User Guide", command=self.user_guide, font=(gameFont, 20))
        self.user_guide_button.pack()


        self.time_limit=20
        self.day_num=1
        self.next_day_button= tk.Button(self.frame, text="Progress to next day", command=self.next_day, font=(gameFont, 20))
        self.next_day_button.pack()
        self.days_count_string="Day number: "+str(self.day_num)
        self.day_num_label= tk.Label(self.frame, text=self.days_count_string)
        self.day_num_label.pack()

        # Ignore these they just stop Pycharm from moaning
        self.eventScreen = None
        self.app = None
        self.level_up_string = None
        self.level_up_box = None
        self.characterScreen = None
        self.user_guide_screen = None

        self.frame.pack()



    # Method to call and configure an event (will pick a random one later)
    def event(self):
        self.eventScreen = tk.Toplevel(self.master)
        self.eventScreen.geometry("764x480")
        self.eventScreen.title("Event")
        self.eventScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon

        event_text = "Your professor was assassinated. You get an extra " + str(randint(1, 5)) + " days to submit."
        event_title = "Professor is dead!"

        self.app = Event(self.eventScreen, event_title, event_text)

    # method that when triggered will increase user   _level by 1 and notify the user they have levelled up
    def levelUp(self):
        # self.user_level+=1
        self.character.level += 1
        # print(self.character.level)
        self.level_up_string = "Good job! You have levelled up to level "+str(self.character.level)
        self.level_up_box = tk.messagebox.showinfo("You have levelled up!", message=self.level_up_string)

    def view_character(self):
        self.characterScreen = tk.Toplevel(self.master)
        self.characterScreen.geometry("500x450")
        self.characterScreen.title(self.character.name)
        self.characterScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))
        self.app = ViewCharacter(self.characterScreen, self.character)

    def user_guide(selfotal_days):
        """self.user_guide_screen = tk.Toplevel(self.master)
        self.user_guide_screen.geometry('900x500')
        self.user_guide_screen.resizable(0, 0)
        self.user_guide_screen.title('User Guide')
        self.user_guide_screen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))
        self.app = UserGuide(self.user_guide_screen)"""
        HelpPage.main()

    def next_day(self):
        self.day_num+=1
        if self.day_num %5==0:
            self.character.intelligence+=3
        if self.day_num%2==0:
            self.character.confidence+=1
        if self.day_num>self.time_limit:
            self.time_limit_box= tk.messagebox.showinfo("Course is finished", message="It has been 20 days and your Ungrading course has been completed. Press OK to see your score")
            self.end_of_sim_scores()
        self.days_count_string="Day number: "+str(self.day_num)
        self.day_num_label.destroy()
        self.day_num_label= tk.Label(self.frame, text=self.days_count_string)
        self.day_num_label.pack()

    def end_of_sim_scores(self):
        pass


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
        self.user_level = 0  # user's level will be automatically 0, they've not learned anything

        tk.Label(self.frame, text="").pack()

        self.done_button = tk.Button(self.frame, text="Done", command=self.done, font=(gameFont, 20))
        self.done_button.pack()

        self.frame.pack()

    def done(self):
        self.master.destroy()


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
