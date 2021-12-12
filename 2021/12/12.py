from collections import defaultdict, deque


def find_paths(graph, start, end, p2=False):
    # Start at "start" and see how many times we can reach "end"
    count = 0
    root = (start, set([start]), None)

    # Create a stack that holds our paths
    S = deque([root])
    while S:

        # We loop our stack from begin to end
        pos, visited, twice = S.popleft()

        # Are we done? Then this path was a valid one and we add 1 to count
        if pos == "end":
            count += 1
            continue

        # If not, we look at all edges from our current pos and walk down them
        for x in graph[pos]:

            # Have we visited this point before?
            if x not in visited:
                new_visited = set(visited)

                # Lower caves get logged so we can skip them in a next run
                if x.lower() == x:
                    new_visited.add(x)

                # We continue with walking from this edge
                S.append((x, new_visited, twice))

            # We have visited this point before, but...
            # In p2 we are allowed to visit small cave points twice, except "start" and "end"
            elif p2 and twice is None and x not in [start, end]:
                S.append((x, visited, x))

    return count


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        edges = [x.split("-") for x in fp.read().splitlines()]

    # I considered using networkx but learning to use that would have taken
    # me longer than just writing my own loop for this case.

    # Create our own multi-directional graph
    E = defaultdict(list)
    for a, b in edges:
        E[a].append(b)
        E[b].append(a)

    return find_paths(E, "start", "end", p2)


# Part 1
assert parse_file('test.txt') == 10
assert parse_file('test2.txt') == 19
assert parse_file('test3.txt') == 226
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 36
assert parse_file('test2.txt', True) == 103
assert parse_file('test3.txt', True) == 3509
print("Part 2: ", parse_file('input.txt', True))
