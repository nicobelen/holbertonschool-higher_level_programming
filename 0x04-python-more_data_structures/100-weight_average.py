#!/usr/bin/python3
def weight_average(my_list=[]):
    num1 = 0
    num2 = 0

    if my_list:
        for i in my_list:
            num1 = num1 + (i[0] * i[1])
            num2 = num2 + (i[1])
        return num1 / num2
    else:
        return 0
