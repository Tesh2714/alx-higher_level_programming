#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        max = my_list[0]
        for e in my_list:
            if e > max:
                max = e
        return max
    return None
