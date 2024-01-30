#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    pipox = 1
    while pipox < len(list):
        if list[pipox] > result:
            result = list[pipox]
        pipox += 1
    return result
