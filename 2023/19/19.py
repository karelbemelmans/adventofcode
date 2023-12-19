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
        print("Part: ", part)
        score = 0

        p = {}
        for pieces in part[1:-1].split(","):
            a, b = pieces.split("=")
            p[a] = int(b)

        # First instruction is always in
        I = deque(['in'])

        done = False
        while not done:

            # No more instructions to process?
            if len(I) == 0:
                break

            # Get the current instruction
            w = I.popleft()
            inst = W[w]
            print("- Instructions: ", w, inst)
            for i in inst:
                print("  - ", i)

                if i == 'A':
                    print("   Accepted")
                    done = True
                    score = sum(p.values())
                    break

                elif i == 'R':
                    print("   REJECTED")
                    done = True
                    break

                elif i.count('>'):
                    x, dest = i.split(':')
                    var, val = x.split('>')
                    if p[var] > int(val):
                        if dest == 'A':
                            print("   Accepted")
                            done = True
                            score = sum(p.values())
                        elif dest == 'R':
                            print("   REJECTED")
                            done = True
                            break
                        else:
                            I.append(dest)
                            break

                elif i.count('<'):
                    x, dest = i.split(':')
                    var, val = x.split('<')
                    if p[var] < int(val):
                        if dest == 'A':
                            print("   Accepted")
                            done = True
                            score = sum(p.values())
                        elif dest == 'R':
                            print("   REJECTED")
                            done = True
                            break
                        else:
                            I.append(dest)
                            break

                # Otherwise our instruction is the id of a workflow
                else:
                    print("   Sending to ", i)
                    I.append(i)

        print(" Score: ", score)
        T += score

    print("Total: ", T)
    return T


def main():
    # Part 1
    assert parse_file('test.txt') == 19114
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    # assert parse_file('test.txt', True) == 0
    # print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
