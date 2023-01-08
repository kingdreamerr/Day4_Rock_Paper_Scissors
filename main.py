import art
import random

items = ["Rock", "Paper", "Scissors"]

# GET THE COMPUTER'S CHOICE:
computer_choice = items[random.randint(0,len(items)-1)]

print("Let's play a game of rock paper scissors!!\n")
# GET THE USER'S CHOICE:
user_data = int(input("Enter a number 0 for Rock 1 for paper 2 for scissors : "))
user_choice = items[user_data]

# CHECK THE WINNER:
if computer_choice == "Rock" and user_choice == "Scissors":
    print(f"the computer choose {computer_choice}")
    print(art.rock)
    print(f"You choose {user_choice}")
    print(art.scissors)
    print("You Lose!")
elif computer_choice == "Scissors" and user_choice == "Paper":
    print(f"the computer choose {computer_choice}")
    print(art.scissors)
    print(f"You choose {user_choice}")
    print(art.paper)
    print("You Lose!")
elif computer_choice == "Paper" and user_choice == "Rock":
    print(f"the computer choose {computer_choice}")
    print(art.paper)
    print(f"You choose {user_choice}")
    print(art.rock)
    print("You Lose!")
elif user_choice == computer_choice:
    print("It's a tie!!")
else:
    if computer_choice == "Scissors" and user_choice == "Rock":
        print(f"the computer choose {computer_choice}")
        print(art.scissors)
        print(f"You choose {user_choice}")
        print(art.rock)
        print("You Win!")
    elif computer_choice == "Paper" and user_choice == "Scissors":
        print(f"the computer choose {computer_choice}")
        print(art.paper)
        print(f"You choose {user_choice}")
        print(art.scissors)
        print("You Win!")
    elif computer_choice == "Rock" and user_choice == "Paper":
        print(f"the computer choose {computer_choice}")
        print(art.rock)
        print(f"You choose {user_choice}")
        print(art.paper)
        print("You Win!")

