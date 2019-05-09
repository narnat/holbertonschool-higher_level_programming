#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l = []
    for k, v in a_dictionary.items():
        if v == value:
            l.append(k)
    for i in l:
        del(a_dictionary[i])
    return a_dictionary
