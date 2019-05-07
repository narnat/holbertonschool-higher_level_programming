#!/usr/bin/python3
def element_at(my_list, idx):
    l = len(my_list)
    if (0 <= idx < l):
        return my_list[idx]
    return None
