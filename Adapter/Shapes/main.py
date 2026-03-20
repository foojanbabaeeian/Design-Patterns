import square
import circle
import triangle

def display_shape(shape):
    print("Area = " + str(shape.area()))
    print("Perimeter = " + str(shape.perimeter()))

def main():
    shapes = [circle.Circle(3), square.Square(2), triangle.Triangle(2, 4)]
    for s in shapes: 
        display_shape(s)

main()