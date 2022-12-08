from collections import defaultdict
from pathlib import Path

here = Path(__file__).parent

stacks = defaultdict(list)

with open(here / 'input.txt', 'r') as fp:
    # Parse initial crates: 
    # 1. Find out number of stacks and create a dict with stack number as key and an empty list as value
    # 2. For each row, parse each crate and add to appropriate list if create is not an empty string. Do this until the 2nd character in the row is a digit.
    # 3. Reverse each list in the dict so that Top box is at the end of the list to make popping easier.
    
    
    # Line looks like [A] [B] [C]    [E]
    
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

        # Pop numberToMove from source stack and append to destination stack
        for _ in range(numberToMove):
            stacks[destination].append(stacks[source].pop())
    
    print(stacks)

    # Sort stacks based on key in dict, and get the last element in each list
    finalMessage = ''.join([stacks[key][-1] for key in sorted(stacks.keys())])
    print(finalMessage)




        