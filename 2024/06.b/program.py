import os
from functools import reduce

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    map = [[c for c in line.strip()] for line in f]
    
w, h = len(map[0]), len(map)
sd, sx, sy = ' ', 0, 0

for y in range(h):
    for x in range(w):
        if map[y][x] in "><^v":
            sd, sx, sy = map[y][x], x, y

def tick(d, px, py):
    x, y = px, py

    if d == '>':
        x += 1
    elif d == '<':
        x -= 1
    elif d == '^':
        y -= 1
    elif d == 'v':
        y += 1
        
    if 0 <= x < w and 0 <= y < h:
        if map[y][x] == "#":
            if d == '>':
                return 'v', px, py
            elif d == '<':
                return '^', px, py
            elif d == '^':
                return '>', px, py
            elif d == 'v':
                return '<', px, py

    return d, x, y

def test_for_loop(d, x, y):
    history = [[[] for _ in range(w)] for _ in range(h)]

    while 0 <= x < w and 0 <= y < h:
        d, x, y = tick(d, x, y)
        
        if 0 <= x < w and 0 <= y < h:
            if d in history[y][x]:
                return 1
            else:
                history[y][x].append(d)
    
    return 0

count = 0
for y in range(h):
    for x in range(w):
        if map[y][x] == '.':
            map[y][x] = '#'
            count += test_for_loop(sd, sx, sy)
            map[y][x] = '.'
print(count)