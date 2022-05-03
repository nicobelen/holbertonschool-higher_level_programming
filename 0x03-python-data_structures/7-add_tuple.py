#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = [0, 0, 0, 0]
    list2 = [0, 0, 0, 0]
    list3 = []

    for i in range(len(tuple_a)):
        list1[i] = tuple_a[i]
    for j in range(len(tuple_b)):
        list2[j] = tuple_b[j]
    list3 = (list1[0] + list2[0], list1[1] + list2[1])
    return tuple(list3)
