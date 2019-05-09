#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    score = 0
    weight = 0
    for i in my_list:
        weight += i[1]
        score += i[0] * i[1]
    return score / weight
