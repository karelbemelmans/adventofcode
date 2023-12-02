#!/usr/bin/env python3

from collections import defaultdict


def parse_file(file, cubes=None, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    S = 0
    for line in lines:
        game, input = line.split(": ")
        id = int(game.split(" ")[1])

        # P1 check if a game is valid
        valid = True
        # P2 counters for the minimum number of cubes needed of a color
        M = defaultdict(int)

        turns = input.split("; ")
        for turn in turns:

            moves = turn.split(", ")
            for move in moves:

                i, color = move.split(" ")
                i = int(i)

                # P1 check if a line is valid
                if cubes and cubes[color] and i > cubes[color]:
                    valid = False
                    break

                # P2 count for minimum needed cubes
                M[color] = max(i, M[color])

        if p2:
            S += M['red'] * M['blue'] * M['green']
        elif valid:
            S += id

    return S


# Part 1
cubes = {'red': 12, 'green': 13, 'blue': 14}
assert parse_file('test.txt', cubes) == 8
print("Part 1: ", parse_file('input.txt', cubes))

# Part 2
assert parse_file('test.txt', p2=True) == 2286
print("Part 2: ", parse_file('input.txt', p2=True))
