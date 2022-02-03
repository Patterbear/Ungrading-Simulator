import tkinter as tk
from tkinter import messagebox
import platform
"""
This is the where the main loop occurs

Also contains the splash screen, which has two buttons: Start and options
Start will launch the game, so everything to do with the sim itself must be in the function it calls.*/
"""


class Launcher:
    # Launcher constructor method
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.start_button = tk.Button(self.frame, text="Start Game", command=self.start, font=(gameFont, 50))
        self.start_button.pack()

        self.options_button = tk.Button(self.frame, text="Options", command=self.options, font=(gameFont, 50))
        self.options_button.pack()

        # These are just to avoid Pycharm warnings
        self.startGame = None
        self.optionsScreen = None
        self.app = None
        self.eventScreen = None

        self.frame.pack()

    # Method to open the game window
    def start(self):
        #  print("Start Game")
        self.startGame = tk.Toplevel(self.master)
        self.startGame.geometry("1920x1080")
        self.startGame.title("Ungrading Simulator")
        self.startGame.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = UngradingSimulator(self.startGame)

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
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.testLabel = tk.Label(self.frame, text="Ungrading Simulator goes here.", font=(gameFont, 20))
        self.testLabel.pack()

        self.testEventButton = tk.Button(self.frame, text="Test Event", command=self.event, font=(gameFont, 20))
        self.testEventButton.pack()

        self.level_up_button = tk.Button(self.frame, text="Level Up test", command=self.levelUp, font=(gameFont, 20))
        self.level_up_button.pack()

        # Ignore these two they just stop Pycharm from moaning
        self.eventScreen = None
        self.app = None
        self.level_up_string = None
        self.level_up_box = None

        self.frame.pack()
        self.user_level = 0  # user's level will be automatically 0, they've not learned anything

    # Method to call and configure an event (will pick a random one later)
    def event(self):
        self.eventScreen = tk.Toplevel(self.master)
        self.eventScreen.geometry("764x480")
        self.eventScreen.title("Event")
        self.eventScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon

        event_text = "Your professor was assassinated. You get an extra 10 days to submit."
        event_title = "Professor is dead!"

        self.app = Event(self.eventScreen, event_text, event_title)

    # method that when triggered will increase user_level by 1 and notify the user they have levelled up
    def levelUp(self):
        self.user_level+=1
        self.level_up_string="Good job! You have levelled up to level "+str(self.user_level)
        self.level_up_box = tk.messagebox.showinfo("You have levelled up!", message=self.level_up_string)


# Options screen
class OptionsScreen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.testLabel = tk.Label(self.frame, text="Options go here.", font=(gameFont, 20))
        self.testLabel.pack()

        self.frame.pack()


# Simple event class, displays event title and text
class Event:
    def __init__(self, master, event_text, event_title):
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
