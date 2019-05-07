#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    c = my_list.copy()
    l = len(my_list)
    if (0 <= idx < l):
        c[idx] = element
    return c
