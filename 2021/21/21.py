from itertools import cycle


# a and b are our start positions
def play_game(a_pos, b_pos):
    dice = cycle(range(1, 101))
    W = 1000

    # We turn 1..10 into 0..9 so we can use % 10
    a_pos -= 1
    b_pos -= 1

    a_score = 0
    b_score = 0

    n = 0
    while True:
        a_roll = sum([next(dice) for _ in range(3)])
        n += 3

        a_pos = (a_pos + a_roll) % 10
        a_score += a_pos + 1

        if a_score >= W:
            return b_score * n

        b_roll = sum([next(dice) for _ in range(3)])
        n += 3

        b_pos = (b_pos + b_roll) % 10
        b_score += b_pos + 1

        if b_score >= W:
            return a_score * n


def parse_file(file):
    with open(file, 'r') as fp:
        players = [x for x in fp.read().splitlines()]

    score = play_game(int(players[0][-1]), int(players[1][-1]))
    return score


# Part 1
assert parse_file('test.txt') == 739785
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', 50) == 3351
# print("Part 1: ", parse_file('input.txt', 50))
