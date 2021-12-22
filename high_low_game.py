#-------------------------------------------------------------------------------
# Name:        High-Low game
# Purpose:     Fun
#
# Author:      nicolescu
#
# Created:     22/12/2021
# Copyright:   (c) nicol 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
score = 0
logo = '''
     :
 '.  _  .'
-=  (~)  =-
 .'  #  '.   \n\n\n\n '''
print(logo)
print("Welcome to HIGH-LOW game!\n")

data_views = [{"name":"Baby Shark", "views": 9.87},{"name":"Luis Fonsi", "views": 7.67},{"name":"LooLoo Kids", "views": 6.04},{"name":"Ed Sheran", "views": 5.56},{"name":"Wiz Khalifa", "views": 5.36},
{"name":"Cocomelon - Nursery Rhymes","views": 4.77},{"name":"Miroshka TV","views": 4.54},
{"name":"Get Movies","views": 4.47},{"name":"Mark Ronson","views": 4.40},{"name":"ChuChu TV","views": 4.36},{"name":"Psy","views": 4.28},{"name":"El Chombo","views": 3.77},{"name":"Maroon 5","views": 3.61},{"name":"Justin Bieber","views": 3.49},{"name":"Katy Perry","views": 3.49},
{"name":"OneRepublic","views": 3.47},{"name":"Alan Walker","views": 3.20},{"name":"Enrique Iglesias","views": 3.14},{"name":"Crazy Frog","views": 3.14},{"name":"Major Lazer","views": 3.14},{"name":"Passenger","views": 3.16},{"name":"Taylor Swift","views": 3.13},
{"name":"J Balvin","views": 3.02},{"name":"Shakira","views": 3.01},{"name":"Lady Gaga","views": 9.30},{"name":"Judson Laipply","views": 6.52},{"name":"RCA Records","views": 2.89}]

# I create a function that takes an input wich is the choice
def format_data(choice):
    '''In this function I create a simple variable to get the key = "name" from the dictionary to format it '''
    choice_name =choice["name"]
    return choice_name

def check_answer(guess, a_views, b_views):
    '''Here I used if statement to check if the user is correct'''
    if a_views > b_views:
        return guess == "A"
    else:
        return guess == "B"

choice_b = random.choice(data_views)
game_should_continue = True
while game_should_continue == True:
    choice_a = choice_b
    choice_b = random.choice(data_views)

    if choice_a == choice_b:
        choice_b = random.choice(data_views)

    print(f"Compare A: {format_data(choice_a)}")

    print('''
                                      _     _
                                     ( \---/ )
                                      ) . . (
        ________________________,--._(___Y___)_,--._______________________
                                `--'           `--' \n''')


    print(f"Compare B: {format_data(choice_b)}")

    ask = input("Who has more views? (A or B)=  ").upper()
    a_views = choice_a["views"]
    b_views = choice_b["views"]
    is_correct = check_answer(ask, a_views, b_views)

    if is_correct:
        score += 1
        print(f"You are right! Your score is {score} points 😉")
    else:
        game_should_continue = False
        print(f"You are wrong! Your score is {score} 😈")
