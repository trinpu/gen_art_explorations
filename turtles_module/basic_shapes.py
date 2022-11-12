def draw_poligon(a_turtle, n_sides: int, side_length:int , clockwise=True):
    """Draws a polygon of n_sides of lenght side_lenght"""
    
    angle = 360 / n_sides
    for side in range(n_sides):
        if clockwise:
            a_turtle.right(angle)
        else:
            a_turtle.left(angle)
        a_turtle.forward(side_length)

def draw_square(a_turtle, side_length, clockwise=True):
    """Draws a square with sides of lenght side_lenght"""
    draw_poligon(a_turtle, 4, side_length, clockwise)

def draw_triangle(a_turtle, side_length, clockwise=True):
    """Draws a tirangle with sides of lenght side_lenght"""
    draw_poligon(a_turtle, 3, side_length, clockwise)

def draw_rhombus(a_turtle, side_length, clockwise=True):
    """Draws a rhombus / diamond of same sizes with sides of lenght side_lenght"""
    angle = 90 / 2
    
    # setup
    if clockwise:
        a_turtle.right(-angle)
    else:
        a_turtle.left(-angle)

    draw_square(a_turtle, side_length, clockwise)


def draw_star(a_turtle, number_of_edges, side_length):
    """Draws a start for uneven edges of lengths"""
    edge_change = 360 / number_of_edges
    
    a_turtle.right(edge_change)
    for point in range(number_of_edges):
        a_turtle.forward(side_length)
        # a_turtle.right(180 - edge_change)
        a_turtle.right(180 - edge_change / 2)
    
    a_turtle.left(edge_change)

    

