#!/usr/bin/python3
for c in range(90, 64, -1):
    print("{:c}".format(c), end="")
    if c % 2 == 0:
        c += 32
print()
