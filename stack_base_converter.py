#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:43:49 2017

@author: maque

note the code and good illustration is from the web below:
http://interactivepython.org/courselib/static/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html

"""

from stack import Stack

def decimal_to_binary(deci_num):
    remainer_stack = Stack()
    
    while deci_num > 0:
        remainer = deci_num % 2
        remainer_stack.push(remainer)
        deci_num = deci_num // 2
        
    binary_string = ''
    
    while not remainer_stack.is_empty():
        binary_string = binary_string + str(remainer_stack.pop())
        
    return binary_string


print(decimal_to_binary(42))


###############################################################################

from stack import Stack

def base_converter(deci_num, base):
    digits = '0123456789ABCDEF'
    
    remainer_stack = Stack()
    
    while deci_num > 0:
        remainer = deci_num % base
        remainer_stack.push(remainer)
        deci_num = deci_num // base
        
    binary_string = ''
    
    while not remainer_stack.is_empty():
        binary_string = binary_string + digits[remainer_stack.pop()]
        
    return binary_string

print(base_converter(100,8))
print(base_converter(100,16))