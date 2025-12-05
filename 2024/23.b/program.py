import sys
import os
import itertools

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

connections, computers = set(), set()
for line in util.read_lines("in.txt"):
    a, b = line.split('-')
    connections.add((a, b))
    connections.add((b, a))
    computers.add(a)
    computers.add(b)
    
# https://en.wikipedia.org/wiki/Clique_problem#Finding_a_single_maximal_clique
#
# A single maximal clique can be found by a straightforward greedy algorithm.
# Starting with an arbitrary clique (for instance, any single vertex or even
# the empty set), grow the current clique one vertex at a time by looping
# through the graph's remaining vertices. For each vertex v that this loop
# examines, add v to the clique if it is adjacent to every vertex that is
# already in the clique, and discard v otherwise. This algorithm runs in linear
# time.

max_connections = []

for root in computers:
    subgraph = [root]

    for c in computers:
        if c not in subgraph and all((b, c) in connections for b in subgraph):
            subgraph.append(c)
    
    if len(subgraph) > len(max_connections):
        max_connections = subgraph

print(','.join(sorted(max_connections)))