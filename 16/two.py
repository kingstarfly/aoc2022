from functools import cache
from pathlib import Path
import re


here = Path(__file__).parent

with open(here / "input.txt", "r") as fp:
    lines = fp.read().splitlines()

MAX_TIME = 30
REDUCED_TIME = 26

# Try all paths and find the pressure released for each path.
# Return the max pressure
flowRates = {}
neighbouringValves = {}

for line in lines:
    # Use regex to parse the line.
    # The line looks like this: Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    regex = re.match(
        r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w\s,]+)", line
    )
    if not regex:
        continue
    valveName, flowRate, tunnels = regex.groups()
    flowRates[valveName] = int(flowRate)
    neighbouringValves[valveName] = tunnels.split(", ")


@cache
def dfs(currentValve: str, timeLeft: int, releasedValves: frozenset[str], isElephant: bool) -> int:
    # Returns the max pressure released if we start at currentValve and have timeLeft minutes left.
    if timeLeft == 0:
        if not isElephant:
            return dfs("AA", REDUCED_TIME, releasedValves, True)
        return 0

    maxPressureReleased = 0

    # Run dfs on all neighbouring valves
    for neighbour in neighbouringValves[currentValve]:
        maxPressureReleased = max(maxPressureReleased, dfs(neighbour, timeLeft - 1, releasedValves, isElephant))

    if flowRates[currentValve] > 0 and currentValve not in releasedValves:
        # Release the valve
        newReleasedValves = set(releasedValves)
        newReleasedValves.add(currentValve)

        pressure = flowRates[currentValve] * (timeLeft - 1)
        maxPressureReleased = max(
            maxPressureReleased, pressure + dfs(currentValve, timeLeft - 1, frozenset(newReleasedValves), isElephant)
        )    

    return maxPressureReleased


# print(dfs("AA", MAX_TIME, frozenset()))
print(dfs("AA", REDUCED_TIME, frozenset(), False))