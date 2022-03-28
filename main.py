import tkinter as tk
from tkinter import messagebox, PhotoImage, StringVar
import platform
from random import random, choice, randint, uniform
import HelpPage
import GradeCalculator
import Submission_File
import CharacterCustomisation.cc
import Feedback_page
#from PIL import ImageTk, Image
import sqlite3
from math import floor
import testing.grade_calculator_tests
from os import remove


# Loads the help page screen
class UserGuide:
    def __init__(self, master):

        HelpPage.main()


# Class to represent an in-game character
class Character:
    def __init__(self, name="Default Character", avatar="assets/default_character.gif", gender="Other", intelligence=round(random(), 2), confidence=0.5, level=1, exp_points=0, activities_completed=0, topic_levels=[1, 1, 1, 1]):  # Default values included
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


# Class for the character creation screen
class CreateCharacter:
    def __init__(self, master, parent, mult):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.parent = parent
        self.mult = mult

        self.startGame = None
        self.app = None
        self.character = None
        self.profile_photo = None

        self.avatar_label = tk.Label(self.frame, text="Avatar:", font=(gameFont, int(15*self.mult)))
        self.avatar_label.grid(column=2, row=1)

        profile_image = tk.PhotoImage(file="assets/default_character.gif")

        self.profile_image = tk.Label(self.frame, image=profile_image)
        self.profile_image.image = profile_image
        self.profile_image.grid(column=2, row=2)

        self.change_avatar_button = tk.Button(self.frame, text="Customise", command=self.customise_avatar, font=(gameFont, int(15*self.mult)))
        self.change_avatar_button.grid(column=2, row=3)

        self.name_label = tk.Label(self.frame, text="Full Name:", font=(gameFont, int(15*self.mult)))
        self.name_label.grid(column=1, row=4)

        self.name_var = tk.StringVar()
        self.name_input = tk.Entry(self.frame, font=(gameFont, int(20*self.mult)), textvariable=self.name_var)
        self.name_input.grid(column=2, row=4)

        self.gender_label = tk.Label(self.frame, text="Gender:", font=(gameFont, int(15*self.mult)))
        self.gender_label.grid(column=1, row=5)

        self.gender_var = StringVar(self.frame)
        gender_options = ["Male", "Female", "Other"]
        self.gender_var.set(gender_options[2])

        self.gender_input = tk.OptionMenu(self.frame, self.gender_var, *gender_options)
        self.gender_input.grid(column=2, row=5)

        tk.Label(self.frame).grid(column=2, row=6)

        self.save_character_button = tk.Button(self.frame, text="Done", command=self.save_character, font=(gameFont, int(20*self.mult)))
        self.save_character_button.grid(column=2, row=7)

        self.avatar = profile_image

        self.frame.pack()

    def customise_avatar(self):

        CharacterCustomisation.cc.run()
        self.profile_photo = CharacterCustomisation.cc.profile_image_location

        profile_image = tk.PhotoImage(file=self.profile_photo)
        self.profile_image = tk.Label(self.frame, image=profile_image)  # THIS HAS BEEN REPLACED BY THE CUSTOM PICTURE
        self.profile_image.image = profile_image
        self.profile_image.grid(column=2, row=2)

    # Function to save character to the database
    # Doesn't allow names over 20 characters in length
    def save_character(self):
        if len(self.name_var.get()) > 20:
            tk.messagebox.showinfo("Warning", message="Character name cannot exceed 20 characters.")
        else:
            # save the character into the database
            self.character = Character(self.name_var.get(), self.profile_photo, self.gender_var.get())  # THIS WORKS 12/02
            with sqlite3.connect("assets/databases/SaveSlots.db") as db:
                c = db.cursor()
            c.execute('''INSERT INTO Characters (name, gender, photolink, daynumber, skilllevel, experiencepoints, intelligence, confidence)
                              VALUES(?, ?, ?, ?, ?, ?, ?, ?);''', (self.character.name, self.character.gender, self.profile_photo, 0, self.character.level, 0, self.character.intelligence, 0.5))
            db.commit()
            db.close()

            self.parent.start(self.character)
            self.done()

    def done(self):
        self.master.destroy()


