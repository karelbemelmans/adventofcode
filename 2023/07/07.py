#!/usr/bin/env python3

from collections import deque, defaultdict
from functools import cmp_to_key, reduce

CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

HAND_FIVE_OF_A_KIND = 7
HAND_FOUR_OF_A_KIND = 6
HAND_FULL_HOUSE = 5
HAND_THREE_OF_A_KIND = 4
HAND_TWO_PAIR = 3
HAND_ONE_PAIR = 2
HAND_HIGH_CARD = 1


def hand_strength(hand):
    s = list(set(hand))

    if len(s) == 1:
        return HAND_FIVE_OF_A_KIND

    if len(s) == 2 and (hand.count(s[0]) == 4 or hand.count(s[1]) == 4):
        return HAND_FOUR_OF_A_KIND

    if len(s) == 2 and (hand.count(s[0]) == 3 or hand.count(s[1]) == 3):
        return HAND_FULL_HOUSE

    for i in s:
        if hand.count(i) == 3:
            return HAND_THREE_OF_A_KIND

    if len(s) == 3 and ((hand.count(s[0]) == 2 and hand.count(s[1]) == 2) or (hand.count(s[0]) == 2 and hand.count(s[2]) == 2) or (hand.count(s[1]) == 2 and hand.count(s[2]) == 2)):
        return HAND_TWO_PAIR

    if len(s) == 4:
        return HAND_ONE_PAIR

    return HAND_HIGH_CARD


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
