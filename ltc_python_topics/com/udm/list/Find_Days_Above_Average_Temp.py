numDays = int(input("How many day's Temp? "))
total = 0
temp = []

for i in range(numDays):
    nxtDay = int(input("Day " + str(i+1) + "'s high temp:"))
    temp.append(nxtDay)
    total += temp[i]

average = round(total/numDays, 2)
print("\nAverage = " + str(average))

aboveTemp = 0
for i in temp:
    if i > average:
        aboveTemp += 1
print(str(aboveTemp) + "day(s) above average")
