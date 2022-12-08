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
        
        bigger = a
        smaller = b
        if b[1] - b[0] > a[1] - a[0]:
            bigger = b
            smaller = a
        
        # if smaller is within bigger, then increment count
        if smaller[0] >= bigger[0] and smaller[1] <= bigger[1]:
            count += 1
    
print(count)