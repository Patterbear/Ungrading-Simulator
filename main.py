import tkinter as tk
from tkinter import messagebox, PhotoImage, StringVar
import platform
from random import random, choice, randint, uniform
import HelpPage
import GradeCalculator
import Submission_File
import CharacterCustomisation.cc
import Feedback_page
from PIL import ImageTk, Image
import sqlite3


class UserGuide:
    def __init__(self, master):

        HelpPage.main()


class Character:
    def __init__(self, name="Default Character", avatar="assets/default_character.gif", gender="Other", intelligence=round(random(), 2), confidence=5, level=1, exp_points=0, activities_completed=0, topic_levels=[1, 1, 1, 1]):  # Default values included
        self.name = name
        self.avatar = avatar
        self.gender = gender
        self.intelligence = intelligence
        self.confidence = confidence
        self.level = level
        self.exp_points = exp_points
        self.activities_completed = activities_completed
        self.topic_levels = topic_levels

    def __str__(self):
        return "name: " + self.name + ", gender: " + self.gender + ", intelligence: " \
               + str(self.intelligence) + ", confidence: " + str(self.confidence) + ", level: " + str(self.level)\
               + "\nTopic 1 Level: " + str(self.topic_levels[0]) + "\nTopic 2 Level: " + str(self.topic_levels[1])\
               + "\nTopic 3 Level: " + str(self.topic_levels[2]) + "\nTopic 4 Level: " + str(self.topic_levels[3])\
                + "\nTotal Activities Completed: " + str(self.activities_completed)


class CreateCharacter:
    def __init__(self, master, parent):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.parent = parent

        self.startGame = None
        self.app = None
        self.character = None
        self.profile_photo = None

        self.avatar_label = tk.Label(self.frame, text="Avatar:", font=(gameFont, 15))
        self.avatar_label.grid(column=2, row=1)

        profile_image = tk.PhotoImage(file="assets/default_character.gif")

        self.profile_image = tk.Label(self.frame, image=profile_image)
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

        #print("Avatar creation.")

        CharacterCustomisation.cc.run()
        self.profile_photo = CharacterCustomisation.cc.profile_image_location


        profile_image = tk.PhotoImage(file=self.profile_photo)
        self.profile_image = tk.Label(self.frame, image=profile_image)  # THIS HAS BEEN REPLACED BY THE CUSTOM PICTURE
        self.profile_image.image = profile_image
        self.profile_image.grid(column=2, row=2)

        #self.frame.pack()

        #return profile_photo

    def save_character(self):
        self.character = Character(self.name_var.get(), self.profile_photo, self.gender_var.get())  # THIS WORKS 12/02

        #save the character into the database
        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute('''INSERT INTO Characters (name, gender, photolink, daynumber, skilllevel, experiencepoints, intelligence)
                  VALUES(?, ?, ?, ?, ?, ?, ?);''', (self.character.name, self.character.gender, self.profile_photo, 0, self.character.level, 0, self.character.intelligence))
        db.commit()
        db.close()

        self.parent.start(self.character)
        self.done()

    def done(self):
        self.master.destroy()


class Launcher:
    # Launcher constructor method
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.name_to_load = "Test Character"

        self.start_button = tk.Button(self.frame, text="New Game", command=self.create_character, font=(gameFont, 50))
        self.start_button.pack()

        #self.load_button = tk.Button(self.frame, text="Load Game", command=lambda: self.load_game(self.name_to_load), font=(gameFont, 50))
        self.load_button = tk.Button(self.frame, text="Load Game", command=self.load_screen, font=(gameFont, 50))
        self.load_button.pack()

        self.options_button = tk.Button(self.frame, text="Options", command=self.options, font=(gameFont, 50))
        self.options_button.pack()

        # These are just to avoid Pycharm warnings
        self.startGame = None
        self.optionsScreen = None
        self.app = None
        self.eventScreen = None
        self.createCharacter = None
        self.loadScreen = None


        self.frame.pack()

    # Method to open the game window
    def start(self, character, time_limit=20, day_num=1):
        self.startGame = tk.Toplevel(self.master)
        self.startGame.geometry("1920x1080")
        self.startGame.title("Ungrading Simulator")
        self.startGame.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = UngradingSimulator(self.startGame, character, time_limit, day_num)

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

    # This method starts a game based on existing values
    # For now, it gets character and game state info from hardcoded variables
    # It will be able to get them from a .db file (sqlite3)
    def load_game(self, g_name):
        #print(g_name)

        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute("SELECT * FROM Characters WHERE name = ?", (g_name,))
        result = c.fetchall()[0]

        l_name = result[1]
        l_avatar = result[3]
        l_gender = result[2]
        l_intelligence = result[7]
        l_confidence = 5
        l_level = result[5]
        l_exp = result[6]

        l_time_limit = 20
        l_day_num = result[4]

        l_activities_completed = 6


        l_topic_levels = [4, 5, 3, 1]




        loaded_character = Character(l_name, l_avatar, l_gender, l_intelligence, l_confidence, l_level, l_exp, l_activities_completed, l_topic_levels)
        #print(loaded_character)
        #print("Loaded time limit: " + str(l_time_limit))
        #print("Loaded day: " + str(l_day_num))

        self.start(loaded_character, l_time_limit, l_day_num)

    def load_screen(self):
        self.loadScreen = tk.Toplevel(self.master)
        self.loadScreen.geometry("825x500")
        self.loadScreen.title("Load Game")
        self.loadScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = LoadScreen(self.loadScreen, self)


