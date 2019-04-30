#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i:
            if i + j != 17:
                print("{}{}, ".format(i, j), end="")
print(i - 1, j, sep="")
