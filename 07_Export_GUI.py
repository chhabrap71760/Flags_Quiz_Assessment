# Comonent 7
# Export GUI

from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random
import csv

# Main Menu Class goes here...
class Main:
    def __init__(self):

        # sets a hard coded list
        self.game_stats_list = [10, 10, 20]

        # set the amount of times hint button is pressed for later use
        self.hints_used = IntVar()
        self.hints_used.set(0)

        # Set the background color in the beginning
        background_color = "#FFE6CC"

        # Set the mode selected by the user as a string varaiable so that it can be used 
        # in the stats 
        self.mode_selected = StringVar()

        # Main Menu Frame
        self.main_frame = Frame(bg=background_color,
                                padx=10, pady=10)
        self.main_frame.grid()


        # Main Menu Heading 1 (row 0_
        self.main_label = Label(self.main_frame, text="Flag Quiz Game",
                            font="Arial 12 bold",
                            bg=background_color)
        self.main_label.grid(row=0)

        # Easy Button goes here...
        self.easy_button = Button(self.main_frame, text="Easy Mode",
                                  font="Arial 12 bold",
                                  bg="#FF9999",
                                  borderwidth=2, 
                                  command=lambda: self.which_button(1))
        self.easy_button.grid(row=1, column=0)
    
        # Expert button goes here...
        self.expert_button = Button(self.main_frame, text="Expert Mode",
                                    font="Arial 12 bold",
                                    width=9,
                                    bg="#FF0000",
                                    borderwidth=2,
                                    command=lambda: self.which_button(2))
                                    
        self.expert_button.grid(row=1, column=1)

        # Hint Button goes here (Row 5)
        self.hint_button = Button(self.main_frame, text="Hint",
                                  font="Arial 12 bold",
                                  bg="#FFFF00",
                                  borderwidth=2,
                                  width=8,
                                  command=self.hints)
        self.hint_button.grid(row=5, column=0, padx=15)
        self.hint_button.config(state=DISABLED)


        # stats button goes here... (row 5)
        self.stats_button = Button(self.main_frame, text="Stats",
                                  font="Arial 12 bold",
                                  bg="#FF9933",
                                  borderwidth=2,
                                  command=lambda:self.gamestats(self.game_stats_list))
        self.stats_button.grid(row=5, column=1, columnspan=4, pady=10)  
        self.stats_button.config(state=DISABLED)

    # hint function for when the user clicks the hint button
    def hints(self):
      
      # retrieve the amount of times the user clicks the hint button 
      hints = self.hints_used.get()

      # Adds 1 number to the amount of times the hint button is pressed
      hints += 1
      self.hints_used.set(hints)
      

  # this function is used for saving which mode was used in the game
    def which_button(self, mode_id):

      # user clicks the easy mode button
      if mode_id == 1:
        
        # enables stats and disables expert button
        self.stats_button.config(state=NORMAL)
        self.expert_button.config(state=DISABLED)
        
        # Set the mode selected as the StringVar to display in stats GUI
        mode = self.easy_button['text']
        print(mode)
        self.mode_selected.set(mode)

      # user clicks expert mode
      else:
        # Enables the stats and hint buttons, disables the easy button
        self.stats_button.config(state=NORMAL)
        self.easy_button.config(state=DISABLED)
        self.hint_button.config(state=NORMAL)
        
        # Set the mode selected as the StringVar to display in stats GUI
        mode = self.expert_button['text']
        print(mode)
        self.mode_selected.set(mode)

        
    def gamestats(self, game_stats):
        
        # Retrive the mode used and amount of times the 
        mode_used = self.mode_selected.get()
        hints_used = self.hints_used.get()

        Gamestats(self, mode_used, game_stats, hints_used)

# Game Stats Class goes here...
class Gamestats:
    def __init__(self, partner, mode_used, game_stats, hints_used):

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # disable stats button
        partner.stats_button.config(state=DISABLED)

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
                                font="arial 13 bold", bg=background_color,
                                anchor="e")
        self.hints_used2.grid(row=3, column=1, pady=5, padx=5)

        # Games played label (row 4)
        self.games_played = Label(self.details_frame, text="Games played:",
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
                                  width=8)
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


    def close_stats(self, partner):
        # Put stats button back to normal
        partner.stats_button.config(state=NORMAL)
        partner.easy_button.config(state=NORMAL)
        partner.expert_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, game_stats, mode_used, hints_used):
        Export(self, game_stats, mode_used, hints_used)

class Export:
    def __init__(self, partner, game_stats, mode_used, hints_used):

        # Set background color to a specific color at the start to avoid confusion
        background_color = "#FFE6CC"

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

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
          f.write("---|  Correct:       |\t\t {} \t\t|---\n".format(game_stats[0]))
          f.write("---|  Incorrect:     |\t\t {} \t\t|---\n".format(game_stats[1]))
          f.write("---|  Hints Used:    |\t\t {} \t\t\t|---\n".format(hints_used))
          f.write("---| Games Played:   |\t\t {} \t\t|---\n".format(game_stats[2]))
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
    something = Main()  
    root.mainloop()