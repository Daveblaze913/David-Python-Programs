try:
    num=int(input("Enter your number:"))
    print(num//0)
except ValueError:
    print("Exception will be handled successfuly")