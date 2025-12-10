#!/usr/bin/env python3

# A lot of inspiration borrowed here...

from collections import defaultdict


def floyd_warshall(graph):
    distance = defaultdict(int)
    for n, neighbours in graph.items():
        for other, _ in graph.items():
            if n != other:
                distance[(n, other)] = 1 if other in neighbours else float("inf")

    for k in graph.keys():
        for i in graph.keys():
            for j in graph.keys():
                if i != j and j != k:
                    distance[(i, j)] = min(
                        distance[(i, j)], distance[(i, k)] + distance[(k, j)]
                    )

    return distance


# dave russels brilliant order generator
def generate_orders(dist, node, todo, done, time):
    for next_node in todo:
        cost = dist[(node, next_node)] + 1
        if cost < time:
            yield from generate_orders(
                dist, next_node, todo - {next_node}, done + [next_node], time - cost
            )
    yield done


def score(dist, order, flow, t):
    pressure = 0

    for i in range(len(order) - 1):
        cost = dist[(order[i], order[i + 1])] + 1
        t -= cost
        pressure += t * flow.get(order[i + 1], 0)

    return pressure


def parse(lines):
    flow = {}
    graph = defaultdict(list)

    for line in lines:
        parts = line.split("; ")
        valve = parts[0].split(" ")

        id = valve[1]
        pressure = int(valve[4].split("=")[1])
        if pressure > 0:
            flow[id] = pressure

        splitword = "valves " if "valves" in parts[1] else "valve "
        neighbours = parts[1].split(splitword)[1].split(", ")
        graph[id].extend(neighbours)

    dist = floyd_warshall(graph)

    return flow, graph, dist


def parse_file(file, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, "r") as fp:
        lines = [x.strip() for x in fp.readlines()]

    flow, _, dist = parse(lines)

    start = "AA"

    if p2:
        # all orders, including incomplete ones
        orders = generate_orders(dist, start, flow.keys(), [start], 26)

        # scores, sent along set of the order to use later when comparing with elephant
        scores = [(score(dist, order, flow, 26), set(order)) for order in orders]
        scores.sort(key=lambda x: -x[0])

        s = 0
        # best score where we and elephant take entirely different paths
        for i, (score1, order1) in enumerate(scores):
            if score1 * 2 < s:
                # here we will already have found our best pair
                # rest of search will repeat pairs
                break

            for score2, order2 in scores[i + 1 :]:
                if order1 & order2 == set([start]):
                    s = max(score1 + score2, s)

        return s

    else:
        orders = generate_orders(dist, start, flow.keys(), [start], 30)

        s = 0
        for order in orders:
            s = max(s, score(dist, order, flow, 30))

        return s


# Part 1
assert parse_file("test.txt") == 1651
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 1707
print("Part 2: ", parse_file("input.txt", True))
