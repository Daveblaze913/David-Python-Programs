def Calculate_change(paid_amt,actual_amt):
    change = paid_amt-actual_amt
    return change

parking_ticket_price = 25
print("======================Parking ticket news========================")
print("The price of a coin is $,:",parking_ticket_price)
print("Accepted coins 1,5,10,20,25:  ")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert coin 1,5,10,20,25: "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 20 and coin != 25:
        print("Invalid coin")
        continue
    total_inserted = total_inserted + coin
    coins_inserted += 1


    print("Inserted:",coin,"Total: ",total_inserted)
    if total_inserted >= parking_ticket_price:
        print("ENOUGH COINS INSERTED!")
        break

change_due = Calculate_change(parking_ticket_price,total_inserted)
print("Printing your parking ticket ...................")
if change_due == 0:
    pass
else:
    print("Here is your change amount  $",change_due)


print("====================Purchase Summary======================")
print("Parking Ticket",parking_ticket_price )
print("Coins inserted:",coins_inserted)
print("Total Paid:", total_inserted)
print("Change given",change_due)
print("========================================================")
print("Thanks for purchasing at the parking ticket machine")