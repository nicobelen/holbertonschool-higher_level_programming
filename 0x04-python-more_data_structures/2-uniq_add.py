#!/usr/bin/python3
def get_unique_numbers(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


def uniq_add(my_list=[]):
    numbers = get_unique_numbers(my_list)
    res = 0

    for n in numbers:
        res = res + n
    return res
