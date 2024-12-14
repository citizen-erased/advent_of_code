import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
from functools import cache

stones = [int(x) for x in util.read_single_line("in.txt").split()]

@cache
def solve(s, depth):
    if depth == 0:
        return 1
    elif s == 0:
        return solve(1, depth - 1)
    elif len(str(s)) % 2 == 0:
        intstr = str(s)
        a, b = intstr[:len(intstr) // 2], intstr[len(intstr) // 2:]
        return solve(int(a), depth - 1) + solve(int(b), depth - 1)
    else:
        return solve(s * 2024, depth - 1)
        
result = sum((solve(s, 75) for s in stones))
            
print(result)
