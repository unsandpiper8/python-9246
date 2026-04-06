import turtle

t = turtle

# check functions
def input_turtle_size():
    global turtle_forward
    turtle_forward = input("turtle size/forward: ")

def input_turtle_shape():
    global turtle_left
    turtle_left = input("turtle shape/left: ")

def turtle_size_checks():
    try:
        val1 = int(turtle_forward)
    except ValueError:
        print("err: not a valid value: has to be numeric")
        input_turtle_size()
    
    if int(turtle_forward) > 400:
        print("err: shape is to big for window")
        input_turtle_size()

def turtle_shape_checks():
    try:
        val2 = int(turtle_left)
    except ValueError:
        print("err: not a valid value: has to be numeric")
        input_turtle_shape()
    if int(turtle_left) > 299:
        print("err: shape wont work: too tight")
        input_turtle_shape()



# user interaction and error handling
print("enter shape attributes:")

input_turtle_size()
size_length = len(turtle_forward)
turtle_size_checks()

input_turtle_shape()
shape_length = len(turtle_left)
turtle_shape_checks()

# logic for displaying shape
def start_script():
    t.resetscreen()
    t.tracer(0)

    t.teleport(-int_turtle_forward / 2, -int_turtle_left / 2)
    t.begin_fill()
    t.color("white")
    t.fillcolor("black")

    for _ in range(200):
        t.fd(int_turtle_forward)
        t.lt(int_turtle_left)
        if abs(t.pos()) < 1:
            break

    t.end_fill()
    t.update()

# logic for start and quit
def handle_quit_on_qpress():
    screen.bye()

t.tracer(0)
screen = turtle.Screen()

int_turtle_forward = int(turtle_forward)
int_turtle_left = int(turtle_left)

start_script()

screen.listen()
screen.onkeypress(handle_quit_on_qpress, "q")

t.done()
