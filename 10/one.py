from collections import deque
from pathlib import Path


here = Path(__file__).parent

# Read from file "input.txt" in the same directory as this file
fp = open(here / "input.txt", "r")
instructions = [x.strip() for x in fp.readlines()]
fp.close()

cycleNumber = 1
xRegister = 1
requiredSumOfSignalStrengths = 0

jobQueue = deque() # contains (value, cycleNumberToExecute)
i = 0
while i < len(instructions) or jobQueue:
    if (cycleNumber - 20) % 40 == 0:
        signalStrength = xRegister * cycleNumber
        requiredSumOfSignalStrengths += signalStrength
        print(f">>> Cycle {cycleNumber}: xRegister = {xRegister}, signalStrength {signalStrength} <<<")


    initialXRegister = xRegister
    # If there is a executing job, then ensure it is done executing before reading the next instruction
    if jobQueue:
        if jobQueue[0][1] == cycleNumber:
            value = jobQueue.popleft()[0]
            xRegister += value
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

    signalStrength = xRegister * cycleNumber
    print(f"Cycle {cycleNumber}: xRegister = {initialXRegister} -> {xRegister}, signalStrength = {signalStrength}")
    
    cycleNumber += 1
    
print(requiredSumOfSignalStrengths)