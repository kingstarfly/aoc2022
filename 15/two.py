from pathlib import Path
import re


here = Path(__file__).parent



def findTuningFrequency(filepath: Path):
    with open(filepath, "r") as fp:
        lines = fp.read().splitlines()
    
    sensors = set()

    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", line))

        manhattenDistance = abs(sx - bx) + abs(sy - by)
        sensors.add((sx, sy, manhattenDistance))
    
    for sx, sy, manhattenDistance in sensors:
        # the possible point must be manhattenDistance + 1 away from the sensor.
        # generate all these possible points and check if they are within the manhatten distance of any other sensor. 
        # if not, then this point is the solution point.
        # if so, then continue to the next point.
        manhattenDistanceOfPossiblePoint = manhattenDistance + 1

        for dx in range(manhattenDistanceOfPossiblePoint + 2):
            # dx refers to the x-displacement of the possible point from sx
            # the corresponding dy must be (manhattenDistanceOfPossiblePoint + 1) - dx
            dy = manhattenDistanceOfPossiblePoint - dx

            possiblePoints = [sx + dx, sy + dy], [sx + dx, sy - dy], [sx - dx, sy + dy], [sx - dx, sy - dy]

            for x, y in possiblePoints:
                if checkIfValidPoint(x, y, sensors):
                    return 4_000_000 * x + y

        
def checkIfValidPoint(x: int, y: int, sensors: set) -> bool:
    if x < 0 or x > 4_000_000 or y < 0 or y > 4_000_000:
        return False
    
    for sx, sy, manhattenDistance in sensors:
        if abs(sx - x) + abs(sy - y) <= manhattenDistance:
            return False

    return True

print(findTuningFrequency(here / "input.txt"))