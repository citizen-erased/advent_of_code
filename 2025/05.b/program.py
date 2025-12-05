import sys
import os

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

def merge_overlapping(ranges):
    for i, (ra0, rb0) in enumerate(ranges):
        for j, (ra1, rb1) in enumerate(ranges):
            a0, a1 = min(ra0, ra1), max(ra0, ra1)
            b0, b1 = min(rb0, rb1), max(rb0, rb1)

            if i != j and a1 <= b0:
                new_ranges = []
                for k, r in enumerate(ranges):
                    if k != i and k != j:
                        new_ranges.append(r)
                new_ranges.append((a0, b1))
                return True, new_ranges

    return False, ranges

ranges = []

for line in util.read_lines("input.txt"):
    if line == "":
        break
    a, b = line.split('-')
    ranges.append((int(a), int(b)))

merging = True
while merging:
    merging, ranges = merge_overlapping(ranges)

result = 0
for a, b in ranges:
    result += b - a + 1
print(result)