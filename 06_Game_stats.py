# Component 6
# Game Statistics GUI

from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random
import csv

# Main Menu Class goes here...
class Main:
    def __init__(self):

      #  self.which_mode = StringVar()
  

        # Formatting Variables
        background_color = "#FFE6CC"

        # Main Menu Frame
        self.main_frame = Frame(bg=background_color,
                                padx=10, pady=10)
        self.main_frame.grid()


        # Main Menu Heading 1 (row 0_
        self.main_label = Label(self.main_frame, text="Flag Quiz Game",
                            font="Arial 12 bold",
                            bg=background_color)
        self.main_label.grid(row=0)

        # Easy Button goes here...
        self.easy_button = Button(self.main_frame, text="Easy Mode",
                                  font="Arial 12 bold",
                                  bg="#FF9999",
                                  borderwidth=2) 
                                # command=lambda do be added in future components
        self.easy_button.grid(row=1, column=0,)
      #  self.which_mode.set(self.easy_button)

        # Expert button goes here...
        self.expert_button = Button(self.main_frame, text="Expert Mode",
                                    font="Arial 12 bold",
                                    width=9,
                                    bg="#FF0000",
                                    borderwidth=2)
                                    # command=lambda do be added in future components
        self.expert_button.grid(row=1, column=1)

        # stats button goes here... (row 5)
        self.stats_button = Button(self.main_frame, text="Stats",
                                  font="Arial 12 bold",
                                  bg="#FF9933",
                                  borderwidth=2,
                                  command=self.gamestats)
        self.stats_button.grid(row=5, column=0, columnspan=4, pady=10)  

       # mode_selected = self.which_mode.get()
       # print(mode_selected)
        
    def gamestats(self):
        Gamestats(self)
# Game Stats Class goes here...
class Gamestats:
    def __init__(self, partner):

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # disable stats button
        partner.stats_button.config(state=DISABLED)

        # Sets up child window (ie: stats box)
        self.stats_box = Toplevel()

        # If user press cross at top, closes help and 'releases' help button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box, bg=background_color)
        self.stats_frame.grid()

        # Set up Stats heading (row 0)
        self.stats_heading = Label(self.stats_frame, text="Game Statistics",
                                    font="arial 20 bold", bg=background_color,
                                    padx=10)
        self.stats_heading.grid(row=0, column=0,)

        stats_text = '''Here are your game statistics. Please use the Export button to 
access the results of each round that you played.'''


        # Game statistics Instructions
        self.stats_instructions = Label(self.stats_frame,
                                        bg=background_color,
                                        text=stats_text, 
                                        font="arial 10 bold",
                                        fg="#000000",
                                        justify=LEFT,
                                        padx=10)
        self.stats_instructions.grid(row=1, column=0)

        # Stats Details Frame goes here...
        self.details_frame = Frame(self.stats_Frame)
        self.details_frame.grid(row=2)

        # Mode used label (row 2) (need to be added)


        # Correct Answers / Incorrect Answers
        self.correct_incorrect
        


    def close_stats(self, partner):
        # Put help button back to normal
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz Game")
    something = Main()  
    root.mainloop()