# Class to represent the launcher or 'splash' screen.
class Launcher:
    # Launcher constructor method
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.name_to_load = "Test Character"
        self.mult = set_multiplier(self.master)

        self.start_button = tk.Button(self.frame, text="New Game", command=self.create_character, font=(gameFont, 50))
        self.start_button.pack()

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
        self.deleteSaves = None

        self.frame.pack()

    # Method to open the game window
    def start(self, character, time_limit=20, day_num=1):
        self.startGame = tk.Toplevel(self.master)
        self.startGame.geometry(set_screen_size(self.master))
        self.startGame.title("Ungrading Simulator")
        self.startGame.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = UngradingSimulator(self.startGame, self, character, time_limit, day_num)

    def create_character(self):
        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute("SELECT * FROM Characters")
        result = c.fetchall()
        if len(result) >= 10:
            tk.messagebox.showinfo("Warning", message="You cannot exceed 10 save slots. Please delete a save to continue")
        else:
            self.createCharacter = tk.Toplevel(self.master)
            self.createCharacter.geometry("764x480")
            self.createCharacter.iconphoto(False, tk.PhotoImage(file='app_icon.png'))
            self.createCharacter.title("Create Character")
            self.app = CreateCharacter(self.createCharacter, self, set_multiplier(self.master))

    # Method to open options window
    def options(self):
        self.optionsScreen = tk.Toplevel(self.master)
        self.optionsScreen.geometry("500x700")
        self.optionsScreen.title("Options")
        self.optionsScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = OptionsScreen(self.optionsScreen)

    # Method to load a game from a selected save file
    def load_game(self, g_name):

        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute("SELECT * FROM Characters WHERE name = ?", (g_name,))
        result = c.fetchall()[0]

        l_name = result[1]
        l_avatar = result[3]
        l_gender = result[2]
        l_intelligence = result[7]
        l_confidence = result[8]
        l_level = result[5]
        l_exp = result[6]

        l_time_limit = 20
        l_day_num = result[4]

        # Number of activities can be determined by how much confidence has increased
        l_activities_completed = int(abs(((0.5 - l_confidence) / 0.05)))

        # Placeholder values (waiting on other user story)
        l_topic_levels = [4, 5, 3, 1]

        loaded_character = Character(l_name, l_avatar, l_gender, l_intelligence, l_confidence, l_level, l_exp, l_activities_completed, l_topic_levels)

        self.start(loaded_character, l_time_limit, l_day_num)

    # Opens the 'load game' screen
    def load_screen(self):
        self.loadScreen = tk.Toplevel(self.master)
        self.loadScreen.geometry("1100x720")
        self.loadScreen.title("Load Game")
        self.loadScreen.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon
        self.app = LoadScreen(self.loadScreen, self)

    def delete_saves(self):
        self.deleteSaves = tk.Toplevel(self.master)
        self.deleteSaves.geometry("1000x600")
        self.deleteSaves.title("Delete Save(s)")
        self.deleteSaves.iconphoto(False, tk.PhotoImage(file='app_icon.png'))
        self.app = DeleteSaves(self.deleteSaves, self)


