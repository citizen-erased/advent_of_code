import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

lines = util.read_lines("in.txt")
lines0, lines1 = util.split_input_lines_into_sections(lines)

wire_state = {}
for line in lines0:
    wire, state = line.split(':')
    wire, state = wire.strip(), True if state.strip() == '1' else False
    wire_state[wire] = state

gates = []
for line in lines1:
    a, op, b, _, c = line.split()
    gates.append((a, op, b, c))
    
def compute(x, y, gates, max_loops=32):
    wire_state = {}

    for i in range(45):
        kx = f'x0{i}' if i < 10 else f'x{i}'
        ky = f'y0{i}' if i < 10 else f'y{i}'
        wire_state[kx] = True if x & (1 << i) else False
        wire_state[ky] = True if y & (1 << i) else False

    running, loop = True, 0
    while running and loop < max_loops:
        running, loop = False, loop + 1

        for (a, op, b, c) in gates:
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
            
    if loop < max_loops:
        return num
    return None

def gate_types_wire_connects_to(wire):
    result = []
    for (a, op, b, _) in gates:
        if a == wire or b == wire:
            result.append(op)
    return list(sorted(result))

def gate_inputs_from(in0, in1):
    result = []
    for (_, op, _, c) in gates:
        if c in (in0, in1):
            result.append(op)
    return list(sorted(result))

wrong = []
for (a, op, b, c) in gates:
    if c[0] == 'z' and op != 'XOR':
        print("case 0")
        print(a, op, b, c)
        wrong.append(c)

    elif op == 'XOR' and a[0] in ('x', 'y') and b[0] in ('x', 'y'):
        if gate_types_wire_connects_to(c) != ['AND', 'XOR']:
            if not (a == 'x00' and b == 'y00'): # okay for first half adder. this is carry.
                print("case 1")
                print(a, op, b, c)
                wrong.append(c)
            
    elif op == "AND":
        if gate_types_wire_connects_to(c) != ['OR']:
            if not (a == 'x00' and b == 'y00'): # okay for first half adder. this is carry.
                print("case 2")
                print(a, op, b, c)
                wrong.append(c)
        if a[0] not in ('x', 'y') and b[0] not in ('x', 'y') and (gate_inputs_from(a, b) != ['OR', 'XOR']):
            if c != 'jjp':
                print("case 3")
                print(a, op, b, c)
                wrong.append(c)

    elif op == "OR":
        if gate_types_wire_connects_to(c) != ['AND', 'XOR']:
            print("case 4")
            print(a, op, b, c)
            wrong.append(c)


    #if op == 'XOR' and c[0] != 'z':
    #    if a[0] not in ('x', 'y') or b[0] not in ('x', 'y'):
    #        #print(a, op, b, c)
    #        wrong.append(c)
print(','.join(sorted(set(wrong))))
asda=asda
    


dst_to_src = {}
for line in lines1:
    a, _, b, _, c = line.split()
    dst_to_src[c] = (a, b)

def wire_to_gates(w):
    if w[0] == 'x' or w[0] == 'y':
        return []
    a, b = dst_to_src[w]
    return [w] + wire_to_gates(a) + wire_to_gates(b)

print(wire_to_gates('z05'))

def swap_outputs(o0, o1):
    gates2 = []
    for a, op, b, c in gates:
        if c == o0:
            gates2.append((a, op, b, o1))
        elif c == o1:
            gates2.append((a, op, b, o0))
        else:
            gates2.append((a, op, b, c))
    return gates2
    

for o0 in wire_to_gates('z05'):
    for o1 in wire_to_gates('z05'):
        gates2 = swap_outputs(o0, o1)
        a = bin(1<<5)
        b = compute(1<<5, 0, gates2)
        if a == b:
            print(o0, o1)

all_wires = []
for line in lines1:
    a, _, b, _, c = line.split()
    all_wires.append(a)
    all_wires.append(b)
    all_wires.append(c)
all_wires = list(set(all_wires))

for o0 in all_wires:
    for o1 in all_wires:
        gates2 = swap_outputs(o0, o1)
        a = bin(1<<5)
        b = compute(1<<5, 0, gates2)
        if a == b:
            print(o0, o1)
        
abc=defg

for i in range(45):
    print(bin(1<<i))
    print(bin(compute(1<<i, 0)))
    print()

for i in range(2000):
    A, B = 0, i
    ans0 = A + B
    ans1 = compute(A, B)

    if ans0 != ans1:
        print(i)
        print(bin(ans0))
        print(bin(ans1))