from pathlib import Path


here = Path(__file__).parent

with open(here / "input.txt", "r") as fp:
    line = fp.read().strip()
    directions = [char for char in line]


'''
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
'''
GRID_X_MAX = 6


def getNextRock(rockCount: int, prevMaxHeight: int) -> set[tuple[int ,int]]:
    type = rockCount % 5

    if type == 0:
        return {(2, prevMaxHeight + 4), (3, prevMaxHeight + 4), (4, prevMaxHeight + 4), (5, prevMaxHeight + 4)}
    elif type == 1:
        return {(3, prevMaxHeight + 4), (2, prevMaxHeight + 5), (3, prevMaxHeight + 5), (4, prevMaxHeight + 5), (3, prevMaxHeight + 6)}
    elif type == 2:
        return {(2, prevMaxHeight + 4), (3, prevMaxHeight + 4), (4, prevMaxHeight + 4), (4, prevMaxHeight + 5), (4, prevMaxHeight + 6)}
    elif type == 3:
        return {(2, prevMaxHeight + 4), (2, prevMaxHeight + 5), (2, prevMaxHeight + 6), (2, prevMaxHeight + 7)}
    elif type == 4:
        return  {(2, prevMaxHeight + 4), (3, prevMaxHeight + 4), (2, prevMaxHeight + 5), (3, prevMaxHeight + 5)}
    else:
        raise Exception("Invalid type of rock")

def moveLeft(currentRock: set[tuple[int, int]], rocks: set[tuple[int, int]]) -> set[tuple[int, int]]:
    for x, y in currentRock:
        if x == 0 or (x - 1, y) in rocks:
            return currentRock
    
    return {(x - 1, y) for x, y in currentRock}

def moveRight(currentRock: set[tuple[int, int]], rocks: set[tuple[int, int]]) -> set[tuple[int, int]]:
    for x, y in currentRock:
        if x == GRID_X_MAX or (x + 1, y) in rocks:
            return currentRock
    
    return {(x + 1, y) for x, y in currentRock}

def moveDownDangerously(currentRock: set[tuple[int, int]]) -> set[tuple[int, int]]:    
    # Does not check for collision with other rocks
    return {(x, y - 1) for x, y in currentRock}

def moveUpDangerously(currentRock: set[tuple[int, int]]) -> set[tuple[int, int]]:
    # Does not check for collision with other rocks
    return {(x, y + 1) for x, y in currentRock}

def showAllRocks(currentRock: set[tuple[int, int]], rocks: set[tuple[int, int]]):
    maxHeight = max(max(y for _, y in rocks), max(y for _, y in currentRock))
    for y in range(maxHeight, -1, -1):
        for x in range(GRID_X_MAX + 1):
            if (x, y) in rocks:
                print("#", end="")
            elif (x, y) in currentRock:
                print("@", end="")
            else:
                print(".", end="")
        print()

rocks: set[tuple[int, int]] = set([(x, 0) for x in range(GRID_X_MAX + 1)])
directionIndex = 0
currentRock = set()
maxHeight = 0
rockCount = 0
currentRock = getNextRock(rockCount, maxHeight)
print(f"rockCount = {rockCount}")

while rockCount < 2022:

    # showAllRocks(currentRock, rocks)

    # Push by direction
    if directions[directionIndex] == "<":
        currentRock = moveLeft(currentRock, rocks)
    elif directions[directionIndex] == ">":
        currentRock = moveRight(currentRock, rocks)
    else:
        raise Exception("Invalid direction")

    # Move down
    currentRock = moveDownDangerously(currentRock)
    if currentRock & rocks:
        # Collision
        currentRock = moveUpDangerously(currentRock)
        rocks |= currentRock
        maxHeight = max(y for _, y in rocks) # potentially slow

        rockCount += 1
        currentRock = getNextRock(rockCount, maxHeight)
        # print(f"rockCount = {rockCount}")

    directionIndex = (directionIndex + 1) % len(directions)

print(maxHeight)

    
