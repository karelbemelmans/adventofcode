#!/usr/bin/env python3

from collections import deque, defaultdict, Counter
from functools import cmp_to_key, reduce

CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def hand_strength(hand):
    c = Counter(hand)
    c = sorted(c.values(), reverse=True)

    if c == [5]:
        return 7

    if c == [4, 1]:
        return 6

    if c == [3, 2]:
        return 5

    if c == [3, 1, 1]:
        return 4

    if c == [2, 2, 1]:
        return 3

    if c == [2, 1, 1, 1]:
        return 2

    return 1


def compare_hands(x, y):
    score_x = hand_strength(x[0])
    score_y = hand_strength(y[0])

    if score_x > score_y:
        return 1
    elif score_y > score_x:
        return -1
    else:
        for (xx, yy) in zip(x[0], y[0]):
            if CARDS.index(xx) < CARDS.index(yy):
                return 1
            if CARDS.index(xx) > CARDS.index(yy):
                return -1
        else:
            return 0


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    hands = []
    for i, line in enumerate(lines):
        hands.append((line.split(' ')[0], int(line.split(' ')[1])))

    hands = sorted(hands, key=cmp_to_key(compare_hands))

    S = 0
    for i, hand in enumerate(hands):
        score = hand[1] * (i+1)
        S += score

    return S


# Part 1
assert parse_file('test.txt') == 6440
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