# Class for the save slot deletion screen
# Allows the user to delete all or individual save slots
class DeleteSaves:
    def __init__(self, master, parent):
        self.master = master
        self.parent = parent
        self.frame = tk.Frame(self.master)

        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute("SELECT * FROM Characters")
        result = c.fetchall()

        # Displays all save files
        for i in range(0, len(result)):
            tk.Label(self.frame, text="Save " + str(result[i][0]) + ": " + result[i][1] + " (Level " + str(result[i][5]) + ") - Day " + str(result[i][4]), font=(gameFont, 30)).grid(column=0, row=i, padx=25, sticky="w", columnspan=3)
        tk.Label(self.frame, text="", font=(gameFont, 50)).grid(column=0, row=i+1)

        # Creates drop down containing all save files
        self.save_var = StringVar(self.frame)
        save_list = ['All']
        for i in range(len(result)):
            save_list.append("Save "+ str(result[i][0]))
        self.save_var.set(save_list[1])
        self.save_input = tk.OptionMenu(self.frame, self.save_var, *save_list)
        self.save_input.config(font=(gameFont, 30))
        menu = self.master.nametowidget(self.save_input.menuname)
        menu.config(font=(gameFont, 30))
        self.save_input.grid(column=0, row=i+1)

        # Button to delete individual or all save slots
        self.delete_save_button = tk.Button(self.frame, font=(gameFont, 30), command=lambda: self.delete_save(self.save_var.get()), text="Delete")
        self.delete_save_button.grid(column=1, row=i+1, sticky='w')

        self.back_button = tk.Button(self.frame, font=(gameFont, 30), command=self.back, text="Back")
        self.back_button.grid(column=2, row=i+1)

        self.frame.grid(row=0, column=0, sticky="nsew")

    # Function to delete all or individual save slots
    def delete_save(self, save):

        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()

        # If 'All' is selected, all records are deleted
        # Deletes the file then sets up the db again to reset auto-increment field
        if save == 'All':
            remove("assets/databases/SaveSlots.db")
            db_setup()

        # Deletes specific save slot
        else:
            c.execute("DELETE FROM Characters WHERE id = ?", (int(save[5:]),))
            db.commit()
            db.close()

        self.back()

    # Function to go back to the load game screen
    def back(self):
        self.master.destroy()
        self.parent.load_screen()


# Class for the load game screen
# Allows the user to choose an existing save file and continue
class LoadScreen:
    def __init__(self, master, parent):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.parent = parent
        self.save_list = None
        self.deleteScreen = None
        self.app = None

        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute("SELECT * FROM Characters")
        result = c.fetchall()

        if len(result) == 0:
            tk.Label(self.frame, text="There are no saved games.", font=(gameFont, 30)).grid(column=0, row=0, padx=250)
            tk.Label(self.frame, text="", font=(gameFont, 10)).grid(column=0, row=1, padx=250)
            tk.Button(self.frame, text="Back", font=(gameFont, 30), command=self.done).grid(column=0, row=2, padx=250)

        else:
            for i in range(0, len(result)):
                tk.Label(self.frame, text="Save " + str(result[i][0]) + ": " + result[i][1] + " (Level " + str(result[i][5]) + ") - Day " + str(result[i][4]), font=(gameFont, 30)).grid(column=0, row=i, padx=25, sticky="w")
                tk.Button(self.frame, text="Load", command=lambda: self.load_character(result[i][1]), font=(gameFont, "30")).grid(column=1, row=i)
            tk.Label(self.frame, text="", font=(gameFont, 10)).grid(column=0, row=i+1)
            tk.Button(self.frame, text="Delete Save(s)", font=(gameFont, 35), command=self.delete_saves).grid(column=0, row=i + 2)
            tk.Button(self.frame, text="Back", font=(gameFont, 35), command=self.done).grid(column=1, row=i+2)

        self.frame.grid(row=0, column=0, sticky="nsew")

    def load_character(self, slot_name):

        self.master.destroy()
        self.parent.load_game(slot_name)

    def done(self):
        self.master.destroy()

    def delete_saves(self):
        self.master.destroy()
        self.parent.delete_saves()


