#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4

for i in dir([hidden_4]):
    if i.startswith("_", 0, 1) is False:
        print(i)
