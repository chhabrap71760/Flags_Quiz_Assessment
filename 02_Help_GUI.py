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

        # Main Menu Heading 1 (row 0_
        self.main_label = Label(self.main_frame, text="Flag Quiz Game",
                            font="Arial 12 bold",
                            bg=background_color)
        self.main_label.grid(row=0)

        # Help/ Instructions buttons go here... (row 5)
        self.help_button = Button(self.main_frame, text="Help/Instructions",
                                  font="Arial 12 bold",
                                  bg="#66B2FF",
                                  borderwidth=2,
                                  command=self.help)
        self.help_button.grid(row=5, column=0)  

    def help(self):
        Help(self)

class Help:

    def __init__(self, partner):

        background_color = "#FFE6CC"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background_color)
        self.help_frame.grid()

         # Set up Help heading (row 0)
        self.help_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 20 bold", bg=background_color)
        self.help_heading.grid(row=0)

        help_text = '''  \t      Greetings fellow user... Welcome aboard to the flags of the  
                       world quiz where you get to build up your knowledge/skills in          \t
                       recognising flags.   \t

                       In our Main Menu you can either click the Easy mode where            \t
                       you will be given options when answering the questions; Or           \t
                       you could either click the Expert Mode where you will have       
                       to guess the flag yourself without any options but you will 
                       get the chance to view hints to help you out.

                       After playing a couple games you can click the stats button
                       and view your statistics of the rounds you've played. And if 
                       want you can also export it into a text file and save it onto 
                       your device so you can brag to your friends and family. 

                       Good Luck... :)
                    '''

        # Help Text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text, bg=background_color,
                               justify=LEFT, padx=10, pady=10)
        self.help_text.grid(row=1, column=0,)

         # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  bg="#CC0000", font="arial 10 bold",
                            command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz Game")
    something = Main()
    root.mainloop()
