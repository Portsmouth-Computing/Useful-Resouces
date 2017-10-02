""" Write a function costOfPizza that asks the user for the diameter (not the radius) of a
pizza (in cm), and then outputs the cost of the pizza’s ingredients (based on its area)
in pence. Assume that the cost of the ingredients is 1.5p per square cm."""

import math


def costOfPizza():
    diameter = input("What is the diameter of the pizza: ")
    area = math.pi * diameter
    cost = area * 1.5
    print("The cost of a pizza with the diameter of {} is {}".format(diameter,cost))
