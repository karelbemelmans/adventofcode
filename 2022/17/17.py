#!/usr/bin/env python3


def show(R):
    max_r = max([r for (r, c) in R])
    for r in range(max_r, 0, -1):
        row = ""
        for c in range(7):
            if (r, c) in R:
                row += "#"
            else:
                row += " "
        print(row)


def print_grid(G, B):
    C = 7
    R = max([y for x, y in G]) + 3

    for r in range(R, -1, -1):
        for c in range(0, C):
            if (r, c) in B:
                print("@", end="")
            elif (r, c) in G:
                print("#", end="")
            else:
                print(".", end="")

        print("")


def load_piece(n, r):
    match n:
        case 0:
            return set([(r, 2), (r, 3), (r, 4), (r, 5)])
        case 1:
            return set([(r + 2, 3), (r + 1, 2), (r + 1, 3), (r + 1, 4), (r, 3)])
        case 2:
            return set([(r, 2), (r, 3), (r, 4), (r + 1, 4), (r + 2, 4)])
        case 3:
            return set([(r, 2), (r + 1, 2), (r + 2, 2), (r + 3, 2)])
        case 4:
            return set([(r + 1, 2), (r, 2), (r + 1, 3), (r, 3)])
        case _:
            assert False


def move_piece(piece, dir):
    match dir:
        case "left":
            if any([c == 0 for (r, c) in piece]):
                return piece
            return set([(r, c - 1) for (r, c) in piece])

        case "right":
            if any([c == 6 for (r, c) in piece]):
                return piece
            return set([(r, c + 1) for (r, c) in piece])

        case "down":
            return set([(r - 1, c) for (r, c) in piece])

        case "up":
            return set([(r + 1, c) for (r, c) in piece])


def signature(R):
    max_r = max([r for (r, c) in R])
    return frozenset([(max_r - r, c) for (r, c) in R if max_r - r <= 30])


def parse_moves(moves, L, p2=False):

    R = set([(0, c) for c in range(7)])
    SEEN = {}
    top = 0
    i = 0
    t = 0
    added = 0

    # Nr. of rocks that have gotten stable
    while t < L:
        piece = load_piece(t % 5, top + 4)

        while True:
            if moves[i] == "<":
                piece = move_piece(piece, "left")
                if piece & R:
                    piece = move_piece(piece, "right")

            else:
                piece = move_piece(piece, "right")
                if piece & R:
                    piece = move_piece(piece, "left")

            # Load next move
            i = (i + 1) % len(moves)

            piece = move_piece(piece, "down")
            if piece & R:
                piece = move_piece(piece, "up")

                # Add this piece to our list of static blocks
                R |= piece
                top = max([r for (r, c) in R])

                SR = (i, t % 5, signature(R))
                if SR in SEEN and t >= 2022:
                    (old_t, old_r) = SEEN[SR]
                    dr = top - old_r
                    dt = t - old_t
                    amt = (L - t) // dt
                    added += amt * dr
                    t += amt * dt
                SEEN[SR] = (t, top)
                # show(R)
                break

        t += 1
        if not p2 and t == 2022:
            return top

    return top + added


def parse_file(file, N, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, "r") as fp:
        moves = [char for char in fp.read().strip()]

    return parse_moves(moves, N, p2)


# Part 1
assert parse_file("test.txt", 2022) == 3068
print("Part 1: ", parse_file("input.txt", 2022))

assert parse_file("test.txt", int(1e12), True) == 1514285714288
print("Part 2: ", parse_file("input.txt", int(1e12), True))
