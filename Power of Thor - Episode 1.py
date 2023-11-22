import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
lightX, lightY, thorX, thorY = [int(i) for i in input().split()]

# game loop
while 1:
    remainingTurns = int(input())
    directionX=""
    directionY=""
    if thorY>lightY:
        directionY+="N"
        thorY-=1
    elif thorY<lightY:
        directionY+="S"
        thorY+=1
    if thorX>lightX:
        directionX+="W"
        thorX+=1
    elif thorX<lightX:
        directionX+="E"
        thorX-=1
    
    print(directionY+directionX)  
