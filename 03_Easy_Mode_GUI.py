from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random
import csv

country_flags = open("country_flags.csv")
read = csv.reader(country_flags)


class Main:
    def __init__(self):

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

        # easy mode button go here... (row 5)
        self.easy_button = Button(self.main_frame, text="Easy Mode",
                                  font="Arial 12 bold",
                                  bg="#FF9999",
                                  borderwidth=2,
                                  command=self.easy)
        self.easy_button.grid(row=5, column=0)  

    def easy(self):
        Easy(self)

class Easy:

    def __init__(self, partner):

        background_color = "#FFE6CC"

        # disable easy button
        partner.easy_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.easy_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.easy_box.protocol('WM_DELETE_WINDOW', partial(self.close_easy, partner))

        # Set up GUI Frame
        self.easy_frame = Frame(self.easy_box, bg=background_color)
        self.easy_frame.grid()

         # Set up Help heading (row 0)
        self.easy_heading = Label(self.easy_frame, text="Easy Mode",
                                 font="arial 20 bold", bg=background_color)
        self.easy_heading.grid(row=0)


    def easygame(): # change this name asap!!!
        countries = country_list()
        flags = flag_list()
        used = [False] * 200

        # Randomly generate the flag
        index = random.randint(0, 200)
        while used[index]:
            index = random.randint(0,200)
        used[index] = True
        alltrue = True
        for variable in range(0,200): # change variable name in due course
            if used[variable] == False:
                allTrue = False
            if alltrue:
                used = [False] * 200
            flag = flags[index]
            country = countries[flag]

            print("{}".format(flag))
            print("{}".format(country))


    # Generate country list
    def country_list():
        with open(country_flags, "countries") as country:
            list = csv.reader(country)
            Countries = []
            for row in list:
                Countries.append(row[0])
            return Countries

    # Generate flag list
    def flag_list():
       with open(country_flags, "flags") as flag:
           chosen_row = csv.reader(flag)
           flags = {}
           for row in chosen_row:
                k, v = row
                flags[k] = v
           return flags 

    def close_easy(self, partner):
        # Put help button back to normal
        partner.easy_button.config(state=NORMAL)
        self.easy_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz Game")
    something = Main()
    root.mainloop()

