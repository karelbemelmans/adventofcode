p1 = 0


def tick(t, X):
    global p1
    if t in [20, 60, 100, 140, 180, 220]:
        p1 += t * X
        print("MARK: ", t, X, t*X, p1)

    print("Tick done: ", t, X)


def parse(lines, p2=False):
    global p1

    X = 1
    t = 0

    for line in lines:
        words = line.split()

        match words[0]:
            case "noop":
                t += 1
                tick(t, X)

            case "addx":
                t += 1
                tick(t, X)
                t += 1
                tick(t, X)
                X += int(words[1])

    print("Final P1:", p1)
    return p1


def parse_file(file, p2=False):
    global p1

    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    p1 = 0
    return parse(lines, p2)


assert parse_file('test2.txt') == 13140
print("Part 1: ", parse_file('input.txt'))

# assert parse_file('test.txt', True) == 1
# assert parse_file('test2.txt', True) == 36
# print("Part 2: ", parse_file('input.txt', True))
