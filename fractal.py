import turtle

# Constants
ANGLE = 20
LENGTH_DECREMENT = 15

def draw_branch(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(ANGLE)
        draw_branch(branch_length - LENGTH_DECREMENT)
        turtle.left(2 * ANGLE)
        draw_branch(branch_length - LENGTH_DECREMENT)
        turtle.right(ANGLE)
        turtle.backward(branch_length)

# Set up the turtle
turtle.speed(0)
turtle.left(90)

# Draw the fractal tree
draw_branch(100)
turtle.done()
