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
    if blocks[j] == -1:
        blocks[j] = 0
        j -= 1
    else:
        file_len, jj, id = 0, j, blocks[j]
        while jj > i and blocks[jj] == id:
            file_len += 1
            jj -= 1

        free_len, free_start, ii = 0, 0, 0
        while ii < j and free_len < file_len:
            free_len, free_start = 0, ii

            while ii < j and blocks[ii] == -1:
                free_len += 1
                ii += 1
            ii += 1

        if file_len <= free_len:
            for x in range(file_len):
                blocks[free_start + x], blocks[j] = id, 0
                j -= 1
        else:
            j = jj
            
checksum = 0
for i, block in enumerate(blocks):
    checksum += i * max(0, block)
print(checksum)