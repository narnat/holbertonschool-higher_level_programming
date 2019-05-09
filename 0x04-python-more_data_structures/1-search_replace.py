#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = my_list.copy()
    for i, el in enumerate(n):
        if (el == search):
            n[i] = replace
    return n
