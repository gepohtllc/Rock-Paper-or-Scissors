import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Are you ready for a game of Rock, Paper, & Scissors? \n")

player_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
computer_choice = random.randint(0, 2)
game_images = [rock, paper, scissors]

if player_choice == 0 and computer_choice == 2:
    print("Player chose:" + game_images[player_choice])
    print("Computer chose:" + game_images[computer_choice])
    print("Player wins!")
elif computer_choice == 0 and player_choice == 2:
    print("Player chose:" + game_images[player_choice])
    print("Computer chose:" + game_images[computer_choice])
    print("Computer wins")
elif computer_choice > player_choice:
    print("Player chose:" + game_images[player_choice])
    print("Computer chose:" + game_images[computer_choice])
    print("Computer wins")
elif player_choice > computer_choice:
    print("Player chose:" + game_images[player_choice])
    print("Computer chose:" + game_images[computer_choice])
    print("Player wins!")
elif computer_choice == player_choice:
    print("Player chose:" + game_images[player_choice])
    print("Computer chose:" + game_images[computer_choice])
    print("It's a draw!")
