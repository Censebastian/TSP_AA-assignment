from graphic import init_graded_sqrs, screen, draw_graphs, pen
from gen_input import gen_vertices, change_nr_nodes, calc_adj_matrix
from simple_alg import ret_path
from held_karp import tour
import random
import time

#change_nr_nodes(20)
vertices = gen_vertices()
path_nn = ret_path(calc_adj_matrix(vertices))
path_hk = tour(calc_adj_matrix(vertices))
init_graded_sqrs()
draw_graphs(vertices, path_hk, path_nn, False)
#draw_graphs(vertices, path_hk, None, False)
screen.exitonclick()
