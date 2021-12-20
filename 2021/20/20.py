def print_points(G):
    r_min = min([r for r, c in G])
    r_max = max([r for r, c in G])
    c_min = min([c for r, c in G])
    c_max = max([c for r, c in G])

    d = 10
    for r in range(r_min - d // 2, r_max + d // 2):
        row = ''
        for c in range(c_min - d // 2, c_max + d // 2):
            if (r, c) in G:
                row += '#'
            else:
                row += '.'
        print(row)
    print("")


def enhance(G, rules, run):
    r_min = min([r for r, c in G])
    r_max = max([r for r, c in G])
    c_min = min([c for r, c in G])
    c_max = max([c for r, c in G])

    d = 4
    N = set()

    for r in range(r_min - d // 2, r_max + d // 2):
        for c in range(c_min - d // 2, c_max + d // 2):
            n = 0

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    n = n * 2

                    rr = r + dr
                    cc = c + dc

                    # Is this an infinity point and our rules state this should be active then?
                    if rr < r_min or rr > r_max or cc < c_min or cc > c_max:
                        if run % 2 == 1 and rules[0] == '#':
                            n += 1

                    # This is an actual point
                    elif (rr, cc) in G:
                        n += 1

            if rules[n] == '#':
                N.add((r, c))

    return N


def parse_file(file, times):
    with open(file, 'r') as fp:
        rules, lines = [x for x in fp.read().split("\n\n")]

    # Make sure our input is sane
    assert len(rules) == 512

    # We build up a list of points. This works better than parsing a grid for this thing.
    S = set()
    for r, line in enumerate(lines.splitlines()):
        for c, v in enumerate(line.strip()):
            if v == '#':
                S.add((r, c))

    for i in range(times):
        S = enhance(S, rules, i)

    return len(S)


# Part 1
assert parse_file('test.txt', 2) == 35
print("Part 1: ", parse_file('input.txt', 2))

# Part 2
assert parse_file('test.txt', 50) == 3351
print("Part 1: ", parse_file('input.txt', 50))
