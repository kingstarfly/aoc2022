from collections import defaultdict
from pathlib import Path

here = Path(__file__).parent

with open(here / 'input.txt', 'r') as fp:
    counts = [0] * 26
    numDifferent = 0

    line = fp.readline()
    print(line)
    
    assert len(line) >= 4
    for i in range(4):
        indexToIncrement = ord(line[i]) - ord('a')
        counts[indexToIncrement] += 1
        if counts[indexToIncrement] == 1:
            numDifferent += 1
            if numDifferent == 4:
                print(i+1)
                exit(0)  
    
    
    for i in range(4, len(line)):
        indexToDecrement = ord(line[i-4]) - ord('a')
        indexToIncrement = ord(line[i]) - ord('a')

        counts[indexToDecrement] -= 1
        if counts[indexToDecrement] == 0:
            numDifferent -= 1

        counts[indexToIncrement] += 1

        if counts[indexToIncrement] == 1:
            numDifferent += 1
            if numDifferent == 4:
                print(i+1)
                exit(0)
        




        


    
