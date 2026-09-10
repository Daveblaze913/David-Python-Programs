def greet_customer():
    print("Welcome to aRT SUPLLY shop!")
    print("Enjoy getting art supplies freely . ")

greet_customer()

price_per_supply = int(input("Enter the cost for your art supplies : "))
supplies_sold = int(input("Enter the number of art supplies sold today: "))

def calculate_total(price,cups):
    total = price*cups
    return total
total_cost = calculate_total(price_per_supply, supplies_sold)
rounded_total = round(total_cost,2)
print(rounded_total)
def calculate_change(paid,total):
    change = paid - total
    return change
amount_paid = int(input("Enter the amount paid by customer: "))

change_due = calculate_change(amount_paid , total_cost)
round_change = round(change_due,2)

def thankyou_message(cup):
    if cup>=5:
        return "Wow Big order thank you for your support"
    else:
        return "Thank you have a nice day"

closing_message = thankyou_message(supplies_sold)
print(" ")
print("=================== Art supllies reciept=======================")
print("Price per supply: ",price_per_supply)
print("No. of Supplies sold : ", supplies_sold)
print("Total cost: ", rounded_total)
print("Amount paid: ", amount_paid)
print("Due amount: ", round_change)
print(closing_message)
print("================================================================")