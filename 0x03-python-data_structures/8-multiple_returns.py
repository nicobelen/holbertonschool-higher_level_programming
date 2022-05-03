#!/usr/bin/python3
def multiple_returns(sentence):
    stringlen = len(sentence)
    if stringlen == 0:
        sentence[0] = None
    count = 0
    for i in sentence:
        count += 1
    return (count, sentence[0])
