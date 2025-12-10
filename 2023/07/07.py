#!/usr/bin/env python3

from collections import Counter
from functools import cmp_to_key

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARDS_P2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def hand_strength(hand, p2=False):

    # The core of the hole solution is the Counter type: it counts the occurences
    # of each char (= card) in a string (= hand).
    c = Counter(hand)

    # Count the number of jokers in our hand
    jokers = c.pop("J", 0) if p2 else 0

    # Make sure that 5 J is also a proper match, since we remove J from our counter
    #
    # We continue with c.values() because we only care about how many times a card
    # appears to give a score, not which the acutal cards are.
    counts = [0] if jokers == 5 else sorted(c.values())

    # Every joker means the most signifcant card in our hand is one higher
    counts[-1] += jokers

    match counts:
        case [*_, 5]:
            return 7

        case [*_, 4]:
            return 6

        case [*_, 2, 3]:
            return 5

        case [*_, 3]:
            return 4

        case [*_, 2, 2]:
            return 3

        case [*_, 2]:
            return 2

        case _:
            return 1


def compare_hands(x, y, p2=False, cards=CARDS):
    score_x = hand_strength(x[0], p2)
    score_y = hand_strength(y[0], p2)

    # X ranks higher than Y
    if score_x > score_y:
        return 1

    # Y ranks higher than X
    elif score_y > score_x:
        return -1

    # X and Y rank the same, then we need to compare the cards one by one
    else:

        # zip() gives us tuples of (card_x, card_y) to compare
        for xx, yy in zip(x[0], y[0]):

            # X appears in the list before Y
            if cards.index(xx) < cards.index(yy):
                return 1

            # Y appears in the list before X
            if cards.index(yy) < cards.index(xx):
                return -1

        else:
            return 0


def compare_hands_p2(x, y):
    return compare_hands(x, y, True, CARDS_P2)


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    hands = [(a, int(b)) for a, b in (line.strip().split() for line in lines)]

    # Sort our hands depending which phase we are (can this be done nicer?)
    if p2:
        hands = sorted(hands, key=cmp_to_key(compare_hands_p2))
    else:
        hands = sorted(hands, key=cmp_to_key(compare_hands))

    # Calculate our score
    #
    # Yes, this can be written as a reduce with a map with a zip but that code
    # will turn out longer and harder to read than this :)
    S = 0
    for i, hand in enumerate(hands):
        S += hand[1] * (i + 1)

    return S


# Part 1
assert parse_file("test.txt") == 6440
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test.txt", True) == 5905
print("Part 2: ", parse_file("input.txt", True))
