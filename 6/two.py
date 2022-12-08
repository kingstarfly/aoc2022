from collections import defaultdict
from pathlib import Path

here = Path(__file__).parent

with open(here / 'test.txt', 'r') as fp:
    counts = [0] * 26
    numDifferent = 0

    line = fp.readline()
    print(line)
    
    assert len(line) >= 14
    for i in range(14):
        indexToIncrement = ord(line[i]) - ord('a')
        counts[indexToIncrement] += 1
        if counts[indexToIncrement] == 1:
            numDifferent += 1
            if numDifferent == 14:
                print(i+1)
                exit(0)  
    
    
    for i in range(14, len(line)):
        indexToDecrement = ord(line[i-14]) - ord('a')
        indexToIncrement = ord(line[i]) - ord('a')

        counts[indexToDecrement] -= 1
        if counts[indexToDecrement] == 0:
            numDifferent -= 1

        counts[indexToIncrement] += 1

        if counts[indexToIncrement] == 1:
            numDifferent += 1
            if numDifferent == 14:
                print(i+1)
                exit(0)
        




        


    
