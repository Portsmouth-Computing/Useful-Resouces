"""Write a function areaOfCircle that asks the user for the radius of a circle, and then
outputs its area (using the formula area = πr2)."""

import math

def areaOfCircle():
    while True:
        radius = input("Radius of circle: ")
        if radius.isnumeric():
            area = math.pi * (radius**2)
            print("The area of a circle with the radius of {} is {}".format(radius,area))
            break
        else:
            print("Please input a number")
