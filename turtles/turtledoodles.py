# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# imports
from random import randint
from turtle import Turtle, Screen


t1 = Turtle()
# t2 = Turtle()
screen = Screen()

running = True


def stop():
    global running
    running = False
    print("quit")

screen.listen()
screen.onkey(stop, "q")


t1.speed(0)

while running:
    t1.forward(randint(1, 20))
    t1.right(randint(40, 90))
    if t1.xcor() > 300:
        t1.penup()   
        t1.home()
        t1.pendown()
    if t1.xcor() < -300:
        t1.penup()
        t1.home()
        t1.pendown()
    if t1.ycor() > 300:
        t1.penup()
        t1.home()
        t1.pendown()
    if t1.ycor() < -300:
        t1.penup()
        t1.home()
        t1.pendown()

    screen.update()

screen.mainloop()

# created by unsandpiper8 3/4/2026 for the python-9246 repo.
