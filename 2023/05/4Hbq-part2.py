#!/usr/bin/env python3

from functools import reduce

seeds, *mappings = open('input.txt').read().split("\n\n")
seeds = list(map(int, seeds.split()[1:]))


def lookup(inputs, mapping):
    for start, length in inputs:
        while length > 0:
            for m in mapping.splitlines()[1:]:
                dst, src, len = map(int, m.split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else:
                yield (start, length)
                break


print(*[min(reduce(lookup, mappings, s))[0] for s in [
    zip(seeds, [1] * len(seeds)),
    zip(seeds[0::2], seeds[1::2])]])
