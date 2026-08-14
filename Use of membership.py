math = int(input("Enter marks for maths: "))
english = int(input("Enter marks for English: "))
Science = int(input("Enter marks for Science: "))
Geography = int(input("Enter marks for Geography: "))
History = int(input("Enter marks for History: "))

total = math+english+Science+Geography+History
avg = total/5

validRange = range (1,101)

if avg not in validRange:
    print("Invalid input")
elif avg in range (91, 101):
    print("Outstanding")
elif avg in range (75,101):
    print("Distinction")
elif avg in range (60, 75):
    print("1st class")
elif avg in range (50,60):
    print("2nd class")
elif avg in range (35,60):
    print("3rd class")
else:
    print("Failed ! try harder next time you can do it")