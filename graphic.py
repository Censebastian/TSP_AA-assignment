import turtle as t

screen = t.Screen()
screen.title("Travelling salesman")
screen.bgcolor("grey")
screen.screensize(1000, 1000)

side_length = 500
line_width = 3
font_size = 10

pen = t.Turtle()
pen.speed(0)
pen.ht()
pen.pensize(3)

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

pen.up()
pen.goto(-(side_length + side_length / 4 + line_width * 3/2), side_length / 2 + line_width / 2)
pen.down()

pen.fillcolor("white")
pen.begin_fill()

for _ in range(4):
    pen.forward(side_length + line_width / 2)
    pen.right(90)

pen.end_fill()

pen.up()
pen.goto(side_length / 4 + line_width / 2, side_length / 2 + line_width / 2)
pen.down()

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

screen.exitonclick()
