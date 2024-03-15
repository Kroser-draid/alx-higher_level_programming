#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as names
    for name in dir(names):
        if name[0] != '_' and name[1] != '_':
            print(name)
