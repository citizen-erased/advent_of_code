import sys
import os

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

result = 0

for line in util.read_lines("input.txt"):
    values = [int(x) for x in line]
    parts  = ""
    a, b = 0, len(values) - 12 + 1

    for i in range(12):
        subrange, max, max_index = values[a:b], -1, 0
        for j, v in enumerate(subrange):
            if v > max:
                max, max_index = v, j
        a, b = a + max_index + 1, b + 1
        parts += str(max)

    result += int(parts)

print(result)