import os
from functools import reduce

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    lines = [line.strip() for line in f]
    
w, h = len(lines[0]), len(lines)

def is_char(c, x, y):
    if 0 <= y < len(lines) and 0 <= x < len(lines[y]):
        return lines[y][x] == c
    return False

def count_at(x, y):
    if is_char('X', x, y) == False:
        return 0
    
    mas_offsets = (
        # horizontal
        (( 1, 0), ( 2, 0), ( 3, 0)),
        ((-1, 0), (-2, 0), (-3, 0)),

        # vertical
        ((0,  1), (0,  2), (0,  3)),
        ((0, -1), (0, -2), (0, -3)),

        # diagonal
        (( 1,  1), ( 2,  2), ( 3,  3)),
        (( 1, -1), ( 2, -2), ( 3, -3)),
        ((-1,  1), (-2,  2), (-3,  3)),
        ((-1, -1), (-2, -2), (-3, -3)),
    )

    count = 0

    for offset in mas_offsets:
        if all(is_char(c, x + dx, y + dy) for c, (dx, dy) in zip("MAS", offset)):
            count += 1

    return count

count = 0
for y in range(h):
    for x in range(w):
        count += count_at(x, y)
print(count)