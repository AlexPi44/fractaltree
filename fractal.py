import turtle
import random
import time

# Constants
BASE_ANGLE = 20
LENGTH_DECREMENT = 15

def draw_branch(branch_length, angle):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(angle)
        draw_branch(branch_length - LENGTH_DECREMENT, angle)
        turtle.left(2 * angle)
        draw_branch(branch_length - LENGTH_DECREMENT, angle)
        turtle.right(angle)
        turtle.backward(branch_length)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
turtle.color("green")
turtle.width(2)
turtle.speed("fastest")

turtle.penup()
turtle.goto(0, -250)
turtle.setheading(90)
turtle.pendown()

# Continuous drawing loop
def draw_loop():
    while True:
        turtle.clear()
        angle_variation = random.randint(-5, 5)
        draw_branch(100, BASE_ANGLE + angle_variation)
        time.sleep(1)  # Pause a bit between redraws

# Run in a try/except block to allow for safe exit
try:
    draw_loop()
except turtle.Terminator:
    print("Turtle graphics window closed.")

# Optional: clean exit on click (if not using while loop)
# screen.exitonclick()
