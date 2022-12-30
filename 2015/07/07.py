#!/usr/bin/env python3

from collections import deque, defaultdict

L = dict()
R = defaultdict(int)


def calculate(name):

    # It's a number? Then we just return this value
    if isinstance(name, int):
        return name
    elif name.isnumeric():
        return int(name)

    if name not in R:
        ops = L[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            if "NOT" in ops:
                res = ~calculate(ops[1]) & 0xffff
            elif "AND" in ops:
                res = calculate(ops[0]) & calculate(ops[2])
            elif "OR" in ops:
                res = calculate(ops[0]) | calculate(ops[2])
            elif "LSHIFT" in ops:
                res = calculate(ops[0]) << calculate(ops[2])
            elif "RSHIFT" in ops:
                res = calculate(ops[0]) >> calculate(ops[2])
            else:
                res = calculate(ops[0])
        R[name] = res

    return R[name]


def parse_file(file, wire, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    L.clear()
    R.clear()
    for line in lines:
        (ops, key) = line.split(" -> ")
        L[key.strip()] = ops.strip().split(" ")

    if p2:
        tmp = calculate(wire)

        L['b'] = [tmp]
        R.clear()
        return calculate(wire)
    else:
        return calculate(wire)


# Part 1
assert parse_file('test.txt', 'd') == 72
assert parse_file('test.txt', 'e') == 507
print("Part 1: ", parse_file('input.txt', 'a'))

# Part 2
print("Part 2: ", parse_file('input.txt', 'a', True))
