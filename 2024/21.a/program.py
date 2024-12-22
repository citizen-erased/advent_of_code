import sys
import os
import functools
from collections import deque

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

"""
 1  function Dijkstra(Graph, source):
 2     
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8     
 9      while Q is not empty:
10          u ← vertex in Q with minimum dist[u]
11          remove u from Q
12         
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
"""

"""
 1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as explored
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7          if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as explored then
11                  label w as explored
12                  w.parent := v
13                  Q.enqueue(w)
"""
def bfs(map, w, h, s, t):
    q, seen, parent = deque([s]), {s}, {}
    
    while q:
        v = q.popleft()
        
        if v == t:
            n, path = v, []
            while n in parent:
                (n, dn) = parent[n]
                path.append(dn)
            return ''.join(reversed(path))

        for dx, dy, dir in ((-1,0,'<'), (1,0,'>'), (0,-1,'^'), (0,1,'v')):
            x, y = util.array_2d_index_of(map, v)
            x, y = x + dx, y + dy
            
            if not (0 <= x < w and 0 <= y < h):
                continue
            
            n = map[y][x]
            
            if n == '-':
                continue

            if n in seen:
                continue
            
            seen.add(n)
            parent[n] = (v, dir)
            q.append(n)


def dijkstra(map, w, h, s):
    q, dist, prev = [], {}, {}

    for y in range(h):
        for x in range(w):
            v = vec2(x, y)
            c = map[y][x]
            if c != '-':
                dist[c] = 0 if c == s else 2**32
                prev[c] = None
                q.append(v)
                
    while q:
        u = q[0]
        uc = map[u.y][u.x]
        d = dist[uc]
        for e in q:
            if dist[map[e.y][e.x]] < d:
                u = e
                uc = map[u.y][u.x]
                d = dist[uc]

        q.remove(u)
        
        for dn in (vec2(-1,0), vec2(1,0), vec2(0,-1), vec2(0,1)):
            v = u + dn
            vc = util.array_2d_get_or_default(map, w, h, v.x, v.y, '-')

            if vc != '-':
                alt = dist[uc] + 1
                if alt < dist[vc]:
                    dist[vc] = alt
                    prev[vc] = uc

    return dist, prev


def get_all_sequences(map, w, h, x, y, dst, moves, depth):
    results = []

    if 0 <= x < w and 0 <= y < h and depth >= 0 and map[y][x] != '-':
        results.extend(get_all_sequences(map, w, h, x + 1, y, dst, moves + '>', depth - 1))
        results.extend(get_all_sequences(map, w, h, x - 1, y, dst, moves + '<', depth - 1))
        results.extend(get_all_sequences(map, w, h, x, y + 1, dst, moves + 'v', depth - 1))
        results.extend(get_all_sequences(map, w, h, x, y - 1, dst, moves + '^', depth - 1))

        if map[y][x] == dst:
            results.append(moves + 'A')

    return results



def bfs(map, w, h, s, t):
    q, seen, parent = deque([s]), {s}, {}
    
    while q:
        v = q.popleft()
        
        if v == t:
            n, count = v, 0
            while n in parent:
                n, count = parent[n], count + 1
            return count

        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            x, y = util.array_2d_index_of(map, v)
            x, y = x + dx, y + dy
            
            if not (0 <= x < w and 0 <= y < h):
                continue
            
            n = map[y][x]
            
            if n == '-':
                continue

            if n in seen:
                continue
            
            seen.add(n)
            parent[n] = v
            q.append(n)


keypad, kw, kh = util.array_2d_create_from_string(
"""
789
456
123
-0A
""")

dirpad, dw, dh = util.array_2d_create_from_string(
"""
-^A
<v>
""")

def keypad_seq(src, dst):
    return bfs(keypad, kw, kh, src, dst)

def dirpad_seq(src, dst):
    return bfs(dirpad, dw, dh, src, dst)

#for s in '123456789A':
#    for t in '123456789A':
#        print(s, t, bfs(keypad, kw, kh, s, t))

#for s in '<>^vA':
#    for t in '<>^vA':
#        print(s, t, bfs(keypad, kw, kh, s, t))

"""
for s in '123456789A':
    dist, prev = dijkstra(keypad, kw, kh, s)

    for c in '123456789A':
        path, n = [], c

        while n is not None:
            n = prev[n]
            if n is not None:
                path.append(n)
                
        seq = []
        for i in range(len(path) - 1):
            n0, n1 = path[i], path[i + 1]
            (x0, y0) = util.array_2d_index_of(keypad, n0)
            (x1, y1) = util.array_2d_index_of(keypad, n1)
            if x1 > x0:
                seq.append('>')
            elif x1 < x0:
                seq.append('<')
            elif y1 > y0:
                seq.append('V')
            else:
                seq.append('^')

        print(s, c, seq)
"""
    
