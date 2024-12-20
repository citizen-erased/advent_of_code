import sys
import os
import heapq
import functools

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

@functools.cache
def dijkstra(start, goal, return_path=False):
    q    = [(0, start)]
    dist = {start: 0}
    prev = {}

    while q:
        (_, current) = heapq.heappop(q)

        if current == goal:
            if return_path:
                path = [current]

                while current in prev:
                    current = prev[current]
                    path.append(current)

                return list(reversed(path))
            else:
                length = 1

                while current in prev:
                    current = prev[current]
                    length += 1

                return length

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
                

map, w, h = util.read_map("in.txt")        

for y in range(h):
    for x in range(w):
        if map[y][x] == 'S':
            start = vec2(x, y)
        elif map[y][x] == 'E':
            end = vec2(x, y)

map[start.y][start.x] = "." 
map[end.y][end.x] = "." 

path = dijkstra(start, end, return_path=True)
base_length = len(path) - 1
result = 0

for path_length0, path_node in enumerate(path):
    print(path_length0, len(path))

    for dy in range(-20, 21):
        for dx in range(-20, 21):
            n = path_node + vec2(dx, dy)
            diff = abs(path_node - n)

            if diff.x + diff.y > 20:
                continue

            if not (0 <= n.x < w and 0 <= n.y < h):
                continue

            if map[n.y][n.x] != '.':
                continue

            path_length1 = dijkstra(n, end) - 1
            path_length  = path_length0 + diff.x + diff.y + path_length1
            saved        = base_length - path_length
            
            if saved >= 100:
                result += 1

print(result)