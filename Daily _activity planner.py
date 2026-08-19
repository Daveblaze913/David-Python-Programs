print("=============Daily activity planner===============")

day = input("Enter your day Monday - Sunday: ").strip().capitalize()
weather = input("What is the weather for today? (Sunny/Rainy/Cloudy) : ").strip().lower()
chores = input("Have you  done your chores? (Yes/No): ").strip().lower()

print()
print("===================== Your plan for ", day , "=========================")

print("-"*50)

if day in ("Saturday","Sunday"):
    print("Day type : weekend time i spend most of the day playing and reading after praying")
elif day == "Monday":
    print ("Day type : First day of  week after praying. I go outside and play for most of the day")
elif day == "Friday":
    print("Day type : Last day of your week/school")
elif day in ("Tuesday","Wednesday","Thursday"):
    print("Day type : Theses are  days i visit my grandma neighbours and cousins after my work is done. or read the bible")
else:
    print("ERROR day is not spelled correctly ! ⚠️ Kindly check spelling")

if weather == "sunny" and chores  == "yes" :
   print (" then go to the park as chores is complete")

if weather == "cloudy" or weather == "rainy":
    print("Weather tip : 🌧️ Take an umbrella with you.") 

if weather == "rainy" and not chores == "yes":
    print("Stay home and do chores ")