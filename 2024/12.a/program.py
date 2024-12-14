import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import *
from functools import cache

map, w, h = util.read_map("in.txt")
region_ids = [[-1 for _ in range(w)]for _ in range(h)]


def flood_fill(p, plant, id):
    if 0 <= p.x < w and 0 <= p.y < h and region_ids[p.y][p.x] == -1 and map[p.y][p.x] == plant:
        region_ids[p.y][p.x] = id
        flood_fill(p + vec2(1, 0), plant, id)
        flood_fill(p + vec2(-1, 0), plant, id)
        flood_fill(p + vec2(0, 1), plant, id)
        flood_fill(p + vec2(0, -1), plant, id)
        

def region_info(id):
    plots, perimeter = 0, 0

    for y in range(h):
        for x in range(w):
            if region_ids[y][x] == id:
                plots += 1
                perimeter += 4
                
                if map[y][x] == array_2d_get_or_default(map, w, h, x + 1, y):
                    perimeter -= 1
                if map[y][x] == array_2d_get_or_default(map, w, h, x - 1, y):
                    perimeter -= 1
                if map[y][x] == array_2d_get_or_default(map, w, h, x, y + 1):
                    perimeter -= 1
                if map[y][x] == array_2d_get_or_default(map, w, h, x, y - 1):
                    perimeter -= 1
                    
    return plots, perimeter


next_id = 0
for y in range(h):
    for x in range(w):
        if region_ids[y][x] == -1:
            flood_fill(vec2(x, y), map[y][x], next_id)
            next_id += 1
            
result = 0
for id in range(next_id):
    plots, perimeter = region_info(id)
    result += plots * perimeter
    
print(result)