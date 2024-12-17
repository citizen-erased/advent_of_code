import sys
import os

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

def run(filename):
    lines = [s for s in util.read_lines(filename) if len(s) > 0]
    sa, sb, sc, pr = lines

    A, B, C = int(sa.split()[-1]), int(sb.split()[-1]), int(sc.split()[-1])
    instructions = [int(s) for s in pr.replace("Program: ", "").split(',')]
    ip, out = 0, []

    while ip < len(instructions):
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
                out.append(str(operand % 8))
            case 6: # bdv
                B = A // (2**operand)
            case 7: # cdv
                C = A // (2**operand)
        
        ip += 2

    print(filename)
    print(A, B, C)
    print(','.join(out))
    print()
    
#run("test0.txt")
#run("test1.txt")
#run("test2.txt")
#run("test3.txt")
#run("test4.txt")
#run("test5.txt")
run("in.txt")