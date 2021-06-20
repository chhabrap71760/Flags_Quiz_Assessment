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

        # Sets up child window
        self.easy_box = Toplevel()

        self.easy_box.protocol('WM_DELETE_WINDOW', partial(self.close_easy, partner))

        # Set up GUI Frame
        self.easy_frame = Frame(self.easy_box, bg=background_color)
        self.easy_frame.grid()

         # Set up Easy Mode heading (row 0)
        self.easy_heading = Label(self.easy_frame, text="Easy Mode",
                                 font="arial 20 bold", bg=background_color,
                                 padx=10, pady=10)
        self.easy_heading.grid(row=0, column=0,)

        # Rounds Text
        self.round_text = Label(self.easy_frame, text="Round 1", bg=background_color,
                                font="Arial 13 bold",
                               justify=LEFT, padx=10, pady=10)
        self.round_text.grid(row=2, column=0) 

        with open("country_flags.csv") as f: #  change variable name
            
            reader = csv.reader(f)
            flag_list = list(reader)

        chosen_country = random.choice(flag_list)
        
        image_to_use = "flag_images\\" + chosen_country[-1]

        flag_image = PhotoImage(file=image_to_use)
       
        # Flag Image label
        self.picture_label = Label(self.easy_frame, text="?\n", font="Arial 21 bold",
                                  image=flag_image,
                                  padx=10, pady=10,)
        
        self.picture_label.photo = flag_image
        self.picture_label.grid(row=1, column=0, padx=30)

        self.picture_label.config(image=flag_image)
        self.picture_label.photo = flag_image

        list_of_countries = []
        
        for item in range(0,3):
            options = random.choice(flag_list)
            country_option = []
            country_option = options[0]
            #print(country_option)
            list_of_countries.append(country_option)
        
        flag_answer = chosen_country[0]
        #print(flag_answer)

        list_of_countries.append(flag_answer)

        print(list_of_countries)

        random.shuffle(list_of_countries)
        print(list_of_countries)

    # Mutliple choices frame
        self.multiple_choices = Frame(self.easy_frame, bg=background_color)
        self.multiple_choices.grid(row=3, pady=15)

        self.country_1 = Button(self.multiple_choices, text = list_of_countries[0],
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=15)
        self.country_1.grid(row=3, column=0, padx=5, pady=5)

        self.country_2 = Button(self.multiple_choices, text = list_of_countries[1],
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=15)
        self.country_2.grid(row=3, column=1, padx=5, pady=5)

        self.country_3 = Button(self.multiple_choices, text = list_of_countries[2],
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=15)
        self.country_3.grid(row=4, column=0, padx=5, pady=5)

        self.country_4 = Button(self.multiple_choices, text = list_of_countries[3],
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=15)
        self.country_4.grid(row=4, column=1, padx=5, pady=5)

        # Help/Stats Frame goes here
        self.help_stats_frame = Frame(self.easy_frame, bg=background_color)
        self.help_stats_frame.grid(row=5, pady=15)

        # Help and stats buttons go here (row 4)
        self.help_button = Button(self.help_stats_frame, text="Help",
                                  font="Arial 12 bold",
                                  bg="#66B2FF",
                                  borderwidth=2,
                                  width=8,
                                  command=self.help)
        self.help_button.grid(row=5, column=0, padx=10, pady=15)

        # Stats button goes here (row 4)
        self.stats_button = Button(self.help_stats_frame, text="Stats",
                                  font="Arial 12 bold",
                                  bg="#FF9933",
                                  borderwidth=2,
                                  width=8)
        self.stats_button.grid(row=5, column=1, padx=10, pady=15)


    def close_easy(self, partner):
        # Put help button back to normal
        partner.easy_button.config(state=NORMAL)
        self.easy_box.destroy()


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

        help_text = '''     \t     Greetings fellow user... Welcome aboard to the flags of the  
                       world quiz where you get to build up your knowledge/skills in      \t    
                       recognising flags.  \t

                       In our Main Menu you can either click the Easy mode where you
                       get given mutliple choices to help you guess the flag or you 
                       could either click the Expert Mode where you will have           \t
                       to guess the flag yourself without any options but you will 
                       get the chance to view the capital city of that country as a hint
                       to help you out.

                       After playing a couple games you can click the stats button
                       and view your statistics of the rounds you've played. And if 
                       want you can also export it into a text file and save it onto 
                       your device so you can brag to your friends and family. 

                       Good Luck... :)
                    '''

        # Help Text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text, bg=background_color,
                                font="Arial 12",
                               justify=LEFT, padx=10, pady=10)
        self.help_text.grid(row=1, column=0)

         # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  bg="#CC0000", font="arial 12 bold", width=10,
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

