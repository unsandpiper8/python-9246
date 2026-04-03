# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "sympy>=1.14.0",
# ]
# ///

# imports
import random
import turtle

from sympy import sieve

# configuration and global variables
t = turtle
screen = turtle.Screen()
t.tracer(0)
shape_number = 0

def start_script():
    t.resetscreen()
    t.tracer(0)

    #logic
    turtle_forward = random.randint(200, 400)
    primes = list(sieve.primerange(80, 181))
    turtle_left = random.choice(primes)

    t.teleport(-turtle_forward / 2, -turtle_left / 2)
    t.begin_fill()
    t.color("white")
    t.fillcolor("black")

    for _ in range(200):
        t.fd(turtle_forward)
        t.lt(turtle_left)
        if abs(t.pos()) < 1:
            break

    t.end_fill()
    t.update()
    return turtle_forward, turtle_left



# function for starting script and restarting it when clicking screen 
def handle_click_and_start(_x, _y):
    global shape_number
    shape_number += 1
    size, shape = start_script()
    print(
        f"shape number {shape_number} has properties:\nsize/turtle_forward = {size} \nshape/turtle_left = {shape}"
        )


# listens for click
screen.onscreenclick(handle_click_and_start)

# starts the script
handle_click_and_start(0, 0)
t.done()

# created by unsandpiper8 3/4/2026 for the python-9246 repo.