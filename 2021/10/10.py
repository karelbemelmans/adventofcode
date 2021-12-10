from collections import deque

# Points for the closing chars
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

# Points for the P2 closing chars
# We simply use the opening tags since those will be on our stack already
p2points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def parse_line(line, p2=False):
    global points, p2points

    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']

    stack = deque()
    skipline = False

    # Stop at the first incorrect closing character on each corrupted line.
    for i, char in enumerate(line):
        if char in openers:
            stack.append(char)

        elif char in closers:
            last = stack.pop()

            # Loop over all the chars we need to check
            for j in range(len(openers)):
                if last == openers[j] and not char == closers[j]:
                    skipline = True
                    if not p2:
                        return points[char]

    # If we reach this phase, we have a line that is not corrupt but needs proper closing
    # Lucky for us that simply means going over all the chars on our stack in reverse order.

    if p2 and not skipline:
        score = 0
        while stack:
            k = stack.pop()
            score *= 5
            score += p2points[k]

        return score

    # In p1, if there was no error, we return a score of 0
    else:
        return 0


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    score = 0
    scores = []

    for line in lines:
        s = parse_line(line, p2)
        if p2 and s > 0:
            scores.append(s)
        else:
            score += s

    if p2:
        scores.sort()
        return scores[(len(scores) - 1) // 2]
    else:
        return score


# Part 1
assert parse_file('test.txt') == 26397
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 288957
print("Part 2: ", parse_file('input.txt', True))
