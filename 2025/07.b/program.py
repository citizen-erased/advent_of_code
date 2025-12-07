import sys
import os
from functools import cache

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

grid, w, h = util.read_map("input.txt")

@cache
def step_timeline(x, y):
    # out of range
    if not (0 <= x < w):
        return 0
    # end condition
    elif y == h:
        return 1 if 0 <= x < w else 0
    elif grid[y][x] == '.':
        return step_timeline(x, y + 1)
    elif grid[y][x] == '^':
        return step_timeline(x - 1, y + 1) + step_timeline(x + 1, y + 1)
    return 0

print(step_timeline(grid[0].index('S'), 1))