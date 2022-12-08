from collections import defaultdict
from pathlib import Path

here = Path(__file__).parent


with open(here / 'input.txt', 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip() for line in lines]

    # 1. Construct graph relating diretories and their children files and subdirectories.
    directoryTree = {"/": {}}
    history = []
    currentDirectoryPath = ""

    i = 0
    while i < len(lines):
        
        line = lines[i]

        if line.startswith("$ cd "):
            nextDirectory = line.split(" ")[-1]

            if nextDirectory == "/":
                history = []
                currentDirectoryPath = "/"
            elif nextDirectory == "..":
                history.pop()
                currentDirectoryPath = "/".join(history)
            else:
                history.append(nextDirectory)
                currentDirectoryPath = "/".join(history)
            
        elif line.startswith("$ ls"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("$"):

                ancestors = currentDirectoryPath.split("/")
                parentDirectory = directoryTree["/"]
                for ancestor in ancestors:
                    if ancestor == "":
                        continue
                    if ancestor not in parentDirectory:
                        parentDirectory[ancestor] = {}
                    parentDirectory = parentDirectory[ancestor]

                if lines[j].startswith("d"):
                    directoryName = lines[j].split(" ")[-1]
                    parentDirectory[directoryName] = {}

                else:
                    
                    fileSize, fileName = lines[j].split(" ")
                    fileSize = int(fileSize)
                    parentDirectory[fileName] = fileSize
                    
                j += 1
            
            i = j - 1

        else:
            raise ValueError(f"Unexpected line: {line}")

        i += 1

desiredTotalSize = 0
THRESHOLD_SIZE = 100_000

def dfs(currentDirectory: dict) -> int:
    global desiredTotalSize
    size = 0

    for child in currentDirectory:
        if type(currentDirectory[child]) == dict:
            size += dfs(currentDirectory[child])
        else:
            size += currentDirectory[child]

    if size <= THRESHOLD_SIZE:
        desiredTotalSize += size

    return size

dfs(directoryTree["/"])

print(desiredTotalSize)