# The game window/class
class UngradingSimulator:
    # Constructor method
    def __init__(self, master, parent, character, time_limit=20, day_num=1):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.character = character
        self.time_limit = time_limit
        self.day_num = day_num
        self.parent = parent
        self.things_done = 0

        self.testEventButton = tk.Button(self.frame, text="Test Event", command=self.event, font=(gameFont, int(15*self.parent.mult)))
        # self.testEventButton.grid(row=1, column=8)

        self.level_up_button = tk.Button(self.frame, text="Level Up test", command=self.level_up, font=(gameFont, int(15*mult)))
        # self.level_up_button.grid(row=2, column=8)

        self.view_character_button = tk.Button(self.frame, text="View Profile", command=self.view_character, font=(gameFont, int(30*mult)))
        self.view_character_button.grid(column=0, row=0, padx=70)

        self.user_guide_button = tk.Button(self.frame, text="User Guide", command=self.user_guide, font=(gameFont, int(30*mult)))
        self.user_guide_button.grid(column=0, row=1, padx=70)

        self.user_guide_button = tk.Button(self.frame, text="Feedback", command=self.feedback, font=(gameFont, int(30*mult)))
        self.user_guide_button.grid(column=0, row=2, padx=90)

        scale_mult = int(floor(mult*10))

        display_file = tk.PhotoImage(file="assets/black_image.gif")
        zoom_display = display_file.zoom(scale_mult, scale_mult)
        display = zoom_display.subsample(9, 11)
        self.display = tk.Label(self.frame, image=display)
        self.display.image = display
        self.display.grid(row=0, column=2, rowspan=4, columnspan=6)

        tk.Label(self.frame, text=" ", font=(gameFont, 40)).grid(column=0, row=7, columnspan=10)

        self.study_button= tk.Button(self.frame, text="Study", command=self.study, font=(gameFont, int(35*mult)))
        self.study_button.grid(column=0, row=8)

        self.activity_button=tk.Button(self.frame, text="Complete Activities", command=self.activities, font=(gameFont, int(35*mult)))
        self.activity_button.grid(column=2, row=8)

        tk.Label(self.frame, text="    ", font=(gameFont, int(40*mult))).grid(column=3, row=8, rowspan=1)

        self.submit_task_button = tk.Button(self.frame, text="Submit Activities", command=self.file_submission, font=(gameFont, int(35*mult)))
        self.submit_task_button.grid(column=4, row=8)

        tk.Label(self.frame, text="    ", font=(gameFont, int(40*mult))).grid(column=0, row=9, columnspan=10)

        self.save_exit_button = tk.Button(self.frame, text="Save and Exit", command=self.save_exit, font=(gameFont, int(30*mult)))
        self.save_exit_button.grid(column=0, row=10)

        self.next_day_button= tk.Button(self.frame, text="Next day", command=self.next_day, font=(gameFont, int(35*mult)))
        self.next_day_button.grid(column=8, row=10)

        self.days_count_string="Day number: "+str(self.day_num)
        self.day_num_label= tk.Label(self.frame, text=self.days_count_string, font=(gameFont, int(35*mult)))
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

    # method that when triggered will increase user_level by 1 and notify the user they have levelled up
    def level_up(self):
        if self.character.level == 9:
            self.level_up_string = "Well done, you have reached max level! You are now level " + str(self.character.level+1)
            self.character.level += 1
            self.character.exp_points-=100
            self.level_up_box = tk.messagebox.showinfo("You have levelled up!", message=self.level_up_string)
        elif self.character.level == 10:
            self.character.exp_points -= 100
        else:
            self.character.level += 1
            self.character.exp_points -= 100
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
        if self.day_num != 20:
            self.day_num+=1
            self.days_count_string = "Day number: " + str(self.day_num)
            self.things_done = 0
            self.day_num_label.destroy()
            self.day_num_label = tk.Label(self.frame, text=self.days_count_string, font=(gameFont, 35))
            self.day_num_label.grid(row=0, column=8, sticky='n')
            self.autosave()

        if self.day_num %5==0:
            intell_inc=round(uniform(1, 4), 2)
            self.character.intelligence+=intell_inc

        if self.day_num == self.time_limit:
            self.time_limit_box= tk.messagebox.showinfo("Course is finished", message="It has been " + str(self.time_limit) + " days and your Ungrading course has been completed. Press OK to see your score")
            self.end_of_sim_scores()

    # Simulates the character studying in-game
    # Increases xp and number of activities done in the day
    # If over 4 activities are attempted, a warning appears and stops the user
    def study(self):
        if self.things_done < 4:
            self.character.exp_points+=50
            self.things_done += 1
            if self.character.exp_points>=100:
                self.level_up()
        else:
            tk.messagebox.showinfo("Daily Limit", message="You can't attempt more than 4 activities a day.")
        self.autosave()

    # Simulates the character attempting activities in-game
    # Increases xp, confidence (awareness), intelligence and number of activities done in the day
    # If over 4 activities are attempted, a warning appears and stops the user
    def activities(self):
        if self.things_done < 4:
            self.things_done += 1
            self.character.exp_points += 20
            self.character.confidence += 0.05
            intell_inc = round(random(), 2)
            self.character.intelligence += intell_inc
            if self.character.exp_points >= 100:
                self.level_up()

            with sqlite3.connect("assets/databases/SaveSlots.db") as db:
                c = db.cursor()
            # add the activity to the database here, cannot complete Feedback_page without it
            db.commit()
            db.close()
            self.character.activities_completed += 1

        else:
            tk.messagebox.showinfo("Daily Limit", message="You can't attempt more than 4 activities a day.")
        self.autosave()

    def end_of_sim_scores(self):
        self.master.destroy()

        GradeCalculator.run(self.character.avatar, self.character.level, self.character.confidence)

    def file_submission(self):
        Submission_File.run()

    def feedback(self):
        Feedback_page.run()

    def save_exit(self):
        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()
        c.execute('''UPDATE Characters SET daynumber = ?, skilllevel = ?, experiencepoints = ?, intelligence = ?, confidence = ? WHERE name = ?''', (
        self.day_num, self.character.level, self.character.exp_points, self.character.intelligence, self.character.confidence, self.character.name))

        db.commit()
        db.close()

        self.master.destroy()

    def autosave(self):
        with sqlite3.connect("assets/databases/SaveSlots.db") as db:
            c = db.cursor()

        c.execute('''UPDATE Characters SET daynumber = ?, skilllevel = ?, experiencepoints = ?, intelligence = ?, confidence = ? WHERE name = ?''',
        (self.day_num, self.character.level, self.character.exp_points, self.character.intelligence, self.character.confidence, self.character.name))

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
    dimensions = set_screen_size(root)
    app = Launcher(root)
    root.geometry(dimensions)
    root.title("Splash Screen")
    root.option_add('*Dialog.msg.font', 'Helvetica 15')  # Sets dialogue message font
    root.iconphoto(False, tk.PhotoImage(file='app_icon.png'))  # Sets window icon

    root.mainloop()


