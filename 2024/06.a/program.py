import os
from functools import reduce

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    map = [[c for c in line.strip()] for line in f]
    
w, h = len(map[0]), len(map)
d, px, py = ' ', 0, 0

for y in range(h):
    for x in range(w):
        if map[y][x] in "><^v":
            d, px, py = map[y][x], x, y
            
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

while 0 <= px < w and 0 <= py < h:
    map[py][px] = 'X'
    d, px, py = tick(d, px, py)
    
count = 0
for row in map:
    for c in row:
        if c == 'X':
            count += 1
print(count)