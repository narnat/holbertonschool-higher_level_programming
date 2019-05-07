#!/usr/bin/python3
def no_c(my_string):
    s = my_string.translate({ord('C'): None, ord('c'): None})
    return s
