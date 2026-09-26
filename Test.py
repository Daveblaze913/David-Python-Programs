print("=================Welcome to calculator====================")
print("Select the operation you wish to do")
print("1. Addition" )
print("2. Multiplication")
print("3. Substraction")
print("4. Division")
try:
    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))
except ValueError:
    print("Invalid Input")
def addition(num1,num2):
    return num1 + num2


def substraction(num1,num2):
    return num1 - num2


def multiplication(num1,num2):
    return num1 * num2


def division(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero")


answer = input("Enter your choice ")
if answer == "1":
    print(addition(number1,number2))
elif answer == "2":
   print(multiplication(number1,number2))
elif answer == "3":
    print(substraction(number1,number2))
elif answer == "4":
    print(division(number1,number2))
