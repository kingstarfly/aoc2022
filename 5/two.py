from collections import defaultdict
from pathlib import Path

here = Path(__file__).parent

stacks = defaultdict(list)

with open(here / 'input.txt', 'r') as fp:
    for line in fp:
        if line[1].isdigit():
            break

        lineLength = len(line)

        for pos in range(1, lineLength, 4):
            if line[pos] != ' ':
                i = (pos-1) // 4 + 1
                stacks[i].append(line[pos])

    # Reverse each list in the dict so that Top box is at the end of the list to make popping easier.
    for stack in stacks.values():
        stack.reverse()

    print(stacks)

    fp.readline()

    for line in fp:
        # Read only numbers from line and convert to int
        numbers = [int(x) for x in line.split() if x.isdigit()]
        
        numberToMove = numbers[0]
        source = numbers[1]
        destination = numbers[2]

        # Pop from source stack into a temporary stack
        tempStack = []
        for _ in range(numberToMove):
            tempStack.append(stacks[source].pop())

        # Pop from deque into destination stack
        while tempStack:
            stacks[destination].append(tempStack.pop())
    
    print(stacks)

    # Sort stacks based on key in dict, and get the last element in each list
    finalMessage = ''.join([stacks[key][-1] for key in sorted(stacks.keys())])
    print(finalMessage)




        