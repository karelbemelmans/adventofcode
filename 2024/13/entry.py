#!/usr/bin/env python3

import sys
from sympy import symbols, Eq, solve

A_COST = 3
B_COST = 1
P2_INC = 10000000000000


def match(a, b, prize, p2=False):
    if p2:
        prize = [x + P2_INC for x in prize]

    # We use sympy to solve the simple equations
    x, y = symbols('x,y')

    eq1 = Eq(a[0] * x + b[0] * y, prize[0])
    eq2 = Eq(a[1] * x + b[1] * y, prize[1])

    try:
        s = solve((eq1, eq2), (x, y))

        # Valid integer solution found?
        if int(s[x]) == s[x] and int(s[y]) == s[y]:
            return s[x] * A_COST + s[y] * B_COST
    except:
        pass

    # No validation integer solution found
    return 0


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        machines = [[line for line in machine.splitlines()] for machine in fp.read().split("\n\n")]

    T = 0
    for m in machines:

        a = [int(x[2:]) for x in m[0][10:].split(', ')]
        b = [int(x[2:]) for x in m[1][10:].split(', ')]
        prize = [int(x[2:]) for x in m[2][7:].split(', ')]

        T += match(a, b, prize, p2)

    return T


def main():
    # Part 1
    assert parse_file('example.txt') == 480
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
