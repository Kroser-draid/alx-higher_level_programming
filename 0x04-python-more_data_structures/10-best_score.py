#!/usr/bin/python3
def best_score(a_dictionary):
    h_score = 0
    h_score_win = 'ayoub'
    if a_dictionary is not None:
        for i in a_dictionary:
            if a_dictionary[i] > h_score:
                h_score = a_dictionary[i]
                h_score_win = i
    else:
        return None
    return h_score_win
