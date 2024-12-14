import sys
import os
import math

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


def solve(a, b, p):
    lcm = math.lcm(a.x, a.y)
    s0  = lcm // a.x
    s1  = lcm // a.y

    lhs = b.x * s0 - b.y * s1
    rhs = p.x * s0 - p.y * s1

    n1 = rhs // lhs
    n0 = (p.x - b.x * n1) // a.x

    has_solution = p == a * n0 + b * n1
    
    if has_solution:
        return n0 * 3 + n1
    return 0


tokens = 0
for i in range(0, len(lines), 3):
    da = parse_xy("Button A:", lines[i + 0])
    db = parse_xy("Button B:", lines[i + 1])
    dst = parse_xy("Prize:", lines[i + 2])

    tokens += solve(da, db, dst + 10000000000000)

print(tokens)