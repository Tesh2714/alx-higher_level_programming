#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if len(my_list) > 0:
        for e in my_list:
            new_list.append(True if e % 2 == 0 else False)
    return new_list
