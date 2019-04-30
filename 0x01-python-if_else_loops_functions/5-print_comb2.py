#!/usr/bin/python3
for i in range(99):
    print(("0" if i < 10 else "") + "{:s}, ".format(str(i)), end='')
print("{:s}".format(str(i + 1)))
