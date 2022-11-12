import turtle as t

def make_window(bg_color: str):
    """Return a window object with a background color"""

    window = t.Screen()
    window.bgcolor(bg_color)
    return  window


def make_turtle(turtle_color: str, pen_size: int, turtle_shape=""):
    """Return a turtle object with a background color"""

    piero = t.Turtle()
    piero.color(turtle_color)
    piero.pensize(pen_size)
    if turtle_shape:
       piero.shape(turtle_shape) 

    return  piero