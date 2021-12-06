from collections import defaultdict


def parse_file(file, days):
    with open(file, 'r') as fp:
        items = [int(x) for x in fp.read().split(",")]

    # We don't iterate over the items, we iterate over the amount of fish of each type we have

    # Build up our initial state before we start processing growth
    fish = defaultdict(int)
    for x in items:
        if x not in fish:
            fish[x] = 0
        fish[x] += 1

    # As we iterate over days, we simply increase the count for each type of fish
    for day in range(days):
        new = defaultdict(int)
        for fish, count in fish.items():

            # For every fish that is about to spawn a new one, we add a new 6 and a new 8
            if fish == 0:
                new[6] += count
                new[8] += count

            # Otherwise we substract one from this fish's life and increase the counter for that one
            else:
                new[fish - 1] += count

        # The results is a new dict with the amount of fish per type
        fish = new

    return sum(fish.values())


# Part 1
assert parse_file('test.txt', 18) == 26
assert parse_file('test.txt', 80) == 5934
print("Part 1: ", parse_file('input.txt', 80))

# Part 2
assert parse_file('test.txt', 256) == 26984457539
print("Part 2: ", parse_file('input.txt', 256))
