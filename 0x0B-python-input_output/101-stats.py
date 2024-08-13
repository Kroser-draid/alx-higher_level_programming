#!/usr/bin/python3
import sys
""" Module for function """


while True:
    ok = 0
    moved = 0
    bad = 0
    unauth = 0
    forbidden = 0
    not_found = 0
    not_supported = 0
    server_error = 0
    size = 0

    for i in range(10):

        line = sys.stdin.readline()
        parts = line.strip().split(' ')
        size += int(parts[-1])

        if str(200) in line:
            ok += 1
        elif str(301) in line:
            moved += 1
        elif str(400) in line:
            bad += 1
        elif str(401) in line:
            unauth += 1
        elif str(403) in line:
            forbidden += 1
        elif str(404) in line:
            not_found += 1
        elif str(405) in line:
            not_supported += 1
        elif str(500) in line:
            server_error += 1

    print("File size:", size)
    if ok != 0:
        print("200:", ok)
    if moved != 0:
        print("301:", moved)
    if bad != 0:
        print("400:", bad)
    if unauth != 0:
        print("401:", unauth)
    if forbidden != 0:
        print("403:", forbidden)
    if not_found != 0:
        print("404:", not_found)
    if not_supported != 0:
        print("405:", not_supported)
    if server_error != 0:
        print("500:", server_error)
