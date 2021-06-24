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

        # expert button goes here... (row 5)
        self.expert_button = Button(self.main_frame, text="Expert Mode",
                                  font="Arial 12 bold",
                                  bg="#FF0000",
                                  borderwidth=2,
                                  command=self.expert)
        self.expert_button.grid(row=5, column=0)  


    def expert(self):
        Expert(self)

class Expert:

    def __init__(self, partner):

        background_color = "#FFE6CC"

        self.correct_ans = StringVar()

        # disable expert button
        partner.expert_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.expert_box = Toplevel()

        self.expert_box.protocol('WM_DELETE_WINDOW', partial(self.close_expert, partner))

        # Set up GUI Frame
        self.expert_frame = Frame(self.expert_box, bg=background_color)
        self.expert_frame.grid()

         # Set up Help heading (row 0)
        self.expert_heading = Label(self.expert_frame, text="Expert Mode",
                                 font="arial 20 bold", bg=background_color,
                                 padx=10, pady=10)
        self.expert_heading.grid(row=0, column=0,)

        # Help Text (label, row 1)
        self.expert_text = Label(self.expert_frame, text="Round 1", bg=background_color,
                                font="Arial 13 bold",
                               justify=LEFT, padx=10, pady=10)
        self.expert_text.grid(row=2, column=0) 

        # with open("country_flags.csv") as f: #  change variable name
            
        #     reader = csv.reader(f)
        #     flag_list = list(reader)

        # chosen_country = random.choice(flag_list)
        
        # image_to_use = "flag_images\\" + chosen_country[-1]
        image_to_use = "flag_images\\NZ-flag.gif"


        flag_image = PhotoImage(file=image_to_use)
       
        # Flag Image label
        self.picture_label = Label(self.expert_frame, text="?\n", font="Arial 21 bold",
                                  image=flag_image,
                                  padx=10, pady=10)
        
        self.picture_label.photo = flag_image
        self.picture_label.grid(row=1, column=0, padx=30)

        self.picture_label.config(image=flag_image)
        self.picture_label.photo = flag_image

        # list_of_countries = []
        
        # for item in range(0,3):
        #     options = random.choice(flag_list)
        #     country_option = []
        #     country_option = options[0]
        #     #print(country_option)
        #     list_of_countries.append(country_option)
        
        # flag_answer = chosen_country[0]
        # print(flag_answer)

        # list_of_countries.append(flag_answer)

        # print(list_of_countries)

        # random.shuffle(list_of_countries)
        # print(list_of_countries)

        # Answer Entry Box frame goes here (row 3)
        self.entry_hint = Frame(self.expert_frame, bg=background_color)
        self.entry_hint.grid(row=3, pady=15)

        # Entry Box goes here (row 3)
        self.enter_answer = Entry(self.entry_hint,
                                  font="Arial 15 bold", width=13)
        self.enter_answer.grid(row=3, column=0)

        # Enter Button goes here (row 3)
        self.entry_button = Button(self.entry_hint, text="Check",
                                   font="Arial 12 bold",
                                   bg="#EA6B66",
                                   borderwidth=2,
                                   width=8,
                                   command=self.answer)
        self.entry_button.grid(row=3, column=1)

        # Hint Button goes here (Row 3)
        self.hint_button = Button(self.entry_hint, text="Hint",
                                  font="Arial 12 bold",
                                  bg="#FFFF00",
                                  borderwidth=2,
                                  width=8,
                                  #command hint)
        )
        self.hint_button.grid(row=3, column=2, padx=15)

        self.entry_error = Label(self.entry_hint, fg="maroon", bg = background_color,
                                 text="", font="Arial 12 bold", wrap=275,
                                 justify=LEFT)
        self.entry_error.grid(row=4, columnspan=2, pady=5)



        # Help/Stats Frame goes here
        self.help_stats_frame = Frame(self.expert_frame, bg=background_color)
        self.help_stats_frame.grid(row=5, pady=15)

        # Help and stats buttons go here (row 4)
        self.help_button = Button(self.help_stats_frame, text="Help",
                                  font="Arial 12 bold",
                                  bg="#66B2FF",
                                  borderwidth=2,
                                  width=8)
        self.help_button.grid(row=5, column=0, padx=10, pady=15)

        # Stats button goes here (row 4)
        self.stats_button = Button(self.help_stats_frame, text="Stats",
                                  font="Arial 12 bold",
                                  bg="#FF9933",
                                  borderwidth=2,
                                  width=8)
        self.stats_button.grid(row=5, column=1, padx=10, pady=15)

        # Next button goes here (row 4)
        self.next_button = Button(self.help_stats_frame, text="Next",
                                  font="Arial 12 bold",
                                  bg="#EA6B66",
                                  borderwidth=2,
                                  width=8,
                                  command=self.next)
        self.next_button.grid(row=6, column=2, padx=10, pady=15, sticky="e")

    def next(self):
        with open("country_flags.csv") as f: #  change variable name
            
            reader = csv.reader(f)
            flag_list = list(reader)

        chosen_country = random.choice(flag_list)
        self.correct_ans.set(chosen_country)

        image_to_use = "flag_images\\" + chosen_country[-1]
        flag_image = PhotoImage(file=image_to_use)

        self.picture_label.config(image=flag_image)
        self.picture_label.photo = flag_image

    def answer(self):
        # with open("country_flags.csv") as f:

        #     reader = csv.reader(f)
        #     flag_list = list(reader)

        # chosen_country = random.choice(flag_list)

        # flag_answer = chosen_country[0]
        # print(chosen_country)

        chosen_country = self.correct_ans.get()
        #print(chosen_country)


        correct = ["Bravo! you got it right", "Awesome keep it up", "Excellent Work",
         "You're Great", "Outstanding"]

        incorrect = ["C'mon, you can do better than that", "Nope, try harder on the next one",
        "oops, you messed up there"]

        correct = random.choice(correct)
        incorrect = random.choice(incorrect)

       # self.answer_entered = self.enter_answer.get()

        has_errors = "no"

        # Change error back to blank
        self.entry_error.config(text="")

        try:
            answer_entered = str(self.correct_ans.get())


            if answer_entered == chosen_country:                
                has_errors = "no"
                correct_feedback = correct

            elif answer_entered != chosen_country:
                has_errors = "yes"
                error_feedback = incorrect


        except ValueError:
            has_errors="yes"
            error_feedback = "Please enter the country name"

        if has_errors == "yes":
            self.entry_error.config(text=error_feedback)
        
        elif has_errors == "no":
            self.entry_error.config(text=correct_feedback)

    def close_expert(self, partner):
        partner.expert_button.config(state=NORMAL)
        self.expert_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz Game")
    something = Main()  
    root.mainloop()

