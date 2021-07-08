# Comonent 3
# Easy Mode

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

        # easy buttons go here... (row 5)
        self.easy_button = Button(self.main_frame, text="Easy Mode",
                                  font="Arial 12 bold",
                                  bg="#FF9999",
                                  borderwidth=2,
                                  command=self.easy)
        self.easy_button.grid(row=5, column=0)  

    def easy(self):
        Easy(self)

# Easy Class goes here...
class Easy:

    def __init__(self, partner):

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # Set country as a stringvar so that it can be used in other functions
        self.correct_ans = StringVar()

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

        # set image to a question mark img just to get things started
        image_to_use = "question_mark2.gif"

        flag_image = PhotoImage(file=image_to_use)

        # Flag Image label
        self.picture_label = Label(self.easy_frame, text="?\n", font="Arial 21 bold",
                                  image=flag_image,
                                  padx=10, pady=10,)
        
        self.picture_label.photo = flag_image
        self.picture_label.grid(row=1, column=0, padx=30)

        self.picture_label.config(image=flag_image)
        self.picture_label.photo = flag_image


    # Mutliple choices frame
        self.multiple_choices = Frame(self.easy_frame, bg=background_color)
        self.multiple_choices.grid(row=3, pady=5)

        # All the multiple choices buttons
        self.country_1 = Button(self.multiple_choices, text ="?",
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=15,
                                command=lambda: self.answer(1))
        self.country_1.grid(row=3, column=0, padx=5, pady=5)
        self.country_1.config(state=DISABLED)

        self.country_2 = Button(self.multiple_choices, text ="?",
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=15,
                                command=lambda: self.answer(2))
        self.country_2.grid(row=3, column=1, padx=5, pady=5)
        self.country_2.config(state=DISABLED)

        self.country_3 = Button(self.multiple_choices, text ="?",
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=15,
                                command=lambda: self.answer(3))
        self.country_3.grid(row=4, column=0, padx=5, pady=5)
        self.country_3.config(state=DISABLED)

        self.country_4 = Button(self.multiple_choices, text="?",
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=15,
                                command=lambda: self.answer(4))
        self.country_4.grid(row=4, column=1, padx=5, pady=5)
        self.country_4.config(state=DISABLED)

        # Feedback label (row 5)
        self.feedback = Label(self.multiple_choices, bg = background_color,
                                 text="", font="Arial 12 bold")
        self.feedback.grid(row=5, columnspan=2, pady=5)

        # country label for printing the correct answer if user gets wrong
        self.correct_country = Label(self.multiple_choices, fg="#000000", bg=background_color,
                                text="", font="Arial 12 bold")
        self.correct_country.grid(row=6,column=0, pady=5)

        self.correct_country1 = Label(self.multiple_choices, fg="#000000", bg=background_color,
                                text="", font="Arial 12 bold",)
        self.correct_country1.grid(row=6,column=1, pady=5)


         # next frame goes here (row 5)
        self.check_next = Frame(self.easy_frame, bg=background_color)
        self.check_next.grid(row=4)

         # start Text (label, row 4)
        self.start_text = Label(self.check_next, text="PRESS ENTER TO START", bg=background_color,
                                font="Arial 14 bold",
                               justify=LEFT,)
        self.start_text.grid(row=4, column=0, padx=10, pady=5) 
        
        # Next button goes here (row 6)
        self.next_button = Button(self.check_next, text="Next",
                                  font="Arial 12 bold",
                                  bg="#EA6B66",
                                  borderwidth=2,
                                  width=10,
                                  command=self.next)
        self.next_button.grid(row=5, column=0, padx=5)

        # Help/Stats Frame goes here
        self.help_stats_frame = Frame(self.easy_frame, bg=background_color)
        self.help_stats_frame.grid(row=5, pady=5)

        # Help and stats buttons go here (row 5)
        self.help_button = Button(self.help_stats_frame, text="Help",
                                  font="Arial 12 bold",
                                  bg="#66B2FF",
                                  borderwidth=2,
                                  width=8)
        self.help_button.grid(row=5, column=0, padx=10, pady=5)

        # Stats button goes here (row 6)
        self.stats_button = Button(self.help_stats_frame, text="Stats",
                                  font="Arial 12 bold",
                                  bg="#FF9933",
                                  borderwidth=2,
                                  width=8)
        self.stats_button.grid(row=5, column=1, padx=10, pady=5)

         # quit button goes here (row 6)
        self.quit = Button(self.easy_frame, text="Quit",
                                  font="Arial 12 bold",
                                  bg="#E00000",
                                  borderwidth=2,
                                  width=16,
                                  command=partial(self.close_easy, partner))
        self.quit.grid(row=6, column=0, padx=10, pady=5)


        self.next_button.focus()
        self.next_button.bind('<Return>', lambda e: self.next())


