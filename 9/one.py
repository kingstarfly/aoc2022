from collections import defaultdict
from pathlib import Path

here = Path(__file__).parent

commands = []
fp = open(here / 'input.txt', 'r')
for line in fp:
    commands.append(line.strip().split(" "))
fp.close()

print(commands)



'''
1. Move H according to the current command one step at a time. Commands are of the form [direction, distance], where direction is one of L, R, U, D and distance is an string digit.
2. For each step that H moves, L keeps track of the distance from H in terms of x and y coordinates. If L is at (x, y) and H is at (x+2, y), then distance from H is (2, 0).

3. If the distance in the x axis has absolute value of 2 or more, than move L in the x axis by distance/2. Move L in the y axis by the y-distance too.

4. Vice versa for the y axis.

5. Whenever L moves to a new position, check if it has been visited before. If it has, then increment the counter. Also, add the new position to the set of visited positions.

'''
# Source: L, Target: H
xDisplacement = 0
yDisplacement = 0

x, y = 0, 0
visitedPositions = set()
visitedPositions.add((x, y))
uniquePositionsVisitedByTail = 1 # starting position has already been visited

for command in commands:
    direction, distance = command[0], int(command[1])

    for _ in range(distance):
        if direction == 'L':
            xDisplacement -= 1
        elif direction == 'R':
            xDisplacement += 1
        elif direction == 'U':
            yDisplacement += 1
        elif direction == 'D':
            yDisplacement -= 1

        if abs(xDisplacement) >= 2:
            x += xDisplacement // 2
            xDisplacement //= 2

            if yDisplacement != 0:
                y += yDisplacement
                yDisplacement = 0

            if (x, y) not in visitedPositions:
                visitedPositions.add((x, y))
                uniquePositionsVisitedByTail += 1

        elif abs(yDisplacement) >= 2:
            y += yDisplacement // 2
            yDisplacement //= 2

            if xDisplacement != 0:
                x += xDisplacement
                xDisplacement = 0

            if (x, y) not in visitedPositions:
                visitedPositions.add((x, y))
                uniquePositionsVisitedByTail += 1

    print(f"L: ({x}, {y})")

print(uniquePositionsVisitedByTail)