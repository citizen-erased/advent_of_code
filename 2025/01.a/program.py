import sys
import os

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

d, p = 50, 0

for line in util.read_lines("input.txt"):
    if line[0] == 'R':
        d += int(line[1:])
    else:
        d -= int(line[1:])

    if d % 100 == 0:
        p += 1

print(p)