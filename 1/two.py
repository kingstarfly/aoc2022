import heapq
from pathlib import Path


here = Path(__file__).parent

topThree = []

# Read file input.txt
with open(here / 'input.txt', 'r') as fp:
    currentCalories = 0
    # For each line in the file, add the calories to the currentCalories until the line is empty
    for line in fp:
        if line == '\n':
            if len(topThree) < 3:
                heapq.heappush(topThree, currentCalories)
            else:
                third = topThree[0]
                if currentCalories > third:
                    heapq.heappushpop(topThree, currentCalories)
            currentCalories = 0
        else:
            currentCalories += int(line)
    
print(sum(topThree))
        







