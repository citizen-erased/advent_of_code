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

result = 0
for (a, b, c) in itertools.combinations(computers, 3):
    if (a, b) in connections and (b, c) in connections and (a, c) in connections:
        if (a[0] == 't' or b[0] == 't' or c[0] == 't'):
            result += 1
print(result)