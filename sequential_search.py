#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:53:35 2017

@author: maque
Note that the demo code is from the link below:
http://interactivepython.org/courselib/static/pythonds/SortSearch/TheSequentialSearch.html
"""

def sequential_search(input_list, item):
    pos = 0
    found = False
    
    while pos < len(input_list) and not found:
        if input_list[pos] == item:
            found = True
        else:
            pos = pos + 1
            
    return found

test_list = [1,4,6,8,12,31,67]
print(sequential_search(test_list, 31))
print(sequential_search(test_list, 44))


##############################################################################
## Assume that the list of items was constructed so that the items were 
## in ascending order, from low to high

def ordered_sequential_search(input_list, item):
    pos = 0
    found = False
    stop = False
    
    while pos < len(input_list) and not found and not stop:
        if input_list[pos] == item:
            found = True
        elif input_list[pos] > item:
            stop = True
        else:
            pos = pos + 1
            
    return found

test_list = [0,2,4,6,8,19]
print(ordered_sequential_search(test_list, 8))