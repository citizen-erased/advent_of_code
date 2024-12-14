import os
from functools import reduce

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    lines = [line.strip() for line in f]
    
rules = []
for line in lines:
    if '|' in line:
        a, b = line.split('|')
        rules.append((int(a), int(b)))
        
updates = []
for line in lines[len(rules) + 1:]:
    updates.append([int(x) for x in line.split(',')])
    
    
def has_contradict(i, pages):
    pages_before, pages_after = pages[:i], pages[i + 1:]

    for (before, after) in rules:
        if before == pages[i] and after in pages_before:
            return True
        if after == pages[i] and before in pages_after:
            return True
        
    return False

result = 0
for update in updates:
    error = False

    for i in range(len(update)):
        if has_contradict(i, update):
            error = True
            
    if error == False:
        result += update[len(update) // 2]

print(result)