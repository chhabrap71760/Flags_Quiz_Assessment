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
                                  command=self.rounds)
        self.easy_button.grid(row=5, column=0)  

        # Exoert buttons go here... (row 5)
        self.expert_button = Button(self.main_frame, text="Expert Mode",
                                  font="Arial 12 bold",
                                  bg="#FF0000",
                                  borderwidth=2,
                                  command=self.rounds)
        self.expert_button.grid(row=5, column=1)  

    def rounds(self):
        Rounds(self)

class Rounds:

    def __init__(self, partner):

        self.round_amount = IntVar()
        self.round_amount.set(0)

        background_color = "#FFE6CC"

        # disable easy button
        partner.easy_button.config(state=DISABLED)
        
        # disable expert button
        partner.expert_button.config(state=DISABLED)

        # Sets up child window
        self.round_box = Toplevel()

        self.round_box.protocol('WM_DELETE_WINDOW', partial(self.close_rounds, partner))

        # Setup up GUI Frame
        self.round_frame = Frame(self.round_box, bg=background_color)
        self.round_frame.grid()

        # Set up Round Counter heading
        self.round_heading = Label(self.round_frame, text="Round Counter",
                                 font="arial 16 bold", bg=background_color,
                                 padx=10)
        self.round_heading.grid(row=0, column=0, sticky="nw")

        rounds_text = "Enter the amount of rounds you'd like to play"

        # Set up Round Counter text
        self.rounds_text = Label(self.round_frame, text=rounds_text, 
                                bg=background_color,
                                fg="#999999",
                                font="Arial 11 italic",
                                justify=LEFT, padx=10)
        self.rounds_text.grid(row=1, column=0)

        self.enter_check = Frame(self.round_frame, bg=background_color)
        self.enter_check.grid(row=2, column=0, sticky="w")

        # Entry Box goes here (row 2)
        self.enter_rounds = Entry(self.enter_check,
                                  font="Arial 15 bold", width=10)
        self.enter_rounds.grid(row=2, column=0, padx=8, sticky="w")

        # check button goes here (row 2)
        self.check_button = Button(self.enter_check, text="Check",
                                  font="Arial 12 bold",
                                  bg="#FFFF00",
                                  borderwidth=2,
                                  width=8,
                                  command=self.round_checker)
        self.check_button.grid(row=2, column=1)

        # Error Label goes here
        self.play_error = Label(self.enter_check, fg="maroon",
                                bg=background_color, text="", 
                                font="Arial 10 bold", wrap=275,
                                justify=LEFT)
        self.play_error.grid(row=3, column=0, padx=5, pady=10)

        # Play Button Goes here (row 4)
        self.play_button = Button(self.enter_check, text="Play",
                                  font="Arial 12 bold",
                                  bg="#EA6B66",
                                  borderwidth=2,
                                  width=14,
                                  command=self.to_game)
        self.play_button.grid(row=4, column=0, padx=5, pady=10)
        self.play_button.config(state=DISABLED)


    def round_checker(self):
        self.amount_entered = self.enter_rounds.get()
        
        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors="no"

        # Change background to white
        self.enter_rounds.config(bg="white")
        self.play_error.config(text="")

        # Disable play button just in case user changes mind
        #self.play_button.config(state=DISABLED)

        try:
            amount_entered = int(self.amount_entered)

            if amount_entered <= 0:
                has_errors = "yes"
                error_feedback = "NUMBER MUST BE ABOVE 0"

            elif amount_entered > 50:
                has_errors = "yes"
                error_feedback = "NUMBER MUST BE LESS THAN 50"

            elif amount_entered > 0:
                self.play_button.config(state=NORMAL)
        
            
        except ValueError:
            has_errors = "yes"
            error_feedback = "TEXT/DECIMALS ARE NOT VALID"

        if has_errors == "yes":
            self.enter_rounds.config(bg=error_back)
            self.play_error.config(text=error_feedback)
        else:
            self.round_amount.set(amount_entered)
            print(amount_entered)
    
    def to_game(self):

        # Retrive round amount
        amount_entered = self.round_amount.get()

        Round_Testing(self, amount_entered)

        # hide start up window
        self.round_frame.destroy()

    def close_rounds(self, partner):
        partner.expert_button.config(state=NORMAL)
        partner.easy_button.config(state=NORMAL)
        self.round_box.destroy()

class Round_Testing:
    def __init__(self, partner):

        background_color = "#FFE6CC"

        # Sets up child window
        self.round_box = Toplevel()

        self.round_box.protocol('WM_DELETE_WINDOW', partial(self.close_round_testing, partner))


        # Set up GUI Frame
        self.round_testing = Label(self.round_box, bg=background_color)
        self.round_testing.grid()

        # setup Heading
        self.rounds_heading = Label(self.round_testing, text="Testing",
                                    font="arial 20 bold", bg=background_color,
                                    padx=10, pady=10)
        self.rounds_heading.grid(row=0, column=0)
        
 
        # Rounds text
        self.round_text = Label(self.round_testing, text="Round 1", bg=background_color,
                            font="Arial 13 bold",
                            justify=LEFT, padx=10, pady=10)
        self.round_text.grid(row=1, column=0) 

        # Testing text (flag/country)
        self.flag = Label(self.round_testing, text="Flag", bg=background_color,
                            font="Arial 17 bold",
                            padx=10, pady=10)
        self.flag.grid(row=2, column=0)

        self.country = Button(self.round_testing, text="Country",
                                font="Arial 12 bold",
                                bg="#FFFF00",
                                borderwidth=2,
                                width=15,
                                command=self.next)
        self.country.grid(row=3, column=0, padx=10, pady=10)
    
    def next(self):
        questions_played = self.round_amount.get()

        while self.round_amount.get():
        
        next_round = amount_entered.get()

        self.round_text.config(text=next_round)


    def close_round_testing(self, partner):
        self.round_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz Game")
    something = Main()  
    root.mainloop()
