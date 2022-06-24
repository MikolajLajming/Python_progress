import os
from art import logo

# >>>>>>> For testing purpose <<<<<<<
# bidders = {
#     "Burzuj": 132,
#     "Krzysio": 122,
#     "Miki": 123,
#     "Krysia": 122,
#     "Kasia": 123,
# }

bids = {}
choices = ["yes", "no"]
next_bidder = True


def clear_console():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def define_winner(bidders):
    winner = {}
    tie = {}
    winner_name = ""
    winner_amount = 0
    tie_amount = 0

    for bidder in bidders:
        current_amount = bidders[bidder]
        if not winner:
            winner = {
                bidder: current_amount
            }
            winner_name = bidder
            winner_amount = current_amount
        elif current_amount == winner_amount:
            if tie and tie_amount < winner_amount:
                tie = winner
            if winner_name not in tie:
                tie.update(winner)
            tie.update({bidder: current_amount})
            tie_amount = winner_amount
        else:
            if current_amount > winner_amount:
                winner = {
                    bidder: current_amount
                }
                winner_name = bidder
                winner_amount = current_amount

    tie_names = []

    if tie:
        for person in tie:
            tie_names.append(person)

    clear_console()

    if len(tie) > 0 and tie_amount >= winner_amount:
        print(f"It's a tie between {', '.join(tie_names)} with the amount of ${tie_amount}.")
    else:
        print(f"The winner is {winner_name} with the amount of ${winner_amount}.")


while next_bidder:
    clear_console()
    print(logo)
    bidder_name = str(input("Please type in your name: "))
    bidder_amount = int(input("What's your bid? : $"))
    wish_to_continue = str(input("Are there any other bidders? Type 'yes' to continue or 'no' to finish\n"))
    if wish_to_continue not in choices:
        print("Something went wrong, starting over")
    elif wish_to_continue == choices[1]:
        bids[bidder_name] = bidder_amount
        next_bidder = False
        define_winner(bidders=bids)
    else:
        bids[bidder_name] = bidder_amount


