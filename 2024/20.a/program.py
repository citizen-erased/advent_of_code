import sys
import os
import heapq

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

def dijkstra(map, start, goal):
    q    = [(0, start)]
    dist = {start: 0}
    prev = {}

    while q:
        (_, current) = heapq.heappop(q)

        if current == goal:
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

no_cheat_time = dijkstra(map, start, end) - 1
saved_to_count = {}

for y in range(h):
    print(y, h)
    for x in range(w):
        if map[y][x] == '#':
            map[y][x] = '.'

            saved = no_cheat_time - dijkstra(map, start, end) + 1

            if saved in saved_to_count:
                saved_to_count[saved] += 1
            else:
                saved_to_count[saved] = 1

            map[y][x] = '#'
            
print(sorted(list(saved_to_count.items())))

result = 0
for saved, count in saved_to_count.items():
    if saved >= 100:
        result += count
print(result)