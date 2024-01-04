#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cunt = len(sys.argv) - 1
    if cunt == 0:
        print("0 arguments.")
    elif cunt == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cunt))
    for i in range(cunt):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
