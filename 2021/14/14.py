from collections import defaultdict


def step_template(template, rules):
    new = ""

    # naive approach: Loop over the template list
    for i in range(len(template)-1):
        word = template[i] + template[i+1]
        if word in rules:
            new += template[i] + rules[word]

    # Append the last char
    new += template[-1]

    return new


def parse_file(file, times=3, p2=False):
    with open(file, 'r') as fp:
        template, raw = [x for x in fp.read().split("\n\n")]

    rules = {}
    for line in raw.splitlines():
        a, b = line.split(" -> ")
        rules[a] = b

    print ("Template: ", template)
    for i in range(1, times+1):
        template = step_template(template, rules)
        print ("After step %d: length is %s" % (i, len(template)))

    # Count occurrences
    count = defaultdict(int)
    for char in template:
        count[char] += 1

    return max(count.values()) - min(count.values())

# Part 1
assert parse_file('test.txt', 10) == 1588
print("Part 1: ", parse_file('input.txt', 10))

# Part 2
assert parse_file('test.txt', 40, True) == 2188189693529
#print("Part 2: ", parse_file('input.txt', 40, True))
