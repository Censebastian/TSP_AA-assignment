from graphic import init_graded_sqrs, screen, draw_graphs, pen
from gen_input import gen_vertices
import random
import time

def make_path():
    path = random.sample(range(0, 20), 20)
    return path

init_graded_sqrs()
path = make_path()
vertices = gen_vertices()
draw_graphs(vertices, None, path, False)
for i in range(50):
    current_path = make_path()
    draw_graphs(vertices, current_path, path, True)
screen.exitonclick()
