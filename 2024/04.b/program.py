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
    if is_char('A', x, y) == False:
        return 0
    
    has0, has1 = False, False

    if is_char('M', x - 1, y - 1) and is_char('S', x + 1, y + 1):
        has0 = True
    elif is_char('S', x - 1, y - 1) and is_char('M', x + 1, y + 1):
        has0 = True

    if is_char('M', x - 1, y + 1) and is_char('S', x + 1, y - 1):
        has1 = True
    elif is_char('S', x - 1, y + 1) and is_char('M', x + 1, y - 1):
        has1 = True

    return 1 if has0 and has1 else 0

count = 0
for y in range(h):
    for x in range(w):
        count += count_at(x, y)
print(count)