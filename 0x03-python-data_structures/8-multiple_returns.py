#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    if sentence == 0:
        sentence[0] = None
    for i in sentence:
        count += 1
    return (count, sentence[0])
