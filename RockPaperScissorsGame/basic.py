#  import the module you’ll use to simulate the computer’s choices:
import random

# take the user input
user_action = input("Enter a choice (rock, paper, scissors): ")

# Define the possible choices and let the computer choose one of them randomly
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Determine a Winner i.e. Implement the logic
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == 'rock':
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print("Your choice doesnt exist, You loose")