class LoadScreen:
    def __init__(self, master, parent):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.parent = parent
        self.save_list = None

        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute("SELECT * FROM Characters")
        result = c.fetchall()
        print(result[0])

        for i in range(0, len(result)):
            tk.Label(self.frame, text="Save " + str(result[i][0]) + ": " + result[i][1] + " (" + result[i][2] + ")", font=(gameFont, 30)).grid(column=0, row=i, padx=25, sticky="w")
            tk.Button(self.frame, text="Load", command=lambda: self.load_character(result[i][1]), font=(gameFont, "30")).grid(column=1, row=i)

        self.frame.grid(row=0, column=0, sticky="nsew")

    def load_character(self, slot_name):
        print(slot_name)

        self.parent.load_game(slot_name)





# The game window/class
class UngradingSimulator:
    # Constructor method
    def __init__(self, master, character, time_limit=20, day_num=1):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.character = character
        self.time_limit = time_limit
        self.day_num = day_num

        self.testEventButton = tk.Button(self.frame, text="Test Event", command=self.event, font=(gameFont, 15))
        self.testEventButton.grid(row=1, column=8)

        self.level_up_button = tk.Button(self.frame, text="Level Up test", command=self.level_up, font=(gameFont, 15))
        self.level_up_button.grid(row=2, column=8)

        self.view_character_button = tk.Button(self.frame, text="View Profile", command=self.view_character, font=(gameFont, 30))
        self.view_character_button.grid(column=0, row=0, padx=70)

        self.user_guide_button = tk.Button(self.frame, text="User Guide", command=self.user_guide, font=(gameFont, 30))
        self.user_guide_button.grid(column=0, row=1, padx=70)

        self.user_guide_button = tk.Button(self.frame, text="Feedback", command=self.feedback, font=(gameFont, 30))
        self.user_guide_button.grid(column=0, row=2, padx=90)

        display = tk.PhotoImage(file="assets/black_image.gif")
        self.display = tk.Label(self.frame, image=display)
        self.display.image = display
        self.display.grid(row=0, column=2, rowspan=4, columnspan=6)

        tk.Label(self.frame, text=" ", font=(gameFont, 40)).grid(column=0, row=7, columnspan=10)

        self.study_button= tk.Button(self.frame, text="Study", command=self.study, font=(gameFont, 35))
        self.study_button.grid(column=0, row=8)

        self.activity_button=tk.Button(self.frame, text="Complete Activities", command=self.activities, font=(gameFont, 35))
        self.activity_button.grid(column=2, row=8)

        tk.Label(self.frame, text="    ", font=(gameFont, 40)).grid(column=3, row=8, rowspan=1)

        self.submit_task_button = tk.Button(self.frame, text="Submit Activities", command=self.file_submission, font=(gameFont, 35))
        self.submit_task_button.grid(column=4, row=8)

        tk.Label(self.frame, text="    ", font=(gameFont, 40)).grid(column=0, row=9, columnspan=10)

        self.save_exit_button = tk.Button(self.frame, text="Save and Exit", command=self.save_exit, font=(gameFont, 30))
        self.save_exit_button.grid(column=0, row=10)




        self.next_day_button= tk.Button(self.frame, text="Next day", command=self.next_day, font=(gameFont, 35))
        self.next_day_button.grid(column=8, row=10)

        self.days_count_string="Day number: "+str(self.day_num)
        self.day_num_label= tk.Label(self.frame, text=self.days_count_string, font=(gameFont, 35))
        self.day_num_label.grid(row=0, column=8, sticky='n')

        # Ignore these they just stop Pycharm from moaning
        self.eventScreen = None
        self.app = None
        self.level_up_string = None
        self.level_up_box = None
        self.characterScreen = None
        self.user_guide_screen = None
        self.time_limit_box = None

        self.frame.grid(row=0, column=0, sticky="nsew")

    # Method to call and configure an event (will pick a random one later)
    def event(self):
        self.eventScreen = tk.Toplevel(self.master)
        self.eventScreen.geometry("764x480")
        self.eventScreen.title("Event")
        self.eventScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon

        event_text = "Your professor was assassinated. You get an extra " + str(randint(1, 5)) + " days to submit."
        event_title = "Professor is dead!"

        self.app = Event(self.eventScreen, event_title, event_text)

        #Code to implement: when an event is triggered it will check to see if the days remaining makes it possible to happen
        #will check days to see if the day value will be negative and then check if it can happen
        #if self.rand_event.days<0:
           # if (20-self.day_num)<=self.rand_event_days:
            #    pass #insert code to prevent event taking place
           # else:
            #    self.day_num+=self.rand_event.days
           #     pass #do event

    # method that when triggered will increase user_level by 1 and notify the user they have levelled up
    def level_up(self):
        self.character.level += 1
        self.character.exp_points-=100
        self.level_up_string = "Good job! You have levelled up to level "+str(self.character.level)
        self.level_up_box = tk.messagebox.showinfo("You have levelled up!", message=self.level_up_string)
        self.autosave()

    def view_character(self):
        self.characterScreen = tk.Toplevel(self.master)
        self.characterScreen.geometry("500x480")
        self.characterScreen.title(self.character.name)
        self.characterScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))

        if self.character.avatar is None:
            self.character.avatar = "assets/default_character.gif"

        self.app = ViewCharacter(self.characterScreen, self.character)

    def user_guide(self):

        HelpPage.main()

    def next_day(self):
        self.day_num+=1
        self.autosave()

        if self.day_num %5==0:
            intell_inc=round(uniform(1, 4), 2)
            self.character.intelligence+=intell_inc
        if self.day_num>self.time_limit:
            self.time_limit_box= tk.messagebox.showinfo("Course is finished", message="It has been " + str(self.time_limit) + " days and your Ungrading course has been completed. Press OK to see your score")
            self.end_of_sim_scores()

        self.days_count_string="Day number: "+str(self.day_num)
        self.day_num_label.destroy()
        self.day_num_label= tk.Label(self.frame, text=self.days_count_string, font=(gameFont, 35))
        self.day_num_label.grid(row=0, column=8, sticky='n')


    def study(self):
        self.character.exp_points+=50
        if self.character.exp_points>=100:
            self.level_up()
        self.autosave()

    def activities(self):
        self.character.exp_points+=20
        intell_inc = round(random(), 2)
        self.character.intelligence += intell_inc
        if self.character.exp_points>=100:
            self.level_up()
        self.character.activities_completed += 1
        self.autosave()

    def end_of_sim_scores(self):
        GradeCalculator.run(self.character.level, self.character.activities_completed)

    def file_submission(self):
        Submission_File.run()

    def feedback(self):
        Feedback_page.run()

    def save_exit(self):
        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()

        c.execute('''UPDATE Characters SET daynumber = ?, skilllevel = ?, experiencepoints = ?, intelligence = ? 
        WHERE name = ?''', (self.day_num, self.character.level, self.character.exp_points, self.character.intelligence, self.character.name))

        db.commit()
        db.close()

        self.master.destroy()

    def autosave(self):
        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()

        c.execute('''UPDATE Characters SET daynumber = ?, skilllevel = ?, experiencepoints = ?, intelligence = ? 
        WHERE name = ?''', (self.day_num, self.character.level, self.character.exp_points, self.character.intelligence, self.character.name))

        db.commit()
        db.close()


