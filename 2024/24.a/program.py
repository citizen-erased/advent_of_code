import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

lines = util.read_lines("in.txt")

wire_state = {}
while (line := lines.pop(0)) != "":
    wire, state = line.split(':')
    wire, state = wire.strip(), True if state.strip() == '1' else False
    wire_state[wire] = state
    
running = True
while running:
    running = False

    for line in lines:
        a, op, b, _, c = line.split()

        if a in wire_state and b in wire_state:
            if op == "AND":
                wire_state[c] = wire_state[a] and wire_state[b]
            elif op == "OR":
                wire_state[c] = wire_state[a] or wire_state[b]
            elif op == "XOR":
                wire_state[c] = wire_state[a] != wire_state[b]
        else:
            running = True

z_keys = sorted(w for w in wire_state.keys() if w[0] == 'z')

num = 0
for i, w in enumerate(z_keys):
    if wire_state[w]:
        num = num | (1 << i)
print(num)