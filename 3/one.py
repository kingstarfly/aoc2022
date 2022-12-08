from pathlib import Path

here = Path(__file__).parent

score = 0

with open(here / 'input.txt', 'r') as fp:
    for line in fp:
        line = line.strip()

        # Split line into two equal halves
        compartmentLength = len(line) // 2
        a = line[:compartmentLength]
        b = line[compartmentLength:]

        # Convert each substring to a set
        a = set(a)
        b = set(b)

        # Find the intersection of the two sets
        intersection = a & b

        # Assert that the length of the intersection is 1
        assert len(intersection) == 1

        # Get the element of the intersection
        element = intersection.pop()

        # Convert the element to the priority
        # If a = 1, z = 26, A = 27, Z = 52
        if element.islower():
            priority = ord(element) - ord('a') + 1
        else:
            priority = ord(element) - ord('A') + 27
        # print(element, priority)

        # Add the priority to the score
        score += priority

print(score)



