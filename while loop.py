totalChores = 4
Originalcount = totalChores

print("You have ",Originalcount,"Chores to complete today")
completechores = 0
chore_num = 1

while chore_num <= totalChores:
    if chore_num == 1:
        next_chore = "Make your bed"
    elif chore_num == 2:
        next_chore == "Feed your pet"
    elif chore_num == 3:
        next_chore == "Take out the trash"
    else:
        next_chore == "Wash the dishes"

    ans = input("Have you finished chores" )
    if ans == "yes":
         completechores = completechores + 1
         chore_num = chore_num + 1
    else :
         print("Okay, finish it and check again !")

    print("Chores reamaining = ",totalChores - completechores)



print("Chore Check list")
print("Chores assigned today: " , Originalcount)
print("Chores completed today: ", completechores)
print("Chores Remaining",totalChores - completechores)