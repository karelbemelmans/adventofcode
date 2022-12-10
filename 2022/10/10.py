p1 = 0
G = [['?' for _ in range(40)] for _ in range(6)]


def show_grid(G):
    for r in range(6):
        print(''.join(G[r]))


def tick(t, X):
    global p1, G

    # Tick logic p1
    if t in [20, 60, 100, 140, 180, 220]:
        p1 += t * X

    # p2 graph logic

    # We start at 0 instead of 1 like our cycles
    t1 = t-1

    # Value X needs to be inside the 3 pixels of the sprite where it's positioned at
    #
    # Thanks JP for the logic as a compact one liner
    # row number: t1//40
    # col number: t1 % 40
    # current position of sprite is t1 % 40
    G[t1//40][t1 % 40] = ('#' if abs(X-(t1 % 40)) <= 1 else ' ')


def parse(lines):
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

    return p1


def parse_file(file):
    global p1, G

    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    p1 = 0
    parse(lines)
    show_grid(G)

    return p1


assert parse_file('test2.txt') == 13140
print("Part 1: ", parse_file('input.txt'))
