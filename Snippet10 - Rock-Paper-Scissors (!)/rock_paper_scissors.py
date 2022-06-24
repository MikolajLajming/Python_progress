import random
from ascii_art import scissors
from ascii_art import paper
from ascii_art import rock

list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(list[user_choice])

computer_choice = random.randint(0,2)
print(f"the program choosed {computer_choice}", list[computer_choice])

if user_choice != computer_choice:
  if user_choice == 0:
    if computer_choice == 1:
      print("You lost")
    else:
      print("You win!")
  elif user_choice == 1:
    if computer_choice == 0:
      print("You win!")
    else:
      print("You lost")
  else:
    if computer_choice == 0:
      print("You lost")
    else:
      print("You win!")
else:
  print("It's a draw!")
