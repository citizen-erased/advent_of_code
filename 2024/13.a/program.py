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

    tokens += brute_force(da, db, dst)
    
    
print(tokens)