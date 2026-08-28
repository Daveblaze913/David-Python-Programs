Players_number = int(input("Enter your number: "))
computer_number = 26
print("Computer Guessing game")
while Players_number in range(1,26):
    if Players_number is not 26:
        print("Incorrect you have 4 guesses")
        if Players_number in range(1,11):
            print("Warm")
    elif Players_number is not 26:
        print("Incorrect you have 3 guesses")
        if Players_number in range(11,27):
            print("Hot")
    elif Players_number is not 26:
        print("Incorrect you have 2 guesses")
        if Players_number in range(27,40):
            print("Cold")
    elif Players_number is not 26:
        print("Incorrect you have 1 more guess remaining")
        if Players_number in range(40,51):
            print("Ice cold")
    elif Players_number is not 26:
        print("You have guessed in correctly THE number was 26 ")
    else:
        print("Check if you have put in valid number")
    if Players_number == computer_number:
        print("You have won the guessing game the number was 26")




