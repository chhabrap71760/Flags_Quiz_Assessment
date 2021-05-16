from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random


class Main:
    def __init__(self, partner):

        # GUI to get starting balance and stakes
        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid()

        # Main Menu Heading 1 (row 0)
        self.main1_label = Label(self.start_frame, text="Welcome To The",
                            font="Arial 12 bold")
        self.main1_label.grid(row=0)

        # Main Menu Heading 2 (row 1)
        self.main2_label = Label(self.start_frame, text="Flags of The World ",
                            font="Arial 20 bold")
        self.main2_label.grid(row=1)

        # Main Menu Heading 3 (row 2)
        self.main3_label = Label(self.start_frame, text="Flags of The World ",
                            font="Arial 15 bold")
        self.main3_label.grid(row=2)
        
        # Easy & Expert Buttons go here... (row 4)
        self.easy_expert_frame = Frame(self.main_frame)
        self.easy_expert_frame.grid(row=4, pady=10)

        self.easy_button = Button(self.help_export_frame, text="Easy Mode",
                                  font="Arial 12 bold",
                                  bg="#FF9999"


    

        