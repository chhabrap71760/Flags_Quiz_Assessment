from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random
import csv

with open("country_flags.csv") as f: #  change variable name
            
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index == 0:
                    chosen_row = row
                else:
                    b = random.randint(0, index) # change variable name asap
                    if b == 0:
                        chosen_row = row
                    
                    print(chosen_row)

                    flag_image = chosen_row[3:5]
                    print(flag_image)

                    
                