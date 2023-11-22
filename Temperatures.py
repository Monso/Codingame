import sys
import math

# To debug: print("Debug messages...", file=sys.stderr)

n = int(input())  # the number of temperatures to analyse
if n == 0: #if there are no temps, return 0; otherwise continue
    print (n)
else:
    maxTemp = 9999
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        if abs(int(t)) < abs(int(maxTemp)):
            maxTemp = int(t)
        elif abs(int(t)) == abs(int(maxTemp)):
            maxTemp = max(int(t), int(maxTemp))
    
    print(maxTemp)
