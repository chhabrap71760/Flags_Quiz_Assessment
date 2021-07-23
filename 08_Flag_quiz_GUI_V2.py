# FLAGS OF THE WORLD FINAL OUT COME

from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random
import csv

# Round Generating Class
class Rounds:

    def __init__(self):

        # set the total amount of round as a Integer variable for later use
        self.round_amount = IntVar()
        self.round_amount.set(0)

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # Setup GUI 
        #self.round_box = Toplevel()


        # Setup up GUI Frame
        self.round_frame = Frame(bg=background_color)
        self.round_frame.grid()

        # Set up Round Counter heading
        self.round_heading = Label(self.round_frame, text="Question Counter",
                                 font="arial 16 bold", bg=background_color,
                                 padx=10)
        self.round_heading.grid(row=0, column=0, sticky="nw")

        # Round text variable
        rounds_text = "Enter the amount of questions you'd like to play"

        # Set up Round Counter text
        self.rounds_text = Label(self.round_frame, text=rounds_text, 
                                bg=background_color,
                                fg="#999999",
                                font="Arial 11 italic",
                                justify=LEFT, padx=10)
        self.rounds_text.grid(row=1, column=0)

        # entry box and check button frame goes here...
        self.enter_check = Frame(self.round_frame, bg=background_color)
        self.enter_check.grid(row=2, column=0, sticky="w")

        # Entry Box goes here (row 2)
        self.enter_rounds = Entry(self.enter_check,
                                  font="Arial 15 bold", width=10)
        self.enter_rounds.grid(row=2, column=0, padx=12)

        # Focuses on the entry box from the beginning to reduce hastle
        self.enter_rounds.focus()

        # binds the check button to <enter> to make things easier
        self.enter_rounds.bind('<Return>', lambda e:self.round_checker())


        # check button goes here (row 2)
        self.check_button = Button(self.enter_check, text="Check",
                                  font="Arial 12 bold",
                                  bg="#FFFF00",
                                  borderwidth=2,
                                  width=8,
                                  command=self.round_checker)
        self.check_button.grid(row=2, column=1)

        # Play button/ error label frame goes here..
        self.play_error = Frame(self.round_frame, bg=background_color)
        self.play_error.grid(row=3, column=0)


        # Error Label goes here
        self.play_feedback = Label(self.play_error, fg="maroon",
                                bg=background_color, text="", 
                                font="Arial 10 bold", wrap=275,
                                justify=LEFT)
        self.play_feedback.grid(row=3, column=0, padx=5, pady=5)

        # Play Button Goes here (row 4)
        self.play_button = Button(self.play_error, text="Play",
                                  font="Arial 12 bold",
                                  bg="#EA6B66",
                                  borderwidth=2,
                                  width=14,
                                  command=self.to_main)
        self.play_button.grid(row=4, column=0, padx=5, pady=5)
        self.play_button.config(state=DISABLED)

        # bind the play button to <enter> to make it easier to move to the game
        self.play_button.bind('<Return>', lambda e: self.to_main())

    # This function checks and validates the amount that the user enters
    def round_checker(self):
        
        self.amount_entered = self.enter_rounds.get()
        
        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors="no"

        # Change background to white
        self.enter_rounds.config(bg="white")
        self.play_feedback.config(text="")

        # Clear the entry box so that user does not need to clear it every time
        self.enter_rounds.delete(0, END)

        try:
            amount_entered = int(self.amount_entered)

            # user enters a value under 0
            if amount_entered <= 0:
                has_errors = "yes"
                error_feedback = "NUMBER MUST BE ABOVE 0"

            # user enters a value above 50
            elif amount_entered > 50:
                has_errors = "yes"
                error_feedback = "NUMBER MUST BE LESS THAN 50"

            # user enters a value above 0
            elif amount_entered > 0:
                has_errors = "no"
                self.play_button.config(state=NORMAL)
                error_feedback = "You may click play or press <enter>"

        # user enters no value, text or decimals
        except ValueError:
            has_errors = "yes"
            error_feedback = '''PLEASE ENTER A NUMBER 
(NO TEXT/DECIMALS)'''

        if has_errors == "yes":
            self.enter_rounds.config(bg=error_back)
            self.play_feedback.config(text=error_feedback)

        else:
            self.play_feedback.config(text=error_feedback)
            self.play_feedback.config(fg="#00CC00")
            self.enter_rounds.config(state=DISABLED)
            self.check_button.config(state=DISABLED)
            self.play_button.focus()
            
            # if valid, set the IntVar as the amount entered by user
            self.round_amount.set(amount_entered)
            print(amount_entered)

    def to_main(self):
        
        # Retrive the amount entered by the user
        amount_entered = self.round_amount.get()

        Main(self, amount_entered)
        
        # hide round counter
        self.round_frame.destroy()


