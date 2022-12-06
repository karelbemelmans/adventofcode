# We take subsets of length l until we have one with all unique values
# set() pretty much does all the heavy lifting here for us :)
def parse(chars, l=4):
    for i in range(len(chars) - l):
        sub = set(chars[i:i+l])
        if len(sub) == l:
            return i+l


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        chars = [x for x in fp.read()]

    if p2:
        return parse(chars, l=14)
    else:
        return parse(chars)


assert parse_file('test.txt') == 7
assert parse_file('test2.txt') == 5
assert parse_file('test3.txt') == 6
assert parse_file('test4.txt') == 10
assert parse_file('test5.txt') == 11
print("Part 1: ", parse_file('input.txt'))


assert parse_file('test.txt', True) == 19
assert parse_file('test2.txt', True) == 23
assert parse_file('test3.txt', True) == 23
assert parse_file('test4.txt', True) == 29
assert parse_file('test5.txt', True) == 26
print("Part 2: ", parse_file('input.txt', True))
