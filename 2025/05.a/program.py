import sys
import os

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

result = 0

lines = iter(util.read_lines("input.txt"))
ranges = []

for line in lines:
    if line == "":
        break
    a, b = line.split('-')
    ranges.append((int(a), int(b)))

ids = []
for line in lines:
    ids.append(int(line))

for id in ids:
    for a, b in ranges:
        if a <= id <= b:
            result += 1
            break

print(result)