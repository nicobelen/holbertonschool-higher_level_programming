#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zipped = zip(tuple_a, tuple_b)
    mapped = map(sum, zipped)
    sum1 = tuple(mapped)

    if len(sum1) < 2:
        for i in range(len(sum1)):
            if sum1[i] == None:
                sum1[i] = 0
        return sum1
    elif len(sum1) > 2:
        return sum1[1, 2]
    return sum1
