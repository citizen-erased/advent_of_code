import os
from functools import reduce

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    lines = [line.strip() for line in f]

reports = [[int(x) for x in line.split()] for line in lines]

def is_safe(report):
    if not (report == sorted(report) or report == list(reversed(sorted(report)))):
        return False

    for i in range(0, len(report) - 1):
        a, b = report[i], report[i + 1]
        diff = abs(a - b)

        if diff < 1 or diff > 3:
            return False
        
    return True
    
result = sum(is_safe(report) for report in reports)
print(result)