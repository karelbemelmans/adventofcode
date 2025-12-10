# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# The score for a single round is the score for the shape you selected (1 for
# Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the
# round (0 if you lost, 3 if the round was a draw, and 6 if you won).


# A is opponent, B is player
def game(a, b):
    base = {"X": 1, "Y": 2, "Z": 3}
    scores = {
        ("X", "A"): 3,
        ("X", "B"): 0,
        ("X", "C"): 6,
        ("Y", "A"): 6,
        ("Y", "B"): 3,
        ("Y", "C"): 0,
        ("Z", "A"): 0,
        ("Z", "B"): 6,
        ("Z", "C"): 3,
    }
    return base[b] + scores[(b, a)]


# X means you need to lose, Y means you need to end the round in a draw,
# and Z means you need to win.


def chose(a, b):
    options = {
        ("X", "A"): "Z",
        ("X", "B"): "X",
        ("X", "C"): "Y",
        ("Y", "A"): "X",
        ("Y", "B"): "Y",
        ("Y", "C"): "Z",
        ("Z", "A"): "Y",
        ("Z", "B"): "Z",
        ("Z", "C"): "X",
    }
    return options[b, a]


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        pairs = [[y for y in x.split(" ")] for x in fp.read().splitlines()]

    score = 0
    for p in pairs:
        me = p[1]
        if p2:
            me = chose(p[0], p[1])
        s = game(p[0], me)
        score += s

    return score


assert parse_file("test.txt") == 15
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 12
print("Part 2: ", parse_file("input.txt", True))
