import os
import itertools

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    fs = [line.strip() for line in f][0]

blocks, ids = [], []
 
for i, count_str in enumerate(fs):
    for j in range(int(count_str)):
        blocks.append(i//2 if i % 2 == 0 else -1)
        
i, j = 0, len(blocks) - 1

while i < j:
    if blocks[i] != -1:
        i += 1
    elif blocks[j] == -1:
        blocks[j] = 0
        j -= 1
    else:
        blocks[i], blocks[j] = blocks[j], 0
        i, j = i + 1, j - 1

checksum = 0
for i, block in enumerate(blocks):
    checksum += i * block
print(checksum)