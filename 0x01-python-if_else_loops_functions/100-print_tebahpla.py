#!/usr/bin/python3
for i, j in zip(reversed(range(98, 123, 2)), reversed(range(65, 91, 2))):
    print("{}{}".format(chr(i), chr(j)), sep="", end="")
