import sys
import os
import copy

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

map, moves = util.read_text("in.txt").split("\n\n")
map, w, h = util.parse_map(map)
moves = "".join(moves.splitlines())

for y in range(h):
    row = []
    for t in map[y]:
        if t == '#':
            row.append('#')
            row.append('#')
        elif t == 'O':
            row.append('[')
            row.append(']')
        elif t == '.':
            row.append('.')
            row.append('.')
        elif t == '@':
            row.append('@')
            row.append('.')
    map[y] = row

w *= 2

#util.array_2d_print(map, column_divider="")
#print()


def move_box(x, y, d):
    assert map[y][x] == '['
    
    if d == '^':
        #   []
        #   []
        if map[y-1][x+0] == '[':
            if not move_box(x, y-1, d):
                return False
        #  [].
        #   []
        elif map[y-1][x+0] == ']' and map[y-1][x+1] == '.':
            if not move_box(x-1, y-1, d):
                return False
        #   .[]
        #   []
        elif map[y-1][x+0] == '.' and map[y-1][x+1] == '[':
            if not move_box(x+1, y-1, d):
                return False
        #  [][]
        #   []
        elif map[y-1][x+0] == ']' and map[y-1][x+1] == '[':
            if not (move_box(x-1, y-1, d) and move_box(x+1, y-1, d)):
                return False

        #   ..
        #   []
        if map[y-1][x+0] == '.' and map[y-1][x+1] == '.':
            map[y-1][x+0], map[y-1][x+1] = '[', ']'
            map[y+0][x+0], map[y+0][x+1] = '.', '.'
            return True
    if d == 'v':
        #   []
        #   []
        if map[y+1][x+0] == '[':
            if not move_box(x, y+1, d):
                return False
        #   []
        #  [].
        elif map[y+1][x+0] == ']' and map[y+1][x+1] == '.':
            if not move_box(x-1, y+1, d):
                return False
        #   []
        #   .[]
        elif map[y+1][x+0] == '.' and map[y+1][x+1] == '[':
            if not move_box(x+1, y+1, d):
                return False
        #   []
        #  [][]
        elif map[y+1][x+0] == ']' and map[y+1][x+1] == '[':
            if not (move_box(x-1, y+1, d) and move_box(x+1, y+1, d)):
                return False

        #   []
        #   ..
        if map[y+1][x+0] == '.' and map[y+1][x+1] == '.':
            map[y+1][x+0], map[y+1][x+1] = '[', ']'
            map[y+0][x+0], map[y+0][x+1] = '.', '.'
            return True
    if d == '>':
        # [][
        if map[y][x+2] == '[':
            if not move_box(x+2, y, d):
                return False

        # [].
        if map[y][x+2] == '.':
            map[y][x], map[y][x+1], map[y][x+2] = '.', '[', ']'
            return True
    if d == '<':
        # ][]
        if map[y][x-1] == ']':
            if not move_box(x-2, y, d):
                return False

        # .[]
        if map[y][x-1] == '.':
            map[y][x-1], map[y][x], map[y][x+1] = '[', ']', '.'
            return True
        

for y in range(h):
    for x in range(w):
        if map[y][x] == '@':
            rx, ry = x, y

for move in moves:
    x0, y0, ok, old_map = rx, ry, True, copy.deepcopy(map)

    if move == '^':
        if map[ry - 1][rx] == '[':
            ok = move_box(rx, ry - 1, move)
        elif map[ry - 1][rx] == ']':
            ok = move_box(rx - 1, ry - 1, move)

        if map[ry - 1][rx] == '.':
            ry -= 1
    elif move == 'v':
        if map[ry + 1][rx] == '[':
            ok = move_box(rx, ry + 1, move)
        elif map[ry + 1][rx] == ']':
            ok = move_box(rx - 1, ry + 1, move)

        if map[ry + 1][rx] == '.':
            ry += 1
    elif move == '>':
        if map[ry][rx + 1] == '[':
            ok = move_box(rx + 1, ry, move)

        if map[ry][rx + 1] == '.':
            rx += 1
    elif move == '<':
        if map[ry][rx - 1] == ']':
            ok = move_box(rx - 2, ry, move)

        if map[ry][rx - 1] == '.':
            rx -= 1
    
    map[y0][x0], map[ry][rx] = '.', '@'
    
    if ok == False:
        map = old_map

    #print(move)
    #util.array_2d_print(map, column_divider="")
    #print()

result = 0
for y in range(h):
    for x in range(w):
        if map[y][x] == '[':
            result += y * 100 + x
print(result)