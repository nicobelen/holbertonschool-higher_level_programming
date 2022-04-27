#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        let = ord(letter)
        if let >= 97 and let <= 122:
            let = let - 32
            letter = chr(let)
        print(letter, end="")
    print("")
