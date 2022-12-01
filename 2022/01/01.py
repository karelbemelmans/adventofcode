from functools import reduce 

def sum(a, b):
    return a+b

def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        elves = [x for x in fp.read().split("\n\n")]

    l = []
    for e in elves:
        c = [int(x) for x in e.splitlines()]
        total = reduce(sum, c)
        l.append(total)

    if p2:
        l.sort(reverse=True)
        return l[0]+l[1]+l[2]
    else:
        return max(l)


assert parse_file('test.txt') == 24000
print("Part 1: ", parse_file('input.txt'))

assert parse_file('test.txt', True) == 45000
print("Part 2: ", parse_file('input.txt', True))
