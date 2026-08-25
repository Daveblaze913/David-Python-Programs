print("==========================")
print("    Welcome to daily holiday planner   ")
print("==========================")


print("Pick your holiday")
print("1. christmas")
print("2. Easter")

choice = int(input("Enter choice of vehicle:"))
if choice == 1:
    print("Pick your type of clothing to wear")
    print("1. Jacket")
    print("2. christmas costume")
    choice = int(input("Enter your type of clothing:"))
    if choice == 1:
        print("your clothing is jacket")
        print("It must be chilly outside  ")
    else: 
        print("Your clothing is christmas")
        print("You really wanna get into holiday spirit ")
else:
    print("Pick your type of Clothing")
    print("1. Casual  t shirt ")
    print("2. Cool jacket")
    choice = int(input("Enter choice of clothing:"))
    if choice == 1:
        print("Your outift is a casual t shirt ")
        print("IT must be warm outside go have fun with your family and celebrate easter")
    else:
        print("Your clothing is cool jacket")
        print("It's a bit chilly outside u can always spend easter indisde as well")