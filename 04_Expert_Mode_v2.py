# Component 4
# Expert Mode

from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random
import csv

# Main Menu Class goes here...
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

# Expert Class goes here...
class Expert:

    def __init__(self, partner):

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # Set capital and country as a stringvar so that it can be used in other functions
        self.correct_ans = StringVar()

        self.hint = StringVar()

        # disable expert button
        partner.expert_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.expert_box = Toplevel()

        self.expert_box.protocol('WM_DELETE_WINDOW', partial(self.close_expert, partner))

        # Set up GUI Frame
        self.expert_frame = Frame(self.expert_box, bg=background_color)
        self.expert_frame.grid()

         # Set up expert heading (row 0)
        self.expert_heading = Label(self.expert_frame, text="Expert Mode",
                                 font="arial 20 bold", bg=background_color,
                                 padx=10, pady=10)
        self.expert_heading.grid(row=0, column=0,)

        # expert Text (label, row 1)
        self.round_text = Label(self.expert_frame, text="Round 1", bg=background_color,
                                font="Arial 13 bold",
                               justify=LEFT, padx=10, pady=10)
        self.round_text.grid(row=2, column=0) 

        # set image to a question mark img just to get things started
        image_to_use = "question_mark2.gif"

        flag_image = PhotoImage(file=image_to_use)
       
        # Flag Image label
        self.picture_label = Label(self.expert_frame, text="?\n", font="Arial 21 bold",
                                  image=flag_image,
                                  padx=10, pady=10)
        
        self.picture_label.photo = flag_image
        self.picture_label.grid(row=1, column=0, padx=30)

        self.picture_label.config(image=flag_image)
        self.picture_label.photo = flag_image

        # Answer Entry Box frame goes here (row 3)
        self.entry_hint = Frame(self.expert_frame, bg=background_color)
        self.entry_hint.grid(row=3, pady=15)

        # Entry Box goes here (row 3)
        self.enter_answer = Entry(self.entry_hint,
                                  font="Arial 15 bold", width=13)
        self.enter_answer.grid(row=3, column=0)

        # Check Button goes here (row 3)
        self.check_button = Button(self.entry_hint, text="Check",
                                   font="Arial 12 bold",
                                   bg="#EA6B66",
                                   borderwidth=2,
                                   width=8,
                                   command=self.answer)
        self.check_button.grid(row=3, column=1)
        self.check_button.config(state=DISABLED)

        # Hint Button goes here (Row 3)
        self.hint_button = Button(self.entry_hint, text="Hint",
                                  font="Arial 12 bold",
                                  bg="#FFFF00",
                                  borderwidth=2,
                                  width=8,
                                  command=self.hints)
        self.hint_button.grid(row=3, column=2, padx=15)
        self.hint_button.config(state=DISABLED)

        # Incorrect feedback label (row 4)
        self.entry_error = Label(self.entry_hint, fg="maroon", bg = background_color,
                                 text="", font="Arial 12 bold")
        self.entry_error.grid(row=4, columnspan=2, pady=5)

        # Correct feedback label (Row 4)
        self.entry_correct = Label(self.entry_hint, fg="#00CC00", bg = background_color,
                                 text="", font="Arial 12 bold")
        self.entry_correct.grid(row=4, columnspan=3, rowspan=2, pady=5)

        # country label for printing the correct answer if user gets wrong
        self.correct_country = Label(self.entry_hint, fg="#000000", bg=background_color,
                                text="", font="Arial 12 bold")
        self.correct_country.grid(row=5, column=0, pady=5, padx=5)

        self.correct_country1 = Label(self.entry_hint, fg="#000000", bg=background_color,
                                text="", font="Arial 12 bold",)
        self.correct_country1.grid(row=5, column=1, pady=5, padx=5)

        # Hint label (row 6)
        self.hint_label = Label(self.entry_hint, fg="#000000", bg = background_color,
                                text="", font="Arial 12 bold")
        self.hint_label.grid(row=6, column=0, pady=5, padx=5)

        self.hint_label1 = Label(self.entry_hint, fg="#000000", bg = background_color,
                                text="", font="Arial 12 bold")
        self.hint_label1.grid(row=6, column=1, pady=5, padx=5)


        # Help/Stats Frame goes here
        self.help_stats_frame = Frame(self.expert_frame, bg=background_color)
        self.help_stats_frame.grid(row=5, pady=15)

        # Help and stats buttons go here (row 5)
        self.help_button = Button(self.help_stats_frame, text="Help",
                                  font="Arial 12 bold",
                                  bg="#66B2FF",
                                  borderwidth=2,
                                  width=8)
        self.help_button.grid(row=5, column=1, padx=5, pady=15)

        # Stats button goes here (row 5)
        self.stats_button = Button(self.help_stats_frame, text="Stats",
                                  font="Arial 12 bold",
                                  bg="#FF9933",
                                  borderwidth=2,
                                  width=8)
        self.stats_button.grid(row=5, column=2, padx=5, pady=15)

        # Help/Stats Frame goes here
        self.next_quit_frame = Frame(self.expert_frame, bg=background_color)
        self.next_quit_frame.grid(row=6, pady=10)
        
        # Next button goes here (row 6)
        self.next_button = Button(self.next_quit_frame, text="Next",
                                  font="Arial 12 bold",
                                  bg="#EA6B66",
                                  borderwidth=2,
                                  width=10,
                                  command=self.next)
        self.next_button.grid(row=6, column=1, padx=10, sticky="e")

        # Quit Button goes here (row 6)
        self.quit = Button(self.next_quit_frame, text="Quit",
                           bg="#CC0000", font="Arial 12 bold", 
                           borderwidth=2, width=10,
                           command=partial(self.close_expert, partner))
        self.quit.grid(row=6, column=2, padx=10)


