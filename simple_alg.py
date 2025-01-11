import math
import verify
from itertools import permutations
from gen_input import calc_adj_matrix, gen_vertices

def tsp(dists):

    if verify(dists) is not True:
        print("Nu exista solutie")
        return

    visited = []
    min_dist = []

    start = 0
    neighbor = start
    nr_nodes = len(dists)
    noN = 0

    while noN < nr_nodes and neighbor not in visited:
        visited.append(neighbor)
        noNei = 0
        MIN = 0
        
        while noNei < len(dists[neighbor]):
            if noNei not in visited:
                if MIN == 0:
                    MIN = dists[neighbor][noNei]
                    neighbor = noNei
                else:
                    min_distance = min(dists[neighbor][noNei], MIN)
                    if dists[neighbor][noNei] < MIN:
                        MIN = min_distance
                        neighbor = noNei
            noNei += 1
        min_dist.append(MIN)
        noN += 1
    
    last = visited[-1]
    min_dist[-1] = dists[last][start]
