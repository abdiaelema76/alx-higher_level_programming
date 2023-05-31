#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        my_tuple = None
    else:
        my_tuple = sentence[0]
    return len(sentence), my_tuple
