def triangle(n):
    return int(n * (n + 1) / 2)


def calc_fuel(list, pos, p2=False):
    count = 0

    for item in list:
        if p2:
            count += triangle(abs(item - pos))
        else:
            count += abs(item - pos)

    return count


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        items = [int(x) for x in fp.read().split(",")]

        start = min(items)
        end = max(items)
        fuel = None

        # For every item in our list calculate the distance between that item and our market
        # We move our marker from the list's other items, start and end
        for i in range(start, end):
            f = calc_fuel(items, i, p2)
            if not fuel:
                fuel = f
            else:
                fuel = min(fuel, f)

        return fuel


# Part 1
assert parse_file("test.txt") == 37
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test.txt", True) == 168
print("Part 2: ", parse_file("input.txt", True))
