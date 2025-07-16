import turtle
import random

def tree(branch_length, t, level):
    """
    Draws a fractal tree using recursion.

    Args:
        branch_length (int): The initial length of the branch.
        t (turtle.Turtle): The turtle object.
        level (int): The current recursion level (controls color and thickness).
    """
    if branch_length > 5:
        # Set color based on recursion level
        if level < 4:
            t.pencolor(random.choice(["sienna", "brown", "darkgreen"]))
        else:
            t.pencolor(random.choice(["forestgreen", "limegreen", "lightgreen"]))

        # Set pen thickness based on branch length
        t.pensize(branch_length / 10)

        # Draw main branch
        t.forward(branch_length)
        t.right(20)

        # Recursively draw right branch
        tree(branch_length - random.randint(10, 20), t, level + 1)

        t.left(40)

        # Recursively draw left branch
        tree(branch_length - random.randint(10, 20), t, level + 1)

        t.right(20)
        t.backward(branch_length) # Go back to the starting point

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("black")
    screen.title("Recursive Fractal Tree")

    t = turtle.Turtle()
    t.speed("fastest") # Max speed for drawing
    t.penup()
    t.left(90) # Point turtle upwards
    t.backward(screen.window_height() / 2 - 50) # Move to bottom of screen
    t.pendown()

    t.color("sienna") # Initial tree trunk color
    t.pensize(15) # Initial trunk thickness

    tree(100, t, 1) # Start drawing the tree

    screen.exitonclick()

if __name__ == "__main__":
    main()
