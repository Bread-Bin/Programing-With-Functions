import math


#Square
def compute_area_square(square_input):
    return compute_area_rectangle(square_input, square_input)

#Rectangle
def compute_area_rectangle(length, width):
    return length * width

#Circle
def compute_area_circle(radius):
    return float(math.pi * (radius ** 2))

shape = ""

while shape != "quit":
    shape = input('what is your shape? '.lower())
    if shape == "square":
        square_input = int(input("What is length of one side of the Square: "))
        print(compute_area_square(square_input))
    
    elif shape == "rectangle":
        length = int(input("What is length of side 1 of the Rectangle: "))
        width = int(input("What is width of side 2 of the Rectangle: "))
        print(compute_area_rectangle())

    elif shape == "circle":
        radius = int(input("What is the radius of the Circle: "))
        print(compute_area_circle())

