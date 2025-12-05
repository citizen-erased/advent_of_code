import sys
import os
import itertools

# Ensure util is in the sys.path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util

connections, computers = {}, set()
in_neighbours, out_neighbours = {}, {}
for line in util.read_lines("test0.txt"):
    a, b = line.split('-')
    #connections.add((a, b))
    connections.setdefault(a, set()).add(b)
    in_neighbours.setdefault(a, set()).add(b)
    out_neighbours.setdefault(b, set()).add(a)
    #connections.add((b, a))
    computers.add(a)
    computers.add(b)
"""
    For each vertex u of the graph, mark u as unvisited. Let L be empty.
    For each vertex u of the graph do Visit(u), where Visit(u) is the recursive subroutine:

        If u is unvisited then:
            Mark u as visited.
            For each out-neighbour v of u, do Visit(v).
            Prepend u to L.
        Otherwise do nothing.

    For each element u of L in order, do Assign(u,u) where Assign(u,root) is the recursive subroutine:

        If u has not been assigned to a component then:
            Assign u as belonging to the component whose root is root.
            For each in-neighbour v of u, do Assign(v,root).
        Otherwise do nothing.
"""

def visit(u, visited, L):
    if u not in visited:
        visited.add(u)
        for v in out_neighbours.get(u, ()):
            visit(v, visited, L)
        L.insert(0, u)
        
def assign(u, root):
    if u not in assigned:
        assigned.add(u)
        component_roots.setdefault(root, []).append(u)

        for v in in_neighbours[u]:
            assign(v, root)
        

visited, L = set(), []
for computer in computers:
    visit(computer, visited, L)
print(L)
    
assigned, component_roots = set(), {}
for u in L:
    assign(u, u)

print(component_roots)