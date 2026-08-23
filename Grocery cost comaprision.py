Grocery_cost1 = int(input("Enter your grocery cost for 1st grocery: "))
Grocery_cost2 = int(input("Enter your grocery cost for 2nd grocery: "))
if Grocery_cost1 % Grocery_cost2 ==0:
    print("Grocery cost for 1st item is Divisible by the cost of the 2nd Grocery item's price")
else:
    print("Grocery cost for 1st item  is  not Divisible the cost of the 2nd Grocery item's price")

grocery_cost_total = Grocery_cost1+Grocery_cost2
mean = 40
wrong_number = 78
right_number = 102

sum = grocery_cost_total*mean
print("Sum of all 40 numbers ;",sum)

num2 = sum - ((wrong_number) - (right_number))
print("New num2 is wrong_number - right number")

mean2 = num2 /grocery_cost_total
print("Updated mean : ",mean2)

Store1 = 240
Store2 = 210
Store3 = 200

total_grocery_store_revenue = Store1+Store2+Store3
avg_revenue_made = total_grocery_store_revenue/3

print("The average revenue for all 3 stores is:", avg_revenue_made)

if Store1 < avg_revenue_made:
    print(" The 1st store revenue is lower than avg revenue of all 3 stores")
elif Store2 < avg_revenue_made:
    print("The 2nd store revenue is lower than the avg revenue of all 3 ")
elif Store3 < avg_revenue_made:
    print("The 3rd store revenue  is  lower than the average revenue of all 3")