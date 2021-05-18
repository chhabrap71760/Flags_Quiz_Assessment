from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random


class Main:
    def __init__(self):

        # Formatting Variables
        background_color = "#FFE6CC"

        # Main Menu Frame
        self.main_frame = Frame(bg=background_color,
                                padx=10, pady=10)
        self.main_frame.grid()

        # Main Menu Heading 1 (row 0)
        self.main1_label = Label(self.main_frame, text="Welcome To The",
                            font="Arial 12 bold",
                            bg=background_color)
        self.main1_label.grid(row=0)

        # Main Menu Heading 2 (row 1)
        self.main2_label = Label(self.main_frame, text="Flags of The World ",
                            font="Arial 20 bold",
                            bg=background_color)
        self.main2_label.grid(row=1)

        # Main Menu Heading 3 (row 2)
        self.main3_label = Label(self.main_frame, text="Quiz ",
                            font="Arial 15 bold",
                            bg=background_color)
        self.main3_label.grid(row=2)
        
        # Easy & Expert Buttons go here... (row 4)
        self.easy_expert_frame = Frame(self.main_frame)
        self.easy_expert_frame.grid(row=4, pady=10)
        
        self.easy_button = Button(self.main_frame, text="Easy Mode",
                                  font="Arial 12 bold",
                                  bg="#FF9999") 
                                # command=lambda do be added in future components
        self.easy_button.grid(row=0, column=0)

        self.expert_button = Button(self.easy_expert_frame, text="Expert Mode",
                                    font="Arial 12 bold",
                                    width=9,
                                    bg="#FF0000")
                                    # command=lambda do be added in future components
        self.expert_button.grid(row=0, column=1)

        # Help/ Instructions buttons go here... (row 5)
        self.help_button = Button(self.easy_expert_frame, text="Help/Instructions",
                                  font="Arial 12 bold",
                                  bg="#66B2FF")
                                  # command=lambda do be added in future components
        self.help_button.grid(row=5, column=0)  

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz Game")
    something = Main()
    root.mainloop()


        