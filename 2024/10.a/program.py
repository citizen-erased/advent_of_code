import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import itertools
from util import vec2

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    map = [[int(c) for c in line.strip()] for line in f]
    
w, h = len(map[0]), len(map)

def dfs(p, closed):
    closed.add(p)
    count = 0
    elevation = map[p.y][p.x]

    if elevation == 9:
        count = 1
    else:
        for offset in (vec2(1,0), vec2(-1,0), vec2(0,1), vec2(0,-1)):
            pn = p + offset

            if 0 <= pn.x < w and 0 <= pn.y < h and map[pn.y][pn.x] == elevation + 1 and pn not in closed:
                count += dfs(pn, closed)
                
    return count

count = 0
for y in range(h):
    for x in range(w):
        if map[y][x] == 0:
            count += dfs(vec2(x, y), set())     

print(count)