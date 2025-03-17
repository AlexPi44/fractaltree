import turtle

def draw_branch(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)
        turtle.left(40)
        draw_branch(branch_length - 15)
        turtle.right(20)
        turtle.backward(branch_length)

turtle.speed(0)
turtle.left(90)
draw_branch(100)
turtle.done()
