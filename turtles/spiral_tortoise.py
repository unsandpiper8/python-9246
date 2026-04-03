import turtle

t = turtle
t.speed(0)
screen = turtle.Screen()
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()


root.resizable(False, False)

t.hideturtle()
for steps in range(300):
    for c in ('black', 'white'):
        t.color(c)
        t.forward(steps)
        t.right(30)
        t.update()


screen.done()

# created by unsandpiper8 3/4/2026 for the python-9246 repo.