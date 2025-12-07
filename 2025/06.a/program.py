import sys
import os
from functools import reduce

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

lines      = util.read_lines("input.txt")
operations = lines[-1].split()
numbers    = []

for line in lines[:-1]:
    numbers.append([int(x) for x in line.split()])

result = 0
for data in zip(*numbers, operations):
    if data[-1] == '*':
        result += reduce(lambda x, y: x*y, data[:-1])
    elif data[-1] == '+':
        result += sum(data[:-1])

print(result)