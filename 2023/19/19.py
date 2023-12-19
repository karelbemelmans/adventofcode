#!/usr/bin/env python3

import sys
from collections import deque, defaultdict


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        workflows, ratings = [line for line in fp.read().split("\n\n")]

    # Parse workflows
    W = {}
    for workflow in workflows.splitlines():
        id, rest = workflow[:-1].split("{")
        W[id] = rest.split(",")

    # Loop over all parts
    T = 0
    for part in ratings.splitlines():
        score = 0

        p = {}
        for pieces in part[1:-1].split(","):
            a, b = pieces.split("=")
            p[a] = int(b)

        # First instruction is always 'in'
        I = deque(['in'])

        done = False
        while not done:

            # No more instructions to process?
            if len(I) == 0:
                break

            # Get the current instruction
            w = I.popleft()
            inst = W[w]

            for i in inst:

                # Accepted or Rejected will end the process
                if i in ['A', 'R']:
                    done = True
                    score = sum(p.values()) if i == 'A' else 0
                    break

                # Comparison instructions
                elif i.count('>') or i.count('<'):
                    x, dest = i.split(':')

                    if i.count('>'):
                        var, val = x.split('>')
                        op = '>'
                    else:
                        var, val = x.split('<')
                        op = '<'

                    # This can probably be written a bit better?
                    if (op == '<' and p[var] < int(val)) or (op == '>' and p[var] > int(val)):
                        if dest in ['A', 'R']:
                            done = True
                            score = sum(p.values()) if dest == 'A' else 0
                            break
                        else:
                            I.append(dest)
                            break

                # Otherwise our instruction is the id of a workflow
                else:
                    I.append(i)

        T += score

    # print("Total: ", T)
    return T


def main():
    # Part 1
    assert parse_file('test.txt') == 19114
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    # assert parse_file('test.txt', True) == 167409079868000
    # print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
