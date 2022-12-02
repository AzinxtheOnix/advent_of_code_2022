import re
import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")

opponentMapping = ("A", "B", "C")
playerMapping = ("X", "Y", "Z")
score = (1, 2, 3)

totalScore = 0
for play in input:
    x = re.search(r"(\S)\s(\S)", play)
    opponent = x.group(1)
    player = x.group(2)

    opponentLocation = opponentMapping.index(opponent)
    playerLocation = playerMapping.index(player)

    if(player == playerMapping[opponentLocation-1]):   # If the player is the previous item, player loses
        totalScore += score[playerLocation]
    elif(playerLocation == opponentLocation):   # Both tie
        totalScore += score[playerLocation] + 3
    else:   # The player must have won
        totalScore += score[playerLocation] + 6
print(totalScore)

totalScore = 0
for play in input:
    x = re.search(r"(\S)\s(\S)", play)
    opponent = x.group(1)
    player = x.group(2)

    opponentLocation = opponentMapping.index(opponent)

    if(player == "X"):      # Lose
        totalScore += score[opponentLocation-1]
    elif(player == "Y"):    # Tie
        totalScore += score[opponentLocation] + 3
    else:   # Win
        if(opponentLocation == 2):
            opponentLocation = -1
        totalScore += score[opponentLocation+1] + 6

print(totalScore)