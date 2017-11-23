# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23  2017

@author: maque

Note the code and well illustrated is from the link below:
http://interactivepython.org/runestone/static/pythonds/BasicDS/PalindromeChecker.html

A palindrome is a string that reads the same forward and backward, for example,
 radar, toot, and madam. We would like to construct an algorithm to input a 
 string of characters and check whether it is a palindrome.
 
"""

from deque import Deque

def palindrome_checker(string_checked):
    char_deque = Deque()
    
    for char in string_checked:
        char_deque.add_rear(char)
        
    still_equal = True
    
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False
            
    return still_equal

print(palindrome_checker('lsdkjfskf'))
print(palindrome_checker('hellolleh'))

