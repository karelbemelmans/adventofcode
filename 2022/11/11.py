# What I learned here:
#
# Use a global 'ITEMS, OPER, TEST, A, B = range(5)' to make list indicides easier
# Make sure you reset your counters if they are globals. Costed me a few hours of debugging...
# Lambda's are something I need to look into
# Same for the path libraries

from math import gcd, prod
from collections import defaultdict, deque
from operator import floordiv, mod

I = defaultdict(int)
ITEMS, OPER, TEST, A, B = range(5)


# I learned this: Build up lists with for for loops
def monkeys(lines, p2=False):
    M = [
        [
            deque(int(x) for x in parts[ITEMS].split(": ")[1].split(", ")),
            parts[OPER].split(" = ")[1],
            int(parts[TEST].split(" ")[-1]),
            int(parts[A].split(" ")[-1]),
            int(parts[B].split(" ")[-1]),
        ]
        for line in lines
        # We ignore the first line with the Monkey id
        for parts in [line.splitlines()[1:]]
    ]
    return M


def round(M, operation, argument):
    global I

    for i, m in enumerate(M):
        while m[ITEMS]:
            I[i] += 1

            item = m[ITEMS].popleft()

            # OPER
            # There is some improvement to do here with lambdas
            opwords = m[OPER].split(" ")
            a = item if opwords[0] == "old" else int(opwords[0])
            b = item if opwords[2] == "old" else int(opwords[2])
            if opwords[1] == "+":
                new = a + b
            elif opwords[1] == "*":
                new = a * b
            else:
                assert False

            # Worry levels
            new = operation(new, argument)

            # Target
            if new % m[TEST] == 0:
                M[m[A]][ITEMS].append(new)
            else:
                M[m[B]][ITEMS].append(new)


def parse_file(file, p2=False):
    global I

    with open(file, "r") as fp:
        lines = [x for x in fp.read().split("\n\n")]

    M = monkeys(lines, p2)

    # Make sure we reset our global every run
    I = defaultdict(int)

    # In p2 we need to be smarter with our worry level our the values of
    # the worry integer will shoot through the roof.
    if p2:
        rounds = 10000
        tests = [m[TEST] for m in M]
        operator = mod
        argument = prod(tests) // gcd(*tests)

    # P1 is pretty simple. We added operator and argument for p2
    else:
        rounds = 20
        operator = floordiv
        argument = 3

    # Rounds
    for i in range(rounds):
        round(M, operator, argument)

    # Get the result value from I
    J = sorted(I.values(), reverse=True)
    return J[0] * J[1]


assert parse_file("test.txt") == 10605
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 2713310158
print("Part 2: ", parse_file("input.txt", True))
