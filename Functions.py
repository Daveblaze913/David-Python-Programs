def greet_customer():
    print("Welcome to lemonade stand!")
    print("Enjoy your fresh lemonade just made for you . ")

greet_customer()

price_per_cup = int(input("Enter the cost for your cup: "))
cups_sold = int(input("Enter the number of cups sold today: "))

def calculate_total(price,cups):
    total = price*cups
    return total
total_cost = calculate_total(price_per_cup, cups_sold)
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

closing_message = thankyou_message(cups_sold)
print(" ")
print("====================Lemonade stand reciept=======================")
print("Price per cup: ",price_per_cup)
print("No. of cups sold : ", cups_sold)
print("Total cost: ", rounded_total)
print("Amount paid: ", amount_paid)
print("Due amount: ", round_change)
print(closing_message)
print("================================================================")