print("=================Welcome to calculator====================")
print("Select the operation you wish to do")
print("1. Addition" )
print("2. Multiplication")
print("3. Substraction")
print("4. Division")

number1 = float(input("Enter your first number"))
number2 = float(input("Enter your second number"))

def addition(num1,num2):
    return num1 + num2


def substraction(num1,num2):
    return num1 - num2


def multiplication(num1,num2):
    return num1 * num2


def division(num1,num2):
    return num1 / num2
