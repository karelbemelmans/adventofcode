#!/usr/bin/env python2

with open('input.txt', 'r') as fp:
    originalLines = fp.read().splitlines()


def run_program(lines):
    accumulator = 0
    line = 0
    seen = set()
    while True:

        if line == len(lines):
            print "NORMAL PROGRAM TERMINATION. Accumulator value: %d" % accumulator
            return True

        if line in seen:
            print "Loop detected, halting program! Accumulator value was: %d" % accumulator
            return False

        words = lines[line].split()
        if words:
            seen.add(line)
            instruction = words[0]
            value = int(words[1])

            # print "Line %d: %s %d" % (line, instruction, value)

            # Accumulate and proceed with next line
            if instruction == 'acc':
                accumulator += value
                line += 1

            # Jump to a new line relative to the current line
            elif instruction == 'jmp':
                line += value

            # Do nothing and proceed with the next line
            elif instruction == 'nop':
                line += 1


# We loop over our input and we change a nop or a jmp with every pass
for i in range(len(originalLines)):

    lines = list(originalLines)
    if lines[i].split()[0] == 'nop':
        lines[i] = 'jmp ' + originalLines[i].split()[1]

    elif originalLines[i].split()[0] == 'jmp':
        lines[i] = 'nop ' + originalLines[i].split()[1]

    if run_program(lines):
        break