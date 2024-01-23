#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        pipox = a / b
    except (ZeroDivisionError):
        pipox = None
    finally:
        print("Inside result: {}".format(pipox))
        return pipox
