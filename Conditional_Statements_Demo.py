temperature = int(input("Enter your temperature"))

if temperature<20:
    outfit = "Jacket"
    print("it is cold outside")
    print("Wear a ",outfit)
else:
    outfit = "T-shirt"
    print("It's warm outside")
    print("Wear a ", outfit) 

is_raining = input("Is it raining outside ? (yes/no) : ")

if is_raining == "yes" :
    print("Bring an Umbrella")

wind_speed = int(input(" Enter your windspeed in Km/h :"))
if wind_speed>20 :
    needs_windbreaker = "yes"
    print("It's windy today")
    print("You might need a windbreaker over your", outfit)
else :
    needs_windbreaker = "no"
    print("It's  not windy today it's calm")
    print("You might not need a windbreaker over your", outfit)

has_puddles = input("Are there puddles on the ground? (Yes/No) : ")
if has_puddles == "yes" :
    shoes = "Boots"
    print("The ground is wet wear ", shoes)
else :
    shoes = "Sneakers"
    print("The ground is dry no need to wear ", shoes)
