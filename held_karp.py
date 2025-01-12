import math
from gen_input import calc_adj_matrix, gen_vertices

distances = [
    [0, 20, 42, 35],
    [20, 0, 30, 34],
    [42, 30, 0, 12],
    [35, 34, 12, 0]
]

distance = calc_adj_matrix(gen_vertices())


def held_karp(dists):
    """
    Implementation of the Held-Karp algorithm
    Solves TCP using dynamic programming

    Receives a cost matrix, writes in an output file the length of the shortest road and the path found
    
    """
    n = len(dists) # Nr. of cities
    table = [[math.inf] * n for _ in range(1 << n)]
    parent = [[None] * n for _ in range(1 << n)]
    
    # Base case
    table[1][0] = 0;
    
    for mask in range(1 << n):
        for last in range(n):
            if not (mask & (1 << last)):
                continue
            for next in range(n):
                if mask & (1 << n):
                    continue
                new_m = mask | (1 << next)
                new_d = table[mask][last] + dists[last][next]
                if new_d < table[new_m][next]:
                    table[new_m][next] = new_d
                    parent[new_m][next] = last
   
    tour = []
    min_cost = math.inf
    end_city = None
    full_mask = (1 << n) - 1
    for last in range(1, n):
        cost = table[full_mask][last] + dists[last][0]
        if cost < min_cost:
            min_cost = cost
            end_city = last
    
    last = end_city
    mask = full_mask
    while mask:
        tour.append(last)
        new_last = parent[mask][last]
        mask ^= (1 << last)
        last = new_last
    
    tour = tour[::-1]
    tour.append(0)
    
    f = open("demofile.txt", "w")
    f.write("Optimal path: " + str(tour))
    f.write("\nMinimum cost: " + str(min_cost))

    return min_cost
