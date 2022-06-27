from random import randint
from errors import error


def choose_random_number():
    """Returns a random number between 1 and 100"""
    random_number = randint(1, 100)
    return random_number


def determine_too_low_or_to_high(guess, number):
    """Returns a message with hint if the guess is too low or too high and vaguely how much"""
    memory = 0
    if guess > number:
        for i in verdicts:
            if i >= (guess - number):
                memory = i
        message = f"{verdicts[memory]} too high!"
    elif guess < number:
        for i in verdicts:
            if i >= (number - guess):
                memory = i
        message = f"{verdicts[memory]} too low!"
    else:
        message = str(error(1))
    return message


verdicts = {
    100: "Definitely way",
    25: "Way",
    15: "Too",
    10: "Close, but",
    5: "Just a bit",
}
