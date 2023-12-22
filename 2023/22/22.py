#!/usr/bin/env python3

import sys
from collections import deque, defaultdict
from typing import cast

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    # Build 3D grid

    # Our bricks
    B = set()

    for line in lines:
        start, end = line.split('~')
        brick = set()

        ax, ay, az = map(int, start.split(','))
        bx, by, bz = map(int, end.split(','))

        for x in range(ax, bx+1) if ax < bx else range(bx, ax+1):
            for y in range(ay, by+1) if ay < by else range(by, ay+1):
                for z in range(az, bz+1) if az < bz else range(bz, az+1):
                    brick.add((x, y, z))

        B.add(frozenset(brick))

    # 3D plot of our input

    # Create axis
    axes = [10] * 3

    # Data
    data = np.ones(axes, dtype=bool)

    # Control Transparency
    alpha = 0.9

    # Control colour
    colors = np.empty(axes + [4], dtype=np.float32)

    colors[0] = [1, 0, 0, alpha]  # red
    colors[1] = [0, 1, 0, alpha]  # green
    colors[2] = [0, 0, 1, alpha]  # blue
    colors[3] = [1, 1, 0, alpha]  # yellow
    colors[4] = [1, 1, 1, alpha]  # grey

    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Voxels is used to customizations of the sizes, positions and colors.
    for i, brick in enumerate(B):
        data = np.zeros(axes, dtype=bool)
        for x, y, z in brick:
            data[x, y, z] = True
        ax.voxels(data, facecolors=colors, edgecolors='grey')

    # return 0


def main():
    # Part 1
    assert parse_file('test.txt') == 5
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    assert parse_file('test.txt', True) == 0
    print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
