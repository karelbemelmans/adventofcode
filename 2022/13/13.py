#!/usr/bin/env python3
import json
from collections import deque


# Exit codes:
#   -1 is done, with success
#    0 is continue
#    1 is done, with fail
def compare(a, b):
    print(a, b)

    # We start looking unto we have a case where we need to return False

    if isinstance(a, int) and isinstance(b, int):
        print(" both int", a, b)
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

        # In other cases we continue

    elif isinstance(a, list) and isinstance(b, list):
        print(" both list")
        L = min(len(a), len(b))
        for i in range(L):
            c = compare(a[i], b[i])
            if c == -1:
                return -1
            elif c == 1:
                return 1

        if len(a[L:]) == 0 and len(b[L:]) > 0:
            print(" a remainder is empty")
            return -1

        elif len(b[L:]) == 0 and len(a[L:]) > 0:
            print(" b remainder is empty")
            return 1

        # We continue
        else:
            return 0

    elif isinstance(a, int) and not isinstance(b, int):
        print(" a int, not b")
        return compare([a], b)

    elif not isinstance(a, int) and isinstance(b, int):
        print(" b int, not a")
        return compare(a, [b])


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        pairs = [[y for y in x.split("\n")]
                 for x in fp.read().split("\n\n")]

    result = 0
    for i, pair in enumerate(pairs):
        left, right = pair
        print(f"Pair %d:" % (i+1), left, right)

        dl = json.loads(left)
        dr = json.loads(right)

        r = compare(dl, dr)
        print(" Result:", r)

        if r == -1:
            result += i+1

        print("")

    print("Total: ", result)
    return result


# Part 1
assert parse_file('test.txt') == 13
print("Part 1: ", parse_file('input.txt'))

# assert parse_file('test.txt', True) == 140
# print("Part 2: ", parse_file('input.txt', True))
