import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

def operand_str(n):
        match n:
            case 4:
                return 'A'
            case 5:
                return 'B'
            case 6:
                return 'C'
            case _:
                return n

def execute(A, B, C, instructions):
    ip, out = 0, []

    while ip < len(instructions):
        opstr = operand_str(instructions[ip + 1])

        match instructions[ip + 1]:
            case 4:
                operand = A
            case 5:
                operand = B
            case 6:
                operand = C
            case _:
                operand = instructions[ip + 1]

        match instructions[ip]:
            case 0: # adv
                A = A // (2**operand)
            case 1: # bxl
                B = B ^ instructions[ip + 1]
            case 2: # bst
                B = operand % 8
            case 3: # jnz
                if A != 0:
                    ip = operand - 2
            case 4: # bxc
                B = B ^ C
            case 5: # out
                out.append(operand % 8)
            case 6: # bdv
                B = A // (2**operand)
            case 7: # cdv
                C = A // (2**operand)
        
        ip += 2
        
    return out

lines = [s for s in util.read_lines("in.txt") if len(s) > 0]
sa, sb, sc, pr = lines

A, B, C = int(sa.split()[-1]), int(sb.split()[-1]), int(sc.split()[-1])
instructions = [int(s) for s in pr.replace("Program: ", "").split(',')]

def bin_str(n):
    s = bin(n).replace("0b", "")
    while len(s)%3 != 0:
        s = '0' + s
    return ' '.join(s[i:i+3] for i in range(0, len(s), 3))

# The observation here is that the highest 3 bits control the output of the final character,
# the second highest three bits control the output of the second to last character, etc.
# Each group of 3 bits can be figured out in order, starting with the highest which produces
# the final character of the output. Each digit can be tried sequantially in order so that
# the final output will give the minimum value for A.

#for n in range(0, 8):
#    A = 7 << (15*3)
#    A = A | (0 << (14*3))
#    A = A | (2 << (13*3))
#    A = A | (6 << (12*3))
#    #A = A | n
#    out = execute(A, B, C, instructions)
#    print(n)
#    print(bin_str(A))
#    print(out)
    

def dfs(digits, i):
    for x in range(8):
        digits[i] = x

        A = 0
        for s, d in enumerate(reversed(digits)):
            A = A | (d << (s*3))

        out = execute(A, B, C, instructions)
    
        if out[-i-1] == instructions[-i-1]:
            if i < len(digits) - 1:
                dfs(digits, i + 1)
            elif out == instructions:
                print(A)
            
dfs([0 for _ in range(16)], 0)