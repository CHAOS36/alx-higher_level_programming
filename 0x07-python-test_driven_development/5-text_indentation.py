#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    pipo = 0
    while pipo < len(text) and text[pipo] == ' ':
        pipo += 1

    while pipo < len(text):
        print(text[pipo], end="")
        if text[pipo] == "\n" or text[pipo] in ".?:":
            if text[pipo] in ".?:":
                print("\n")
            pipo += 1
            while pipo < len(text) and text[pipo] == ' ':
                pipo += 1
            continue
        pipo += 1