# Next function for when user wants to go to next question
# This code hsa the main generation for flag and country
# Where it accesses it from the csv file
    
    def next(self):
            
        # Multiple button and label Disables for reducing a mess in the GUI
        self.hint_button.config(state=NORMAL)
        self.check_button.config(state=NORMAL)
        self.hint_label.config(text=" ")
        self.hint_label1.config(text=" ")
        self.entry_error.config(text=" ")
        self.entry_correct.config(text=" ")
        self.correct_country.config(text=" ")
        self.correct_country1.config(text=" ")
        
        # Here is where the code accesses the csv file
        with open("country_flags.csv") as f: 
            
            reader = csv.reader(f)
            flag_list = list(reader)

        # randomly generate a list from the csv file
        chosen_country = random.choice(flag_list)
        
        # Links the answer with the previously set StrVar
        self.correct_ans.set(chosen_country[0])
       
       # links the capital city with the previously set StrVar
        self.hint.set(chosen_country[1])

        # chooses the flag out of the randomly generated list
        image_to_use = "flag_images\\" + chosen_country[-1]
        flag_image = PhotoImage(file=image_to_use)

        # flag image configuration
        self.picture_label.config(image=flag_image)
        self.picture_label.photo = flag_image

        self.entry_error.config(text="")

# answer function for checking user input and sending feedback
    def answer(self):

        # Multiple button and label Disables for reducing a mess in the GUI
        self.hint_label.config(text=" ")
        self.hint_button.config(state=DISABLED)
        self.hint_label1.config(text=" ")
        self.check_button.config(state=DISABLED)
        answer_entered = self.enter_answer.get()
        
        # takes in the correct_answer StrVar from the 'next' function
        chosen_country = self.correct_ans.get()
        
        # Correct feedback randomly generates 
        correct = ["Bravo! you got it right", "Awesome keep it up", "Excellent Work",
         "You're Great", "Outstanding"]

        # Incorrect feedback randomly generates
        incorrect = ["C'mon, you can do better than that", "Nope, try harder on the next one",
        "oops, you messed up there"]

        correct = random.choice(correct)
        incorrect = random.choice(incorrect)

        has_errors = "no"
 
    # If statement for checking user input and sending a valid response
        
        # If user gets it right
        if answer_entered == chosen_country:                
            has_errors = "no"
            correct_feedback = correct
            self.entry_error.config(text=" ")

        # if user does not type anything
        elif answer_entered == "":
            has_errors = "blank"
            error_feedback="Please enter a Country"
            self.check_button.config(state=NORMAL)
            self.hint_button.config(state=NORMAL)

        # If user gets it wrong
        elif answer_entered != chosen_country:
            has_errors = "yes"
            error_feedback = incorrect
            correct_country = chosen_country

        if has_errors == "yes":
            self.entry_error.config(text=error_feedback)
            self.correct_country.config(text="Answer:")
            self.correct_country1.config(text=correct_country)

        if has_errors == "blank":
            self.entry_error.config(text=error_feedback)

        elif has_errors == "no":
            self.entry_correct.config(text=correct_feedback)


# Hints function goes here..
# very short code because hint is set to a StrVar in the beginning
# This makes it conveniant and saves a lot of lines of code
    def hints(self):

        # Retrieves the StrVar value
        get_hint = self.hint.get()

        self.hint_label.config(text="Capital City:")
        self.hint_label1.config(text=get_hint)

    # For when user decides to click quit 
    def close_expert(self, partner):
        partner.expert_button.config(state=NORMAL)
        self.expert_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz Game")
    something = Main()  
    root.mainloop()

