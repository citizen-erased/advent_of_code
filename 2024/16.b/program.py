import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import heapq
import util
from util import vec2

def create_path_r(current, prev):
    path = [current]

    while current in prev:
        prev_list = prev[current]
        
        if len(prev_list) == 1:
            path.append(prev_list[0])
            current = prev_list[0]
        else:
            for n in prev_list:
                path.extend(create_path_r(n, prev))
            current = None

    return list(reversed(path))

            
def dijkstra(start, goal):
    q    = [(0, start)]
    dist = {start: 0}
    prev = {}

    while q:
        (_, current) = heapq.heappop(q)
        (direction, position) = current

        if position == goal:
            return create_path_r(current, prev)

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
                prev[neighbour] = [current]
                dist[neighbour] = alt
                heapq.heappush(q, (alt, neighbour))
            elif alt == dist.get(neighbour, 2**32):
                prev[neighbour].append(current)


map, w, h = util.read_map("in.txt")

for y in range(h):
    for x in range(w):
        if map[y][x] == 'S':
            s = vec2(x, y)
        if map[y][x] == 'E':
            e = vec2(x, y)

nodes = [p for (_, p) in dijkstra((vec2(1,0), s), e)]

for p in nodes:
    map[p.y][p.x] = 'O'
util.array_2d_print(map)

print(len(set(nodes)))