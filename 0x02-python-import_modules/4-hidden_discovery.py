#!/usr/bin/python3
def listToString(s):
    str1 = " "

    return (str1.join(s))


if __name__ == "__main__":
    import hidden_4

hid = dir(hidden_4)
str1 = listToString(hid)
str2 = str1.split(" ")

for n in str2:
    if n[0:2] != "__":
        print(n)
