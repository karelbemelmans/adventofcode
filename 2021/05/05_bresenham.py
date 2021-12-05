import re

from bresenham import bresenham


# Make an empty grid of size RxR
def make_grid(R=1000):
    return [[0] * R for i in range(R)]


# Parse a line of our input file. Simple regex
def parse_file(G, file, diagonal=False):
    with open(file, 'r') as fp:
        lines = fp.read().splitlines()

    for line in lines:
        matches = re.match(r'(\d*),(\d*) -> (\d*),(\d*)$', line)
        if matches:

            # TODO: This can probably be a smarter one liner?
            x1 = int(matches.group(1))
            y1 = int(matches.group(2))
            x2 = int(matches.group(3))
            y2 = int(matches.group(4))

            if diagonal or x1 == x2 or y1 == y2:
                for (x, y) in list(bresenham(x1, y1, x2, y2)):
                    G[x][y] += 1


# Calculate the actual result score of our grid
def filter_overlap(grid, number):
    count = 0

    # TODO: Can we reduce our grid in a single oneliner?
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > number:
                count += 1
    return count


# Part 1
## Test
G = make_grid(10)
parse_file(G, 'test.txt')
assert filter_overlap(G, 1) == 5

## Actual
G = make_grid(1000)
parse_file(G, 'input.txt')
print("Part 1: ", filter_overlap(G, 1))

# Part 2
## Test
G = make_grid(10)
parse_file(G, 'test.txt', True)
assert filter_overlap(G, 1) == 12

# Actual
G = make_grid(1000)
parse_file(G, 'input.txt', True)
print("Part 2: ", filter_overlap(G, 1))
