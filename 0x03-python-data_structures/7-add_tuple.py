#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp = ()
    max_index = min(len(tuple_a), len(tuple_b))
    for i in range(max_index):
        temp = temp + (tuple_a[i] + tuple_b[i],)
    if len(tuple_a) > max_index:
        temp += tuple_a[max_index:]
    elif len(tuple_b) > max_index:
        temp += tuple_b[max_index:]
    return temp
