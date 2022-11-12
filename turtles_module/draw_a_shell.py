import turtle as t
from random import randint

def draw_multicolor_square(a_turtle, size:int, base_color:str, colors_range: list ):
    """Void function instructing a trutle to draw a square with 3rd size of different color"""
    for side in [1,2,3,4]:
        if side == 3 or side == 1:
            a_turtle.color(colors_range[randint(0, len(colors_range) - 1)])
        else:
            a_turtle.color(base_color)
        a_turtle.forward(size)
        a_turtle.left(90)

def draw_shell(a_turtle, base_color:str, colors_range: list, size: int, size_increase: int, n_pieces: int, bank_angle:int):
    """Void function instructing a trutle object to draw a shell made of squares"""
    current_size = size
    for piece in range(n_pieces):
        draw_multicolor_square(a_turtle, current_size, base_color, colors_range)
        a_turtle.forward(size_increase)
        current_size += size_increase
        a_turtle.right(bank_angle)

# testing

# window = t.Screen()
# window.bgcolor("black") # .bgcolor is a void method

# alex = t.Turtle()
# alex.shape("turtle")
# alex.pensize(2)

# alex.speed(0)
# # alex.speed(10)

# colors = ["red", "pink", "green", "yellow"]

# draw_shell(alex, "blue", colors, 10, 5, 50, 15)

# window.mainloop()