totalhomework = 4
Originalhomeworkcount = totalhomework

print("You have ",Originalhomeworkcount,"homework to complete today")
completedhomeworks = 0
homework_num = 1

while homework_num <= totalhomework:
    if homework_num == 1:
        next_homework = "Do ur math homework"
    elif homework_num == 2:
        next_homework == "Finish english homework"
    elif homework_num == 3:
        next_homework == "Do quantitative reasoning"
    else:
        next_homework == "Do language asignment"

    ans = input("Have you finished your homework" )
    if ans == "yes":
         completedhomeworks = completedhomeworks + 1
         next_homework = homework_num + 1
    else :
         print("Okay, finish it and check again !")

    print("Homework reamaining = ",totalhomework - completedhomeworks)



print("Homework Check list")
print("Homework assigned today: " , Originalhomeworkcount)
print("Homework completed today: ", completedhomeworks)
print("Homework Remaining",totalhomework - completedhomeworks)