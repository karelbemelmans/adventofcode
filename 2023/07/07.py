#!/usr/bin/env python3

from collections import Counter
from functools import cmp_to_key

CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARDS_P2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def hand_strength(hand, p2=False):
    c = Counter(hand)

    jokers = c.pop("J", 0) if p2 else 0

    # Make sure that 5 J is also a proper match
    counts = [0] if jokers == 5 else sorted(c.values())

    # Every joker means the most signifcant card is one higher
    counts[-1] += jokers

    match counts:
        case *_, 5:
            return 7

        case *_, 4:
            return 6

        case *_, 2, 3:
            return 5

        case *_, 3:
            return 4

        case *_, 2, 2:
            return 3

        case *_, 2:
            return 2

    return 1


def compare_hands(x, y, p2=False, cards=CARDS):
    score_x = hand_strength(x[0], p2)
    score_y = hand_strength(y[0], p2)

    if score_x > score_y:
        return 1
    elif score_y > score_x:
        return -1
    else:
        for (xx, yy) in zip(x[0], y[0]):
            if cards.index(xx) < cards.index(yy):
                return 1
            if cards.index(xx) > cards.index(yy):
                return -1
        else:
            return 0


def compare_hands_p2(x, y):
    return compare_hands(x, y, True, CARDS_P2)


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    # Build our input as tuples of (cards, score)
    hands = []
    for i, line in enumerate(lines):
        hands.append((line.split(' ')[0], int(line.split(' ')[1])))

    # Sort our hands depending which phase we are (can this be done nicer?)
    if p2:
        hands = sorted(hands, key=cmp_to_key(compare_hands_p2))
    else:
        hands = sorted(hands, key=cmp_to_key(compare_hands))

    # Calculate our score
    S = 0
    for i, hand in enumerate(hands):
        score = hand[1] * (i+1)
        S += score

    return S


# Part 1
assert parse_file('test.txt') == 6440
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 5905
print("Part 2: ", parse_file('input.txt', True))
