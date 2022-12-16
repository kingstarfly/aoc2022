from pathlib import Path


here = Path(__file__).parent
with open(here / "input.txt", "r") as fp:
    lines = fp.read().splitlines()

# 1. Use a set to keep track of the occupied positions (can be rock or sand).
# 2. Create a Sand class that has fallTillAtRest method which returns the position where it will rest.
# 3. The sand class will also check that it's y position is not lower than the lowest rock. If so, then stop the simulation and report the number of sand particles.

class Sand:
    x: int
    y: int
    particleId: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particleId = 0

    def reset(self):
        self.x = 500
        self.y = 0
        self.particleId += 1


    def fallTillAtRest(self, occupiedPositions: set[tuple[int, int]], largestY: int) -> tuple[int, int]:
    
        while True:
            # 3 possible positions - x, y + 1, x - 1, y + 1, x + 1, y + 1
            x = self.x
            y = self.y

            # The sand particle has fallen past the lowest rock. Return (-1, -1) to indicate that the simulation should stop.
            if y + 1 > largestY:
                return (-1, -1)

            possiblePositions = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]

            atRest = True
            for nextPosition in possiblePositions:
                if nextPosition not in occupiedPositions:
                    # print(f"({x}, {y}) -> ({nextPosition[0]}, {nextPosition[1]})")
                    self.x, self.y = nextPosition
                    atRest = False
                    break
            
            if atRest:
                print(f"Particle ended at {self.x}, {self.y}")
                return self.x, self.y

def parseLines(lines: list[str], occupiedPositions: set[tuple[int, int]]) -> int:
    # Parse the lines and add the occupied positions to the set. Return the largest y value.
    largestY = 0
    for line in lines:
        prevX = -1
        prevY = -1
        for pair in map(str.strip, line.split("->")):
            x, y = map(int, pair.split(","))
            if prevX != -1 and prevY != -1:
                # Add all the positions between the previous and current position to the occupied positions.
                if prevX == x:
                    # Vertical line
                    smallerY = min(prevY, y)
                    biggerY = max(prevY, y)

                    for ny in range(smallerY, biggerY + 1):
                        occupiedPositions.add((x, ny))

                elif prevY == y:
                    # Horizontal line
                    smallerX = min(prevX, x)
                    biggerX = max(prevX, x)

                    for nx in range(smallerX, biggerX + 1):
                        occupiedPositions.add((nx, y))

            else:
                occupiedPositions.add((x, y))

            prevX = x
            prevY = y
            largestY = max(largestY, y)

    return largestY


def main():
    occupiedPositions = set()
    largestY = parseLines(lines, occupiedPositions)

    sandParticle = Sand(500, 0)
    while True:
        restX, restY = sandParticle.fallTillAtRest(occupiedPositions, largestY)
        if (restX, restY) == (-1, -1):
            print("Simulation stopped")
            return sandParticle.particleId + 1 # Add 1 since the particle that blocks the source should also be counted.
        else:
            occupiedPositions.add((restX, restY))
            sandParticle.reset()
        

if __name__ == "__main__":
    print(main())

