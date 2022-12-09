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


maxEachDirection = defaultdict(list)
# l, r, u, d

ROWS, COLS = len(grid), len(grid[0])

for r in range(ROWS):
    maxValues = [-1] * ROWS
    for c in range(COLS):
        maxEachDirection[(r, c)].append(maxValues[r])
        maxValues[r] = max(maxValues[r], grid[r][c])

    maxValues = [-1] * ROWS
    for c in range(COLS - 1, -1, -1):
        maxEachDirection[(r, c)].append(maxValues[r])
        maxValues[r] = max(maxValues[r], grid[r][c])

for c in range(COLS):
    maxValues = [-1] * COLS
    for r in range(ROWS):
        maxEachDirection[(r, c)].append(maxValues[c])
        maxValues[c] = max(maxValues[c], grid[r][c])

    maxValues = [-1] * COLS
    for r in range(ROWS - 1, -1, -1):
        maxEachDirection[(r, c)].append(maxValues[c])
        maxValues[c] = max(maxValues[c], grid[r][c])

count = 0
for r in range(ROWS):
    for c in range(COLS):
        minSurrounding = min(maxEachDirection[(r, c)])
        visible = False
        if grid[r][c] > minSurrounding:
            count += 1
            visible = True
        # print(f"{grid[r][c]} vs {minSurrounding} {visible}", end=" | ")
    print()

        
print(count)