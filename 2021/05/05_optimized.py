import re

from bresenham import bresenham


def parse_file(R, file, diagonal=False):
    # Create an empty grid of RxR
    G = [[0] * R for i in range(R)]

    with open(file, "r") as fp:
        lines = fp.read().splitlines()

    # Open the file, parse every line and update the grid with the line
    for line in lines:
        matches = re.match(r"(\d*),(\d*) -> (\d*),(\d*)$", line)
        if matches:
            x1, y1, x2, y2 = map(lambda x: int(x), matches.groups())

            # Only in p2 we look at diagonal lines
            if diagonal or x1 == x2 or y1 == y2:
                for x, y in list(bresenham(x1, y1, x2, y2)):
                    G[x][y] += 1
    return G


# Calculate the actual result score of our grid
def filter_overlap(grid):
    flat_list = [item for sublist in grid for item in sublist]
    return len(list(filter(lambda x: int(x) > 1, flat_list)))


# Part 1
assert filter_overlap(parse_file(10, "test.txt")) == 5
print("Part 1: ", filter_overlap(parse_file(1000, "input.txt")))

# Part 2
assert filter_overlap(parse_file(10, "test.txt", True)) == 12
print("Part 2: ", filter_overlap(parse_file(1000, "input.txt", True)))
