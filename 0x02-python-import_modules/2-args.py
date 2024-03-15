#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    _len = len(sys.argv) - 1
    if _len == 0:
        print("0 arguments.")
    else:
        if _len == 1:
            print("{} argument:".format(_len))
        else:
            print("{} arguments:".format(_len))
        for i in range(1, _len + 1):
            print("{}: {}".format(i, sys.argv[i]))
