import turtle as t
import gen_input

screen = t.Screen()
screen.title("Travelling salesman")
screen.bgcolor("grey")
screen.screensize(1000, 1000)
screen.colormode(255)
screen.tracer(0)

side_length = 500
line_width = 3
font_size = 10
vertex_size = 20

pen = t.Turtle()
pen.ht()
pen.pensize(3)

def teleport(x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()

def write_gradations(x, y, vertical):
    nr_gradations = 5
    for i in range(nr_gradations + 1):
        gradation = int(i * 100 / nr_gradations)
        pen.up()
        if vertical == False:
            pen.goto(x + i * side_length / nr_gradations, y)
            pen.write(str(gradation), False, align="center", font=("Arial", font_size, "normal"))
        if vertical == True:
            pen.goto(x, y + i * side_length / nr_gradations)
            pen.write(str(gradation), False, align="right", font=("Arial", font_size, "normal"))
        pen.down()

def adjust_coordinates(coord_arr, left_bound, bottom_bound):
    scale_factor = side_length / 100
    adjusted_coord = []

    for vertex in coord_arr:
        new_x = left_bound + scale_factor * vertex.x
        new_y = bottom_bound + scale_factor * vertex.y
        adjusted_coord.append(gen_input.vertex(new_x, new_y))

    return adjusted_coord

def draw_vertex(x, y, color):
    pen.up()
    pen.goto(x - vertex_size / 2, y + vertex_size / 2)

    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(vertex_size)
        pen.right(90)
    pen.end_fill()

    pen.goto(x - vertex_size / 3, y + vertex_size / 3)

    pen.fillcolor((3, 6, 186))
    pen.begin_fill()
    for _ in range(4):
        pen.forward(vertex_size * 2 / 3)
        pen.right(90)
    pen.end_fill()
    pen.down()

def draw_vertices(coord_arr, color):
    for element in coord_arr:
        draw_vertex(element.x, element.y, color)

def draw_edge(x1, y1, x2, y2, color):
    teleport(x1, y1)
    pen.color(color)
    pen.pensize(6)
    pen.goto(x2, y2)
    pen.color("black")

def draw_edges(coord_arr, path, color):
    for i in range(len(path)):
        first_node = coord_arr[path[i % len(path)]]
        second_node = coord_arr[path[(i + 1) % len(path)]]
        draw_edge(first_node.x, first_node.y, second_node.x, second_node.y, color)
        

def init_graded_sqrs():
    teleport(-(side_length + side_length / 4 + line_width * 3/2), side_length / 2 + line_width / 2)
    
    pen.fillcolor("white")
    pen.begin_fill()
    
    for _ in range(4):
        pen.forward(side_length + line_width / 2)
        pen.right(90)
    
    pen.end_fill()
    
    teleport(side_length / 4 + line_width / 2, side_length / 2 + line_width / 2)
    
    pen.begin_fill()
    
    for _ in range(4):
        pen.forward(side_length + line_width / 2)
        pen.right(90)
    
    pen.end_fill()
    
    write_gradations(-(side_length + side_length / 4 + line_width * 5/2), -(side_length / 2 + line_width), True)
    write_gradations(-(side_length + side_length / 4 + line_width * 5/2 - font_size), -(side_length / 2 + line_width + 3/2 * font_size), False)
    
    write_gradations(side_length / 4, -(side_length / 2 + line_width), True)
    write_gradations(side_length / 4 + font_size, -(side_length / 2 + line_width + 3/2 * font_size), False)
    
    pen.up()
    pen.goto(-(side_length * 3/4 + line_width), side_length / 2 + line_width * 3 / 2)
    pen.write("Held-Karp", False, align="center", font=("Arial", 2 * font_size, "normal"))
    pen.down()
    
    pen.up()
    pen.goto(side_length * 3/4 + line_width, side_length / 2 + line_width * 3 / 2)
    pen.write("Nearest Neighbor", False, align="center", font=("Arial", 2 * font_size, "normal"))
    pen.down()

def draw_graph(coord_arr, path, left_bound, bottom_bound, color):
    adj_coords = adjust_coordinates(coord_arr, left_bound, bottom_bound)
    if path != None:
        draw_edges(adj_coords, path, color)
    draw_vertices(adj_coords, color)

def draw_temp_graph(coord_arr, path, left_bound, bottom_bound, color):
    global pen
    perm_turtle = pen
    pen = t.Turtle()
    adj_coords = adjust_coordinates(coord_arr, left_bound, bottom_bound)
    if path != None:
        screen.ontimer(draw_edges(adj_coords, path, color), 2000)
    pen = perm_turtle
    draw_vertices(adj_coords, color)
    
def draw_graphs(coord_arr, current_path, correct_path, temp):
    x_left = -(side_length * 5 / 4 + line_width)
    x_right = side_length / 4 + line_width
    y_right = y_left = -side_length / 2
    #if temp == True:
    #    draw_temp_graph(coord_arr, current_path, x_left, y_left, (255, 0, 0))
    #else:
    draw_graph(coord_arr, current_path, x_left, y_left, (255, 0, 0))
    draw_graph(coord_arr, correct_path, x_right, y_right, (10, 230, 57))
