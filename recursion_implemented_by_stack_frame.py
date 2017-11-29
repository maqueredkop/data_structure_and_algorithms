# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29  2017

@author: maque

Note that the demo illustrated well in the link:
http://interactivepython.org/courselib/static/pythonds/Recursion/StackFramesImplementingRecursion.html

When a function is called in Python, a stack frame is allocated to handle the 
local variables of the function. When the function returns, the return value 
is left on top of the stack for the calling function to access. 
"""

class Stack:
        
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
my_stack = Stack()


def to_string(n, base):
    convert_string = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            my_stack.push(convert_string[n])
        else:
            my_stack.push(convert_string[n % base])
        n = n // base
        
    result = ""
    while not my_stack.is_empty():
        result = result + str(my_stack.pop())
    return result

print(to_string(1453, 16))
print(to_string(1453, 2))
