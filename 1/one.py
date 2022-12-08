from pathlib import Path


maxCalories = 0

here = Path(__file__).parent

# Read file input.txt
with open(here / 'input.txt', 'r') as fp:
    currentCalories = 0
    # For each line in the file, add the calories to the currentCalories until the line is empty
    for line in fp:
        if line == '\n':
            # If the currentCalories is greater than the maxCalories, update the maxCalories
            if currentCalories > maxCalories:
                maxCalories = currentCalories
            currentCalories = 0
        else:
            currentCalories += int(line)
    
print(maxCalories)
        







