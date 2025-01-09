import turtle as t

screen = t.Screen()
screen.title("Travelling salesman")
screen.bgcolor("grey")
screen.screensize(1000, 1000)
screen.colormode(255)

side_length = 500
line_width = 3
font_size = 10
vertex_size = 20

pen = t.Turtle()
pen.speed(0)
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

def draw_vertices(x_center, y_center, coord_arr, color):
    left_bound = x_center - side_length / 2
    bottom_bound = y_center - side_length / 2
    scale_factor = side_length / 100

    for element in coord_arr:
        draw_vertex(left_bound + element.x * scale_factor, bottom_bound + element.y * scale_factor, color)

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
    pen.write("Current evaluation", False, align="center", font=("Arial", 2 * font_size, "normal"))
    pen.down()
    
    pen.up()
    pen.goto(side_length * 3/4 + line_width, side_length / 2 + line_width * 3 / 2)
    pen.write("Best path", False, align="center", font=("Arial", 2 * font_size, "normal"))
    pen.down()
