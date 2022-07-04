#!/usr/bin/python3
"""
Module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exactly instance of  class, otherwise false"""
    return (type(obj) == a_class)
