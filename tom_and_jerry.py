import turtle as tu
import re
import docx  # Make sure 'python-docx' is installed

# Load coordinates from DOCX file
source = "tom_and_jerry"  # Make sure "tom_and_jerry.docx" is in the same folder
data = docx.Document("{}.docx".format(source))

coordinates = []
colour = []

for i in data.paragraphs:
    try:
        coord_stg_tup = re.findall(r'\(([-+]?\d*\.?\d+[eE]?[-+]?\d*?), ([-+]?\d*\.?\d+[eE]?[-+]?\d*?)\)', i.text)
        coord_num_tup = []

        color_stg_tup = re.findall(r'\(([-+]?\d*\.?\d+[eE]?[-+]?\d*?), ([-+]?\d*\.?\d+[eE]?[-+]?\d*?), ([-+]?\d*\.?\d+[eE]?[-+]?\d*?)\)', i.text)
        color_val = re.findall(r'[-+]?\d*\.?\d+', str(color_stg_tup[0]))
        color_val_lst = [float(k) for k in color_val]
        colour.append(tuple(color_val_lst))

        for j in coord_stg_tup:
            coord_pos = re.findall(r'[-+]?\d*\.?\d+', str(j))
            coord_num_lst = [float(k) for k in coord_pos]
            coord_num_tup.append(tuple(coord_num_lst))

        coordinates.append(coord_num_tup)

    except:
        pass

# Setup turtle
pen = tu.Turtle()
screen = tu.Screen()
tu.tracer(0)
pen.hideturtle()
pen.speed(0)
screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)

# Drawing loop
for i in range(len(coordinates)):
    draw = 1
    path = coordinates[i]
    col = colour[i]
    pen.color(col)
    pen.begin_fill()

    for order_pair in path:
        x, y = order_pair
        y = -1 * y
        if draw:
            pen.up()
            pen.goto(x, y)
            pen.down()
            draw = 0
        else:
            pen.goto(x, y)

    pen.end_fill()
    pen.hideturtle()

screen.mainloop()
