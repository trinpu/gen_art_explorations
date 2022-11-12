import setup
import basic_shapes as shapes
import draw_a_shell as shell
from random import randint

# Turtle Control

def reset_and_clear(a_turtle):
    """Resets turtle to starting position ready for a new drawing"""
    a_turtle.clear()
    a_turtle.home()

def back_to_center(a_turtle):
    """Brings turtle back to 0, 0 position"""
    a_turtle.penup()
    a_turtle.goto(0,0)
    a_turtle.pendown()

def pick_random_turtle_color(color_options:list):
    """Picks a random color for the turtle"""
    turtle_color = color_options[randint(0, len(color_options)- 1)]
    return turtle_color

# Advanced shapes

def draw_line_of_squares(n_squares, side_size):
    """ Draw line of consecutive squares"""
    step_size = side_size * 2
    for square in range(n_squares):
        shapes.draw_square(alex, side_size, False)
        alex.penup()
        alex.forward(step_size)
        alex.pendown()

def draw_line_of_diamonds(n_diamonds, side_size):
    """ Draw line of consecutive diamonds"""
    step_size = side_size * 2
    for square in range(n_diamonds):
        shapes.draw_rhombus(alex, side_size, False)
        alex.left(45)
        alex.penup()
        alex.forward(step_size)
        alex.pendown()

# Show sections

def squares_and_diamonds_section(a_turtle, turtle_colors: list):
    """Turtle draws square and diamonds section"""

    first_color = pick_random_turtle_color(turtle_colors)
    second_color = pick_random_turtle_color(turtle_colors)

    side_size = 30

    n_squares = randint(3,5)
    n_diamonds = randint(3,5)

    for loops in range(4):
        a_turtle.color(first_color)
        draw_line_of_squares(n_squares, side_size)

        back_to_center(a_turtle)

        a_turtle.right(45)
        
        a_turtle.color(second_color)
        draw_line_of_diamonds(n_diamonds, side_size)
        back_to_center(a_turtle)

        a_turtle.right(45)


def shell_section(a_turtle, color_options: list):
    """ Turtle draws a shell section"""
    base_color = pick_random_turtle_color(color_options)

    n_pieces = randint(5,15)
    side_size = randint(20,50)
    side_growth = int(side_size / 2)
    shell.draw_shell(a_turtle, base_color, color_options, side_size, side_growth, n_pieces, bank_angle=15)




# main show

background_color = 'black'
window = setup.make_window('black')

colors = ["red", "pink", "green", "yellow", "blue", "hot pink"]

alex = setup.make_turtle(background_color, 1, 'turtle')
alex.speed(7)

squares_and_diamonds_section(alex, colors)
# reset_and_clear(alex)

alex.pensize(3)
shell_section(alex, colors)
back_to_center(alex)
reset_and_clear(alex)


squares_and_diamonds_section(alex, colors)
reset_and_clear(alex)

shell_section(alex, colors)
back_to_center(alex)
reset_and_clear(alex)

alex.penup()
alex.color('white')
alex.write('Thank You', True, align='center', font=('Arial', 45, 'normal'))

window.mainloop()