class Main:
    def __init__(self, partner, amount_entered):

        # Formatting Variables
        background_color = "#FFE6CC"

        # Set an IntVar() for the total amount of rounds
        self.round_end = IntVar()
        self.round_end.set(amount_entered)

        # Set the mode selected by the user as a string varaiable so that it can be used 
        # in the stats 
        self.mode_selected = StringVar()

        # GUI Setup
        self.main_box = Toplevel()

        self.main_box.protocol('WM_DELETE_WINDOW', partial(self.close_main, partner))

        # Main Menu Frame
        self.main_frame = Frame(self.main_box, bg=background_color,
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
        self.easy_expert_frame = Frame(self.main_frame, bg=background_color)
        self.easy_expert_frame.grid(row=4, pady=10)
        
        self.easy_button = Button(self.easy_expert_frame, text="Easy Mode",
                                  font="Arial 12 bold",
                                  bg="#FF9999",
                                  borderwidth=2,
                                  command=self.easy)
        self.easy_button.grid(row=0, column=0,)

        self.expert_button = Button(self.easy_expert_frame, text="Expert Mode",
                                    font="Arial 12 bold",
                                    width=9,
                                    bg="#FF0000",
                                    borderwidth=2,
                                    command=self.expert)
        self.expert_button.grid(row=0, column=1)

        # Help/ Instructions buttons go here... (row 5)
        self.help_button = Button(self.main_frame, text="Help/Instructions",
                                  font="Arial 12 bold",
                                  bg="#66B2FF",
                                  borderwidth=2,
                                  command=self.help)
        self.help_button.grid(row=5, column=0)  

         # quit button goes here (row 6)
        self.quit = Button(self.main_frame, text="QUIT",
                                  font="Arial 10 bold",
                                  bg="#E00000",
                                  borderwidth=2,
                                  width=7,
                                  command=partial(self.close_main, partner))
        self.quit.grid(row=6, column=0, padx=10, pady=10)


    def easy(self):
        # Retrive the amount entered by the user
        amount_entered = self.round_end.get()
        
        # Set the mode selected to the StringVar for later use in stats
        mode = self.easy_button['text']
        print(mode)
        self.mode_selected.set(mode)

        # Retrieve it here so I can add it the main function of the easy class
        mode_used = self.mode_selected.get()

        Easy(self, amount_entered, mode_used)
        
        # hide main menu
        self.main_box.destroy()
    
    def expert(self):
       
        # Retrieve the amount entered by the user
        amount_entered = self.round_end.get()

        # Set the mode selected to the StringVar for later use in stats
        mode = self.expert_button['text']
        print(mode)
        self.mode_selected.set(mode)

        # Retrieve it here so I can add it to the main function of the expert class
        mode_used = self.mode_selected.get()

        Expert(self, amount_entered, mode_used)
        
        # hide main menu
        self.main_box.destroy()

    def help(self):
        Help(self)
    
    def close_main(self, partner):
        root.destroy()
        


# Easy Class goes here...
class Easy:

    def __init__(self, partner, amount_entered, mode_used):

        # Set another String variable for the mode used
        self.which_mode = StringVar()
        self.which_mode.set(mode_used)

        # Set an IntVar for rounds played
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        # Set another IntVar() for the total amount of rounds
        self.round_end = IntVar()
        self.round_end.set(amount_entered)

        # List for holding the game statistics
        self.game_stats_list = [0, 0, 0]

        # Create IntVar for the point system
        self.correct_answers = IntVar()
        self.correct_answers.set(0)

        self.incorrect_answers = IntVar()
        self.incorrect_answers.set(0)

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # Set country as a stringvar so that it can be used in other functions
        self.correct_ans = StringVar()

        # disable easy button
       # partner.easy_button.config(state=DISABLED)

        # Sets up child window
        self.easy_box = Toplevel()

        self.easy_box.protocol('WM_DELETE_WINDOW', partial(self.close_easy))

        # Set up GUI Frame
        self.easy_frame = Frame(self.easy_box, bg=background_color)
        self.easy_frame.grid()

         # Set up Easy Mode heading (row 0)
        self.easy_heading = Label(self.easy_frame, text="Easy Mode",
                                 font="arial 20 bold", bg=background_color,
                                 padx=10, pady=10)
        self.easy_heading.grid(row=0, column=0,)

        # Rounds Text
        self.round_text = Label(self.easy_frame, text="Question:", bg=background_color,
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
                                width=18,
                                wrap=200,
                                command=lambda: self.answer(1))
        self.country_1.grid(row=3, column=0, padx=5, pady=5)
        self.country_1.config(state=DISABLED)

        self.country_2 = Button(self.multiple_choices, text ="?",
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=18,
                                wrap=200,
                                command=lambda: self.answer(2))
        self.country_2.grid(row=3, column=1, padx=5, pady=5)
        self.country_2.config(state=DISABLED)

        self.country_3 = Button(self.multiple_choices, text ="?",
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=18,
                                wrap=200,
                                command=lambda: self.answer(3))
        self.country_3.grid(row=4, column=0, padx=5, pady=5)
        self.country_3.config(state=DISABLED)

        self.country_4 = Button(self.multiple_choices, text="?",
                                font="Arial 12 bold",
                                bg = "#E6E6E6",
                                borderwidth = 2,
                                width=18,
                                wrap=200,
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
                                  width=8,
                                  command=self.help)
        self.help_button.grid(row=5, column=0, padx=10, pady=5)

        # Stats button goes here (row 6)
        self.stats_button = Button(self.help_stats_frame, text="Stats",
                                  font="Arial 12 bold",
                                  bg="#FF9933",
                                  borderwidth=2,
                                  width=8,
                                  command=lambda:self.gamestats(self.game_stats_list))
        self.stats_button.grid(row=5, column=1, padx=10, pady=5)
        self.stats_button.config(state=DISABLED)

         # quit button goes here (row 6)
        self.quit = Button(self.easy_frame, text="Quit",
                                  font="Arial 12 bold",
                                  bg="#E00000",
                                  borderwidth=2,
                                  width=16,
                                  command=partial(self.close_easy))
        self.quit.grid(row=6, column=0, padx=10, pady=5)

        # Focuses on the next button in the beginning so the user can press enter to start
        self.next_button.focus()
        self.next_button.bind('<Return>', lambda e: self.next())


# Next function for when user wants to go to next question
# This code hsa the main generation for flag and country
# Where it accesses it from the csv file

    def next(self):
        
        # Retrive the amount of times that user clicks the country button
        rounds = self.rounds_played.get()

        # adds 1 number to the amount of rounds played
        rounds += 1
        self.rounds_played.set(rounds)

        # Display it in the GUI
        rounds_text = "Question: {}".format(rounds)
        self.round_text.config(text=rounds_text)


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

       # generates 3 random countries 
        while len(list_of_countries) < 3:
            options = random.choice(flag_list)
            country_option = []
            country_option = options[0]

            # Checks if there are no duplicates if not then it
            # Adds the three countries to the list
            if country_option not in list_of_countries:
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

        # Retrive the amount of rounds played
        rounds = self.rounds_played.get()
        
        # Retrive the total rounds that user wants to play
        round_total = self.round_end.get()

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

        # Set a point system
        correct_answers = self.correct_answers.get()
        incorrect_answers = self.incorrect_answers.get()
        self.game_stats_list[2] = rounds

    # If statement for checking user input and sending a valid response

        # If user gets it right
        if answer_entered == chosen_country:                
            has_errors = "no"
            correct_answers += 1
            self.correct_answers.set(correct_answers)
            feedback = correct
            self.next_button.focus()

        # If user gets it wrong
        elif answer_entered != chosen_country:
            has_errors = "yes"
            incorrect_answers += 1
            self.incorrect_answers.set(incorrect_answers)
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

        # binds the entry to <enter> button to reduce user hastle
        self.stats_button.bind('<Return>', lambda e: self.gamestats(self.game_stats_list))

        self.game_stats_list[0] = correct_answers
        self.game_stats_list[1] = incorrect_answers

        # user plays all the round then GAME is OVER
        if rounds == round_total:
            self.start_text.config(text="GAME OVER")
            self.stats_button.focus()
            self.next_button.config(state=DISABLED)

        # enable the stats button after one round
        if rounds == 1:
            self.stats_button.config(state=NORMAL)

    def gamestats(self, game_stats):

        # binds the quit button to <enter> button to reduce user hastle
        self.quit.bind('<Return>', lambda e: self.close_easy())
        

        # focuses on the quit button after it opens stats so that user
        # cannot go back into easy mode and click enter again for stats
        self.quit.focus()

        # Retrieve the mode used 
        mode_used = self.which_mode.get()

        # create an IntVar for hints used just so that errors dont occur
        # It has no use for this function
        self.hints_used = IntVar()
        self.hints_used.set(0)
        hints_used = self.hints_used.get()

        # disable stats button
        self.stats_button.config(state=DISABLED)


        Gamestats(self, mode_used, game_stats, hints_used)

    def close_easy(self):

        # Retrive the amount entered by the user
        amount_entered = self.round_end.get()

        Main(self, amount_entered)
        
        # hides easy mode window
        self.easy_box.destroy()

    def help(self):
        Help(self)

# Expert Class goes here...
class Expert:

    def __init__(self, partner, amount_entered, mode_used):

        # Set another string variable for the mode used
        self.which_mode = StringVar()
        self.which_mode.set(mode_used)

        # set an IntVar for rounds played
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        # Set another IntVar() for the total amount of rounds
        self.round_end = IntVar()
        self.round_end.set(amount_entered)

        # List for holding the game statistics
        self.game_stats_list = [0, 0, 0]

        # Create IntVar for the point system
        self.correct_answers = IntVar()
        self.correct_answers.set(0)

        self.incorrect_answers = IntVar()
        self.incorrect_answers.set(0)


        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # Set capital and country as a stringvar so that it can be used in other functions
        self.correct_ans = StringVar()
        self.hint = StringVar()

        # Set the amount of times hint button is pressed for stats
        self.hints_used = IntVar()
        self.hints_used.set(0)

        # Sets up child window (ie: help box)
        self.expert_box = Toplevel()

        self.expert_box.protocol('WM_DELETE_WINDOW', partial(self.close_expert))

        # Set up GUI Frame
        self.expert_frame = Frame(self.expert_box, bg=background_color)
        self.expert_frame.grid()

         # Set up expert heading (row 0)
        self.expert_heading = Label(self.expert_frame, text="Expert Mode",
                                 font="arial 20 bold", bg=background_color,
                                 padx=10, pady=10)
        self.expert_heading.grid(row=0, column=0,)

        # round Text (label, row 2)
        self.round_text = Label(self.expert_frame, text="Question:", bg=background_color,
                                font="Arial 13 bold",
                               justify=LEFT, padx=10, pady=10)
        self.round_text.grid(row=2, column=0) 

        # start Text (label, row 4)
        self.start_text = Label(self.expert_frame, text="PRESS ENTER TO START", bg=background_color,
                                font="Arial 14 bold",
                               justify=LEFT, padx=10)
        self.start_text.grid(row=4, column=0) 

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
        self.entry_hint.grid(row=3, pady=5)

        # Entry Box goes here (row 3)
        self.enter_answer = Entry(self.entry_hint,
                                  font="Arial 15 bold", width=15)
        self.enter_answer.grid(row=3, column=0)
        self.enter_answer.config(state=DISABLED)

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
        self.help_stats_frame.grid(row=5, pady=5)

        # Help and stats buttons go here (row 5)
        self.help_button = Button(self.help_stats_frame, text="Help",
                                  font="Arial 12 bold",
                                  bg="#66B2FF",
                                  borderwidth=2,
                                  width=8,
                                  command=self.help)
        self.help_button.grid(row=5, column=1, padx=5, pady=15)

        # Stats button goes here (row 5)
        self.stats_button = Button(self.help_stats_frame, text="Stats",
                                  font="Arial 12 bold",
                                  bg="#FF9933",
                                  borderwidth=2,
                                  width=8,
                                  command=lambda:self.gamestats(self.game_stats_list))
        self.stats_button.grid(row=5, column=2, padx=5, pady=15)
        self.stats_button.config(state=DISABLED)

        # Help/Stats Frame goes here
        self.next_quit_frame = Frame(self.expert_frame, bg=background_color)
        self.next_quit_frame.grid(row=6, pady=5)
        
        # Next button goes here (row 6)
        self.next_button = Button(self.next_quit_frame, text="Next",
                                  font="Arial 12 bold",
                                  bg="#EA6B66",
                                  borderwidth=2,
                                  width=10,
                                  command=self.next)
        self.next_button.grid(row=6, column=1, padx=10, sticky="e")

        # binds the entry to <enter> button to reduce user hastle
        self.enter_answer.bind('<Return>', lambda e: self.answer())

        self.next_button.focus()
        self.next_button.bind('<Return>', lambda e: self.next())

        # Quit Button goes here (row 6)
        self.quit = Button(self.next_quit_frame, text="Quit",
                           bg="#CC0000", font="Arial 12 bold", 
                           borderwidth=2, width=10,
                           command=partial(self.close_expert))
        self.quit.grid(row=6, column=2, padx=10)


# Next function for when user wants to go to next question
#  - This code is the the main generation for flag and country
# Where it accesses it from the csv file
    
    def next(self):
            
        # Retrive the amount of times that user clicks the country button
        rounds = self.rounds_played.get()
                
        # adds 1 number to the amount of rounds played
        rounds += 1
        self.rounds_played.set(rounds)
        
        # Display it in the GUI
        rounds_text = "Question: {}".format(rounds)
        self.round_text.config(text=rounds_text)


        # Multiple button and label Disables for reducing a mess in the GUI
        self.hint_button.config(state=NORMAL)
        self.check_button.config(state=NORMAL)
        self.hint_label.config(text=" ")
        self.hint_label1.config(text=" ")
        self.entry_error.config(text=" ")
        self.entry_correct.config(text=" ")
        self.correct_country.config(text=" ")
        self.correct_country1.config(text=" ")
        self.enter_answer.config(state=NORMAL)
        self.start_text.config(text=" ")
        self.next_button.config(state=DISABLED)

        # Clear the entry box so that user does not need to clear it every time
        self.enter_answer.delete(0, END)
        
        # focuses on the entry box from the start so user doesn't need to do it themselves
        self.enter_answer.focus()

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

        # Retrive the amount of rounds played
        rounds = self.rounds_played.get()

        # Retrive the total rounds that user wants to play
        round_total = self.round_end.get()

        # Multiple button and label Disables for reducing a mess in the GUI
        self.hint_label.config(text=" ")
        self.hint_button.config(state=DISABLED)
        self.hint_label1.config(text=" ")
        self.check_button.config(state=DISABLED)
        self.hint_button.config(state=DISABLED)
        self.next_button.config(state=NORMAL)
        #self.stats_button.config(state=DISABLED)

        # retrieves the answer that the user enters
        answer_entered = self.enter_answer.get()
        
        # converts the entry so that first letter for each word is capital
        answer_entered = answer_entered.title()

        # takes in the correct_answer StrVar from the 'next' function
        chosen_country = self.correct_ans.get()
       

        # Correct feedback randomly generates 
        correct = ["Bravo! you got it right", "Awesome keep it up", "Excellent Work",
         "You're Great", "Outstanding", "Good Job"]

        correct_feedback = ""

        # Incorrect feedback randomly generates
        incorrect = ["C'mon, you can do better than that", "Nope, try harder on the next one",
        "oops, you messed up there", "Keep Trying", "Nice try"]

        correct = random.choice(correct)
        incorrect = random.choice(incorrect)

        # assumes there are no errors at the start
        has_errors = "no"
 
        # Set a point system
        correct_answers = self.correct_answers.get()
        incorrect_answers = self.incorrect_answers.get()
        self.game_stats_list[2] = rounds

    # If statement for checking user input and sending a valid response
        

        # if user does not type anything
        if answer_entered == "":
            has_errors = "blank"
            error_feedback="Please enter a Country"
            self.check_button.config(state=NORMAL)
            self.hint_button.config(state=NORMAL)
            self.start_text.config(text="")
            self.entry_error.config(text=error_feedback)
            self.next_button.config(state=DISABLED)
           # self.stats_button.config(state=DISABLED)
            self.enter_answer.config(state=NORMAL)
            
        # If user gets it right
        elif answer_entered == chosen_country:             
            has_errors = "no"
            correct_answers += 1
            self.correct_answers.set(correct_answers)
            correct_feedback = correct
            self.entry_error.config(text=" ")
            self.next_button.focus()
           # self.enter_answer.config(state=DISABLED)

        # If user gets it wrong
        elif answer_entered != chosen_country:
            has_errors = "yes"
            incorrect_answers += 1
            self.incorrect_answers.set(incorrect_answers)
            error_feedback = incorrect
            correct_country = chosen_country
            self.next_button.focus()
            #self.enter_answer.config(state=DISABLED)

        if has_errors == "yes":
            self.entry_error.config(text=error_feedback)
            self.correct_country.config(text="Answer:")
            self.correct_country1.config(text=correct_country)
            self.enter_answer.config(state=DISABLED)
           # self.stats_button.config(state=NORMAL)


        elif has_errors == "no":
            self.entry_correct.config(text=correct_feedback)
            self.enter_answer.config(state=DISABLED)
            #self.stats_button.config(state=NORMAL)
        
        elif has_errors == "blank": 
            self.start_text.config(text="")
            #self.stats_button.config(state=DISABLED)

        

        # binds the entry to <enter> button to reduce user hastle
        self.stats_button.bind('<Return>', lambda e: self.gamestats(self.game_stats_list))
        
        # update the points in the list
        self.game_stats_list[0] = correct_answers
        self.game_stats_list[1] = incorrect_answers

        # User plays all the rounds then GAME is OVER
        if rounds == round_total:
            self.start_text.config(text="GAME OVER")
            self.next_button.config(state=DISABLED)
            self.stats_button.focus()

        # enable the stats button after one round
        if rounds == 1:
            self.stats_button.config(state=NORMAL)

# Hints function goes here..
# very short code because hint is set to a StrVar in the beginning
# This makes it conveniant and saves a lot of lines of code
    def hints(self):

        # Retrieves the amount of times the user clicks the hint button
        hints = self.hints_used.get()

        # Adds 1 number to the amount of time the hint button is pressed
        hints += 1
        self.hints_used.set(hints)

        # disables hint button
        self.hint_button.config(state=DISABLED)

        # Retrieves the StrVar value
        get_hint = self.hint.get()

        # Display the hint
        self.hint_label.config(text="Capital City:")
        self.hint_label1.config(text=get_hint)

    def help(self):
        Help(self)

    def gamestats(self, game_stats):

        # binds the quit button to <enter> button to reduce user hastle
        self.quit.bind('<Return>', lambda e: self.close_expert())
        

        # focuses on the quit button after it opens stats so that user
        # cannot go back into easy mode and click enter again for stats
        self.quit.focus()


        # Retrieve the amount of hints used
        hints_used = self.hints_used.get()

        # Retrieve the mode used
        mode_used = self.which_mode.get()

        # Disable stats button so user does not press mulitple times
        self.stats_button.config(state=DISABLED)
        
        Gamestats(self, mode_used, game_stats, hints_used)

    # For when user decides to click quit 
    def close_expert(self):

        # Retrive the amount entered by the user
        amount_entered = self.round_end.get()

        # leads to the main menu when user clicks quit
        Main(self, amount_entered)
        
        # hides expert box
        self.expert_box.destroy()

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

                       After answering a couple questions you can click the stats button
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

    # Game Stats Class goes here...
class Gamestats:
    def __init__(self, partner, mode_used, game_stats, hints_used):

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # Sets up child window (ie: stats box)
        self.stats_box = Toplevel()

        # If user press cross at top, closes stats 
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box, bg=background_color)
        self.stats_frame.grid()

        # Set up Stats heading (row 0)
        self.stats_heading = Label(self.stats_frame, text="Game Statistics",
                                    font="arial 20 bold", bg=background_color,
                                    padx=10, pady=5)
        self.stats_heading.grid(row=0, column=0,)

        # stats text variable goes here...
        stats_text = '''Here are your game statistics. You may use the 
Export button to save these statistics into a 
.txt file'''


        # Game statistics Instructions
        self.stats_instructions = Label(self.stats_frame,
                                        bg=background_color,
                                        text=stats_text, 
                                        font="arial 11 bold",
                                        fg="#00994D",
                                        justify=LEFT,
                                        padx=10, pady=5)
        self.stats_instructions.grid(row=1, column=0)

        # Stats Details Frame goes here...
        self.details_frame = Frame(self.stats_frame, bg=background_color)
        self.details_frame.grid(row=2, pady=5)

        # Mode selected (row 0) 
        self.which_mode = Label(self.details_frame, text="Mode Played:",
                               font="arial 12 bold", bg=background_color,
                               anchor="w")
        self.which_mode.grid(row=0, column=0, pady=5, padx=5)


        # mode selected label (row 0.5)
        self.which_mode2 = Label(self.details_frame, text=mode_used,
                               font="arial 12 bold", bg=background_color,
                               anchor="e")
        self.which_mode2.grid(row=0, column=1, pady=5, padx=5)

        # Correct answers label (row 1)
        self.correct_answers = Label(self.details_frame, text="Correct Answers:",
                                     font="arial 12 bold", bg=background_color,
                                     fg="#00CC00",
                                     anchor="w",)
        self.correct_answers.grid(row=1, column=0, pady=5, padx=5)

        # Correct answers label (row 1.5)
        self.correct_answers2 = Label(self.details_frame,
                                    text="{}".format(game_stats[0]),
                                    font="arial 13 bold", bg=background_color,
                                    fg="#00CC00",
                                    anchor="e")
        self.correct_answers2.grid(row=1, column=1, pady=5, padx=5)

        # Incrrect Answers label (row 2)
        self.incorrect_answers = Label(self.details_frame, text="Incorrect Answers:",
                                       font="arial 12 bold", bg=background_color,
                                       fg="maroon",
                                       anchor="w")
        self.incorrect_answers.grid(row=2, column=0, pady=5, padx=5)

        # Incorrect answers label (row 2.5)
        self.incorrect_answers2 = Label(self.details_frame,
                                    text="{}".format(game_stats[1]),
                                    font="arial 13 bold", bg=background_color,
                                    fg="maroon",
                                    anchor="e")
        self.incorrect_answers2.grid(row=2, column=1, pady=5, padx=5)

        # Hints used label (row 3)

        self.hints_used = Label(self.details_frame,
                                    text="Hints Used:",
                                    font="arial 12 bold", bg=background_color,
                                    anchor="w")
        self.hints_used.grid(row=3, column=0, pady=5, padx=5)

        # Hints used label (row 3.5)
        self.hints_used2 = Label(self.details_frame,
                                text="{}".format(hints_used),
                                font="arial 13 bold",
                                bg=background_color,
                                anchor="e")
        self.hints_used2.grid(row=3, column=1, pady=5, padx=5)

        # Games played label (row 4)
        self.games_played = Label(self.details_frame, text="Questions played:",
                                       font="arial 12 bold", bg=background_color,
                                       anchor="w")
        self.games_played.grid(row=4, column=0, pady=5, padx=5)

        # Games played label (row 4.5)
        self.games_played2 = Label(self.details_frame,
                                    text="{}".format(game_stats[2]),
                                    font="arial 12 bold", bg=background_color,
                                    anchor="e")
        self.games_played2.grid(row=4, column=1, pady=5, padx=5)

        # Calculates the percentage 
        percentage = game_stats[0] / game_stats[2] * 100

        # Total Score label (row 5)
        self.total_score = Label(self.details_frame, text=" Total Score:",
                                       font="arial 8 bold", bg=background_color,
                                       anchor="w")
        self.total_score.grid(row=5, column=0, padx=5)

        # Total Score label (row 5.5)
        self.total_score2 = Label(self.stats_frame,
                                    text="{:.0f}%".format(percentage),
                                    font="arial 25 bold", bg=background_color,
                                    anchor="e")
        self.total_score2.grid(row=3, column=0, padx=5)

        # Export / Dismiss buttons frame (row 3)
        self.export_dismiss = Frame(self.stats_frame, bg=background_color)
        self.export_dismiss.grid(row=4, pady=10)

        # Help and stats buttons go here (row 5)
        self.help_button = Button(self.export_dismiss, text="Help",
                                  font="Arial 12 bold",
                                  bg="#66B2FF",
                                  borderwidth=2,
                                  width=8,
                                  command=self.help)
        self.help_button.grid(row=0, column=0, padx=5, pady=5)

        # Export Button
        self.export_button = Button(self.export_dismiss, text="Export",
                                    font="Arial 12 bold",
                                    bg="#FF9933",
                                    borderwidth=2,
                                    width=8,
                                    command=lambda:self.export(game_stats, mode_used, hints_used))
        self.export_button.grid(row=0, column=1, padx=5, pady=5)

        # Dismiss Button
        self.dismiss_button = Button(self.stats_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     bg="#E00000",
                                     borderwidth=2,
                                     width=10,
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=5, column=0, padx=10, pady=10)

        # takes the focus of the stats button so that user cannot press enter 
        self.export_button.focus()


    def help(self):
        Help(self)

    def export(self, game_stats, mode_used, hints_used):
        Export(self, game_stats, mode_used, hints_used)


    def close_stats(self, partner):
        self.stats_box.destroy()
        partner.stats_button.config(state=NORMAL)



