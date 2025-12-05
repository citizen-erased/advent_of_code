import sys
import os

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

result = 0

for line in util.read_single_line("input.txt").split(','):
    a, b = line.split('-')

    for i in range(int(a), int(b) + 1):
        s = str(i)
        l = len(s)

        for j in range(1, l // 2 + 1):
            parts = [s[i:i + j] for i in range(0, l, j)]

            if all(part == parts[0] for part in parts):
                result += i
                break

print(result)