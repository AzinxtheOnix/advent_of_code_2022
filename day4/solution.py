import re
import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")

totalPairs = 0
totalOverlaps = 0
for line in input:
    x = re.search(r"(\d+)\-(\d+)\,(\d+)\-(\d+)", line)
    elf1_lower = int(x.group(1))
    elf1_higher = int(x.group(2))
    elf2_lower = int(x.group(3))
    elf2_higher = int(x.group(4))
    
    # If elf1 has the lower or equal range
    status = 1
    overlap = 0

    if(elf1_higher-elf1_lower <= elf2_higher-elf2_lower):
        for number in range(elf1_lower, elf1_higher+1):
            if(elf2_lower <= number and number <= elf2_higher):
                overlap = 1
            if(number < elf2_lower or number > elf2_higher):
                status = 0
            if(status == 0 and overlap == 1):
                break
    else:
        for number in range(elf2_lower, elf2_higher+1):
            if(elf1_lower <= number and number <= elf1_higher):
                overlap = 1
            if(number < elf1_lower or number > elf1_higher):
                status = 0
            if(status == 0 and overlap == 1):
                break
    if(overlap == 1):
        totalOverlaps += 1
    if(status == 1):
        totalPairs += 1
print(totalPairs)
print(totalOverlaps)