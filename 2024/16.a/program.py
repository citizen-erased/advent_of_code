import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import heapq
import util
from util import vec2

def dijkstra(start, goal):
    q    = [(0, start)]
    dist = {start: 0}
    prev = {}

    while q:
        (_, current) = heapq.heappop(q)
        (direction, position) = current

        if position == goal:
            path = [current]

            while current in prev:
                current = prev[current]
                path.append(current)

            return list(reversed(path))

        for n_direction in (vec2(1,0), vec2(-1,0), vec2(0,1), vec2(0,-1)):
            if n_direction == -direction:
                continue

            n_position = position + n_direction

            if map[n_position.y][n_position.x] == '#':
                continue

            weight    = 1 if n_direction == direction else 1000
            alt       = dist[current] + weight
            neighbour = (n_direction, n_position)

            if alt < dist.get(neighbour, 2**32):
                prev[neighbour] = current
                dist[neighbour] = alt
            
                heapq.heappush(q, (alt, neighbour))

map, w, h = util.read_map("in.txt")

for y in range(h):
    for x in range(w):
        if map[y][x] == 'S':
            s = vec2(x, y)
        if map[y][x] == 'E':
            e = vec2(x, y)

print(dijkstra((vec2(1,0), s), e))

nodes = dijkstra((vec2(1,0), s), e)

for (d, p) in nodes:
    if d == vec2(1,0):
        c = '>'
    elif d == vec2(-1,0):
        c = '<'
    elif d == vec2(0,1):
        c = 'v'
    elif d == vec2(0,-1):
        c = '^'
    map[p.y][p.x] = c
util.array_2d_print(map)

result = len(nodes) - 1

for i in range(len(nodes) - 1):
    (d0, _), (d1, _) = nodes[i], nodes[i + 1]
    if d0 != d1:
        result += 1000
print(result)