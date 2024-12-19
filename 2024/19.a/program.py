import sys
import os
from functools import cache

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

lines = util.read_lines("in.txt")
towels = [t.strip() for t in lines[0].split(",")]

@cache
def dfs(rest):
    if not rest:
        return True

    for towel in towels:
        if rest.startswith(towel):
            if dfs(rest[len(towel):]):
                return True

    return False

result = 0
for p in lines[2:]:
    if dfs(p):
        result += 1
print(result)