#/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for i in range((len(argv) - 1)):
        number = argv[i + 1]
        result += int(number)
    print("{}".format(result))