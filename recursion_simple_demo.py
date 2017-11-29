# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29  2017

@author: maque
"""
##############################################################################
 
## example 1: Calculating the Sum of a List of Numbers
## Note that the demo code is well illustrated from the link:
## http://interactivepython.org/courselib/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html

"""
 All recursive algorithms must obey three important laws:
1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.
"""

def list_sum(number_list):
    if len(number_list) == 1:
        return number_list[0]
    else:
        return number_list[0] + list_sum(number_list[1:])
    
print(list_sum([1,3,5,7,9]))

##############################################################################
## example 2: Recursively Converting from Integer to String

def to_string(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        # The algorithm works correctly because we make the recursive call 
        #first, then we add the string representation of the remainder.
        return to_string(n // base, base) + convert_string[n % base]
    
print(to_string(1453, 16))
print(to_string(1453, 10))
print(to_string(1453, 2))


##############################################################################
## example 3: takes a string returns a new string that is the reverse of the old string.

def reverse_of_string(my_string):
    if len(my_string) == 1:
        return my_string[0]
    else:
        return reverse_of_string(my_string[1:]) + my_string[0] 
    
print(reverse_of_string('hello_the_fucking_world'))


##############################################################################
## Write a function that takes a string as a parameter and returns True if the 
## string is a palindrome, False otherwise.

import re

def check_palindrome(my_string):
    my_string = re.sub(r'\W','', my_string).upper()
    
    if len(my_string) <= 1:
        return True
    elif my_string[0] == my_string[-1]:
        return check_palindrome(my_string[1:-1])
    else:
        return False
    
print(check_palindrome('Live not on evil'))
print(check_palindrome('Reviled did I live, said I, as evil I did deliver'))
print(check_palindrome('hello the unhappy world'))

