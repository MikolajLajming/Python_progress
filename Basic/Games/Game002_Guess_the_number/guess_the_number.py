from art import logo
from errors import error
import os
import functions


def clear_console():
    """Clears the console"""
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def start_game():
    """Generates number and starts the game. Here user can pick difficulty lvl"""
    clear_console()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking about a number between 1 and 100")
    random_number = functions.choose_random_number()
    option = str(input('Choose difficulty. Type "easy", "medium" or "hard": ')).lower()
    if option in functions.difficulties:
        guess_the_number(functions.choose_difficulty(option)[0], random_number, functions.choose_difficulty(option)[1])
    else:
        print("Option not found. Choosing the easiest difficulty for you :)")
        guess_the_number(15, random_number, True)


def guess_the_number(tries, number, easy_mode):
    print(f"You have {tries} attempts remaining to guess the number.")
    end_game_message = False
    play = True
    while play and tries != 0:
        guess = int(input("Make a guess: "))
        if guess and guess in range(0, 101) and guess != number:
            tries -= 1
            message = functions.determine_too_low_or_to_high(guess, number, easy_mode)
            print(message)
            if tries == 0:
                play = False
                end_game_message = f"You've run out of guesses. The correct answer was {number}. You lose"
            else:
                print(f"You have {tries} left.")
        elif guess and guess in range(0, 101) and guess == number:
            play = False
            end_game_message = f"You win! The correct answer is {number}"
        else:
            print(error(1))
    print(end_game_message)
    loop = True
    while loop:
        question = str(input("Do you want to play again? Type Y or N: ")).upper()
        if question == "Y":
            loop = False
            start_game()
        elif question == "N":
            loop = False
            clear_console()
            print("Bye!")
        else:
            print(error(1))


start_game()
