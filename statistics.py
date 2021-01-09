import math
import sys


try:

    print("Enter data set:")

    # we can use the sys module to read user input until EOF, create multi-line list of user input floats
    user_input = sys.stdin.read().split()
    numbers_list = [float(x) for x in user_input]

    # create statistical functions
    def mean(numbers):
        return sum(numbers) / len(numbers)


    def variance(numbers, m):
        squared_dev = [(x - m) ** 2 for x in numbers]

        return 1 / len(numbers) * sum(squared_dev)


    def sd(v):
        return math.sqrt(v)

    # initialize variables
    average = mean(numbers_list)
    var = variance(numbers_list, average)
    sd = sd(var)

    # print the output
    print()
    print("Mean = {0:.4f}".format(average))
    print("Variance = {0:.4f}".format(var))
    print("Standard deviation = {0:.4f}".format(sd))

    # if user enters no data
except ZeroDivisionError:
    print()
    print("No data!")