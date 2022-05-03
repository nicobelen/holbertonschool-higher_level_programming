#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    if len(sentence) - 1 == 0:
        sentence[0] = None
    for i in sentence:
        count += 1
    return (count, sentence[0])
