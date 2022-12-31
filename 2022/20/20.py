#!/usr/bin/env python3

from collections import deque, defaultdict
from copy import deepcopy


def mix(numbers, p2=False):

    if p2:
        numbers = [n*811589153 for n in numbers]

    # Double ended queue with items being lists
    # (position in list, value of list item)
    X = deque(list(enumerate(numbers)))

    # Loop over all items in our list
    for t in range(10 if p2 else 1):
        for i in range(len(X)):

            # Find the next item in the list we need to process now
            # After this loop j is set to that position
            for j in range(len(X)):
                if X[j][0] == i:
                    break

            # Set our current item to the start of the list
            while X[0][0] != i:
                X.append(X.popleft())

            val = X.popleft()
            to_pop = val[1]
            to_pop %= len(X)

            # Then add the rest again at the end
            for _ in range(to_pop):
                X.append(X.popleft())

            # And finally append our item
            X.append(val)

    # Find our start item position in the new list
    for j in range(len(X)):
        if X[j][1] == 0:
            break

    # j is now the start item's position
    return (X[(j+1000) % len(X)][1] + X[(j+2000) % len(X)][1] + X[(j+3000) % len(X)][1])


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        numbers = [int(line) for line in fp.read().splitlines()]

    return mix(numbers, p2)


# Part 1
assert parse_file('test.txt') == 3
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 1623178306
print("Part 2: ", parse_file('input.txt', True))
