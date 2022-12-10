
def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        chars = [x for x in fp.read()]

    F = 0
    for i, c in enumerate(chars):
        match c:
            case "(":
                F += 1
            case ")":
                F -= 1

        if p2 and F == -1:
            return i+1

    return F


assert parse_file('test.txt') == 3
print("Part 1: ", parse_file('input.txt'))

print("Part 2: ", parse_file('input.txt', True))
