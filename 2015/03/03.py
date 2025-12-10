def parse_file(file, p2=False):
    with open(file, "r") as fp:
        moves = [x for x in fp.read()]

    pos = (0, 0)
    robot = (0, 0)
    visited = set()
    visited.add(pos)

    DIR = {"<": [-1, 0], ">": [1, 0], "^": [0, 1], "v": [0, -1]}

    for i, move in enumerate(moves):
        if p2 and i % 2 == 1:
            robot = (robot[0] + DIR[move][0], robot[1] + DIR[move][1])
            visited.add(robot)
        else:
            pos = (pos[0] + DIR[move][0], pos[1] + DIR[move][1])
            visited.add(pos)

    return len(visited)


print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 3
assert parse_file("test2.txt", True) == 11
print("Part 2: ", parse_file("input.txt", True))
