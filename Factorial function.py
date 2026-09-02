def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

print("Factorial of 0: ", factorial (0))
print("Factorial of 1: ", factorial (1))
print("Factorial of 2: ", factorial(2))
print("Factorial of 3: ", factorial (3))
print("Factorial of 4: ", factorial (4))