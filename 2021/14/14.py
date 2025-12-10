from collections import Counter


# Better p2 solution?
def step_smarter(template, rules, steps):
    # Create tuples
    tuples = Counter()
    for i in range(len(template) - 1):
        tuples[template[i] + template[i + 1]] += 1

    for i in range(steps):

        # Make a new counter since we can't change our running one
        tmp = Counter()

        # Loop over all the words we have
        for word in tuples:
            # We add 2 new nodes, A and B
            ## A is first char of word + new
            a = word[0] + rules[word]
            tmp[a] += tuples[word]

            ## B is new + 2nd char of word
            b = rules[word] + word[1]
            tmp[b] += tuples[word]

        tuples = tmp

    return tuples


def parse_file(file, times=3, p2=False):
    with open(file, "r") as fp:
        template, raw = [x for x in fp.read().split("\n\n")]

    rules = {}
    for line in raw.splitlines():
        a, b = line.split(" -> ")
        rules[a] = b

    tuples = step_smarter(template, rules, times)

    # Count all the unique chars in each pair
    count = Counter()
    for t in tuples:
        count[t[0]] += tuples[t]

    # Add one for the last char of the template
    count[template[-1]] += 1

    return max(count.values()) - min(count.values())


# Part 1
assert parse_file("test.txt", 10) == 1588
print("Part 1: ", parse_file("input.txt", 10))

# Part 2
assert parse_file("test.txt", 40, True) == 2188189693529
print("Part 2: ", parse_file("input.txt", 40, True))
