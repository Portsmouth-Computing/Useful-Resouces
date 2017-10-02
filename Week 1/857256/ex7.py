"""Write a function sumOfNumbers that outputs the sum of the first n positive integers,
where n is provided by the user. For example, if the user enters 4, the function should
output 10 (i.e. 1 + 2 + 3 + 4). (Hint: This function should use a loop.)
"""

def sumOfNumbers():
    while True:
        end = input("Where should I stop? ")
        if end.isnumeric():
            end = int(end)
            total = 0
            for i in range(1, end+1):
                total += i
            print("Total is: {}".format(total))
        else:
            print("Please enter a number")

sumOfNumbers()
