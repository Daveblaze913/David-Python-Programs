def match_word(words):
    count  = 0
    list1 = []
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            count = count + 1 
            list1. append(i)

    print("List of strings that have the same first and last letter: ",list1)
    return count

count = match_word(["awa" ,"GFG", "BCH", "OPK"])
print(count)