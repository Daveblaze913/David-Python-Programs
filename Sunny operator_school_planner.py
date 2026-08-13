print("======================Daily Planner=====================")
print ("Answer 3 questions and I will plan your day")

day = input("Enter your day Monday - Sunday: ").strip().capitalize()
weather = input("What is the weather for today? (Sunny/Rainy/Cloudy) : ").strip().lower()
homework = input("Have you  done your homework? (Yes/No): ").strip().lower()

print()
print("===================== Your plan for ", day , "=========================")

print("-"*50)

if day in ("Saturday","Sunday"):
    print("Day type : weekend - Enjoy your free time")
elif day == "Monday":
    print ("Day type : First day of your week")
elif day == "Friday":
    print("Day type : Last day of your week/school")
elif day in ("Tuesday","Wednesday","Thursday"):
    print("Day type : Theses are regular school days")
else:
    print("ERROR day is not spelled correctly ! ⚠️ Kindly check spelling")

if weather == "sunny" and homework == "yes" :
   print ("After school then go to the park as homework is complete")

if weather == "cloudy" or weather == "rainy":
    print("Weather tip : 🌧️ Take an umbrella with you.") 

if weather == "rainy" and not homework == "yes":
    print("Stay home and do assignment naughty one 🙅‍♂️")