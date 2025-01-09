from graphic import init_graded_sqrs, draw_vertices, side_length, line_width, screen
from gen_input import gen_vertices

init_graded_sqrs()
draw_vertices(-side_length * 3/4 - line_width, 0, gen_vertices(), (255, 0, 0))
screen.exitonclick()
