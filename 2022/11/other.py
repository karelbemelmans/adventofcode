#!/usr/bin/env python
from collections import deque
from math import gcd, prod
from operator import floordiv, mod
from functools import reduce
from pprint import pprint

ITEMS, OPER, TEST, A, B = range(5)


def solve(monkeys, iterations, op, number):
    inspections = [0] * len(monkeys)

    for _ in range(iterations):
        for i, m in enumerate(monkeys):
            while m[ITEMS]:
                inspections[i] += 1
                item = op(m[OPER](m[ITEMS].popleft()), number)
                if item % m[TEST] == 0:
                    monkeys[m[A]][ITEMS].append(item)
                else:
                    monkeys[m[B]][ITEMS].append(item)

    for i, m in enumerate(monkeys):
        print("Monkey:", i, m[ITEMS])

    print(inspections)
    print(prod(sorted(inspections)[-2:]))
    return prod(sorted(inspections)[-2:])


monkeys = [
    [
        deque(map(int, item[ITEMS].replace(",", "").split()[2:])),
        eval("lambda old: " + item[OPER].split(" = ")[-1]),
        int(item[TEST].split()[-1]),
        int(item[A].split()[-1]),
        int(item[B].split()[-1]),
    ]
    for block in open(0).read().split("\n\n")
    for item in [block.splitlines()[1:]]
]

print("Part 1:", solve(monkeys, 20, floordiv, 3))

# tests = [m[TEST] for m in monkeys]
# Use least common multiple
# print(solve(monkeys, 10_000, mod, prod(tests) // gcd(*tests)))
