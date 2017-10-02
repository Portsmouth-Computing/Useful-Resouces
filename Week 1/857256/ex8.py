"""[harder] Write a function averageOfNumbers which outputs the average of a series
of numbers entered by the user. The function should first ask the user how many
numbers there are to be inputted."""

from statistics import mean

def averageOfNumbers():
    while True:
        list_of_numbers = input("Please input a list of numbers that are split by a space ' ': ")
        list_of_numbers_no_space = list_of_numbers.replace(" ", "")
        if list_of_numbers_no_space.isnumeric():
            list_of_numbers = list_of_numbers.split(" ")
            list_of_numbers_int = []
            for num in list_of_numbers:
                list_of_numbers_int.append(int(num))
            average = mean(list_of_numbers_int)
            print("The average for your list is {}".format(average))
        else:
            print("Please use only numbers")

averageOfNumbers()
