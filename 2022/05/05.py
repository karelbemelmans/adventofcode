from collections import defaultdict
import re

def parse_stacks(stacks):
    S = defaultdict(list)
    lines = [x for x in stacks.split("\n")]

    # ID line
    ids = lines.pop()

    # Take the rest and reverse them so we have the correct parse order
    lines.reverse()

    for pos in range(len(ids)):
        # Are we on a valid position?
        if ids[pos] != " ":
            id = int(ids[pos])
            for line in lines:
                if line[pos] != " ":
                    S[id].append(line[pos])
            
    return S


def parse_ops(S, ops):
    for op in [x for x in ops.split("\n")]:
        matches = re.match(r'move (\d+) from (\d+) to (\d+)', op)
        assert matches

        count = int(matches.group(1))
        source = int(matches.group(2))
        dest = int(matches.group(3))

        for i in range(count):
            item = S[source].pop()
            S[dest].append(item)
            

    res = []
    # Result is the last item from every stack
    for i in S.keys():
        res.append(str(S[i].pop()))

    return "".join(res)


def parse (stacks, ops):
    S = parse_stacks(stacks)
    return parse_ops(S, ops)


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        (stacks, ops) = [x for x in fp.read().split("\n\n")]

    res = parse(stacks, ops)
    return res

assert parse_file('test.txt') == "CMZ"
print("Part 1: ", parse_file('input.txt'))

# assert parse_file('test.txt', True) == 4
# print("Part 2: ", parse_file('input.txt', True))
