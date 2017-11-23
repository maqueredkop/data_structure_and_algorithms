# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23  2017

@author: maque
note that the demo code is from the book <Problem solving with algorithms 
and data structure >
"""

class Queue:
    """
    A queue is structured, as described above, as an ordered collection of 
    items which are added at one end, called the “rear,” and removed from the
    other end, called the “front.” 
    The queue maintain a FIFO, means "first in first out"
    """
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    ## enqueue(item) adds a new item to the rear of the queue. 
    ## It needs the item and returns nothing.
    def enqueue(self, item):
        self.items.insert(0, item)
    
    ## dequeue() removes the front item from the queue. 
    ## It needs no parameters and returns the item. The queue is modified.    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    

q = Queue()

q.is_empty()
q.enqueue('john')
q.enqueue('tim')
q.enqueue('susan')
q.enqueue('mike')

q.is_empty()
q.size()

q.dequeue()
q.size()

