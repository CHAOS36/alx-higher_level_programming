#!/usr/bin/python3
def magic_string():
    magic_string.pipo = getattr(magic_string, 'pipo', 0) + 1
    return ("BestSchool, " * (magic_string.pipo - 1) + "BestSchool")
