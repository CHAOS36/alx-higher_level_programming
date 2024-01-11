#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for p in sorted(my_dict.keys()):
        print("{}: {}".format(p, my_dict[p]))
