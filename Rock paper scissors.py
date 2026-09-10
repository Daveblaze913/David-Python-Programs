import random

choices = ["rock", "paper", "scissors"]

while True:
    print("1. Rock \n2. Paper \n3 . Scissors \n4 exit ")
    users_choice = input("Enter your choice: ").strip().lower()

    if users_choice == "exit":
        print("Thanks for playing....")
        break
    computer_choice = random.choice(choices)

    print("Your choice:", users_choice)
    print("Computer choice:",computer_choice)

    if computer_choice == users_choice:
        print("tie")
    elif users_choice == "rock" and computer_choice == "scissors" or users_choice == "paper" and computer_choice == "rock" or users_choice == "scissors" and computer_choice == "paper":
        print("You won")
    elif users_choice in choices:
        print("Computer wins")
    else:
        print("Invalid input")