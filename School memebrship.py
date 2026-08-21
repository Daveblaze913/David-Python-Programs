Name = str(input("Enter your name : "))
School = str(input("Enter The school name: "))
Age = str(input("Enter your age : "))
Gender = str(input("State your gender : "))
Grade = int(input("Enter grade to enter school : "))

validRange = range (50,101)

if Grade not in validRange:
    print("Invalid input")
elif Grade in range (91, 101):
    print("Outstanding")
elif Grade in range (75,101):
    print("Distinction")
elif Grade in range (60, 75):
    print("1st class")
elif Grade in range (50,60):
    print("2nd class")
else:
    print("Failed ! try harder next time you can do it")