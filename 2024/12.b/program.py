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


def plot_count(id):
    plots = 0

    for y in range(h):
        for x in range(w):
            if region_ids[y][x] == id:
                plots += 1

    return plots


def sides_count(id):
    sides = 0
    
    for y in range(h):
        x = 0
        while x < w:
            x, n = span_scan_x(x, y, id, 1)
            sides += n

        x = 0
        while x < w:
            x, n = span_scan_x(x, y, id, -1)
            sides += n

    for x in range(w):
        y = 0
        while y < h:
            y, n = span_scan_y(x, y, id, 1)
            sides += n

        y = 0
        while y < h:
            y, n = span_scan_y(x, y, id, -1)
            sides += n
            
    return sides


def span_scan_x(start_x, y, id, increment):
    count = 0
    for x in range(start_x, w):
        if region_ids[y][x] == id and map[y][x] != array_2d_get_or_default(map, w, h, x, y + increment):
            count = 1
        else:
            break
    return x + 1, count


def span_scan_y(x, start_y, id, increment):
    count = 0
    for y in range(start_y, h):
        if region_ids[y][x] == id and map[y][x] != array_2d_get_or_default(map, w, h, x + increment, y):
            count = 1
        else:
            break
    return y + 1, count


next_id = 0
for y in range(h):
    for x in range(w):
        if region_ids[y][x] == -1:
            flood_fill(vec2(x, y), map[y][x], next_id)
            next_id += 1
            
result = 0
for id in range(next_id):
    plots, sides = plot_count(id), sides_count(id)
    result += plots * sides
    
print(result)