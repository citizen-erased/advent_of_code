import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

change_to_count = {}
for line in util.read_lines("in.txt"):
    n, prices, sequence = int(line), [], [None]
    for step in range(2001):
        prices.append(n % 10)

        if step > 0:
            sequence.append(prices[step] - prices[step - 1])

        n = (n ^ (n << 6)) & 16777215
        n = (n ^ (n >> 5)) & 16777215
        n = (n ^ (n << 11)) & 16777215

    seen = set()
    for i in range(1, len(sequence) - 3):
        changes = tuple(sequence[i:i+4])

        if changes not in seen:
            change_to_count[changes] = change_to_count.get(changes, 0) + prices[i + 3]
            seen.add(changes)
    
print(max(change_to_count.values()))