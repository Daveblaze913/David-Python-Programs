try:
    num = int(input("Enter your number "))
    num//0
except ValueError:
    print("Exception Succesfully handled")
except ZeroDivisionError:
    print ("Exception handled succesfully handled")
finally:
    print("This will be printed no matter what")