#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def repSerElem(i):
        return (i if i != search else replace)
    return list(map(repSerElem, my_list))
