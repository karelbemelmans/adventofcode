from itertools import cycle
from collections import Counter

def play_game(a_pos, b_pos, a_score=0, b_score=0, wins=1000):
    dice = cycle(range(1, 101))

    n = 0
    while True:
        a_roll = sum([next(dice) for _ in range(3)])
        n += 3

        a_pos = (a_pos + a_roll) % 10
        a_score += a_pos + 1

        if a_score >= wins:
            return b_score * n

        b_roll = sum([next(dice) for _ in range(3)])
        n += 3

        b_pos = (b_pos + b_roll) % 10
        b_score += b_pos + 1

        if b_score >= wins:
            return a_score * n

CACHE = {}
def dirac_dice(a_pos, b_pos, a_score, b_score):
    win = 21

    if a_score >= win:
        return (1, 0)

    if b_score >= win:
        return (0, 1)

    # Did we already play this game and know the outcome?
    if (a_pos, b_pos, a_score, b_score) in CACHE:
        return CACHE[(a_pos, b_pos, a_score, b_score)]

    score = (0, 0)
    # We roll 3 times and every time the universe splits
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                new_a_pos = (a_pos + i + j + k) % 10
                new_a_score = a_score + new_a_pos + 1

                a, b = dirac_dice(b_pos, new_a_pos, b_score, new_a_score)
                score = (score[0] + b, score[1] + a)

    CACHE[a_pos, b_pos, a_score, b_score] = score
    return score


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        players = [x for x in fp.read().splitlines()]

    a_pos = int(players[0][-1])
    b_pos = int(players[1][-1])

    # We turn 1..10 into 0..9 so we can use % 10
    a_pos -= 1
    b_pos -= 1

    if p2:
        score = dirac_dice(a_pos, b_pos, 0, 0)
        return max(score)

    else:
        score = play_game(a_pos, b_pos, 0, 0, 1000)
        return score


# Part 1
assert parse_file('test.txt') == 739785
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 444356092776315
print("Part 2: ", parse_file('input.txt', True))
