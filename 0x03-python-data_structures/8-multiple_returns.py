#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sennat = len(sentence)
    else:
        sennat = 0
    return (sennat, sentence if not sentence else sentence[:1])
