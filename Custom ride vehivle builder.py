print("==========================")
print("    Welcome to ride builder   ")
print("==========================")


print("Pick your vehicle")
print("1. Bike")
print("2. Car")

choice = int(input("Enter choice of vehicle:"))
if choice == 1:
    print("Pick your type of bike")
    print("1. Scooty")
    print("2. Motorcycle")
    choice = int(input("Enter your type of bike:"))
    if choice == 1:
        print("your ride is scooty")
        print("Maximum speed =95kph  ")
    else: 
        print("Your ride is motorcycle")
        print("Top speed : 115kph ")
else:
    print("Pick your type of car")
    print("1. Toyota")
    print("2. Mclarem")
    choice = int(input("Enter choice of vehicle:"))
    if choice == 1:
        print("Your ride is toyota")
        print("Maximum speed is 210kph")
    else:
        print("Your ride is a Mclaren")
        print("Maximum speed is 220kph")