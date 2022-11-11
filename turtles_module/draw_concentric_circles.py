import turtle as t
from random import randint

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
    max_pensize = 8

    for circle in range(n_circles):
        a_turtle.pensize(pen_size)
        draw_centered_circle(a_turtle, radius)
        radius += radius_growth

        if pen_size > max_pensize:
            pen_size = max_pensize
        else:
            pen_size += 2

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
    max_pensize = 20

    turtle_colors = ['deep sky blue', 'blue', 'cornflower blue']

    # drawing
    for circle in range(n_circles):

        a_turtle.color(turtle_colors[randint(0, len(turtle_colors) - 1)])
        movement_growth_ratio = randint(0,70) / 100
        movement = radius + radius_growth * movement_growth_ratio

        a_turtle.pensize(pen_size)
        draw_offcenter_circle(a_turtle, radius, movement)

        radius += radius_growth

        if pen_size > max_pensize:
            pen_size = max_pensize
        else:
            pen_size += 2


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
