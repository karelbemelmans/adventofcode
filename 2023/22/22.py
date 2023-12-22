# %%
#!/usr/bin/env python3

import sys
from collections import deque, defaultdict
from typing import cast
from functools import reduce

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    MAX = 10

    # Our bricks
    B = defaultdict(int)
    x, y, z = np.indices((MAX, MAX, MAX))

    # Add our inputs
    for i, line in enumerate(lines):
        start, end = line.split('~')

        ax, ay, az = map(int, start.split(','))
        bx, by, bz = map(int, end.split(','))

        (x1, x2) = (ax, bx) if ax < bx else (bx, ax)
        (y1, y2) = (ay, by) if ay < by else (by, ay)
        (z1, z2) = (az, bz) if az < bz else (bz, az)

        B[i] = (x1 <= x) & (x <= x2) & (y1 <= y) & (y <= y2) & (z1 <= z) & (z <= z2)

    # Create axis
    axes = [MAX] * 3

    # Control colour
    colors = np.empty(axes, dtype=object)
    COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink']
    for i in range(len(B)):
        colors[B[i]] = COLORS[i % len(COLORS)]

    # Voxels
    voxelarray = reduce(np.logical_or, B.values())

    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

    plt.show()

    return 0


def main():
    # Part 1
    assert parse_file('test.txt') == 0
    # print("Part 1: ", parse_file('input.txt'))

    # Part 2
    # assert parse_file('test.txt', True) == 0
    # print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())

# %%
