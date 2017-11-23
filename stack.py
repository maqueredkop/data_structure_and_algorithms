#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:18:39 2017

@author: maque

the demo code is from the book <Problem solving with algorithms and data 
structure >

"""

class Stack:
    
    """
    A stack (sometimes called a “push-down stack”) is an ordered collection of
    items where the addition of new items and the removal of existing items 
    always takes place at the same end. This end is commonly referred to as the
    “top.” The end opposite the top is known as the “base.”
    
    LIFO means Last in first out
    """
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    

stack = Stack()

stack.isEmpty()
stack.push('tree')
stack.push('river')
stack.push('wall')

stack.peek()

stack.pop()
stack.size()


