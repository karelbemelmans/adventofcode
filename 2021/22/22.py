import re


def switch_cubes(cube, area, action):
    new = cube

    for x in area["x"]:
        for y in area["y"]:
            for z in area["z"]:
                if action == "on" and not (x, y, z) in cube:
                    new.add((x, y, z))
                elif action == "off":
                    new.discard((x, y, z))

    return new


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        lines = [x for x in fp.read().splitlines()]

    # Our initial empty cube
    cube = set()

    for line in lines:
        matches = re.match(
            r"^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$",
            line,
        )
        if matches:
            action = matches.group(1)

            if p2:
                area = {}
                area["x"] = [
                    i for i in range(int(matches.group(2)), int(matches.group(3)) + 1)
                ]
                area["y"] = [
                    i for i in range(int(matches.group(4)), int(matches.group(5)) + 1)
                ]
                area["z"] = [
                    i for i in range(int(matches.group(6)), int(matches.group(7)) + 1)
                ]

            # In p1 we only look at -50,50 as an accepted range for our cube
            else:
                area = {}
                area["x"] = [
                    i
                    for i in range(
                        max(int(matches.group(2)), -50),
                        min(int(matches.group(3)), 50) + 1,
                    )
                ]
                area["y"] = [
                    i
                    for i in range(
                        max(int(matches.group(4)), -50),
                        min(int(matches.group(5)), 50) + 1,
                    )
                ]
                area["z"] = [
                    i
                    for i in range(
                        max(int(matches.group(6)), -50),
                        min(int(matches.group(7)), 50) + 1,
                    )
                ]

            cube = switch_cubes(cube, area, action)

    return len(cube)


# Part 1
assert parse_file("sample.txt") == 39
assert parse_file("test.txt") == 590784
print("Part 1: ", parse_file("input.txt"))

# Part 2
# assert parse_file('test2.txt', True) == 2758514936282235
# print("Part 2: ", parse_file('input.txt', True))
