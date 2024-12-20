#!/usr/bin/env python3

def print_grid(grid):
    max_real = int(max(p.real for p in grid)) + 1
    max_imag = int(max(p.imag for p in grid)) + 1

    for r in range(0, max_real):
        for i in range(0, max_imag):
            print(grid[r + i*1j], end="")
        print()
    print()


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        a, b = fp.read().split("\n\n")

    # This should be doable in one run as well....
    grid = {i+j*1j: c for i, row in enumerate(a.splitlines()) for j, c in enumerate(row.strip())}
    moves = "".join(i.replace("\n", "") for i in b)

    print(grid, moves)

    T = 0
    cursor = [k for k in grid if grid[k] == '@'][0]
    print("cursor: ", cursor)
    DIR = {'^': -1, '>': 1j, 'v': 1, '<': -1j}

    for m in moves:
        next = cursor + DIR[m]
        print("move, next: ", m, next)

        # We can move to a free spot
        if next in grid and grid[next] == '.':
            grid[cursor] = '.'
            grid[next] = '@'
            cursor = next

        # We hit a box
        elif next in grid and grid[next] == 'O':

            # Is there a dot in the direction we are going?
            step = next

            while True:
                step += DIR[m]
                match grid[step]:

                    # We have a free spot
                    case '.':
                        # Move boxes
                        grid[step] = 'O'

                        # Move our cursor
                        grid[cursor] = '.'
                        grid[next] = '@'
                        cursor = next
                        break

                    # We hit a wall, we are done
                    case '#':
                        break

                    # Other spots can only be boxes, we ignore those

        # print_grid(grid)

    T = sum(int(k.real * 100 + k.imag) for k in grid if grid[k] == 'O')
    print("T: ", T)
    return T


# Part 1
assert parse_file('example.txt') == 2028
assert parse_file('example2.txt') == 10092
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('example.txt', True) == 300
# print("Part 2: ", parse_file('input.txt', True))