@functools.cache
def cost_of_button(src, button, depth):
    if depth == 0:
        return 1
        #return dirpad_seq('A', button)

    x, y = util.array_2d_index_of(dirpad, src)
    min_cost = 2**32

    for subseq in get_all_sequences(dirpad, dw, dh, x, y, button, '', 3):
        seq_cost = 0
        dpad_src = 'A'
        for sub_button in subseq:
            #if depth == 1:
            #    seq_cost += dirpad_seq(dpad_src, sub_button)
            #    dpad_src = sub_button
            #else:
            #    seq_cost += cost_of_button(sub_button, depth - 1)
            seq_cost += cost_of_button(dpad_src, sub_button, depth - 1)
            dpad_src = sub_button
        min_cost = min(min_cost, seq_cost)

    return min_cost


def cost_of_sequence2(buttons, depth):
    if depth == 0:
        return len(buttons)
    else:
        cost = 0
        for button in buttons:
            x, y = util.array_2d_index_of(dirpad, 'A')
            min_cost = 2**32
            for subseq in get_all_sequences(dirpad, dw, dh, x, y, button, '', 3):
                subseq_cost = cost_of_sequence2(subseq, depth - 1)
                min_cost = min(min_cost, subseq_cost)
            cost += min_cost
        return cost

def cost_of_sequence(sequences, depth):
    min_cost = 2**32
    min_seq = ''
    for buttons in sequences:
        #cost = sum(cost_of_button(button, depth) for button in buttons)
        cost = 0
        src = 'A'
        for button in buttons:
            cost += cost_of_button(src, button, depth)
            src = button
        if cost < min_cost:
            min_seq = buttons
        min_cost = min(min_cost, cost)
        #print(buttons, cost)
    #print(min_cost, min_seq)
    return min_cost
        

def solve(line):
    cost = 0
    x, y = util.array_2d_index_of(keypad, 'A')
    for c in line:
        #print(c)
        results = get_all_sequences(keypad, kw, kh, x, y, c, '', 5)
        x, y = util.array_2d_index_of(keypad, c)
        #print(c)
        cost += cost_of_sequence(results, 2)
    print(cost)
    return cost * int(line.replace('A', ''))
    #print(cost_of_sequence2('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A', 0))
    cost = 0
    for c in line:
        x, y = util.array_2d_index_of(keypad, 'A')
        results = get_all_sequences(keypad, kw, kh, x, y, c, '', 5)
        cost += min(cost_of_sequence2(seq, 2) for seq in results)
        min_cost = min(cost_of_sequence2(seq, 2) for seq in results)
        #for seq in results:
        #    if cost_of_sequence2(seq, 2) == min_cost:
        #        print(c, seq, cost_of_sequence2(seq, 2))
    print(line, cost)
    return
    cost = 0
    for c in line:
        #print(c)
        x, y = util.array_2d_index_of(keypad, 'A')
        results = get_all_sequences(keypad, kw, kh, x, y, c, '', 5)
        cost += cost_of_sequence(results, 2)
    print(line, cost)
    return
    src_keypad, src_dirpad0, src_dirpad1, src_dirpad2 = 'A', 'A', 'A', 'A'
    seq0, seq1, seq2, seq3 = [], [], [], []

    for c in line:
        seq, src_keypad = keypad_seq(src_keypad, c), c
        seq0.extend(seq)
        seq0.append('A')

    for c0 in seq0:
        seq, src_dirpad0 = dirpad_seq(src_dirpad0, c0), c0
        seq1.extend(seq)
        seq1.append('A')
        
    for c1 in seq1:
        seq, src_dirpad1 = dirpad_seq(src_dirpad1, c1), c1
        seq2.extend(seq)
        seq2.append('A')

    for c2 in seq2:
        seq, src_dirpad2 = dirpad_seq(src_dirpad2, c2), c2
        seq3.extend(seq)
        seq3.append('A')
    print(''.join(seq0))
    print(''.join(seq1))
    print(''.join(seq2))
    print(''.join(seq3))
    print(len(seq0))
    print(len(seq1))
    print(len(seq2))
    print(len(seq3))

result = 0
for line in util.read_lines("in.txt"):
    result += solve(line)
print(result)