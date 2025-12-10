#!/usr/bin/env python3

with open("input.txt", "r") as fp:
    lines = fp.read().splitlines()

rows = len(lines)
cols = len(lines[0])
count = {}

gamma_rate = ""
epsilon_rate = ""

# Part 1

# We loop over all the columns
for col in range(cols):
    count[col] = 0

    # We then check every line for that column's value
    # We simply add the value of that position then, since we have either 0 or 1 as value
    for line in lines:
        count[col] += int(line[col])

    # If we have more 1's than 0's
    if count[col] > (rows / 2):
        gamma_rate += "1"
        epsilon_rate += "0"

    # Otherwise we have more 0's than 1'
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))


# Part 2


def reduce(lines, col=0, compare="most common"):
    # We are done if our list only has 1 item left
    if len(lines) == 1:
        return lines[0]

    rows = len(lines)
    new_lines = []
    count = 0

    # Check how many times we have a "1" on this col in a row
    for line in lines:
        count += int(line[col])

    # We can probably squeeze this logic into one block, but I always prefer to have easy readable code
    # over the fewest lines of code possible.
    if compare == "most common":
        # Is 1 more common than 0, then we add all lines with 1
        if count >= (rows / 2):
            for line in lines:
                if line[col] == "1":
                    new_lines.append(line)

        # If 0 is more common, we add all lines with 0
        else:
            for line in lines:
                if line[col] == "0":
                    new_lines.append(line)

    elif compare == "least common":
        # Is 1 less common than 0, then we add the lines with 1
        if count < (rows / 2):
            for line in lines:
                if line[col] == "1":
                    new_lines.append(line)

        # If 0 is less common than 1, we add the lines with 0
        else:
            for line in lines:
                if line[col] == "0":
                    new_lines.append(line)

    # Recurse with our smaller list of codes
    return reduce(new_lines, col + 1, compare)


most_common = reduce(lines, 0, "most common")
least_common = reduce(lines, 0, "least common")

print(int(most_common, 2) * int(least_common, 2))
