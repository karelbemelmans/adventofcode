#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()

rows = len(lines)
cols = len(lines[0])
count = {}
gamma_rate = ""

for col in range(cols):
    count[col] = 0

    for line in lines:
        count[col] += int(line[col])

    if count[col] > (rows/2):
        gamma_rate += "1"
    else:
        gamma_rate += "0"


gamma_rate_decimal = int(gamma_rate, 2)

# Inverse the string
epsilon_rate = ""
for char in gamma_rate:
    if char == "1":
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"

epsilon_rate_decimal = int(epsilon_rate, 2)

# Part 1
print (gamma_rate_decimal * epsilon_rate_decimal)

# Part 2


def reduce(lines, col=0, compare="most common"):
    # We are done.
    if len(lines) == 1:
        return lines[0]

    rows = len(lines)
    count = {}
    new_lines = []
    count[col] = 0

    # Check how many times we have 1 on this col in a row
    for line in lines:
        count[col] += int(line[col])

    if compare == "most common":
        # Is 1 more common than 0, then we add all lines with 1
        if count[col] >= (rows/2):
            for line in lines:
                if line[col] == "1":
                    new_lines.append(line)

        # If 0 is more common, we add all lines with 0
        else:
            for line in lines:
                if line[col] == "0":
                    new_lines.append(line)

    elif compare == "least common":
        # Is 0 more common than 1, then we add the lines with 1
        if count[col] < (rows/2):
            for line in lines:
                if line[col] == "1":
                    new_lines.append(line)

        # If 1 is more common, we add the lines with 0
        else:
            for line in lines:
                if line[col] == "0":
                    new_lines.append(line)

    return reduce(new_lines, col+1, compare)


most_common = reduce(lines, 0, "most common")
least_common = reduce(lines, 0, "least common")
print (most_common, least_common)

most_common_decimal = int(most_common, 2)
least_common_decimal = int(least_common, 2)

print(most_common_decimal, least_common_decimal, most_common_decimal * least_common_decimal)
