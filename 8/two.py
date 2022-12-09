from collections import defaultdict
from pathlib import Path

here = Path(__file__).parent

grid = []
fp = open(here / 'input.txt', 'r')
for line in fp:
    row = []
    for c in line.strip():
        row.append(int(c))
    grid.append(row)
fp.close()

# For every tree in the grid, traverse in one of the four directions to find the distance from it to the next tree with same and higher height.
# Multiply the distances to get the total score for the current tree.
# Get the max score among all trees in the grid.

ROWS, COLS = len(grid), len(grid[0])

def getDistanceToBlockingTree(r: int, c: int, direction: str) -> int:
    # A blocking tree has height >= current tree. 
    # Trees at the edge are blocking trees.

    if direction == 'l':
        for i in range(c-1, -1, -1):
            if i == 0 or grid[r][i] >= grid[r][c]:
                return c-i
    elif direction == 'r':
        for i in range(c+1, COLS):
            if i == COLS-1 or grid[r][i] >= grid[r][c]:
                return i-c
    elif direction == 'u':
        for i in range(r-1, -1, -1):
            if i == 0 or grid[i][c] >= grid[r][c]:
                return r-i
    elif direction == 'd':
        for i in range(r+1, ROWS):
            if i == ROWS-1 or grid[i][c] >= grid[r][c]:
                return i-r

    return 0

def getScore(r: int, c: int) -> int:
    score = 1
    for direction in ['l', 'r', 'u', 'd']:
        score *= getDistanceToBlockingTree(r, c, direction)
    return score

maxScore = 0
for r in range(ROWS):
    for c in range(COLS):
        maxScore = max(maxScore, getScore(r, c))

print(maxScore)