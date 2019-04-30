#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if (ord(i) >= 97 and ord(i) <= 122):
            c -= 32
        print("{}".format(chr(c)), end="")
    print()
