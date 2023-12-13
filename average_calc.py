#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: December 13, 2023
# This program display the average of 10 marks

import random
import constants


def main():
    # declare marks_array
    marks_array = []

    # initialize sum to 0
    sum = 0

    # tell the user what the program does
    print("This program display the average of the following marks :")

    # use a for loop when counter < ARRAY_SIZE
    for counter in range(0, constants.ARRAY_SIZE):
        # generate a random number
        rand_num = random.randint(constants.MIN, constants.MAX)

        # append marks_array  to the random number
        marks_array.append(rand_num)

        # display marks array
        print(marks_array[counter])

    # use a for loop when counter < ARRAY_SIZE
    for counter in range(0, constants.ARRAY_SIZE):
        # set sum to marks array + sum
        sum += marks_array[counter]

    # calculate average
    average = sum / constants.ARRAY_SIZE

    # display the average
    print("The average of the above random marks is {}.".format(average))


if __name__ == "__main__":
    main()
