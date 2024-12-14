import os
from functools import reduce

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    data = f.read()
    
    
result = 0
enabled = True

for i in range(len(data)):
    rest = data[i:]
    
    if rest.startswith("don't"):
        enabled = False
        continue
    
    if rest.startswith("do"):
        enabled = True
        continue
    
    if not rest.startswith("mul("):
        continue

    rest = rest[4:]
    a, rest = rest.split(',', 1)
    b, rest = rest.split(')', 1)
    
    try:
        if enabled:
            result += int(a) * int(b)
    except:
        pass
    
print(result)