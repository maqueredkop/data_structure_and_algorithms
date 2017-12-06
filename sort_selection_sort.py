# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6  2017

@author: maque

Note that the demo code is from the below link:
http://interactivepython.org/courselib/static/pythonds/SortSearch/TheSelectionSort.html

 The selection sort improves on the bubble sort by making only one exchange for
 every pass through the list. In order to do this, a selection sort looks for 
 the largest value as it makes a pass and, after completing the pass, places it 
 in the proper location. 
"""

## The selection sort makes the same number of comparisons as the bubble sort 
## and is therefore also O(n^2). However, due to the reduction in the number 
## of exchanges, the selection sort typically executes faster in benchmark studies


def selection_sort(input_list):
    for fill_slot in range(len(input_list)-1, 0, -1):
        position_of_max = 0
        for location in range(1,fill_slot + 1):   ## key step
            if input_list[location] > input_list[position_of_max]:
                position_of_max = location
                
        temp = input_list[fill_slot]
        input_list[fill_slot] = input_list[position_of_max]
        input_list[position_of_max] = temp
        

test_list = [4,7,0,21,34,2,57,8]
print(test_list)
selection_sort(test_list)
print(test_list)

