import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2 * k) - 2 * \
           math.cos(3 * k) - \
           math.cos(4 * k)

speed(1000)
bgcolor("black")

for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(5):
        color("#f73487")
        goto(0, 0) # This line seems to reset the turtle to (0,0) repeatedly, which might not draw a complete heart.
                  # In the previous code I provided, the turtle continuously drew the curve.
                  # This specific implementation from the image will likely draw many lines from (0,0) to points on the curve.

done()
