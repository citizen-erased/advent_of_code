import os
from functools import reduce

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    lines = [line.strip() for line in f]

l, r = [], []
for line in lines:
    a, b = line.split()
    l.append(int(a))
    r.append(int(b))

result = 0
for a in l:
    count = sum(1 for x in r if x == a)
    result += a * count
print(result)