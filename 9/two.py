from collections import defaultdict
from pathlib import Path
here = Path(__file__).parent

commands = []
fp = open(here / 'input.txt', 'r')
for line in fp:
    commands.append(line.strip().split(" "))
fp.close()

class Node:
    x: int
    y: int
    leader: "Node"

    def __init__(self) -> None:
        self.x = 0
        self.y = 0


    def catchup(self) -> None:
        xDisplacement = self.leader.x - self.x
        yDisplacement = self.leader.y - self.y

        if abs(xDisplacement) >= 2 or abs(yDisplacement) >= 2:
            if xDisplacement > 0: self.x += 1
            elif xDisplacement < 0: self.x -= 1

            if yDisplacement > 0: self.y += 1
            elif yDisplacement < 0: self.y -= 1

# Create 10 Nodes and connect them in a chain
NUM_NODES = 10
nodes = [Node() for _ in range(NUM_NODES)]
for i in range(1, len(nodes)):
    nodes[i].leader = nodes[i-1]


visitedPositions = set()
visitedPositions.add((nodes[NUM_NODES-1].x, nodes[NUM_NODES-1].y))

for command in commands:
    direction, distance = command[0], int(command[1])

    for _ in range(distance):
        if direction == 'L':
            nodes[0].x -= 1
        elif direction == 'R':
            nodes[0].x += 1
        elif direction == 'U':
            nodes[0].y += 1
        elif direction == 'D':
            nodes[0].y -= 1

        for node in nodes[1:]:
            node.catchup()

        if (nodes[-1].x, nodes[-1].y) not in visitedPositions:
            visitedPositions.add((nodes[-1].x, nodes[-1].y))

print(nodes[-1].x, nodes[-1].y)
print(len(visitedPositions))



