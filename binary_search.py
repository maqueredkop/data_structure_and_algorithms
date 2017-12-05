# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 2017

@author: maque
Note that the demo code is from the below link:
http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBinarySearch.html
the binary search is O(logn)

Even though a binary search is generally better than a sequential search, 
it is important to note that for small values of n, the additional cost of 
sorting is probably not worth it. In fact, we should always consider whether 
it is cost effective to take on the extra work of sorting to gain searching benefits. 

"""

def binary_search(input_list, item):
    first = 0
    last = len(input_list) - 1
    found = False
    
    while first <= last and not found:
        mid_point = (first + last) // 2
        if input_list[mid_point] == item:
            found = True
        elif item < input_list[mid_point]:
            last = mid_point - 1
        else:
            first = mid_point + 1
            
    return found

test_sorted_list = [0,2,4,7,9,12,15,17]
print(binary_search(test_sorted_list, 8))
print(binary_search(test_sorted_list, 15))


###############################################################################
## binary search in recursive version

def binary_search(input_list, item):
    if len(input_list) == 0:
        return False
    else:
        mid_point = len(input_list) // 2
        if input_list[mid_point] == item:
            return True
        elif item < input_list[mid_point]:
            return binary_search(input_list[:mid_point], item)
        else:
            return binary_search(input_list[mid_point + 1:], item)


test_sorted_list = [0,2,4,7,9,12,15,17]
print(binary_search(test_sorted_list, 8))
print(binary_search(test_sorted_list, 15))


