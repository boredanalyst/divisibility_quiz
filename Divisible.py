## Divisibility Checker

## Import modules and libraries

from os.path import exists
import random
import time

## Create functions and variables.

def display_menu():
    print("<-------DIVISIVE------->")
    print("Welcome to DIVISIVE!")
    print("In this game, you will be asked to check if a number is divisible by another number.")
    print("If you get it right, you go to the next stage and get another question.")
    print("Aim to get the highest score!")
    ask_ready()

## ask for the user's input.
def ask_ready():
    print("Are you ready?")
    user_ready = input("(yes/no) > ")
    user_ready = user_ready.upper()
    if user_ready == "YES":
        global user_name 
        start_game()
        round_start()
    elif user_ready == "NO":
        display_menu()
    else:
        print("Please provide a valid response.")
        ask_ready()

def start_game():
    print("<-----START GAME----->")
    print("What is your name?")
    global user_name
    user_name = input("> ")
    print(f'Welcome to the game {user_name}!')
    print("Your game is starting now.")
    global round_number, score_counter
    round_number = 1
    score_counter = 0

def check_answer(num1, num2):
    if num1 % num2 == 0:
        return "Y"
    else:
        return "N"

def round_start():
    global round_number, score_counter
    print(f"<-----Round {round_number}----->")
    print(f'Current Score: {score_counter}')
    test_number = random.randint(1,1000)
    divisor = random.randint(1,10)
    correct_answer = check_answer(test_number,divisor)
    print(f'Is {test_number} divisible by {divisor}?')
    user_answer = input("(y/n) > ")
    user_answer = user_answer.upper()

    if user_answer == "Y" or user_answer =="N":
        if user_answer == correct_answer:
            print(f'You are correct {user_name}!')
            round_number += 1
            score_counter += 1
            if round_number == 15:
                print("The game is over!")
                print(f'You got a total of {score_counter} out of {round_number}')
                print("<-----END GAME----->")
            else:
                time.sleep(1)
                round_start()
        else:
            print(f"Sorry {user_name}. That is incorrect.")
            round_number += 1
            round_start()
    else:
        print("Please provide a valid response.")
        round_start()


## User workflow

display_menu()