#!/usr/bin/env python3


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    def search_grid(grid, r, c, word):
        R = len(grid)
        C = len(grid[0])
        T = 0

       # Return false if the given coordinate does not match with first index char.
        if grid[r][c] != word[0]:
            return False

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            rr = r + dr
            cc = c + dc
            k = 1

            while k < len(word):

                # Break if out of bounds
                if not 0 <= rr < R or not 0 <= cc < C:
                    break

                # break if characters dont match
                if grid[rr][cc] != word[k]:
                    break

                # Moving in particular direction
                rr += dr
                cc += dc
                k += 1

            # If all character matched, then value of must be equal to length of word
            if k == len(word):
                T += 1

        return T

    def match_cross(grid, r, c):
        R = len(grid)
        C = len(grid[0])

        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        M = 0
        S = 0
        for dr, dc in directions:
            rr = r + dr
            cc = c + dc

            # Count the occurrences of M and S
            if 0 <= rr < R and 0 <= cc < C:
                if grid[rr][cc] == 'M':
                    M += 1
                if grid[rr][cc] == 'S':
                    S += 1

            # We got the 2 M and 2 S, but are the M in the right spot?
            if S == 2 and M == 2:

                # We only look at the M, the S will follow anyway
                # Diagonal M is not allowed in 2 cases where we would get MAM and SAS as words

                if grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'M':
                    return False
                elif grid[r+1][c-1] == 'M' and grid[r-1][c+1] == 'M':
                    return False
                else:
                    return True

    R = len(grid)
    C = len(grid[0])
    T = 0

    if p2:
        # We can skip the borders
        for r in range(1, R-1):
            for c in range(1, C-1):
                # We look for the middle point of the cross
                if grid[r][c] == 'A' and match_cross(grid, r, c):
                    T += 1
    else:
        for r in range(R):
            for c in range(C):
                # Look how many XMAS we can make from this starting point
                T += search_grid(grid, r, c, 'XMAS')

    return T


# Part 1
assert parse_file('example.txt') == 18
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 9
print("Part 2: ", parse_file('input.txt', True))
