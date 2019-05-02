#!/usr/bin/python3
def func():
    import hidden_4
    for str in dir(hidden_4):
        if str[:2] != "__":
            print(str)
if __name__ == "__main__":
    func()