# Character profile
class ViewCharacter:
    def __init__(self, master, character):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.character = character

        profile_image = tk.PhotoImage(file=self.character.avatar)
        self.profile_image = tk.Label(self.frame, image=profile_image)  # THIS WILL BE REPLACED BY THE CUSTOM PICTURE
        self.profile_image.image = profile_image
        self.profile_image.pack()

        self.name_label = tk.Label(self.frame, text="Name: " + self.character.name, font=(gameFont, 20))
        self.name_label.pack()

        self.gender_label = tk.Label(self.frame, text="Gender: " + self.character.gender, font=(gameFont, 20))
        self.gender_label.pack()

        self.level_label = tk.Label(self.frame, text="Skill Level: " + str(self.character.level), font=(gameFont, 20))
        self.level_label.pack()

        self.activities_label = tk.Label(self.frame, text= "Activities Completed: " + str(self.character.activities_completed), font=(gameFont, 20))
        self.activities_label.pack()

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

    with sqlite3.connect("assets/databases/SaveSlots.db") as db:
        c = db.cursor()

    # Character database
    c.execute('''CREATE TABLE IF NOT EXISTS Characters(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(30) NOT NULL, 
    gender VARCHAR(30) NOT NULL, 
    photolink VARCHAR(200), 
    daynumber INT NOT NULL, 
    skilllevel INT NOT NULL, 
    experiencepoints INT NOT NULL, 
    intelligence FLOAT NOT NULL);''')
    db.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS Topic(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL);''')
    db.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS Feedback(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message VARCHAR(200) NOT NULL);''')
    db.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS Activity(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    type CHAR(30) NOT NULL,
    characterid INT NOT NULL,
    completed BOOLEAN NOT NULL,
    grade FLOAT,
    feedbackid INT,
    topiccode INT NOT NULL,
    FOREIGN KEY (characterid) REFERENCES Characters(id),
    FOREIGN KEY (feedbackid) REFERENCES Feedback(id),
    FOREIGN KEY (topiccode) REFERENCES Topic(id));''')

    """
    try:
        #insert feedback data here
    except:
        pass

    try:
        #insert activity-topic relationships here
    except:
        pass
    
    """

    db.close()


    global gameFont
    gameFont = set_game_font()

    main()
