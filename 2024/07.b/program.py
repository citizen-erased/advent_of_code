import os
import itertools

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    lines = [line.strip() for line in f]
    
result = 0

for line in lines:
    value, rest = line.split(':')
    value = int(value)

    operands = [int(x) for x in rest.strip().split(' ')]

    for ops in itertools.product("+*|", repeat=len(operands) - 1):
        a = operands[0]

        for op, b in zip(ops, operands[1:]):
            if op == '+':
                a += b
            elif op == '*':
                a *= b
            elif op == '|':
                a = int(str(a) + str(b))
                
        if a == value:
            result += a
            break

print(result)
