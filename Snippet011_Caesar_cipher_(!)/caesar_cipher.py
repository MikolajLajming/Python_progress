import art
import os
import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def clear_console():
    if os.name == "nt":
        _ = os.system('CLS')
    else:
        _ = os.system('clear')


def good_ending():
    print("Bye!")


def bad_ending():
    print("Wrong operation")
    sys.exit()


def start():
    print(art.logo)
    directions = ["encode", "decode"]
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in directions:
        bad_ending()
    text = input("Type your message:\n").lower()
    if len(text) == 0:
        bad_ending()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)


def caesar(text, shift, direction):
    message = ""
    shift = shift % 26
    if direction == "decode":
        shift *= -1
    for character in text:
        if character not in alphabet:
            message += character
        else:
            if alphabet.index(character) + shift + 1 > len(alphabet):
                message += alphabet[alphabet.index(character) + shift - len(alphabet)]
            else:
                message += alphabet[alphabet.index(character) + shift]

    print(f"The {direction}d text is {message}")
    restart = input("Restart cipher? Type 'yes' to restart, type 'no' to end:\n")
    if restart == "yes":
        clear_console()
        start()
    elif restart == "no":
        good_ending()
    else:
        bad_ending()


start()