def db_setup():
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
    intelligence FLOAT NOT NULL,
    confidence FLOAT NOT NULL);''')
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

    try:
        # Entering feedback information. Will only run once so database is created with all relevant data
        c.execute(
            "INSERT INTO Feedback (id, message) VALUES (1, 'Student clearly demonstrates their understanding of the learning objectives and has missed no details. Job well done!');")
        db.commit()
        c.execute(
            "INSERT INTO Feedback (message) VALUES ('Student has completed the activity well and shows a firm understanding of their work. Watch out for spelling and grammar.');")
        db.commit()
        c.execute(
            "INSERT INTO Feedback (message) VALUES ('Student has missed a few questions but the work they have completed is correct and demonstrates their learning of the recent lessons.');")
        db.commit()
        c.execute(
            "INSERT INTO Feedback (message) VALUES ('Student has completed all of the questions however has not explained their reasoning. Try to include how you came to your understandings so you can demonstrate your learning.');")
        db.commit()
        c.execute(
            "INSERT INTO Feedback (message) VALUES ('Student has definitely put in extra time to learn more about this topic. You have clearly understood the learning objectives for this!');")
        db.commit()
        c.execute(
            "INSERT INTO Feedback (message) VALUES ('Student has mostly understood the topic, but is uneasy on a few points. I would recommend some extra study on this topic to develop your understanding further.');")
        db.commit()
        c.execute(
            "INSERT INTO Feedback (message) VALUES ('Student should try to answer all the questions for this exercise. Do not be afraid to ask for help when learning about this topic.');")
        db.commit()
    except:
        pass
    """
    try:
        #insert activity-topic relationships here
    except:
        pass

    """
    db.close()


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


# Method to set the screen size of the main window
def set_screen_size(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    return str(screen_width)+"x"+str(screen_height)


# Sets multiplier global to scale widgets and text according to screen size
def set_multiplier(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    global mult
    mult = ((screen_width / 1920) + (screen_height / 1080)) / 2

    return mult


# Testing function for the grade calculator
def grade_calculator_testing():
    testing.grade_calculator_tests.test_1()
    testing.grade_calculator_tests.test_2()
    testing.grade_calculator_tests.test_3()
    testing.grade_calculator_tests.test_4()
    testing.grade_calculator_tests.test_5()


# Runs main method
if __name__ == "__main__":

    db_setup()

    global gameFont
    gameFont = set_game_font()

    main()

    #grade_calculator_testing()
