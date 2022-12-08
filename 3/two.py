from itertools import islice
from pathlib import Path

here = Path(__file__).parent

score = 0

with open(here / 'input.txt', 'r') as fp:
    while True:
        try :
            
            # Read next 3 lines and store into a list
            rucksacks = [next(fp).strip() for x in range(3)]

            # Convert each rucksack into a set
            rucksacks = [set(rucksack) for rucksack in rucksacks]

            # Find the overlap of the three rucksacks
            overlap = rucksacks[0] & rucksacks[1] & rucksacks[2]

            # Assert that the length of the overlap is 1
            assert len(overlap) == 1

            # Get the element of the overlap
            element = overlap.pop()

            # Convert the element to the priority
            # If a = 1, z = 26, A = 27, Z = 52
            if element.islower():
                priority = ord(element) - ord('a') + 1
            else:
                priority = ord(element) - ord('A') + 27

            # Add the priority to the score
            print(element, priority)
            score += priority       
        except StopIteration:
            break
     

print(score)