# Next function for when user wants to go to next question
# This code hsa the main generation for flag and country
# Where it accesses it from the csv file

    def next(self):
        
        # blanks out the feedback & start text so that user 
        # does not see them next round
        self.start_text.config(text=" ")
        self.correct_country.config(text=" ")
        self.correct_country1.config(text=" ")
        self.feedback.config(text=" ")

        # disable next button
        self.next_button.config(state=DISABLED)

        # re-enables the multiple choice button so user can move onto next question
        self.country_1.config(state=NORMAL)
        self.country_2.config(state=NORMAL)
        self.country_3.config(state=NORMAL)
        self.country_4.config(state=NORMAL)

        # focuses on a different frame instead of next button
        self.multiple_choices.focus()

        # Here is where the code accesses the csv file
        with open("country_flags.csv") as f: 
            
            reader = csv.reader(f)
            flag_list = list(reader)

        # randomly generate a list from the csv file
        chosen_country = random.choice(flag_list)
        
        # Links the answer with the previously set StrVar
        self.correct_ans.set(chosen_country[0])
       
        # chooses the flag out of the randomly generated list
        image_to_use = "flag_images\\" + chosen_country[-1]
        flag_image = PhotoImage(file=image_to_use)

        # flag image configuration
        self.picture_label.config(image=flag_image)
        self.picture_label.photo = flag_image
        
        # Create master list for the multiple choices
        list_of_countries = []

        for item in range(0,3):
            options = random.choice(flag_list)
            country_option = []
            country_option = options[0]

            # Add the three countries to the list
            list_of_countries.append(country_option)
        
        # Add the answer to the list as well
        flag_answer = chosen_country[0]
        list_of_countries.append(flag_answer)

        # Shuffle it so that answer isn't always 
        # the fourth choice
        random.shuffle(list_of_countries)

        # add each country to the buttons 
        self.country_1.config(text=list_of_countries[0])
        self.country_2.config(text=list_of_countries[1])
        self.country_3.config(text=list_of_countries[2])
        self.country_4.config(text=list_of_countries[3])

    def answer(self, button_id):

        # Multiple button and label Disables for reducing a mess in the GUI
        self.country_1.config(state=DISABLED)
        self.country_2.config(state=DISABLED)
        self.country_3.config(state=DISABLED)
        self.country_4.config(state=DISABLED)

        # Enables the next button so that user can continue
        self.next_button.config(state=NORMAL)

        # retrieves the answer that the user enters
        chosen_country = self.correct_ans.get()

        # Correct feedback randomly generates
        correct = ["Bravo! you got it right", "Awesome keep it up", "Excellent Work",
         "You're Great", "Outstanding", "Good Job"]
        
        # Incorrect feedback randomly generates
        incorrect = ["C'mon, you can do better than that", "Nope, try harder on the next one",
        "oops, you messed up there", "Keep Trying", "Nice try"]

        correct = random.choice(correct)
        incorrect = random.choice(incorrect)

        # Get answer entered from user...
        if button_id == 1:
            answer_entered = self.country_1['text']
        elif button_id == 2:
            answer_entered = self.country_2['text']
        elif button_id == 3:
            answer_entered = self.country_3['text']
        else:
            answer_entered = self.country_4['text']

        # assumes there are no errors at the start 
        has_errors = "no"

        # If user gets it right
        if answer_entered == chosen_country:                
            has_errors = "no"
            feedback = correct
            self.next_button.focus()

        # If user gets it wrong
        elif answer_entered != chosen_country:
            has_errors = "yes"
            feedback = incorrect
            correct_country = chosen_country
            self.next_button.focus()

        if has_errors == "yes":
            self.feedback.config(text=feedback)
            self.feedback.config(fg="maroon")
            self.correct_country.config(text="Answer:")
            self.correct_country1.config(text=correct_country)

        elif has_errors == "no":
            self.feedback.config(text=feedback)
            self.feedback.config(fg="#00CC00")

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

