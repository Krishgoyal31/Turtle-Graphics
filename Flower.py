from turtle import *
import colorsys

# Setup
speed(0)
bgcolor("black")
pensize(2)
h = 0  # hue for color

# Total number of petals
n = 36

# Draw petals
for i in range(n):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 1/n  # Gradual color change

    # Begin petal
    begin_fill()
    rt(360 / n)  # Rotate to next petal angle
    circle(100, 60)
    lt(120)
    circle(100, 60)
    end_fill()

# Optional flower center
penup()
goto(0, -20)
pendown()
color("yellow")
begin_fill()
circle(20)
end_fill()

hideturtle()
done()
