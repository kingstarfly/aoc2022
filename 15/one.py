from pathlib import Path
import re


here = Path(__file__).parent


MAX_INT = 2 ** 31 - 1
MIN_INT = -2 ** 31


def numImpossiblePositions(y: int, filepath: Path) -> int:

    with open(filepath, "r") as fp:
        lines = fp.read().splitlines()

    gridLeft, gridRight, gridTop, gridBottom = MAX_INT, MIN_INT, MAX_INT, MIN_INT
    sensors: set[tuple[int, int, int]] = set()
    beacons: set[tuple[int, int]] = set()

    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", line))
        minX = min(sx, bx)
        maxX = max(sx, bx)
        minY = min(sy, by)
        maxY = max(sy, by)
        if gridLeft is None or minX < gridLeft:
            gridLeft = minX
        if gridRight is None or maxX > gridRight:
            gridRight = maxX
        if gridTop is None or minY < gridTop:
            gridTop = minY
        if gridBottom is None or maxY > gridBottom:
            gridBottom = maxY

        manhattenDistance = abs(sx - bx) + abs(sy - by)

        sensors.add((sx, sy, manhattenDistance))
        beacons.add((bx, by))


    # Go to the row
    # For each non-beacon position, calculate the manhatten distance to each sensor.
    # Since each sensor already has a closest beacon, we can calculate the smallest manhatten distance for this sensor.
    # Compare the smallest manhatten distance to the manhatten distance from the current position to the sensor. If the current position is closer, then it is impossible.
    # If the position is impossible, increment the counter and move on to the next column. After checking against all sensors, if the position is still possible, then move on to the next column.


    numPositions = 0

    for x in range(gridLeft, gridRight + 1):
        if (x, y) in beacons:
            print("B", end="")
            continue
        isImpossible = False
        for sensor in sensors:
            manhattenDistance = abs(x - sensor[0]) + abs(y - sensor[1])
            if manhattenDistance <= sensor[2]:
                numPositions += 1
                isImpossible = True
                break
        if isImpossible:
            print("#", end="")
        else:
            print(".", end="")
    print()
    return numPositions


# assert(numImpossiblePositions(10, here/"test.txt") == 26)
# print(numImpossiblePositions(2_000_000, here/"input.txt"))
print(numImpossiblePositions(10, here/"test.txt"))
