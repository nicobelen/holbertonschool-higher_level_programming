#!/usr/bin/python3
def uppercase(str):
    letter = str[0]
    for letter in str:
        let = ord(letter)
        if let > 97 and let < 122:
            let = let - 32
            letter = chr(let)
            print(letter, end="")
        else:
            print(letter, end="")
    print("")