class Export:
    def __init__(self, partner, game_stats, mode_used, hints_used):

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()
        
        # disable help button
        partner.export_button.config(state=DISABLED)


        # if users press cross at top, closes export 
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Setup GUI Frame
        self.export_frame = Frame(self.export_box, bg=background_color)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.export_heading = Label(self.export_frame, text="Export...",
                                    font="arial 20 bold", bg=background_color,
                                    padx=10, pady=5)
        self.export_heading.grid(row=0, column=0)

        export_text = '''Please enter your desired filename below. 
your game statistics will be exported as a .txt file and will 
apear in the same folder as this program.'''

        # Export GUi instructions label
        self.export_instructions = Label(self.export_frame,
                                         bg=background_color,
                                         text=export_text,
                                         font="arial 11 bold",
                                         fg="#00994D",
                                         padx=10, pady=5)
        self.export_instructions.grid(row=1, column=0)

        # Filename Entry Box (row 2)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=2, column=0)
        
    # focus on the entry box from the start so the user does not need to select it 
        self.filename_entry.focus()

        # Error message label (row 3)
        self.save_error = Label(self.export_frame, bg=background_color, text="", fg="maroon")
        self.save_error.grid(row=3)

        # Save / Cancel Frame (row 4)
        self.save_cancel = Frame(self.export_frame, bg=background_color)
        self.save_cancel.grid(row=4, pady=10)

        # Save button goes here...
        self.save_button = Button(self.save_cancel, text="Save",
                                  font="Arial 12 bold",
                                  bg="#00CC00",
                                  borderwidth=2,
                                  width=8,
                                  command=partial(lambda:self.save_history(partner, game_stats, mode_used, hints_used)))
        self.save_button.grid(row=4, column=0, padx=5, pady=5)


        # Binds the entry box to <enter> to make it easier for the user
        self.filename_entry.bind('<Return>', lambda e: self.save_history(partner, game_stats, mode_used, hints_used))

        # Cancel Button goes here...
        self.cancel_button = Button(self.save_cancel, text="Cancel",
                                    font="Arial 12 bold",
                                    bg="#CC0000",
                                    borderwidth=2,
                                    width=8,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=4, column=1)

    # Checking and saving function for user's filename
    def save_history(self, partner, game_stats, mode_used, hints_used):

      # Regular expression to check filename is valid
      valid_char = "[A-Za-z0-9_]"
      
      # Assumes there are no errors at the start
      has_errors="no"

      # Retrieves the filename that the user enters 
      filename = self.filename_entry.get()
      print(filename)

        # Clear the entry box so that user does not need to clear it every time
      self.filename_entry.delete(0, END)


      for letter in filename:
        if re.match(valid_char, letter):
          continue

      # if user enters a space in the filename
        elif letter == " ":
          problem = "(no spaces allowed)"

      # if user enters an invalid character eg.( . -)
        else:
            problem = ("no {}'s allowed".format(letter))
        has_errors = "yes"
        break

      # if user enters a blank file
      if filename == "":
        problem = "Can't be blank"
        has_errors = "yes"

      if has_errors == "yes":
        # Display error message
        self.save_error.config(text="Invalid filename - {}".format(problem))
        # Change entry box to pink/red
        self.filename_entry.config(bg="#ffafaf")
        print()
      
      else:
          #change entry box to white
          self.filename_entry.config(bg="#FFFFFF")
          
          # change the error message
          self.save_error.config(text="{} Successfully Saved".format(filename))

          # disable save button so that user does not save another file
          self.save_button.config(state=DISABLED)

          # disable entry box
          self.filename_entry.config(state=DISABLED)

        # Binds the cancel to <enter> to make it easier for the user
          self.cancel_button.bind('<Return>', lambda e: self.close_export(partner))

        # focuses on the cancel button so user can press enter
          self.cancel_button.focus()

          # change the color of the error message
          self.save_error.config(fg="#00CC00")

          # add.txt suffix
          filename = filename + ".txt"

          # Calculates the percentage 
          percentage = game_stats[0] / game_stats[2] * 100

          # create file to hold data
          f = open(filename, "w+")

          # Print out the Game Stats
          f.write("\n\n")

          f.write("--------------------------------------------\n")
          f.write("-----          GAME STATISTICS         -----\n")
          f.write("--------------------------------------------\n")
          f.write("---|  Mode Used:     |\t {} \t|---\n".format(mode_used))
          f.write("---|  Correct:       |\t\t {} \t|---\n".format(game_stats[0]))
          f.write("---|  Incorrect:     |\t\t {} \t|---\n".format(game_stats[1]))
          f.write("---|  Hints Used:    |\t\t {} \t|---\n".format(hints_used))
          f.write("---|Questions Played:|\t\t {} \t|---\n".format(game_stats[2]))
          f.write("--------------------------------------------\n")
          f.write("----------------|  {:.0f} %  |------------------\n".format(percentage))
          f.write("\n")
          f.write("^^^ Thank You for playing my Flags quiz :) ^^^")


    def close_export(self, partner):
        # Put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz Game")
    something = Rounds()
    root.mainloop()
