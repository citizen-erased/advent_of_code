import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

lines = util.read_lines("in.txt")
lines = [line for line in lines if line != ""]


def parse_xy(prefix, s):
    (dir0, dir1) = s.replace(prefix, "").split(",")
    dir0 = int(dir0.replace('=', '').strip()[1:])
    dir1 = int(dir1.replace('=', '').strip()[1:])
    return vec2(dir0, dir1)


def uniform_cost_search(da, db, goal):
    frontier = [(0, 0, 0, (vec2(0, 0), ' '))]
    frontier_set = set()
    expanded = set()
    
    while True:
        if not frontier:
            return None
        
        min_cost, min_index = 2**32, 0
        for i, node in enumerate(frontier):
            if node[0] < min_cost:
                min_cost, min_index = node[0], i

        (cost, a_count, b_count, (position, button)) = frontier.pop(min_index)
        
        if position == goal:
            print(a_count, b_count, cost)
            return cost
        elif cost > 300:
            return 0

        expanded.add((position, button))
        
        neighbours = (
            (cost + 3, a_count + 1, b_count + 0, (position + da, 'a')),
            (cost + 1, a_count + 0, b_count + 1, (position + db, 'b')),
        )

        for (n_cost, n_a, n_b, n_node) in neighbours:
            if n_a > 100 or n_b > 100:
                continue

            if n_node not in expanded and n_node not in frontier_set:
                frontier.append((n_cost, n_a, n_b, n_node))
                frontier_set.add(n_node)
            elif n_node in frontier_set:
                for i, (x_cost, _, _, x_node) in enumerate(frontier):
                    if x_node == n_node and x_cost > n_cost:
                        frontier[i] = (cost, n_a, n_b, x_node)
                        break
                    
def extended_gcd(a, b):
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    
    print( "Bézout coefficients:", (old_s, old_t))
    print( "greatest common divisor:", old_r)
    print( "quotients by the gcd:", (t, s))

    # gcd, quotients
    return old_r, t, s


def brute_force(a, b, p):
    min_cost = 2**32

    for x in range(101):
        for y in range(101):
            if a * x + b * y == p:
                cost = x * 3 + y
                min_cost = min(cost, min_cost)
                
    return min_cost if min_cost < 2**32 else 0


tokens = 0
for i in range(0, len(lines), 3):
    da = parse_xy("Button A:", lines[i + 0])
    db = parse_xy("Button B:", lines[i + 1])
    dst = parse_xy("Prize:", lines[i + 2])

    #print(da, db, dst)
    #gcd, n0, n1 = extended_gcd(dst.x, dst.y)
    #tokens += uniform_cost_search(da, db, dst)

    tokens += brute_force(da, db, dst)
    
    
print(tokens)