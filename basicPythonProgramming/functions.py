def payment (hours, rate) :
    if hours > 40:
        ord = hours * rate
        ot = (hours - 40) * (rate * 0.5)
        total = ord + ot
    else:
        total = hours * rate
    return total

sh= input("Enter hours:")
sr = input ("Enter rate:")

hours = float(sh)
rate = float(sr)

xp =payment(hours, rate)
print ("your pay is", xp)