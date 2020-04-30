
import math
import unittest

# ref : https://www.tutorialspoint.com/python/string_count.htm
# https://www.w3schools.com/python/ref_func_isinstance.asp


def get_max_frequency(input_string):
    """ Accept a string.
    Check if it is a valid string.
    IF valid, run a for loop and count char and update count
    If no winner, ignore. 
    if winner, return max frequency at the end"""

    if isinstance(input_string, str):

        max_count = 0
        # Sanitize the input
        input_string = input_string.lower()

        for i in input_string:
            if input_string.count(i) > max_count:
                max_count = input_string.count(i)
                required_char = i

        # checking if there are no winners
        if max_count == 1:
            print("All chars occur at same frequency. \n")
        elif max_count > 1:
            print("Input string was: %s", input_string)
            print("Most frequent character was %s", required_char, "\n")

    elif isinstance(input_string, int) or isinstance(input_string, float):
        print("Number entered. Exiting")


get_max_frequency("Kashmir")
get_max_frequency("Kashmirrrrr")
get_max_frequency("Amazon")
get_max_frequency(1234)

