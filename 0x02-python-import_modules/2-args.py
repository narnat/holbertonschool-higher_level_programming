#!/usr/bin/python3
import sys
l = len(sys.argv) - 1
if l == 0:
    print("{} arguments.".format(l))
elif l == 1:
    print("{0} argument:\n{0}: {1}".format(l, sys.argv[l]))
else:
    print("{} arguments:".format(l))
    arg = sys.argv[1:]
    for i, str in enumerate(arg, start=1):
        print("{}: {}".format(i, str))
