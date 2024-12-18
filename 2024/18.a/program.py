import sys
import os
import heapq

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

w, h = 71, 71
map = [['.' for _ in range(w)] for _ in range(h)]

for coord in util.read_lines("in.txt")[:1024]:
    x, y = coord.split(",")
    map[int(y)][int(x)] = '#'

def dijkstra(start, goal):
    q    = [(0, start)]
    dist = {start: 0}
    prev = {}

    while q:
        (_, current) = heapq.heappop(q)

        if current == goal:
            path = [current]

            while current in prev:
                current = prev[current]
                path.append(current)

            return path

        for n_direction in (vec2(1,0), vec2(-1,0), vec2(0,1), vec2(0,-1)):
            neighbour = current + n_direction
            
            if not (0 <= neighbour.x < w and 0 <= neighbour.y < h):
                continue

            if map[neighbour.y][neighbour.x] == '#':
                continue

            alt = dist[current] + 1

            if alt < dist.get(neighbour, 2**32):
                prev[neighbour] = current
                dist[neighbour] = alt
                heapq.heappush(q, (alt, neighbour))

print(len(dijkstra(vec2(0, 0), vec2(70, 70))) - 1)