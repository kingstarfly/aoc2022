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




numPairs = (len(lines) + 1) // 3
sumOfCorrectIndices = 0

for i in range(numPairs):
    list1 = eval(lines[3 * i].strip())
    list2 = eval(lines[3 * i + 1].strip())
    
    if compareLists(list1, list2) == -1:
        print(i+1, list1, list2)
        sumOfCorrectIndices += i + 1
    

print(sumOfCorrectIndices)


