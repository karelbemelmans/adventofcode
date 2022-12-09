def touching(H, T):
    # Same spot
    if H[0] == T[0] and H[1] == T[1]:
        return True

    # Either to the left or right side
    elif abs(H[0] - T[0]) == 1 and H[1] == T[1]:
        return True

    # Either above or below
    elif H[0] == T[0] and abs(H[1] - T[1]) == 1:
        return True

    # Diagonal
    elif abs(H[0] - T[0]) == 1 and abs(H[1] - T[1]) == 1:
        return True

    return False


def move_tail(H, T):

    # Touching? We don't move.
    if touching(H, T):
        return T

    # If the head is ever two steps directly up, down, left, or right from the tail,
    # the tail must also move one step in that direction so it remains close enough:

    elif H[1] == T[1]:
        # Head 2 up from T
        if H[0] - T[0] == 2:
            T[0] += 1

        # Head 2 down from T
        elif H[0] - T[0] == -2:
            T[0] -= 1

    elif H[0] == T[0]:
        # Head 2 right from T
        if H[1] - T[1] == 2:
            T[1] += 1

        # Head 2 left from T
        elif H[1] - T[1] == -2:
            T[1] -= 1

    # Otherwise, if the head and tail aren't touching and aren't in the same row or column,
    # the tail always moves one step diagonally to keep up:
    else:
        # 0
        if H[0] > T[0]:
            T[0] += 1
        else:
            T[0] -= 1

        # 1
        if H[1] > T[1]:
            T[1] += 1
        else:
            T[1] -= 1

    return T


def parse(lines, p2=False):

    H = [0, 0]
    T = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0]]

    DR = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    DC = {'L': -1, 'U': 0, 'R': 1, 'D': 0}

    visited = set()

    for line in lines:
        (dir, count) = line.strip().split(" ")

        for _ in range(int(count)):
            H[0] = H[0] + DR[dir]
            H[1] = H[1] + DC[dir]

            # After each step, you'll need to update the position of the tail
            # if the step means the head is no longer adjacent to the tail.
            T[0] = move_tail(H, T[0])
            if p2:
                for i in range(1, len(T)):
                    T[i] = move_tail(T[i-1], T[i])

            # After simulating the rope, you can count up all of the positions the tail visited at least once.
            if p2:
                visited.add((T[-1][0], T[-1][1]))
            else:
                visited.add((T[0][0], T[0][1]))

    return len(visited)


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    return parse(lines, p2)


assert parse_file('test.txt') == 13
print("Part 1: ", parse_file('input.txt'))

assert parse_file('test.txt', True) == 1
assert parse_file('test2.txt', True) == 36
print("Part 2: ", parse_file('input.txt', True))
