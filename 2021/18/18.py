import json


def add(a, b):
    val = [a, b]
    return reduce_(val)


def reduce_(n):
    did1, n1 = explode(n)
    if did1:
        return reduce_(n1)
    else:
        did2, n2 = split(n)
        if did2:
            return reduce_(n2)
        else:
            return n2


def explode(n):
    ns = str(n)
    parts = []

    # Parse our input string into more usuable parts
    i = 0
    while i < len(ns):

        if ns[i] == '[':
            parts.append('[')
            i += 1

        elif ns[i] == ',':
            parts.append(',')
            i += 1

        elif ns[i] == ']':
            parts.append(']')
            i += 1

        elif ns[i] == ' ':
            i += 1

        else:
            j = i
            while j < len(ns) and ns[j].isdigit():
                j += 1
            parts.append(int(ns[i:j]))
            i = j

    depth = 0
    for i, c in enumerate(parts):

        # Opener
        if c == '[':
            depth += 1

            if depth == 5:
                left = parts[i + 1]
                right = parts[i + 3]
                left_i = None
                right_i = None

                for j in range(len(parts)):
                    if isinstance(parts[j], int) and j < i:
                        left_i = j
                    elif isinstance(parts[j], int) and j > i + 3 and right_i is None:
                        right_i = j

                if right_i is not None:
                    parts[right_i] += right

                parts = parts[:i] + [0] + parts[i + 5:]

                if left_i is not None:
                    parts[left_i] += left

                return True, json.loads(''.join([str(x) for x in parts]))

        # Closer
        elif c == ']':
            depth -= 1

        else:
            pass

    return False, n


# To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by
# two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up.
def split(n):
    if isinstance(n, list):
        did1, n1 = split(n[0])
        if did1:
            return True, [n1, n[1]]
        else:
            did2, n2 = split(n[1])
            return did2, [n1, n2]
    else:
        assert isinstance(n, int)
        if n >= 10:
            return True, [n // 2, (n + 1) // 2]
        else:
            return False, n


def magnitude(n):
    if isinstance(n, list):
        return 3 * magnitude(n[0]) + 2 * magnitude(n[1])
    else:
        return n


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    # Simple hack to read our lists is to load the line as a json object
    X = []
    for line in lines:
        data = json.loads(line)
        X.append(data)

    if p2:
        ans = None
        for x in X:
            for y in X:
                if x != y:
                    score = magnitude(add(x, y))
                    if ans is None or score > ans:
                        ans = score
        return ans

    else:
        sum = X[0]
        for i in range(1, len(X)):
            sum = add(sum, X[i])

        return magnitude(sum)


# Part 1
assert add(5, 6) == [5, 6]

assert split(10) == (True, [5, 5])
assert split(11) == (True, [5, 6])
assert split(12) == (True, [6, 6])

assert explode([[[[[9, 8], 1], 2], 3], 4]) == (True, [[[[0, 9], 2], 3], 4])
assert explode([7, [6, [5, [4, [3, 2]]]]]) == (True, [7, [6, [5, [7, 0]]]])

assert magnitude([9, 1]) == 29
assert magnitude([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]) == 1384
assert magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]) == 3488

assert parse_file('test.txt') == 4140
print("Part 1: ", parse_file('input.txt'))

assert parse_file('test.txt', True) == 3993
print("Part 2: ", parse_file('input.txt', True))
