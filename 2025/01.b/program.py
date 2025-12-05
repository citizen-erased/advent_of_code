import sys
import os

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

d, p = 50, 0

for line in util.read_lines("input.txt"):
    value = int(line[1:])
    a     = -1 if line[0] == 'L' else 1

    for i in range(value):
        d += a

        if d % 100 == 0:
            p += 1

print(p)