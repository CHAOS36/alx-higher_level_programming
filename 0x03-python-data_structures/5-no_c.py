#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for emlent in my_string:
        if emlent != "c" and emlent != "C":
            new_string += emlent
    return new_string
