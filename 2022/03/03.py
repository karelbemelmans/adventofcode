#   ord('a') = 97
#   ord('A') = 65
def priority(x):
    # uppercase?
    # results  gets 26 extra value points
    if x < 97:
        return x - 64 + 26
    else:
        return x - 96


# p1
def parse(l):
    m = len(l) // 2
    common = [x for x in l[0:m] if x in l[m : len(l) + 1]]
    return priority(ord(common[0]))


# p2
def parse2(a, b, c):
    common = [x for x in a if x in b and x in c]
    return priority(ord(common[0]))


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        lines = [list(x) for x in fp.read().splitlines()]

    total = 0
    i = 0
    while i < len(lines):
        if p2:
            total += parse2(lines[i], lines[i + 1], lines[i + 2])
            i += 3
        else:
            total += parse(lines[i])
            i += 1

    return total


assert parse_file("test.txt") == 157
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 70
print("Part 2: ", parse_file("input.txt", True))
