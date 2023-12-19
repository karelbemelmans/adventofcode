#!/usr/bin/env python3

import sys
from math import prod


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        a, b = [line for line in fp.read().split("\n\n")]

    # Parse our workflows into d
    d = {k: v[:-1] for k, v in (line.split("{") for line in a.splitlines())}

    # Parse our P1 inputs into xs
    xs = (eval(line.replace("{", "dict(").replace("}", ")"))
          for line in b.splitlines())

    # Going with inline functions to prevent having to declare globals
    # or pass in the data structure in the function call
    def f1(k, xmas):

        # Are we done? Either success or failure
        if k in ['R', 'A']:
            return k == 'A'

        for p in d[k].split(","):
            match p.split(":"):

                # pattern of a, b
                case cond, dest:
                    if eval(f"{xmas[cond[0]]}{cond[1:]}"):
                        return f1(dest, xmas)

                # anything else we select just the first part
                case dest, :
                    return f1(dest, xmas)

    def f2(k, lims):

        if k in ['R', 'A']:

            # Are we done with faillure?
            if k == 'R':
                return 0

            # Reached success? Recurse backwards
            return prod(max(0, lims[f"{k}<"] - lims[f"{k}>"] - 1) for k in "xmas")

        o = 0
        for p in d[k].split(","):
            match p.split(":"):
                case cond, dest:
                    ck = cond[:2]
                    cv = (min, max)[cond[1] == ">"](int(cond[2:]), lims[ck])
                    o += f2(dest, lims | {ck: cv})
                    ck, cv = f"{ck[0]}{'<>'[ck[1]=='<']}", cv + \
                        (-1, 1)[ck[1] == ">"]
                    lims[ck] = cv
                case dest, :
                    o += f2(dest, lims)
        return o

    if p2:
        return f2("in", {f"{c}{o}": (0, 4001)[o == "<"] for c in "xmas" for o in "<>"})
    else:
        # Filter out the accepted inputs and return the sum
        return sum(sum(x.values()) for x in xs if f1("in", x))


def main():
    # Part 1
    assert parse_file('test.txt') == 19114
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    assert parse_file('test.txt', True) == 167409079868000
    print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
