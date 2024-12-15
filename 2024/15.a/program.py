import sys
import os
import math

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

map, moves = util.read_text("in.txt").split("\n\n")
map, w, h = util.parse_map(map)
moves = "".join(moves.splitlines())


def count_sequential(x, y, dx, dy):
    count, x, y = 0, x+dx, y+dy

    while 0 < x < w and 0 < y < h:
        if map[y][x] == 'O':
            count, x, y = count+1, x+dx, y+dy
        else:
            break

    return count
        

def shift_u(rx, ry):
    count = count_sequential(rx, ry, 0, -1)

    if count > 0:
        dst_y = ry - count - 1
        if dst_y > 0 and map[dst_y][rx] != "#":
            map[dst_y][rx], map[y - 2][rx] = '.', 'O'


def shift(move, rx, ry):
    src_x, src_y, dst_x, dst_y = rx, ry, rx, ry

    if move == '^':
        count = count_sequential(rx, ry, 0, -1)
        src_y = ry - 1
        dst_y = ry - 1 - count
    elif move == 'v':
        count = count_sequential(rx, ry, 0, 1)
        src_y = ry + 1
        dst_y = ry + 1 + count
    elif move == '>':
        count = count_sequential(rx, ry, 1, 0)
        src_x = rx + 1
        dst_x = rx + 1 + count
    elif move == '<':
        count = count_sequential(rx, ry, -1, 0)
        src_x = rx - 1
        dst_x = rx - 1 - count

    if count > 0:
        if 0 < src_x <= w and 0 < y and src_y <= h and 0 < dst_x <= w and 0 < y:
            if map[dst_y][dst_x] != "#":
                map[dst_y][dst_x], map[src_y][src_x] = 'O', '.'


for y in range(h):
    for x in range(w):
        if map[y][x] == '@':
            rx, ry = x, y

for move in moves:
    x0, y0 = rx, ry

    shift(move, rx, ry)

    if move == '^':
        if map[ry - 1][rx] == '.':
            ry -= 1
    elif move == 'v':
        if map[ry + 1][rx] == '.':
            ry += 1
    elif move == '>':
        if map[ry][rx + 1] == '.':
            rx += 1
    elif move == '<':
        if map[ry][rx - 1] == '.':
            rx -= 1
    
    map[y0][x0], map[ry][rx] = '.', '@'

    #print(move)
    #util.array_2d_print(map)
    #print()

result = 0
for y in range(h):
    for x in range(w):
        if map[y][x] == 'O':
            result += y * 100 + x
print(result)