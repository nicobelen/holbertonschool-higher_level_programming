#!/usr/bin/python3
number = 0
for number in range(0, 100):
    print("{:02d}, ".format(number), end="")
    if number == 98:
        print("99")
