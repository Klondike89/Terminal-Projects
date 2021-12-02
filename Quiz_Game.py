from time import sleep
from random import randint

TITLE = "\u0332".join("Quiz Game ")
FILE_PATH = r'C:\Users\brian\Documents\GitHub\Terminal-Projects\Trivia.txt'
yes = "Y\u0332es/y\u0332es"
no = "N\u0332o/n\u0332o"


player = {'score':0,'losses':0}
asked_questions = {}

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
    valid_choices = ['a','h','m','s','t']
    valid_input = False
    while not valid_input:
        print("\nPlease choose a catagory from the list below.\n"+
            "To make a selection enter the Corisponding letter.\n")
        type_choice = input(art+history+math+science+trivia+":")
        if type_choice in valid_choices:
            if type_choice.lower() == 'a':
                choice = 0
            elif type_choice.lower() == 'h':
                choice = 1
            elif type_choice.lower() == 'm':
                choice = 2
            elif type_choice.lower() == 's':
                choice = 3
            elif type_choice.lower() == 't':
                choice = 4
            valid_input = True    
            return int(choice)
    # Encountering some bug here.
        else:
            print("Invalid character entered, "+ 
            "please choose one of the options given.")

def ask_question(choice):
    draw = randint(0,4)
    question_pair = all_catagories[choice][draw]
    player_answer = str(input('\n'+question_pair[0])).lower()
    if player_answer == str(question_pair[1]).lower():
        print("\nCorrect!")
        player["score"] +=1
        print("Score: "+str(player["score"])+" Losses: "+str(player["losses"]))
    else:
        print("\nSorry the correct answer is: " + question_pair[1])
        player["losses"] +=1
        print("Score: "+str(player["score"])+" Losses: "+str(player["losses"]))

def check_score():
    if player["score"]==10:
        print('\nCONGRATULATIONS!!!\n'+
        'You ACED this quiz!\n'+
        'You are one smart cookie!')
    
    if player["losses"]==3:
        print('\nMy condolences, you have lost the game.')


while player["score"]<10 and player["losses"]<3:
    ask_question(choose_catagory())
    check_score()


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