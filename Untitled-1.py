
import csv

import random
import math
import operator as op

# Welcome
name = input("What is your name: ")
print("Hello there", name, "Welcome to the math quiz, you will be asked 10 random questions on Addition, Multiplication and Subtraction")

choice = random.choice(['x','-','+'])
correctquestions = 0

# give the quiz
for questionnumber in range(1,11):

    choice = random.choice(['x','-','+'])
    number1 = random.randrange(1,10)
    number2 = random.randrange(1,10)
    print((number1),(choice),(number2))
    answer = int(input("What is the answer?"))

    if choice == "+":
        realanswer = number1 + number2
    elif choice == "x":
        realanswer = number1 * number2
    elif choice == "-":
        realanswer = number1 - number2


    if answer == realanswer:
        print("Well done that's the correct answer")
        correctquestions +=  1
    else:
        print("Unlucky wrong answer")

else:
    print("Well done You have completed the math quiz, Your score was " + str(correctquestions) + "/10 questions.")

# save their score
class_number = None
while class_number not in ("1" , "2" , "3"):
    class_number = input("which class are you in?")

classfilename = "class{}.csv".format(class_number)
ScoresList = []
position = -1

with open(classfilename, "r") as classfile:
    reader = csv.reader(classfile)
    for row in reader:
        if row and row[0] == name:
            player_row = len(ScoresList)
        ScoresList.append(row)

print(position)

if position < 0: # not found in the class
    ScoresList.append([name, str(correctquestions)])
else:
    row = ScoresList[position] 
    if len(row) == 4:  
        del row[1]
    row.append(str(correctquestions))  

for row in ScoresList:
    print(row)

with open (classfilename, "w", newline='') as file:
    writer = csv.writer(file)
    for row in ScoresList:
        writer.writerow(row)

import random

def playerTriviaQuestions():
    fo = open("playerstriviaquestions.csv","r")
    players = fo.readlines()
    for p in players:
        data = p.split(",")
    questions = data[0]
    answers = data[1]
    print(questions)

    fo.close()


    with open(filename) as f:
    reader = csv.reader(f)
    for index, row in enumerate(reader):
        if index == 0:
            chosen_row = row
        else:
            r = random.randint(0, index)
            if r == 0:
                chosen_row = row
