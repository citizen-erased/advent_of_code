import sys
import os
import functools
from collections import deque

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

keypad, kw, kh = util.array_2d_create_from_string(
"""
789
456
123
-0A
""")

dirpad, dw, dh = util.array_2d_create_from_string(
"""
-^A
<v>
""")

def get_all_sequences(map, w, h, x, y, dst, moves, depth):
    results = []

    if 0 <= x < w and 0 <= y < h and depth >= 0 and map[y][x] != '-':
        results.extend(get_all_sequences(map, w, h, x + 1, y, dst, moves + '>', depth - 1))
        results.extend(get_all_sequences(map, w, h, x - 1, y, dst, moves + '<', depth - 1))
        results.extend(get_all_sequences(map, w, h, x, y + 1, dst, moves + 'v', depth - 1))
        results.extend(get_all_sequences(map, w, h, x, y - 1, dst, moves + '^', depth - 1))

        if map[y][x] == dst:
            results.append(moves + 'A')

    return results


@functools.cache
def cost_of_button(src, button, depth):
    if depth == 0:
        return 1

    x, y = util.array_2d_index_of(dirpad, src)
    min_cost = 2**63

    for subseq in get_all_sequences(dirpad, dw, dh, x, y, button, '', 3):
        seq_cost, dpad_src = 0, 'A'

        for sub_button in subseq:
            seq_cost += cost_of_button(dpad_src, sub_button, depth - 1)
            dpad_src = sub_button

        min_cost = min(min_cost, seq_cost)

    return min_cost


def cost_of_sequence(sequences, depth):
    min_cost = 2**63
    for buttons in sequences:
        cost, src = 0, 'A'
        for button in buttons:
            cost += cost_of_button(src, button, depth)
            src = button
        min_cost = min(min_cost, cost)
    return min_cost
        

def solve(line):
    cost = 0
    x, y = util.array_2d_index_of(keypad, 'A')

    for c in line:
        results = get_all_sequences(keypad, kw, kh, x, y, c, '', 5)
        x, y = util.array_2d_index_of(keypad, c)
        cost += cost_of_sequence(results, 25)

    return cost * int(line.replace('A', ''))

result = 0
for line in util.read_lines("in.txt"):
    result += solve(line)
print(result)