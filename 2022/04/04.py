def parse(a, b, p2=False):

    # Sets are awesome as always
    sa = set(range(int(a[0]), int(a[1]) + 1))
    sb = set(range(int(b[0]), int(b[1]) + 1))

    # Is there an intersection? Then we overlap
    if p2 and sa.intersection(sb):
        return 1
    # If the union is the same as one of the sets? Then we contain the other one
    elif (sa & sb) == sa or (sa & sb) == sb:
        return 1

    return 0


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        pairs = [
            [[z for z in y.split("-")] for y in x.split(",")]
            for x in fp.read().splitlines()
        ]

    total = 0
    for p in pairs:
        total += parse(p[0], p[1], p2)

    return total


assert parse_file("test.txt") == 2
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 4
print("Part 2: ", parse_file("input.txt", True))
