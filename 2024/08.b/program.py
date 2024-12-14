import os
import itertools

class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    
    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)
    
    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)
    
    def __ge__(self, other):
        return (self.x, self.y) >= (other.x, other.y)
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __ne__(self, other):
        return (self.x, self.y) != (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

input_filename = "in.txt"
input_filepath = os.path.join(os.path.dirname(__file__), input_filename)

with open(input_filepath) as f:
    map = [[c for c in line.strip()] for line in f]
    
w, h = len(map[0]), len(map)

freq_to_nodes = {}

for y in range(h):
    for x in range(w):
        freq = map[y][x] 
        if freq != '.':
            freq_to_nodes.setdefault(freq, [])
            freq_to_nodes[freq].append(vec2(x, y))
            
antinodes = set()
for freq, nodes in freq_to_nodes.items():
    for a, b in itertools.combinations(nodes, 2):
        delta = b - a

        while 0 <= a.x < w and 0 <= a.y < h:
            antinodes.add(a)
            a -= delta

        while 0 <= b.x < w and 0 <= b.y < h:
            antinodes.add(b)
            b += delta
            
print(len(antinodes))