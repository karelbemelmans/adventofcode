#!/usr/bin/env python

# Shamelessly ripped from:
#   https://www.reddit.com/r/adventofcode/comments/k8a31f/2020_day_07_solutions/gexio8m/?utm_source=reddit&utm_medium=web2x&context=3
#
# I was stuck writing my own python graph, and this solution is elegant
# with using an external graph library.

import re
import networkx as nx

with open("./input.txt", "r") as fp:
    data = fp.readlines()


G = nx.DiGraph()

for line in data:
    m = re.match(r"(.*) bags contain (.*)$", line)
    if m:
        color = m.group(1)
        remain = m.group(2)

        children = re.findall(r"([\d]+) (.*?) bag", remain)
        if not children:
            continue

        for child in children:
            G.add_edge(color, child[1], count=int(child[0]))


def countBagsIn(root):
    totalBags = 0
    for k, val in G[root].items():
        totalBags += val['count'] * countBagsIn(k) + val['count']

    return totalBags

print(len(nx.ancestors(G, "shiny gold")))
print(countBagsIn('shiny gold'))