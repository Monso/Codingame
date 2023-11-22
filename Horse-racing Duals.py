import sys
import math

numHorses = int(input())

hList = []
for i in range(numHorses): # create array of horses
    hList.append(input())
hList.sort(key = int, reverse = True) # sort list

closest = hList[0] # set initial value to highest strength

for i in range(numHorses): # iterate through sorted list comparing differences
    if i == numHorses - 1: #stay within array limits
        break
    hOld = hList[i] # set existing horse to current index
    hNew = hList[i+1] # set comparison hrose as next index
    if (int(hOld) - int(hNew)) < int(closest): # if different is less than closest
        closest = int(hOld) - int(hNew) # save new closest

print(closest)
print("Debug messages...", file=sys.stderr)
