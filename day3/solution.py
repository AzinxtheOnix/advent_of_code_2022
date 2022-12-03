import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")

lowerMapping = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upperMapping = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

priorityTotal = 0
for sack in input:
    compartment1 = sack[:int(len(sack)/2)]
    compartment2 = sack[int(len(sack)/2):]
    
    for letter in compartment1:
        if(letter in compartment2):
            if(letter in lowerMapping):
                priorityTotal += lowerMapping.index(letter) + 1
            else:
                priorityTotal += upperMapping.index(letter) + 27
            break
print(priorityTotal)

priorityTotal = 0
for group in range(0, len(input), 3):
    elf1 = input[group]
    elf2 = input[group+1]
    elf3 = input[group+2]

    possibleMatches = []
    for letter in elf1:
        if(letter in elf2):
            possibleMatches.append(letter)

    for letter in possibleMatches:
        if(letter in elf3):
            if(letter in lowerMapping):
                priorityTotal += lowerMapping.index(letter) + 1
            else:
                priorityTotal += upperMapping.index(letter) + 27
            break
print(priorityTotal)