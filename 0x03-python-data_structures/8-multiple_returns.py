#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    for i in sentence:
        if len(sentence) == 0:
            sentence[0] = None
        count += 1
    return (count, sentence[0])
