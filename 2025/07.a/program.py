import sys
import os
from functools import reduce

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

grid, w, h = util.read_map("input.txt")

split_count = 0

for y in range(h):
    for x in range(w):
        above = util.array_2d_get_or_default(grid, w, h, x, y - 1)
        if grid[y][x] == '.':
            if above == 'S' or above == '|':
                grid[y][x] = '|'
        elif grid[y][x] == '^':
            if above == 'S' or above == '|':
                split = False

                for xx in (x - 1, x + 1):
                    if util.array_2d_get_or_default(grid, w, h, xx, y) == '.':
                        grid[y][xx] = '|'
                        split = True

                if split:
                    split_count += 1

print(split_count)