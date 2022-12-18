#!/usr/bin/env python3


def print_grid(G, B):
    C = 7
    R = max([y for x, y in G]) + 3

    for r in range(R, -1, -1):
        for c in range(0, C):
            if (r, c) in B:
                print("@", end='')
            elif (r, c) in G:
                print("#", end='')
            else:
                print(".", end='')

        print("")


def move_block(block, dir, G):
    new = set()

    match dir:
        case 'left':
            for (r, c) in block:
                cc = c - 1
                if cc < 0:
                    return False
                else:
                    new.add((r, cc))

        case 'right':
            for (r, c) in block:
                cc = c + 1
                if cc > 6:
                    return False
                else:
                    new.add((r, cc))

        case 'down':
            for (r, c) in block:
                rr = r - 1
                new.add((rr, c))

    # Is this a valid move?
    for (r, c) in new:
        if (r, c) in G:
            return False

    return new


def parse_moves(moves, N):

    # row, columm
    SHAPES = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],          # horizontal bar
        [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],  # plus sign
        [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],  # reverse L shape
        [(0, 0), (1, 0), (2, 0), (3, 0)],          # vertical bar
        [(0, 0), (1, 0), (0, 1), (1, 1)]           # cube
    ]

    B = set([])
    F = 0  # row number of the floor or the highest item
    G = 0  # the new relative floor level
    R = 0  # number of the rock we are currently processing
    new_shape = True
    buffer = set()
    m = 0

    # The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away
    # from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

    # Nr. of rocks that have gotten stable
    n = 1
    while n <= N:
        # Do we need to load a new shape?
        if new_shape:
            new_shape = False

            # We start 2 from the left, 3 from the floor F
            buffer = set()
            for (r, c) in SHAPES[R]:
                rr = r + F + 4
                cc = c + 2
                buffer.add((rr, cc))

            # Load the next shape
            R = (R + 1) % 5

        # Otherwise we move in the direction requested, if possible
        else:
            move = moves[m % len(moves)]
            m += 1

            # Calculate our next direction
            match move:
                case '<':
                    next_block = move_block(buffer, "left", B)
                    if next_block:
                        buffer = next_block

                case '>':
                    next_block = move_block(buffer, "right", B)
                    if next_block:
                        buffer = next_block

            # Can we still move down?
            # - we are not at the bottom with this move
            # - we are not hitting a block that is stable
            move_down = True
            finished = False

            next_block = move_block(buffer, "down", B)
            if not next_block:
                move_down = False
                finished = True

            if move_down:
                buffer = next_block
                # We hit the ground floor
                if min([r for r, c in buffer]) == G:
                    finished = True

            if finished:
                B.update(buffer)
                new_shape = True
                F = max(r for r, c in B)
                n += 1

    return max(r for r, c in B) + 1


def parse_file(file, N):

    # Shape is a list of lists that contains pairs
    with open(file, 'r') as fp:
        moves = [char for char in fp.read().strip()]

    return parse_moves(moves, N)


# Part 1
assert parse_file('test.txt', 2022) == 3068
print("Part 1: ", parse_file('input.txt', 2022))

# assert parse_file('test.txt', int(1e12)) == 1514285714288
# print("Part 2: ", parse_file('input.txt', 4000000, True))
