import random

computer = random.randint(1,10)

while True:
    guess = int(input("Enter your number and try to guess the computer's number : "))

    if guess == computer:
        print ("⭐🎉🎉CONGRAGULATIONS YOU WIN")
        break
    elif guess < computer:
        print("Incorrect try a higher number")
    else:
        print("Incorrect pick a lower number")