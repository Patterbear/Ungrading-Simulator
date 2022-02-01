import tkinter as tk
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

        self.start_button = tk.Button(self.frame, text="Start Game", command=self.start)
        self.start_button.pack()

        self.options_button = tk.Button(self.frame, text="Options", command=self.options)
        self.options_button.pack()

        # These are just to avoid Pycharm warnings
        self.startGame = None
        self.optionsScreen = None
        self.app = None
        self.eventScreen = None

        self.frame.pack()

    # Method to open the game window
    def start(self):
        print("Start Game")
        self.startGame = tk.Toplevel(self.master)
        self.startGame.geometry("1920x1080")
        self.startGame.title("Ungrading Simulator")
        self.app = UngradingSimulator(self.startGame)

    # Method to open options window
    def options(self):
        self.optionsScreen = tk.Toplevel(self.master)
        self.optionsScreen.geometry("500x700")
        self.optionsScreen.title("Options")
        self.app = OptionsScreen(self.optionsScreen)


# The game window/class
class UngradingSimulator:
    # Constructor method
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.testLabel = tk.Label(self.frame, text="Ungrading Simulator goes here.")
        self.testLabel.pack()

        self.testEventButton = tk.Button(self.frame, text="Test Event", command=self.event)
        self.testEventButton.pack()

        # Ignore these two they just stop Pycharm from moaning
        self.eventScreen = None
        self.app = None

        self.frame.pack()

    # Method to call and configure an event (will pick a random one later)
    def event(self):
        self.eventScreen = tk.Toplevel(self.master)
        self.eventScreen.geometry("764x480")
        self.eventScreen.title("Event")

        event_text = "Your professor was assassinated. You get an extra 10 days to submit."
        event_title = "Professor is dead!"

        self.app = Event(self.eventScreen, event_text, event_title)


# Options screen
class OptionsScreen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.testLabel = tk.Label(self.frame, text="Options go here.")
        self.testLabel.pack()

        self.frame.pack()


# Simple event class, displays event title and text
class Event:
    def __init__(self, master, event_text, event_title):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.eventTitleLabel = tk.Label(self.frame, text=event_title)
        self.eventTitleLabel.pack()

        self.eventTextLabel = tk.Label(self.frame, text=event_text)
        self.eventTextLabel.pack()

        self.frame.pack()


# Main method, Creates the root screen and begins the main loop
def main():
    root = tk.Tk()
    app = Launcher(root)
    root.geometry("1280x720")
    root.title("Splash Screen")
    root.mainloop()


# Runs main method
if __name__ == "__main__":
    main()
