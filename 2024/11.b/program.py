import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import itertools
from util import vec2

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    lines = [line.strip() for line in f]
    
stones = [int(x) for x in lines[0].split()]
lookup = {}

def solve(s, depth):
    if depth == 0:
        return 1
    
    result = lookup.get((s, depth))

    if result is not None:
        return result

    if s == 0:
        result = solve(1, depth - 1)
    elif len(str(s)) % 2 == 0:
        intstr = str(s)
        a, b = intstr[:len(intstr) // 2], intstr[len(intstr) // 2:]
        result = solve(int(a), depth - 1) + solve(int(b), depth - 1)
    else:
        result = solve(s * 2024, depth - 1)
        
    lookup[(s, depth)] = result
    return result

result = 0
for s in stones:
    result += solve(s, 75)
            
print(result)