#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    l = len(my_list)
    if (0 <= idx < l):
        del my_list[idx]
    return my_list
