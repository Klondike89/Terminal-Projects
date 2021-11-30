'''Program Goals:
-5 Catagories of questions
-5 Questions in each Catagory
-Answer 10 questions correctly to win
-Get 3 questions wrong and you lose'''

"""Game Plan
-initialize variables for score, losses
-initialize dicitonaries for each Catagory with the key being 
    the question and the value being the answers
-open txt file and populate dictionaries
-create funtion that asks player to choose a catagory
-select a random key from catagory of players choice and ask that question
-add ditionary location to list of asked questions
-update score acording to player input regardles of capitalization
-ask player to choose a catagory for next question
-when all questions froma catagory have been asked 
    no longer include that catagory as option
-once player has won or lost print that and their total score to the screen"""