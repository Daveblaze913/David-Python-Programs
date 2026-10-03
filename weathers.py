weather = (0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0)
sunny = 0
rainy = 0
for i in weather:
    if weather[1] == 0:
        sunny+=1
    else:
        rainy+=1
if sunny > rainy:
    print("Its a good weather")
else:
    print("Its raining outside")