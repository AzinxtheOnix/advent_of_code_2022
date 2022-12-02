import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")

calorieTotals = []
currentTotal = 0
for calorie in input:
    if(calorie == ""):
        calorieTotals.append(currentTotal)
        currentTotal = 0
    else:
        currentTotal += int(calorie)
calorieTotals.sort()
print(calorieTotals[-1] + calorieTotals[-2] + calorieTotals[-3])