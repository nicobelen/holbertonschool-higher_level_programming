#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (len(sentence), None)
    count = 0
    for i in sentence:
        count += 1
    return (count, sentence[0])
