import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

while True:
	# initialize vars
	mountainMax = 0
    mountainIndex = 0

    for i in range(8):
        mountainH = int(input())		# save current mountain
        if mountainH > mountainMax: 	# if current mountain is higher than highest mountain
            mountainIndex = i			# save the index to be destroyed
            mountainMax = mountainH		# save new highest mountain value
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(mountainIndex)
