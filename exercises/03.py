# A robot moves in a plane starting from the original point
# (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as
# the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps.
# Please write a program to compute the distance from
# current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.

vertical = 0
lateral = 0
base = 0

while True:
    up = int(input('up: '))
    down = int(input('down: '))
    left = int(input('left: '))
    right = int(input('right: '))
    new_vertical = vertical + up - down
    new_lateral = lateral + left - right
    if abs(new_lateral) > abs(new_vertical):
        print(new_lateral)
    elif abs(new_vertical) > abs(new_lateral):
        print(new_vertical)
    elif abs(new_lateral) == abs(new_vertical):
        print(new_vertical)
    break

