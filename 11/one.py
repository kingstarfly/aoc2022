# Read all lines from the file "input.txt"

from collections import deque
from pathlib import Path
from typing import Optional


here = Path(__file__)

with open(here.parent / "input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

monkeys = []

class Monkey:
    numberItemsInspected: int
    items: deque[int]
    operation: str
    modulus: int
    targetIfTrue: "Monkey"
    targetIfFalse: "Monkey"


    def __init__(self, lines: Optional[list[str]] = None):
        self.numberItemsInspected = 0

        if lines:
            self.parseLines(lines)

    def parseLines(self, lines: list[str]):
        self.items = deque([int(x) for x in lines[1].strip().split(":")[-1].split(", ") if len(x) > 0])
        self.operation = lines[2].strip().split("=")[1]
        self.modulus = int(lines[3].strip().split(" ")[-1])
        self.targetIfTrue = monkeys[int(lines[4].strip().split(" ")[-1])]
        self.targetIfFalse = monkeys[int(lines[5].strip().split(" ")[-1])]
        
    def takeOneTurn(self):
        self.numberItemsInspected += len(self.items)

        while self.items:
            item = self.items.popleft()

            # use eval() to evaluate the expression
            new = eval(self.operation.replace("old", str(item)))

            # Divide by 3 and round down to nearest integer.
            new = new // 3

            if self.testCondition(new):
                self.targetIfTrue.receiveItem(new)
            else:
                self.targetIfFalse.receiveItem(new)


    def testCondition(self, item: int) -> bool:
        return item % self.modulus == 0     
        

    # Called by other Monkey objects.
    def receiveItem(self, item: int) -> None:
        self.items.append(item)
        return

numMonkeys = (len(lines) + 1 ) // 7

# Create as many monkey objects here as necessary. 
for i in range(numMonkeys):
    monkey = Monkey()
    monkeys.append(monkey)


# Parse the lines into the monkey objects.
for i in range(numMonkeys):
    monkeys[i].parseLines(lines[i * 7 : (i + 1) * 7])

    
NUM_ROUNDS = 20
for i in range(NUM_ROUNDS):
    for monkey in monkeys:
        monkey.takeOneTurn()

# Find top two monkeys with most number of items inspected.
topMonkeys = sorted(monkeys, key=lambda monkey: monkey.numberItemsInspected, reverse=True)[:2]

print(topMonkeys[0].numberItemsInspected * topMonkeys[1].numberItemsInspected)