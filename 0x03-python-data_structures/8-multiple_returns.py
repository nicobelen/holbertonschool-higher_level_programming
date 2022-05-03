#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    for i in sentence:
        count += 1
    if count == 0:
        sentence[0] = None
    return (count, sentence[0])
