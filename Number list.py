Numberlist1 = [1,5,20,30]
sum = 0
for i in Numberlist1:
    sum = sum+i

avg = sum/len(Numberlist1)
print("The avg is :",avg)

Numberlist1.sort()
print(Numberlist1)
print("smallest element is ",Numberlist1[0])
print("largest element is ",Numberlist1[-1])