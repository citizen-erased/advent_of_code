import sys
import os

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

result = 0

for line in util.read_lines("input.txt"):
    max_joltage = 0
    for i in range(0, len(line)):
        for j in range(i + 1, len(line)):
            joltage = int(line[i] + line[j])
            max_joltage = max(max_joltage, joltage)
    result += max_joltage

print(result)