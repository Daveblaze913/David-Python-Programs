num = int(input("Enter your number: "))
sum = 0
power=int(input("Enter your indice: "))

for i in range(1,num**power):
    sum = sum ** i
    print("Sum:  ", sum)