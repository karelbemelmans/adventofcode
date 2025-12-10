#!/usr/bin/env python3

DIR = {"^": -1, ">": 1j, "v": 1, "<": -1j}


# Helper function to print the grid
def print_grid(grid):
    max_real = int(max(p.real for p in grid)) + 1
    max_imag = int(max(p.imag for p in grid)) + 1

    for r in range(0, max_real):
        for i in range(0, max_imag):
            print(grid[r + i * 1j], end="")
        print()
    print()


# Blow up the grid for p2
def create_p2_grid(grid):
    new = {}
    max_real = int(max(p.real for p in grid)) + 1
    max_imag = int(max(p.imag for p in grid)) + 1

    for i in range(0, max_real):
        for j in range(0, max_imag):
            match grid[i + j * 1j]:
                case "@":
                    (
                        a,
                        b,
                    ) = (
                        "@",
                        ".",
                    )
                case "#":
                    (
                        a,
                        b,
                    ) = (
                        "#",
                        "#",
                    )
                case ".":
                    (
                        a,
                        b,
                    ) = (
                        ".",
                        ".",
                    )
                case "O":
                    (
                        a,
                        b,
                    ) = (
                        "[",
                        "]",
                    )

            new[i + (2 * j) * 1j] = a
            new[i + (2 * j + 1) * 1j] = b

    return new


def move_p1(grid, moves):

    # Starting position
    cursor = [k for k in grid if grid[k] == "@"][0]

    for m in moves:
        next = cursor + DIR[m]

        # We can move to a free spot
        if next in grid and grid[next] == ".":
            grid[cursor] = "."
            grid[next] = "@"
            cursor = next

        # We hit a box
        elif next in grid and grid[next] == "O":
            step = next

            while True:
                step += DIR[m]
                match grid[step]:

                    # We have a free spot
                    case ".":
                        # Move boxes
                        grid[step] = "O"

                        # Move our cursor
                        grid[cursor] = "."
                        grid[next] = "@"
                        cursor = next
                        break

                    # We hit a wall, we are done
                    case "#":
                        break

    return sum(int(k.real * 100 + k.imag) for k in grid if grid[k] == "O")


def move_p2(grid, moves):

    print_grid(grid)

    # Starting position
    cursor = [k for k in grid if grid[k] == "@"][0]

    counter = 0
    for m in moves:
        counter += 1

        next = cursor + DIR[m]
        print("move, next:", m, next)

        # We can move to a free spot
        if next in grid and grid[next] == ".":
            grid[cursor] = "."
            grid[next] = "@"
            cursor = next

        # We hit a box
        elif next in grid and grid[next] in ["[", "]"]:
            step = next

            k = 0
            while True:
                step += DIR[m]
                k += 1
                match grid[step]:

                    # We have a free spot
                    case ".":

                        # Up or down - we need to move two spots
                        if m in ["^", "v"]:
                            if grid[step] == "[":
                                grid[step] = grid[step + (k - l - 1) * DIR[m]]

                        # Otherwise we just push everything one spot to the side
                        else:
                            for l in range(2, k + 2):
                                print(step, k, l, k - l)
                                # Move boxes
                                grid[step + (k - l) * DIR[m]] = grid[
                                    step + (k - l - 1) * DIR[m]
                                ]

                        # Move our cursor
                        grid[cursor] = "."
                        grid[next] = "@"
                        cursor = next

                        break

                    # We hit a wall, we are done
                    case "#":
                        break
        print_grid(grid)
        if counter > 5:
            return 0

    return sum(int(k.real * 100 + k.imag) for k in grid if grid[k] == "O")


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        a, b = fp.read().split("\n\n")

    grid = {
        i + j * 1j: c
        for i, row in enumerate(a.splitlines())
        for j, c in enumerate(row.strip())
    }
    moves = "".join(i.replace("\n", "") for i in b)

    if p2:
        grid = create_p2_grid(grid)
        return move_p2(grid, moves)

    else:
        return move_p1(grid, moves)


# Part 1
assert parse_file("example.txt") == 2028
assert parse_file("example2.txt") == 10092
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example2.txt", True) == 9021
# print("Part 2: ", parse_file('input.txt', True))
