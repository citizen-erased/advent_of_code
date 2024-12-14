import sys
import os
import math

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

lines = util.read_lines("in.txt")
robots = []

for line in lines:
    p, v = line.split();
    p = vec2(*[int(c) for c in p.replace("p=", "").split(',')])
    v = vec2(*[int(c) for c in v.replace("v=", "").split(',')])
    robots.append((p, v))
    
w, h = 101, 103
map = [[' ' for _ in range(w)] for _ in range(h)]

def run_step(step):
    for y in range(h):
        for x in range(w):
            map[y][x] = ' '

    for i, (p, v) in enumerate(robots):
        p = (p + v) % vec2(w, h)
        robots[i] = (p, v)
        map[p.y][p.x] = '#'
        
    print('-' * w, step)
    util.array_2d_print(map, column_divider="")

from contextlib import redirect_stdout
with open('out.txt', 'w') as f:
    with redirect_stdout(f):
        for step in range(1, 10000):
            run_step(step)
