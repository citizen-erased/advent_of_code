import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

result = 0
for line in util.read_lines("in.txt"):
    n = int(line)
    for step in range(2000):
        n = (n ^ (n << 6)) & 16777215
        n = (n ^ (n >> 5)) & 16777215
        n = (n ^ (n << 11)) & 16777215
    result += n
print(result)