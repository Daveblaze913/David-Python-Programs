field1 = 150
field2 = 250
field3 = 350
field4 = 450
field5 = 550
totalgrain = field1 + field2 + field3 + field4 + field5
avg = totalgrain/5
print("Total harvest: ", totalgrain, "Kg")
print("Avg", avg , "Kg")

price_per_kg = 75
earnings = totalgrain * price_per_kg
print("Total Earnings: $", earnings )

bags = totalgrain // 25
leftover = totalgrain% 25

print("Full bag packed:", bags)
print("Left over grain:", leftover)

lastyear=1200
print("Better than Last year ?",totalgrain>lastyear)
print("Same as last year: ", totalgrain == lastyear )
totalgrain+=30
print("Bonus crop:",totalgrain)
totalgrain-=15
print("After reserving seed for next season: ", totalgrain)
