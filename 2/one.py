from pathlib import Path

here = Path(__file__).parent

# X is lose, Y is draw, Z is win
mapping = {
    "X": {"A": "Scissors", "B": "Rock", "C": "Paper"},
    "Y": {"A": "Rock", "B": "Paper", "C": "Scissors"},
    "Z": {"A": "Paper", "B": "Scissors", "C": "Rock"},
}

def getOutcomeScore(outcome: str) -> int:
    # X = lose, Y = draw, Z = win

    if outcome == "X":
        return 0
    elif outcome == "Y":
        return 3
    elif outcome == "Z":
        return 6

def getMyChoiceScore(myChoice: str) -> int:
    return 1 + ["Rock", "Paper", "Scissors"].index(myChoice)

def getRoundScore(opponentChoice: str, outcome: str) -> str:
    # X = lose, Y = draw, Z = win

    myChoice = mapping[outcome][opponentChoice]
    outcomeScore = getOutcomeScore(outcome)
    myChoiceScore = getMyChoiceScore(myChoice)

    return outcomeScore + myChoiceScore
    

totalScore = 0
# Read file input.txt
with open(here / 'input.txt', 'r') as fp:
    for line in fp:
        opponentChoice, outcome = line.split()
        opponentChoice = opponentChoice.strip()
        outcome = outcome.strip()

        roundScore = getRoundScore(opponentChoice, outcome)
        print(roundScore)
        totalScore += roundScore

print(totalScore)