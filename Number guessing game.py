print("=============================Number guessing games======================================")
computer = 26
player_Number = int(input("Enter your number from 1 to 50: "))

while True:
    if player_Number == computer:
        print("you guessed it congrats")
        break
    elif player_Number in range(29,56):
        print("You are wrong you 4 attempts left. hint: you are cold ")
    elif player_Number in range(1,6):
        print("You are wrong you have 3 attempts left. hint you are very cold")
    elif player_Number in range(10,21):
        print("You are hot. But you are wrong  2 attempts remaining")
    elif player_Number in range(21,26):
        print("You are so close but u are still wrong 1 attempts remaining")
    elif player_Number in range(25,27):
        print("You were so close but you are still wrong sadly and your attempts are over sadly ")
    else:
        print("Invalid input")
    break



