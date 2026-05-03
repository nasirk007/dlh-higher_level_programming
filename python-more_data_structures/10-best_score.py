#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    biggest_value = None
    for key, value in a_dictionary.items():
        if biggest_value is None or value > biggest_value:
            biggest_value = value
            best_key = key
    return best_key
