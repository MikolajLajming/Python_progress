from random import randint
from errors import error


def choose_difficulty(option):
    """Determines difficulty"""
    difficulty = difficulties[option]
    return difficulty


def choose_random_number():
    """Returns a random number between 1 and 100"""
    random_number = randint(1, 100)
    return random_number


def determine_too_low_or_to_high(guess, number, mode):
    """Returns a message if the guess is too low or too high, on easy mode it returns a hint
    vaguely how much the guess is off"""
    memory = 0
    if guess > number:
        if mode:
            for i in verdicts:
                if i >= (guess - number):
                    memory = i
            message = f"{verdicts[memory]} too high!"
        else:
            message = "Too high!"
    elif guess < number:
        if mode:
            for i in verdicts:
                if i >= (number - guess):
                    memory = i
            message = f"{verdicts[memory]} too low!"
        else:
            message = "Too low!"
    else:
        message = str(error(1))
    return message


difficulties = {
    # "level": [number_of_attempts, hints_on],"
    "easy": [10, True],
    "medium": [10, False],
    "hard": [5, False]
}

verdicts = {
    100: "Definitely way",
    25: "Way",
    15: "Too",
    10: "Close, but",
    5: "Just a bit",
}

