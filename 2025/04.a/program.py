import sys
import os

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

result = 0

grid, w, h = util.read_map("input.txt")

for y in range(h):
    for x in range(w):
        if grid[y][x] == '@':
            offsets = (
                (-1, -1), (0, -1), (1,-1),
                (-1,  0),          (1, 0),
                (-1,  1), (0,  1), (1, 1)
            )

            count = 0
            for (ox, oy) in offsets:
                if 0 <= x + ox < w and 0 <= y + oy < h:
                    if grid[y + oy][x + ox] == '@':
                        count += 1

            if count < 4:
                result += 1

print(result)