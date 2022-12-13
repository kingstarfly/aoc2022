from collections import deque
from pathlib import Path


here = Path(__file__)

with open(here.parent / "input.txt") as f:
    lines = f.read().splitlines()


# Map a-z to 1-26. S is 1, E is 26.
startingPositions = []
endPosition = (0, 0)


grid = []
for r, line in enumerate(lines):
    row = []
    for c, char in enumerate(line):
        if char == "E":
            endPosition = (r, c)
            row.append(26)
        elif char == "S":
            startingPositions.append((r, c))
            row.append(1)
        else:
            if char == "a":
                startingPositions.append((r, c))
            row.append(ord(char) - ord("a") + 1)

    grid.append(row)

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def getShortestDistance(startingPosition: tuple[int, int], endPosition: tuple[int, int]) -> int:

    queue = deque()
    queue.append(startingPosition)

    visited = set()

    distances = {}
    distances[startingPosition] = 0
    distances[endPosition] = float("inf")

    previous = {}

    while queue:

        (r, c) = queue.popleft()

        if (r, c) == endPosition:
            break

        if (r, c) not in visited:
            visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] > grid[r][c] + 1 or (nr, nc) in visited:
                    continue
            
                queue.append((nr, nc))

                if (nr, nc) not in distances or distances[(nr, nc)] > distances[(r, c)] + 1:
                    distances[(nr, nc)] = distances[(r, c)] + 1
                    previous[(nr, nc)] = (r, c)

    return distances[endPosition]

globalShortest = float("inf")
for i in range(len(startingPositions)):
    shortestDistance = getShortestDistance(startingPositions[i], endPosition)
    
    print(shortestDistance)

    globalShortest = min(globalShortest, shortestDistance)

print(globalShortest)