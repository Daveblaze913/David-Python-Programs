Valid = False
while not Valid:
    try:
        num = int(input("Enter your number: "))
        while num %2 == 0:
            print("bye")
        Valid - True
    except ValueError:
        print("Invalid iNPUT")