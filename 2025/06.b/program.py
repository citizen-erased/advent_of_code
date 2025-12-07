import sys
import os
from functools import reduce

# Ensure util is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

rows = util.read_lines("input.txt", strip=False)
row_length = max([len(row) for row in rows])

for i, row in enumerate(rows):
    while len(row) < row_length:
        row += ' '
    rows[i] = row

op, nums, column_count, result = ' ', [], len(rows) - 1, 0

for i in range(row_length):
    new_op = rows[-1][i]
    if new_op in ('+', '*'):
        op = new_op

    nums.append(''.join(row[i] for row in rows[:-1]))

    is_end = all(row[i] == ' ' for row in rows) or i == row_length - 1

    if is_end:
        nums = [int(x) for x in nums if x.strip() != '']
        print(op, nums)

        if op == '*':
            result += reduce(lambda x, y: x*y, nums)
        elif op == '+':
            result += sum(nums)

        op, nums = ' ', []

print(result)