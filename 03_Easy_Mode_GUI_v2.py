from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random
import csv


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

        # easy buttons go here... (row 5)
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

        easy_text = "What is this flag?"

        # Help Text (label, row 1)
        self.easy_text = Label(self.easy_frame, text=easy_text, bg=background_color,
                                font="Arial 10",
                               justify=LEFT, padx=10, pady=10)
        self.easy_text.grid(row=1, column=0) 

        
        with open("country_flags.csv") as f: #  change variable name
            
            reader = csv.reader(f)
            flag_list = list(reader)

        chosen_country = random.choice(flag_list)

        image_to_use = "flag_images\\" + chosen_country[-1]

        flag_image = PhotoImage(file=image_to_use)
       
        # Flag Image label
        self.picture_label = Label(self.easy_frame, text="?\n", font="Arial 21 bold",
                                  image=flag_image,
                                  padx=10, pady=10)
        
        self.picture_label.photo = flag_image
        self.picture_label.grid(row=0, column=0)

        self.picture_label.config(image=flag_image)
        self.picture_label.photo = flag_image

    def answer(self):

        with open("country_flags.csv") as f:

            reader = csv.reader(f)
            flag_list = list(reader)

        country_list = [flag_list,[0]]
        print(country_list)


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

