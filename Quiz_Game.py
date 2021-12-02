from time import sleep
from random import randint

TITLE = "\u0332".join("Quiz Game ")
FILE_PATH = r'C:\Users\brian\Documents\GitHub\Terminal-Projects\Trivia.txt'
yes = "Y\u0332es/y\u0332es"
no = "N\u0332o/n\u0332o"


player = {'score':0,'losses':0}

art = "[A\u0332rt]  "
history = "[H\u0332istory]  "
math = "[M\u0332ath]  "
science = "[S\u0332cience]  "
trivia = "[90's T\u0332rivia]  "

art_questions = []
history_questions = []
math_questions = []
science_questions = []
nineties_trivia_questions = []
all_catagories = [art_questions,
                history_questions,
                math_questions,
                science_questions,
                nineties_trivia_questions
                ]

with open(FILE_PATH, 'r') as file:
    for line in file:
        line = line.rstrip("\n")
        catagory, question, answer = line.split('|')
        key = [question, answer]
        if catagory == 'Art':
             art_questions.append(key)
        elif catagory == 'History':
             history_questions.append(key)
        elif catagory == 'Math':
             math_questions.append(key)
        elif catagory == 'Science':
             science_questions.append(key)
        elif catagory == 'Trivia':
             nineties_trivia_questions.append(key)

# Welcome
want_to_play = input("Welcome to "+TITLE+"would you like to play?\n"+
                yes+" or "+no+":")
if want_to_play.lower() != 'y':
    print("Ok, have a great day. GOODBYE!")
    sleep(1)
    quit()

# Choose a catagory
def choose_catagory():
    print("Please choose a catagory from the list below.\n"+
        "To make a selection enter the Corisponding letter.\n")
    choice = input(art+history+math+science+trivia+":")
    if choice.lower() == 'a':
        choice = 0
    elif choice.lower() == 'h':
        choice = 1
    elif choice.lower() == 'm':
        choice = 2
    elif choice.lower() == 's':
        choice = 3
    elif choice.lower() == 't':
        choice = 4
    else:
        print("Invalid character entered, please choose one of the options given.")
    return choice

def ask_question(choice):
    x = choice
    print(choice)
    #print(all_catagories[x])


ask_question(choose_catagory())
'''Program Goals:
-5 Catagories of questions
-5 Questions in each Catagory
-Answer 10 questions correctly to win
-Get 3 questions wrong and you lose'''

"""Game Plan
-initialize dictionaries for score, losses
-initialize list for each Catagory nested lists containing 
    the question and the answer
-open txt file and populate lists
-create funtion that asks player to choose a catagory
-select a random key from catagory of players choice and ask that question
-add ditionary location to list of asked questions
-update score acording to player input regardles of capitalization
-ask player to choose a catagory for next question
-when all questions froma catagory have been asked 
    no longer include that catagory as option
-once player has won or lost print that and their total score to the screen"""