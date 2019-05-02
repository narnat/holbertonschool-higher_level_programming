#!/usr/bin/python3
def func():
    import sys
    res = 0
    for i in sys.argv[1:]:
        res += int(i)
    print(res)
if __name__ == "__main__":
    func()
