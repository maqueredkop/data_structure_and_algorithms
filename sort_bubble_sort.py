# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 2017

@author: maque

Note that the demo code is from the below link:
http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBubbleSort.html
"""

def bubble_sort(input_list):
    for pass_num in range(len(input_list)-1, 0, -1):
        for i in range(pass_num):
            if input_list[i] > input_list[i+1]:
                temp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = temp
                
input_list = [4,6,12,13,54,68,9,8,123,467,12]
print(input_list)
bubble_sort(input_list)
print(input_list)

## A bubble sort is often considered the most inefficient sorting method 
## since it must exchange items before the final location is known. These “wasted” 
## exchange operations are very costly.
## and is O(n^2)

###############################################################################
## if during a pass there are no exchanges, then we know that the list must be sorted.
## A bubble sort can be modified to stop early if it finds that the list has become sorted.

def short_bubble_sort(input_list):
    exchanges = True
    pass_num = len(input_list) - 1
    
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if input_list[i] > input_list[i+1]:
                exchanges = True
                temp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = temp
                
        pass_num = pass_num - 1
        
input_list = [4,6,12,13,54,68,9,8,123,467,12]
print(input_list)
short_bubble_sort(input_list)
print(input_list)
        
        
        