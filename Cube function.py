def cubefuntion(num):
    return num**3
def divisileby3(num):
    if num  % 3 == 0:
        return cubefuntion(num)
    else:
        return False

print(divisileby3())