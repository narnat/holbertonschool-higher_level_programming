#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Function to find a peak in a list"""
    if list_of_integers == []:
        return None
    l = len(list_of_integers)
    m = l // 2
    arr = list_of_integers
    while True:
        if m != 0 and arr[m - 1] < arr[m] < arr[m + 1]:
            m += 1
        elif m != 0 and arr[m - 1] > arr[m] > arr[m + 1]:
            m -= 1
        elif m != 0 and arr[m - 1] > arr[m] < arr[m + 1]:
            m -= 1
        else:
            return arr[m]
