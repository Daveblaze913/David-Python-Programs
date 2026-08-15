print ("===============Libary visit planner=================")
print("I will help you plan your visit schedule to the libary")

day = input ("Enter today's date Monday - sunday? "). strip().capitalize()
weather = input  ("Enter today's weather condition (Sunny/Rainy/Cloudy)"). strip().lower()
book = input ("Which genre of  books will you like to read (Action/Informative/Romantic)"). strip() .lower()

print()
print ("Your book genre for the day is:", book)

print("-"*50)

if day == ("Monday"):
    print("What book are u reading from the book you borrowed on sunday")
elif day in ("Tuesday, Wednesday, Thursday, Friday"):
    print("How is the progress of your book doing if you want to read another oen the libary is always open on weekdays")
elif day == ("Saturday"):
    print("It's one more day till the time to have your book is over I suggest you finish reading what you have now")
elif day == ("Sunday"):
    print("Its sunday it is time to submit the book you're reading feel free to borrow another one")
else:
    print("Error i can not find the day you are talking about")
