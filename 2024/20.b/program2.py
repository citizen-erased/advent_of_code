import sys
import os
from collections import deque

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

# Creates a 2d map of the distance from each node on the track '.' to the goal.
# For each pair of track nodes a cheat is created. The cheat distance is the
# distance from the start to the first node + the distance from the second node
# to the goal + the cheat distance.
#
# This checks all possible cheat pairs so it's not fast but runs in a reasonable
# time for the input.


def flood(start, end, dist_map):
    q, seen = deque([start]), set([start])
    
    while q:
        p = q.popleft()

        if p == end:
            continue
        
        for dn in (vec2(1,0), vec2(-1,0), vec2(0,1), vec2(0,-1)):
            n = p + dn
            
            if 0 <= n.x < w and 0 <= n.y < h and n not in seen:
                seen.add(n)

                if map[n.y][n.x] != '#':
                    dist_map[n.y][n.x] = dist_map[p.y][p.x] + 1
                    q.append(n)


map, w, h = util.read_map("in.txt")        

for y in range(h):
    for x in range(w):
        if map[y][x] == 'S':
            start = vec2(x, y)
        elif map[y][x] == 'E':
            end = vec2(x, y)

dist_map = util.array_2d_create(w, h, 2**32)
dist_map[start.y][start.x] = 0
flood(start, end, dist_map)

nodes = []
for y in range(h):
    for x in range(w):
        if dist_map[y][x] < 2**32:
            nodes.append(vec2(x, y))
            
result = 0
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i == j:
            continue

        n0, n1 = nodes[i], nodes[j]
        diff = abs(n1 - n0)
        cheat_len = diff.x + diff.y
        
        if cheat_len > 20:
            continue
        
        d0 = dist_map[n0.y][n0.x]
        d1 = dist_map[n1.y][n1.x]
        d2 = dist_map[end.y][end.x]
        
        dist = cheat_len + d0 + (d2-d1)

        if dist <= d2 - 100:
            result += 1
            
print(result)