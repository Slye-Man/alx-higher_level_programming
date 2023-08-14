#!/usr/bin/python3
"""Function that returns a multipled number"""

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        res = (length, sentence[0:1])
        return res
