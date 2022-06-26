from art import logo
from errors import error
import functions


def blackjack():
    functions.clear_console()
    print(logo)
    hands = functions.draw_from_deck()
    player_hand = hands["player"]
    computer_hand = hands["computer"]
    player_value = functions.check_value(player_hand)[0]
    computer_value = functions.check_value(computer_hand)[0]
    result = ""
    end = False
    while not end:
        print(f"    Your cards: [{', '.join(player_hand)}], current score: {player_value}")
        print(f"    Computer's first card: [{computer_hand[0]}]")
        ask = str(input('Type "y" to get another card, type "n" to pass: ')).upper()
        if ask == "Y":
            new_card = functions.deal_card()
            player_hand.append(new_card)
            player_value = functions.check_value(player_hand)[0]
            end = functions.check_value(player_hand)[1]
            if end:
                result = functions.end_game(player_hand, player_value, computer_hand, computer_value)
        elif ask == "N":
            while computer_value < 17:
                new_card = functions.deal_card()
                computer_hand.append(new_card)
                computer_value = functions.check_value(computer_hand)[0]
                print("Computer got another card!")
            result = functions.end_game(player_hand, player_value, computer_hand, computer_value)
            end = True
        else:
            print(error(1))
    print(f"{result[0]}\n{result[1]}")


def start():
    functions.clear_console()
    wish_to_start = str(input('Do you want to play a game of BlackJack? Type "Y" for yes, type "N" for no: ')).upper()
    game = True
    while game:
        if wish_to_start == "Y":
            functions.clear_console()
            blackjack()
            wish_to_continue = str(input('Do you want to play again? Type "Y" for yes, type "N" for no: ')).upper()
            if wish_to_continue == "N":
                wish_to_start = "N"
            elif wish_to_continue != "Y":
                game = False
                print(error(1))
                print("Bye!")
            else:
                wish_to_start = wish_to_continue
        elif wish_to_start == "N":
            functions.clear_console()
            game = False
            print("Bye!")
        else:
            print(error(1))
            start()


start()



