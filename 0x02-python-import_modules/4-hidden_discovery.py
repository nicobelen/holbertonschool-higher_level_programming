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
"""
if __name__ == "__main__":
    import hidden_4

def listToString(s):
    str1 = " "

    return (str1.join(s))

filename = dir(hidden_4)
str1 = listToString(filename)

for i in str1:
    hid = str1.split("\'")
    if str1[i] != "__":
        print(i)
        """
