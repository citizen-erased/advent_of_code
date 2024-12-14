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

for j in range(25):
    result = []

    for i, s in enumerate(stones):
        if s == 0:
            result.append(1)
        elif len(str(s)) % 2 == 0:
            intstr = str(s)
            a, b = intstr[:len(intstr) // 2], intstr[len(intstr) // 2:]
            result.append(int(a))
            result.append(int(b))
        else:
            result.append(s * 2024)
            
    stones = result
            
print(len(stones))