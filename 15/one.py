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


    # We can find the x range of impossible positions for each sensor on the desired y value.
    # We can then sort the ranges by the start of the range and merge overlapping ranges.
    # The number of impossible positions is the sum of the lengths of the ranges, minus any beacons in the ranges.

    ranges = []
    for sx, sy, manhattenDistance in sensors:
        xDisplacement = manhattenDistance - abs(sy - y)
        if xDisplacement < 0:
            continue
        xRange = (sx - xDisplacement, sx + xDisplacement)
        ranges.append(xRange)
    
    ranges.sort(key=lambda x: x[0])
    mergedRanges = []
    for xRange in ranges:
        if not mergedRanges or xRange[0] > mergedRanges[-1][1]:
            mergedRanges.append(xRange)
        else:
            mergedRanges[-1] = (mergedRanges[-1][0], max(mergedRanges[-1][1], xRange[1]))
    
    numImpossiblePositions = 0
    for xRange in mergedRanges:
        for bx, by in beacons:
            if bx >= xRange[0] and bx <= xRange[1] and by == y:
                numImpossiblePositions -= 1

        numImpossiblePositions += xRange[1] - xRange[0] + 1
    
    return(numImpossiblePositions)

# assert(numImpossiblePositions(10, here/"test.txt") == 26)
print(numImpossiblePositions(2_000_000, here/"input.txt"))
# print(numImpossiblePositions(10, here/"test.txt"))
