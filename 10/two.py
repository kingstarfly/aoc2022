from collections import deque
from pathlib import Path


here = Path(__file__).parent

# Read from file "input.txt" in the same directory as this file
fp = open(here / "input.txt", "r")
instructions = [x.strip() for x in fp.readlines()]
fp.close()

cycleNumber = 1 # crtPosition is cycleNumber - 1.
spritePosition = 1 # Represents middle of sprite which has length 3.

ROW_LENGTH = 40

def isSpriteOverlappingCrt(spritePosition, crtPosition):
    return spritePosition -1 <= (crtPosition % ROW_LENGTH) <= spritePosition + 1

jobQueue = deque() # contains (value, cycleNumberToExecute)
i = 0
while i < len(instructions) or jobQueue:

    if isSpriteOverlappingCrt(spritePosition, cycleNumber-1):
        print("#", end="")
    else:
        print(".", end="")

    # If there is a executing job, then ensure it is done executing before reading the next instruction
    if jobQueue:
        if jobQueue[0][1] == cycleNumber:
            value = jobQueue.popleft()[0]
            spritePosition += value
    else:
        # Read the next instruction and add to job queue
        splitInstruction = instructions[i].split(" ")
        if splitInstruction[0] == "noop":
            pass
        elif splitInstruction[0] == "addx":
            nextInstructionValue = int(splitInstruction[1])
            nextCycle = cycleNumber + 1
            jobQueue.append((nextInstructionValue, nextCycle))
        else:
            raise Exception("Invalid instruction")
        
        i += 1

    # print(f"Cycle {cycleNumber}: spritePosition = {spritePosition}")
    
    if cycleNumber % ROW_LENGTH == 0:
        print()

    cycleNumber += 1
