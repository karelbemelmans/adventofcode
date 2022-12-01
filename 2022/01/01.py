def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    c = []
    current = 0
    for line in lines:
        if line == "":
            c.append(current)
            current = 0
        else:
            current += int(line)

    # Make sure we append the last item as well
    c.append(current)

    if p2:
        c.sort(reverse=True)
        return c[0]+c[1]+c[2]
    else:
        return max(c)

assert parse_file('test.txt') == 24000
print("Part 1: ", parse_file('input.txt'))

assert parse_file('test.txt', True) == 45000
print("Part 2: ", parse_file('input.txt', True))