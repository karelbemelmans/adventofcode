#!/usr/bin/env python3

from collections import deque, defaultdict
import math


def score(i):
    if i < 2:
        return i
    else:
        return 2 * score(i-1)


def process_cards(cards, p2=False):
    S = 0

    # Process cards
    for id in cards.keys():
        data = cards[id]
        winners, numbers = data.split(' | ')

        W = set([int(x) for x in winners.split()])
        N = set([int(x) for x in numbers.split()])

        matches = len(N.intersection(W))
        S += score(matches)

    return S


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    C = {}

    # Parse cards
    for line in lines:
        card, data = line.split(': ')
        _, id = card.split()
        C[int(id)] = data

    # Process cards
    S = process_cards(C, p2)
    return S


# Part 1
assert parse_file('test.txt') == 13
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 30
# print("Part 2: ", parse_file('input.txt', True))
