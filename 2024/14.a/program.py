import sys
import os
import math

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from util import vec2

lines = util.read_lines("in.txt")

qc = [0,0,0,0]
for line in lines:
    p, v = line.split();
    p = vec2(*[int(c) for c in p.replace("p=", "").split(',')])
    v = vec2(*[int(c) for c in v.replace("v=", "").split(',')])
    p = (p + v*100) % vec2(101, 103)
    if not (p.x == 101 // 2 or p.y == 103 // 2):
        x = 0 if p.x < 101 // 2 else 1
        y = 0 if p.y < 103 // 2 else 1
        qc[x | (y << 1)] += 1
print(math.prod(qc))