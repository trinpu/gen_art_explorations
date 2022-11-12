import turtle as t
from random import randint

def set_pen_size(pen_size, pen_size_step, max_pen_size):
    """Returns adjusted pen_size, with a maximum max_pen_size """
    if pen_size > max_pen_size:
        pen_size = max_pen_size
    else:
        pen_size += pen_size_step
    return pen_size


def draw_centered_circle(a_turtle, radius):
    """ Void function that draws a centred circle """
    a_turtle.penup()
    a_turtle.sety(-radius)
    a_turtle.pendown()
    a_turtle.circle(radius)

def draw_concentric_circles(a_turtle, starting_radius, radius_growth, n_circles):
    """ Void function. Turtle draw concentric circles """

    radius = starting_radius

    # pensize settings
    pen_size = 1
    pen_size_step = 1
    max_pen_size = 8

    for circle in range(n_circles):
        a_turtle.pensize(pen_size)
        draw_centered_circle(a_turtle, radius)
        radius += radius_growth
        pen_size = set_pen_size(pen_size, pen_size_step, max_pen_size)

def draw_offcenter_circle(a_turtle, radius, movement):
    """ Void function that draws an offcentered circle """

    a_turtle.penup()
    a_turtle.sety(-movement)
    a_turtle.pendown()
    a_turtle.circle(radius)


def draw_twisted_tube(a_turtle, starting_radius, radius_growth, n_circles):
    """ Void function. Turtle draw concentric circles """

    radius = starting_radius
    
    # pensize settings
    pen_size = 1
    pen_size_step = 2
    max_pen_size = 20

    turtle_color_options = ['deep sky blue', 'blue', 'cornflower blue', 'green']

    # drawing
    for circle in range(n_circles):

        a_turtle.color(turtle_color_options[randint(0, len(turtle_color_options) - 1)])
        
        movement_growth_ratio = randint(0,70) / 100
        movement = radius + radius_growth * movement_growth_ratio

        a_turtle.pensize(pen_size)
        draw_offcenter_circle(a_turtle, radius, movement)

        radius += radius_growth

        pen_size = set_pen_size(pen_size, pen_size_step, max_pen_size)


### fill property to increase it

# test
window = t.Screen()
window.bgcolor("black")

alex = t.Turtle()
alex.hideturtle()
alex.color('red') 
alex.speed(0)


# draw_concentric_circles(alex, 10, 30, 20)
draw_twisted_tube(alex, 10, 20, 40)
window.mainloop()
