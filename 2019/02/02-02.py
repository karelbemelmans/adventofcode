#!/usr/bin/env python

with open('input.txt') as f:
    input = [int(i) for i in f.read().split(',')]


# Replace values

for noun in range(100):
    for verb in range(100):

        # Get a 'fresh' copy of the input
        lines = list(input)

        lines[1] = noun
        lines[2] = verb

        i = 0
        while i < len(lines):

            # Program is done
            if lines[i] == 99:
                break

            elif lines[i] == 1:
                lines[lines[i+3]] = lines[lines[i+1]] + lines[lines[i+2]]
                i += 4

            elif lines[i] == 2:
                lines[lines[i+3]] = lines[lines[i+1]] * lines[lines[i+2]]
                i += 4

            # If we had no valid opcode we just move on 1 step
            else:
                i += 1

        if lines[0] == 19690720:
            print noun, verb, 100 * noun + verb
            exit(0)

