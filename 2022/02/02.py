# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# The score for a single round is the score for the shape you selected (1 for 
# Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the 
# round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# A is opponent, B is player
def game(a, b):
    score = 0

    if b == "X":
        score = 1
        if a == "A":
            score += 3
        elif a == "B":
            score += 0
        elif a == "C":
            score += 6

    elif b == "Y":
        score = 2
        if a == "A":
            score += 6
        elif a == "B":
            score += 3
        elif a == "C":
            score += 0

    elif b == "Z":
        score = 3
        if a == "A":
            score += 0
        elif a == "B":
            score += 6
        elif a == "C":
            score += 3

    return score

# X means you need to lose, Y means you need to end the round in a draw, 
# and Z means you need to win.

# A for Rock, B for Paper, and C for Scissors

def chose(a, b):
    # We need to lose
    if b == "X":
        if a == "A":
            return "Z"
        elif a == "B":
            return "X"
        elif a == "C":
            return "Y"

    # We need to draw = return the same as a
    elif b == "Y":
        if a == "A":
            return "X"
        elif a == "B":
            return "Y"
        elif a == "C":
            return "Z"

    # We need to win
    elif b == "Z":
        if a == "A":
            return "Y"
        elif a == "B":
            return "Z"
        elif a == "C":
            return "X"


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        pairs = [[y for y in x.split(" ")] for x in fp.read().splitlines()]

    score = 0
    for p in pairs:
        me = p[1]
        if p2:
            me = chose(p[0], p[1])
        s = game(p[0], me)
        score += s
        
    return score

assert parse_file('test.txt') == 15
print("Part 1: ", parse_file('input.txt'))

assert parse_file('test.txt', True) == 12
print("Part 2: ", parse_file('input.txt', True))
