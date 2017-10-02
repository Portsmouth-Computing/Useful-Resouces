"""Write a function circumferenceOfCircle that asks the user for the radius of a circle,
and then outputs its circumference. (Use the formula circumference = 2πr. For π, use
math.pi from the math module.)"""

import math

def circumferenceOfCircle():
    while True:
        radius = input("What is the radius of the circle: ")
        if radius.isnumeric():
            circumference = 2 * (math.pi * int(radius))
            print("The circumference of a circle with the radius of {} is {}".format(radius, circumference))
            break
        else:
            print("Please use a number")
