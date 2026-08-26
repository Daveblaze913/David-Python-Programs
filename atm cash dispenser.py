print("================ ATM CASH DISPENSER ============")
total_100 =total_50 = total_20 = total_10 = total_5 = total_1 = 0
cutomers_served = 0
total_dispensed = 0

serving = True
while  serving:
    name= input("Enter user's name")
    WithdrawAmt = int(input("Enter amount to be writhdrawn: "))
    if WithdrawAmt <=0:
        print("Invalid input")
        continue

    print("Dispensing", WithdrawAmt,"units from", name)
    remainingAmt = WithdrawAmt
    idx = 1
    while idx <=6: 
        if idx ==1: value=100
        elif idx ==2: value=50
        elif idx ==3: value =20
        elif idx ==4: value = 10
        elif idx ==5: value = 5
        else : value = 1
        count = remainingAmt // value
        if count > 0:
            remainingAmt  -= count*value
            if value == 100: total_100+=count
            elif value == 50: total_50+=count
            elif value == 20: total_20+=count
            elif value == 10: total_10+=count
            elif value == 5: total_5+= count
            elif value == 1 : total_15+= count
            else: total_1 += count
    idx = idx + 1
    customers_Served = cutomers_served = + 1
    total_dispensed = total_dispensed +WithdrawAmt
    print("Transaction complete : ",name)

print("Customers served :", customers_Served)
print("Total dispensed : ",total_dispensed)
 
