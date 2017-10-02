"""Write a function distanceBetweenPoints that asks the user for four values x1, y1,
x2 and y2 that represent two points in two-dimensional space, and then outputs the
distance between them. (Hint: copy the relevant expression from the shell see the
warm-up exercises!)"""

import math


def distanceBetweenPoints():
    while True:
        x1 = input("x1: ")
        if x1.isnumeric():
            x1 = int(x1)
            break
        else:
            print("Please enter a number")
    while True:
        y1 = input("y1: ")
        if y1.isnumeric():
            y1 = int(y1)
            break
        else:
            print("Please enter a number")
    while True:
        x2 = input("x1: ")
        if x2.isnumeric():
            x2 = int(x2)
            break
        else:
            print("Please enter a number")
    while True:
        y2 = input("x1: ")
        if y2.isnumeric():
            y2 = int(y2)
            break
        else:
            print("Please enter a number")
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("The slope of the line is {}".format(distance))
