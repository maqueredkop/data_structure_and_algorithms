# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 2017

@author: maque

Note that the demo code is from the below link:
http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html

"""

## The maximum number of comparisons for an insertion sort is the sum of the 
## first n−1 integers. Again, this is O(n^2). 

## One note about shifting versus exchanging is also important. In general, 
## a shift operation requires approximately a third of the processing work of 
## an exchange since only one assignment is performed.


def insertion_sort(input_list):
    for index in range(1, len(input_list)):
        
        current_value = input_list[index]
        position = index
        
        while position > 0 and input_list[position-1] > current_value:
            input_list[position] = input_list[position-1]
            position = position - 1
            
        input_list[position] = current_value
        

test_list = [4,7,0,21,34,2,57,8]
print(test_list)
insertion_sort(test_list)
print(test_list)

