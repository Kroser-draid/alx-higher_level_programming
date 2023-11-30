#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    _len = len(sys.argv)
    result = 0
    for i in range(1, _len):
        result += int(sys.argv[i])
    print(result)
