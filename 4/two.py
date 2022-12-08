from pathlib import Path

here = Path(__file__).parent

count = 0

with open(here / 'input.txt', 'r') as fp:
    for line in fp:
        a, b = line.strip().split(",")
        a = a.split("-")
        a = [int(x) for x in a]
        b = b.split("-")
        b = [int(x) for x in b]
        
        first = a
        second = b
        
        if a[0] > b[0]:
            first = b
            second = a
        
        # If first and second overlap, then increment count.
        if second[0] <= first[1]:
            count += 1
    
print(count)