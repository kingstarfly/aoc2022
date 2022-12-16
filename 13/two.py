from functools import cmp_to_key
from pathlib import Path


here = Path(__file__).parent

with open(here / 'input.txt') as f:
    lines = f.read().splitlines()


# Returns -1 if list1 is "smaller" than list2, 0 if they are equal, and 1 if list1 is "larger" than list2
def compareLists(list1: list, list2: list) -> int:
    for i in range(max(len(list1), len(list2))):
        if i >= len(list1):
            return -1
        if i >= len(list2):
            return 1

        result = compareElements(list1[i], list2[i])
        if result != 0:
            return result

    return 0

# Returns -1 if element1 is "smaller" than element2, 0 if they are equal, and 1 if element1 is "larger" than element2
def compareElements(element1, element2) -> int:

    # If both elements are lists, then use compareLists
    if type(element1) == list and type(element2) == list:
        return compareLists(element1, element2)

    # If both elements are integers, then compare them
    if type(element1) == int and type(element2) == int:
        if element1 < element2:
            return -1
        elif element1 == element2:
            return 0
        else:
            return 1

    # If either element is an integer, then replace it with a list of that integer and use compareLists
    return compareLists(element1 if type(element1) == list else [element1], element2 if type(element2) == list else [element2])



lines = [line for line in lines if line != '']

lines.append("[[2]]")
lines.append("[[6]]")

def comparator(line1: str, line2: str) -> int:
    list1 = eval(line1)
    list2 = eval(line2)
    return compareLists(list1, list2)
    
sortedLines = sorted(lines, key=cmp_to_key(comparator)) 

firstIndex = sortedLines.index("[[2]]")
secondIndex = sortedLines.index("[[6]]")

print(firstIndex + 1, secondIndex + 1)
print((firstIndex + 1) * (secondIndex + 1))