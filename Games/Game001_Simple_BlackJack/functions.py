import os
from random import choice
from cards import deck


def deal_card():
    card = choice(list(deck))
    return card


def draw_from_deck():
    player_ids = ["player", "computer"]
    hands = {}
    for player in player_ids:
        cards = []
        for i in range(2):
            new_card = deal_card()
            cards.append(new_card)
        hands[player] = cards
    return hands


def check_value(hand):
    value = 0
    bust = False
    for card in hand:
        card_value = deck[card]
        value += card_value
    if "A" in hand and value > 21:
        value -= 10
    elif value > 21:
        bust = True
    else:
        bust = False
    return value, bust


def end_game(player_hand, player_value, computer_hand, computer_value):
    message = f"    Your final hand: [{', '.join(player_hand)}], final score: {player_value}\n"\
              f"    Computer's final hand: [{', '.join(computer_hand)}], final score: {computer_value}"
    if player_value <= 21 and computer_value <= 21:
        if player_value < computer_value:
            end_message = "Computer wins! You LOST!"
        elif player_value > computer_value:
            end_message = "You WIN!"
        else:
            end_message = "It's a draw!"
    elif player_value <= 21 < computer_value:
        end_message = "Computer bust! You WIN!"
    else:
        end_message = "Bust! You LOST!"
    return message, end_message


def clear_console():
    """Clears the console"""
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')



